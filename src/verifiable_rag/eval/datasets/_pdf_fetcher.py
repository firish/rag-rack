"""PDF fetcher for benchmark datasets — multiple legitimate fallbacks.

Given a DOI (and optionally extra metadata), tries to obtain a free, legal
PDF copy via:

1. **Local cache** — if the file is already on disk, return it.
2. **Unpaywall API** — best general-purpose source for legally-OA papers
   (https://unpaywall.org/products/api). Free with email registration.
3. **OpenAlex API** — keyless aggregator that often has alternative OA
   mirrors not in Unpaywall (https://openalex.org).
4. **Semantic Scholar API** — paper graph with ``openAccessPdf.url`` field
   (https://api.semanticscholar.org). Uses ``SEMANTIC_SCHOLAR_API_KEY`` if
   set; falls back to rate-limited unauth otherwise.
5. **CORE API** — best for institutional repository content. Requires
   ``CORE_API_KEY`` env var.
6. **PMC (PubMed Central)** — NIH biomedical research. Note: NIH PMC has
   reCAPTCHA on PDF endpoints; we route through Europe PMC mirror first.
7. **bioRxiv / medRxiv** — preprint servers.
8. **arXiv** — mostly CS / physics / math, occasional biology preprints.
9. **Direct DOI landing page** — last-ditch attempt: scrape the publisher
   landing page for an obvious PDF link.

What this fetcher deliberately does NOT do:
- No Sci-Hub, no library-proxy / EZproxy support, no scrapers that violate
  publisher ToS.  The framework is shipped as a library; users in
  jurisdictions with stricter rules should not be dragged in unwillingly.
- For papers no legitimate channel finds, drop the PDF manually into the
  cache directory at ``<cache_dir>/<doi-hash>.pdf`` and the framework will
  pick it up on the next call.

Email requirement
-----------------
Unpaywall and Crossref both require an email address in API calls (their
politeness policy). Pass it explicitly to ``PdfFetcher``, or set the
``UNPAYWALL_EMAIL`` environment variable. ``example.com`` and obviously fake
domains are rejected — use a real address.
"""

from __future__ import annotations

import hashlib
import logging
import os
import re
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)

# Aggregator API endpoints
_UNPAYWALL_URL = "https://api.unpaywall.org/v2/{doi}"
_OPENALEX_URL = "https://api.openalex.org/works/doi:{doi}"
_SEMSCHOLAR_URL = "https://api.semanticscholar.org/graph/v1/paper/DOI:{doi}"
_CORE_SEARCH_URL = "https://api.core.ac.uk/v3/search/works"
_PMC_DOI_LOOKUP = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/elink.fcgi"
_PMC_PDF_URL = "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC{pmcid}/pdf/"
_BIORXIV_DETAIL = "https://api.biorxiv.org/details/{server}/{doi}"
_ARXIV_QUERY = "http://export.arxiv.org/api/query"

# Sleep between requests to a source that's unauthenticated and rate-limited.
# 100 req / 5 min = 1 req / 3s for Semantic Scholar without key.
_SEMSCHOLAR_UNAUTH_DELAY_SECS = 3.5

# Sleep between Google searches to stay below their automated-bot threshold.
# Aggressive scripted searches will trigger reCAPTCHA after ~5-10 hits/min.
_GOOGLE_DELAY_SECS = 5.0

# Polite user-agent for API calls — Unpaywall / Crossref ask for contact info
_API_USER_AGENT = "verifiable-rag-benchmark-fetcher/0.1 (mailto:{email})"

# Browser-like user-agent for PDF downloads. Many publishers (Elsevier/Cell,
# Science, bioRxiv) return 403 to non-browser UAs on their PDF endpoints,
# even for legally OA papers. This is purely a "look like a human reader"
# move; the underlying access permission is identical.
_BROWSER_USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/126.0.0.0 Safari/537.36"
)

# Cap individual HTTP requests so a slow source can't stall the whole pipeline
_REQUEST_TIMEOUT_SECS = 30.0


@dataclass(frozen=True)
class FetchResult:
    """Outcome of attempting to fetch one paper."""

    doi: str
    path: Path | None  # None when no source returned a PDF
    source: str | None  # which fallback succeeded ("cache", "unpaywall", "pmc", ...)
    error: str | None = None  # set when all fallbacks failed


class PdfFetcher:
    """Try multiple legitimate sources to fetch a PDF for a given DOI.

    Parameters
    ----------
    cache_dir:
        Directory to store fetched PDFs.  Files are named by SHA-256 of
        the normalized DOI so re-fetches hit the cache instantly.
    email:
        Contact address for Unpaywall (required by their ToS) and used in
        the User-Agent header for politeness.
    """

    def __init__(self, cache_dir: Path, email: str | None = None) -> None:
        # Unpaywall rejects obviously-fake emails (example.com, etc.). Require
        # a real address, either via param or env var.
        resolved_email = email or os.environ.get("UNPAYWALL_EMAIL", "")
        if not resolved_email or "@" not in resolved_email:
            raise ValueError(
                "PdfFetcher needs a real email address (Unpaywall/Crossref "
                "politeness policy). Pass `email=...` or set UNPAYWALL_EMAIL "
                "in your environment."
            )
        if resolved_email.lower().endswith("@example.com"):
            raise ValueError("Unpaywall rejects example.com addresses. Use a real email.")

        self._cache_dir = Path(cache_dir)
        self._cache_dir.mkdir(parents=True, exist_ok=True)
        self._email = resolved_email
        self._api_user_agent = _API_USER_AGENT.format(email=resolved_email)

        # Optional API keys — picked up from env if not passed
        self._semscholar_key = os.environ.get("SEMANTIC_SCHOLAR_API_KEY", "") or None
        self._core_key = os.environ.get("CORE_API_KEY", "") or None

        # Playwright singleton — lazy-loaded on first browser-required fetch
        self._playwright: Any = None
        self._browser: Any = None

    # ------------------------------------------------------------------ #
    # Public API
    # ------------------------------------------------------------------ #

    def fetch(self, doi: str) -> FetchResult:
        """Run the fallback chain and return where (if anywhere) the PDF was found.

        Strategy (two passes over the candidate URL set):

        **Pass 1 — fast HTTP via ``requests``.** Walk each source
        (Unpaywall, OpenAlex, SemScholar, CORE, PMC, biorxiv, etc.). Each
        source can yield MULTIPLE candidate URLs (publisher + repository
        mirrors). The first URL that returns a valid PDF wins.

        **Pass 2 — real browser via Playwright.** If pass 1 failed, take
        every candidate URL we collected and retry through a headless
        Chromium browser. This defeats Cloudflare / JS-based bot detection
        on publisher and PMC endpoints — most legally-OA papers behind
        those walls become accessible.

        Playwright is only invoked when pass 1 fails entirely. For papers
        that the aggregators easily resolve to a repository PDF, we never
        pay the browser cost.
        """
        norm_doi = _normalize_doi(doi)
        if not norm_doi:
            return FetchResult(doi=doi, path=None, source=None, error="invalid DOI")

        cache_path = self._cache_path(norm_doi)
        if cache_path.exists() and cache_path.stat().st_size > 0:
            return FetchResult(doi=norm_doi, path=cache_path, source="cache")

        # ----- Pass 1: requests-based -----
        all_candidates: list[tuple[str, str]] = []  # (source_name, url)
        for source_name, source_fn in (
            ("unpaywall", self._try_unpaywall),
            ("openalex", self._try_openalex),
            ("semantic_scholar", self._try_semantic_scholar),
            ("core", self._try_core),
            ("pmc", self._try_pmc),
            ("biorxiv", self._try_biorxiv),
            ("medrxiv", self._try_medrxiv),
            ("arxiv", self._try_arxiv),
            ("direct_doi", self._try_direct_doi),
            # Google search is expensive (Playwright + 5s delay + Google
            # CAPTCHA risk). Save it for last — only fires when every
            # cheaper source has failed.
            ("google_search", self._try_google_search),
        ):
            try:
                candidates = list(source_fn(norm_doi))
            except Exception as exc:  # noqa: BLE001 — one bad source shouldn't kill the chain
                logger.debug("%s lookup failed for %s: %s", source_name, norm_doi, exc)
                continue

            for pdf_url in candidates:
                all_candidates.append((source_name, pdf_url))
                try:
                    self._download(pdf_url, cache_path)
                except Exception as exc:  # noqa: BLE001
                    logger.debug(
                        "requests download from %s (%s) failed for %s: %s",
                        source_name,
                        pdf_url[:60],
                        norm_doi,
                        exc,
                    )
                    continue
                if cache_path.exists() and cache_path.stat().st_size > 1024:
                    return FetchResult(doi=norm_doi, path=cache_path, source=source_name)
                cache_path.unlink(missing_ok=True)  # tiny → likely error HTML

        # ----- Pass 2: Playwright (real browser) -----
        for source_name, pdf_url in all_candidates:
            try:
                ok = self._download_via_playwright(pdf_url, cache_path)
            except Exception as exc:  # noqa: BLE001
                logger.debug(
                    "playwright download from %s (%s) failed for %s: %s",
                    source_name,
                    pdf_url[:60],
                    norm_doi,
                    exc,
                )
                continue
            if ok and cache_path.exists() and cache_path.stat().st_size > 1024:
                return FetchResult(
                    doi=norm_doi,
                    path=cache_path,
                    source=f"{source_name}+playwright",
                )
            cache_path.unlink(missing_ok=True)

        return FetchResult(
            doi=norm_doi,
            path=None,
            source=None,
            error="no source returned a PDF (try manual fetch)",
        )

    # ------------------------------------------------------------------ #
    # Browser lifecycle (Playwright is lazy-loaded; cleaned up on close)
    # ------------------------------------------------------------------ #

    def __enter__(self) -> PdfFetcher:
        return self

    def __exit__(self, *exc_info: object) -> None:
        self.close()

    def close(self) -> None:
        """Release Playwright resources if they were lazy-initialized."""
        import contextlib

        if self._browser is not None:
            with contextlib.suppress(Exception):
                self._browser.close()
            self._browser = None
        if self._playwright is not None:
            with contextlib.suppress(Exception):
                self._playwright.stop()
            self._playwright = None

    # ------------------------------------------------------------------ #
    # Internals — one method per fallback
    # ------------------------------------------------------------------ #

    def _try_unpaywall(self, doi: str) -> Iterable[str]:
        """Yield ALL Unpaywall OA-location URLs, repositories first.

        Publishers (host_type='publisher') routinely 403 even legally-OA PDFs
        via Cloudflare bot checks. Repository mirrors (PMC, university IRs)
        almost always work. We sort repositories first, publishers last, but
        still try everything.

        Also: when an Unpaywall location references NIH PMC (which now has
        reCAPTCHA on PDF endpoints), we derive an Europe PMC URL from it.
        Europe PMC mirrors NIH PMC content and serves PDFs cleanly.
        """
        url = _UNPAYWALL_URL.format(doi=doi)
        data = self._get_json(url, params={"email": self._email})
        if not data:
            return
        locs = list(data.get("oa_locations") or [])
        locs.sort(key=lambda loc: 0 if loc.get("host_type") == "repository" else 1)

        seen: set[str] = set()
        for loc in locs:
            for key in ("url_for_pdf", "url"):
                candidate = loc.get(key)
                if not candidate or candidate in seen:
                    continue
                seen.add(candidate)
                # If this is a PMC URL, prefer the Europe PMC mirror first
                pmc_match = re.search(r"PMC(\d+)", str(candidate))
                if pmc_match and "pmc" in str(candidate).lower():
                    epmc = (
                        f"https://europepmc.org/backend/ptpmcrender.fcgi"
                        f"?accid=PMC{pmc_match.group(1)}&blobtype=pdf"
                    )
                    if epmc not in seen:
                        seen.add(epmc)
                        yield epmc
                yield str(candidate)

    def _try_openalex(self, doi: str) -> Iterable[str]:
        """OpenAlex aggregator — keyless. Often has alt mirrors Unpaywall lacks."""
        url = _OPENALEX_URL.format(doi=doi)
        data = self._get_json(url, params={"mailto": self._email})
        if not data:
            return
        # OpenAlex returns ``best_oa_location`` and ``locations`` (with OA flag)
        candidates: list[str] = []
        best = data.get("best_oa_location") or {}
        for key in ("pdf_url", "landing_page_url"):
            if best.get(key):
                candidates.append(str(best[key]))
        for loc in data.get("locations") or []:
            if not loc.get("is_oa"):
                continue
            for key in ("pdf_url", "landing_page_url"):
                if loc.get(key):
                    candidates.append(str(loc[key]))
        seen: set[str] = set()
        for c in candidates:
            if c not in seen:
                seen.add(c)
                # Promote PMC URLs to Europe PMC mirror
                pmc_match = re.search(r"PMC(\d+)", c)
                if pmc_match and "pmc" in c.lower():
                    epmc = (
                        f"https://europepmc.org/backend/ptpmcrender.fcgi"
                        f"?accid=PMC{pmc_match.group(1)}&blobtype=pdf"
                    )
                    if epmc not in seen:
                        seen.add(epmc)
                        yield epmc
                yield c

    def _try_semantic_scholar(self, doi: str) -> Iterable[str]:
        """Semantic Scholar paper graph — has direct ``openAccessPdf.url``.

        Unauthenticated tier is 100 req / 5 min; we sleep 3.5s between
        unauth calls to stay under. With ``SEMANTIC_SCHOLAR_API_KEY`` env
        var set, no rate-limit pacing is applied.
        """
        if not self._semscholar_key:
            # Pace: 100 req / 5 min = ~3s/req. Better safe than 429.
            import time

            time.sleep(_SEMSCHOLAR_UNAUTH_DELAY_SECS)

        headers: dict[str, str] = {}
        if self._semscholar_key:
            headers["x-api-key"] = self._semscholar_key

        data = self._get_json(
            _SEMSCHOLAR_URL.format(doi=doi),
            params={"fields": "openAccessPdf,externalIds"},
            extra_headers=headers,
        )
        if not data:
            return
        oa = data.get("openAccessPdf") or {}
        if oa.get("url"):
            yield str(oa["url"])

    def _try_core(self, doi: str) -> Iterable[str]:
        """CORE API — strong for institutional repository content. Requires key."""
        if not self._core_key:
            return
        # CORE search endpoint: POST with query body
        try:
            import requests  # type: ignore[import-untyped]

            resp = requests.post(
                _CORE_SEARCH_URL,
                json={"q": f'doi:"{doi}"', "limit": 5},
                headers={
                    "Authorization": f"Bearer {self._core_key}",
                    "User-Agent": self._api_user_agent,
                    "Accept": "application/json",
                },
                timeout=_REQUEST_TIMEOUT_SECS,
            )
            if resp.status_code != 200:
                return
            data = resp.json()
        except Exception:  # noqa: BLE001
            return

        for result in data.get("results", []) or []:
            if result.get("downloadUrl"):
                yield str(result["downloadUrl"])
            # CORE also exposes a ``links`` field with mirror URLs sometimes
            for link in result.get("links") or []:
                if link.get("type") == "download" and link.get("url"):
                    yield str(link["url"])

    def _try_pmc(self, doi: str) -> Iterable[str]:
        """Map DOI → PMC ID, then try Europe PMC (mirrors NIH without captcha) first.

        NIH PMC itself has put a Google reCAPTCHA wall on PDF endpoints,
        so automated scripts are blocked even on legally-OA papers.
        Europe PMC mirrors the same content and serves PDFs cleanly.
        """
        pmid_data = self._get_text(
            _PMC_DOI_LOOKUP,
            params={
                "dbfrom": "pubmed",
                "db": "pmc",
                "linkname": "pubmed_pmc",
                "term": doi,
                "tool": "verifiable-rag-bench",
                "email": self._email,
            },
        )
        if not pmid_data:
            return
        for pmcid in re.findall(r"<Id>(\d+)</Id>", pmid_data):
            # Europe PMC mirror — friendliest to scripts
            yield (f"https://europepmc.org/backend/ptpmcrender.fcgi?accid=PMC{pmcid}&blobtype=pdf")
            # NIH PMC fallback URLs (often captcha-walled now)
            yield f"https://pmc.ncbi.nlm.nih.gov/articles/PMC{pmcid}/pdf/"
            yield _PMC_PDF_URL.format(pmcid=pmcid)

    def _try_biorxiv(self, doi: str) -> Iterable[str]:
        yield from self._try_rxiv(doi, server="biorxiv")

    def _try_medrxiv(self, doi: str) -> Iterable[str]:
        yield from self._try_rxiv(doi, server="medrxiv")

    def _try_rxiv(self, doi: str, server: str) -> Iterable[str]:
        """bioRxiv / medRxiv: yield landing pages first, then direct PDF URLs.

        Direct ``.full.pdf`` URLs return 403 to bots (Cloudflare). Landing
        pages return HTML that Playwright can navigate, then the existing
        "find PDF link in page" logic clicks through with a valid session
        cookie. So we prefer landing pages for the Playwright fallback.
        """
        if not doi.startswith("10.1101/"):
            return
        # Landing pages first — Playwright finds the PDF link inside, with
        # a valid Cloudflare-passed session cookie.
        yield f"https://www.{server}.org/content/{doi}v1"
        yield f"https://www.{server}.org/content/{doi}"
        # Direct PDF URLs — these typically 403 but are kept as a backup
        # in case the requests-based pass gets lucky on a different version.
        yield f"https://www.{server}.org/content/{doi}v1.full.pdf"
        yield f"https://www.{server}.org/content/{doi}.full.pdf"

    def _try_arxiv(self, doi: str) -> Iterable[str]:
        """arXiv search by DOI; rare for biology but covers occasional preprints."""
        data = self._get_text(
            _ARXIV_QUERY,
            params={
                "search_query": f'doi:"{doi}"',
                "start": 0,
                "max_results": 1,
            },
        )
        if not data:
            return
        match = re.search(r"https?://arxiv\.org/abs/(?P<id>[\w./\-]+)", data)
        if match:
            arxiv_id = match.group("id")
            yield f"https://arxiv.org/pdf/{arxiv_id}.pdf"

    def _try_google_search(self, doi: str) -> Iterable[str]:
        """Last-resort: Google for the DOI in a real browser, take top result URLs.

        Many open-access papers are reachable via the publisher's landing page
        (which has a "Download PDF" button with a valid session cookie chain),
        but the DIRECT PDF URLs from aggregators are 403'd by Cloudflare. A
        Google search gets us to the right landing page, where Playwright's
        normal navigate-then-find-PDF-link path can succeed.

        Costs:
        * Each call burns a Playwright navigation (slow).
        * Google starts serving CAPTCHAs if we search too fast — we sleep
          ``_GOOGLE_DELAY_SECS`` between calls.

        Yields top-3 non-Google result URLs.
        """
        # Throttle to stay below Google's automated-search detection
        import time

        time.sleep(_GOOGLE_DELAY_SECS)

        try:
            browser = self._ensure_browser()
        except Exception as exc:  # noqa: BLE001 — Playwright unavailable
            logger.debug("Playwright unavailable for Google search: %s", exc)
            return

        context = browser.new_context(
            user_agent=_BROWSER_USER_AGENT,
            viewport={"width": 1280, "height": 800},
        )
        try:
            page = context.new_page()
            search_url = f"https://www.google.com/search?q={_url_quote(doi)}"
            try:
                page.goto(search_url, wait_until="domcontentloaded", timeout=30000)
            except Exception as exc:  # noqa: BLE001
                logger.debug("Google search navigation failed: %s", exc)
                return

            # Pull out the top organic result links. Google's HTML changes
            # often, so we look broadly: any <a> whose href is an http(s) URL
            # and isn't a google.com domain or a search-helper link.
            try:
                hrefs: list[str] = page.evaluate(
                    """() => {
                        const out = [];
                        const seen = new Set();
                        const links = document.querySelectorAll('a[href]');
                        for (const a of links) {
                            const h = a.getAttribute('href') || '';
                            if (!h.startsWith('http')) continue;
                            try {
                                const u = new URL(h);
                                const host = u.hostname.toLowerCase();
                                if (host.endsWith('google.com') ||
                                    host.endsWith('googleusercontent.com') ||
                                    host.endsWith('youtube.com') ||
                                    host.endsWith('webcache.googleusercontent.com')) continue;
                                if (seen.has(u.href)) continue;
                                seen.add(u.href);
                                out.push(u.href);
                                if (out.length >= 3) break;
                            } catch (e) { continue; }
                        }
                        return out;
                    }"""
                )
            except Exception as exc:  # noqa: BLE001
                logger.debug("Google result extraction failed: %s", exc)
                return
            for href in hrefs:
                yield str(href)
        finally:
            context.close()

    def _try_direct_doi(self, doi: str) -> Iterable[str]:
        """Resolve doi.org and scrape the landing page for any obvious PDF link."""
        landing = f"https://doi.org/{doi}"
        html = self._get_text(landing, allow_redirects=True)
        if not html:
            return
        # Loose heuristic — find every <a href=...pdf...>
        for match in re.finditer(r'href=["\']([^"\']+\.pdf[^"\']*)["\']', html, re.IGNORECASE):
            yield _resolve_relative(landing, match.group(1))

    # ------------------------------------------------------------------ #
    # HTTP helpers
    # ------------------------------------------------------------------ #

    def _get_json(
        self,
        url: str,
        params: dict[str, Any] | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> dict[str, Any] | None:
        import requests

        headers = {
            "User-Agent": self._api_user_agent,
            "Accept": "application/json",
        }
        if extra_headers:
            headers.update(extra_headers)
        resp = requests.get(
            url,
            params=params,
            headers=headers,
            timeout=_REQUEST_TIMEOUT_SECS,
        )
        if resp.status_code != 200:
            return None
        try:
            return resp.json()  # type: ignore[no-any-return]
        except ValueError:
            return None

    def _get_text(
        self,
        url: str,
        params: dict[str, Any] | None = None,
        allow_redirects: bool = False,
    ) -> str | None:
        import requests

        resp = requests.get(
            url,
            params=params,
            headers={"User-Agent": self._api_user_agent},
            timeout=_REQUEST_TIMEOUT_SECS,
            allow_redirects=allow_redirects,
        )
        if resp.status_code != 200:
            return None
        return str(resp.text)

    def _download(self, pdf_url: str, dest: Path) -> None:
        """Download a PDF, using a browser-like UA + Accept headers.

        Many publishers serve 403 to anything that doesn't look like a
        browser, even on legally-OA papers. The UA swap is purely cosmetic;
        the underlying access is identical.
        """
        import requests

        resp = requests.get(
            pdf_url,
            headers={
                "User-Agent": _BROWSER_USER_AGENT,
                "Accept": "application/pdf,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.9",
            },
            timeout=_REQUEST_TIMEOUT_SECS,
            stream=True,
            allow_redirects=True,
        )
        if resp.status_code != 200:
            return
        # Some publishers serve HTML error pages with PDF Content-Type spoofed,
        # so we sanity-check the magic header after writing.
        with dest.open("wb") as fh:
            for chunk in resp.iter_content(chunk_size=8192):
                if chunk:
                    fh.write(chunk)
        # Validate: real PDFs start with the "%PDF-" magic
        with dest.open("rb") as fh:
            header = fh.read(5)
        if header != b"%PDF-":
            dest.unlink(missing_ok=True)

    # ------------------------------------------------------------------ #
    # Playwright fallback — real browser to defeat bot detection
    # ------------------------------------------------------------------ #

    def _ensure_browser(self) -> Any:
        """Lazy-init a headless Chromium browser shared across all fetches."""
        if self._browser is not None:
            return self._browser
        try:
            from playwright.sync_api import sync_playwright
        except ImportError as exc:
            raise ImportError(
                "playwright is not installed. Install with: "
                "pip install playwright && python -m playwright install chromium"
            ) from exc

        self._playwright = sync_playwright().start()
        self._browser = self._playwright.chromium.launch(
            headless=True,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--no-sandbox",
            ],
        )
        return self._browser

    def _download_via_playwright(self, pdf_url: str, dest: Path) -> bool:
        """Open *pdf_url* in a real Chromium browser and capture the PDF bytes.

        The trick: when ``accept_downloads=True``, navigating to a URL that
        serves PDF triggers Chromium's download flow, NOT a normal
        ``response.body()``. We have to use ``expect_download`` to capture
        it. For HTML landing pages no download fires, so we fall through
        to scanning for a "Download PDF" link and clicking through.

        Older code used a 5s expect_download which timed out before the
        publisher's cookie wall finished setting up — by the time the second
        navigation tried, the now-pending download error'd ("Download is
        starting"). The fix: use ONE expect_download with a long timeout,
        and on its timeout fall through to HTML-scan with a fresh page.
        """
        browser = self._ensure_browser()
        context = browser.new_context(
            user_agent=_BROWSER_USER_AGENT,
            viewport={"width": 1280, "height": 800},
            accept_downloads=True,
        )
        try:
            # Strategy 1: try the URL as a download (works when URL serves
            # PDF — handles bioRxiv landing pages that auto-redirect to PDF
            # download, plus plain .pdf URLs).
            if self._try_capture_download(context, pdf_url, dest):
                return True

            # Strategy 2: treat as HTML and look for a PDF link inside.
            # Always use a FRESH page — the previous one may be in a bad
            # state from the failed download attempt.
            return self._try_html_then_pdf_link(context, pdf_url, dest)
        finally:
            context.close()

    def _try_capture_download(self, context: Any, url: str, dest: Path) -> bool:
        """Navigate to *url* expecting a PDF download to fire."""
        page = context.new_page()
        try:
            with page.expect_download(timeout=45000) as dl_info:
                # The goto often raises mid-navigation when a download starts;
                # that's expected — the expect_download still captures it.
                import contextlib
                with contextlib.suppress(Exception):
                    page.goto(url, wait_until="domcontentloaded", timeout=60000)
            download = dl_info.value
            download.save_as(str(dest))
            if _is_pdf_file(dest):
                return True
            dest.unlink(missing_ok=True)
            return False
        except Exception:
            # Timeout (no download fired) or other error — caller falls back
            return False
        finally:
            import contextlib
            with contextlib.suppress(Exception):
                page.close()

    def _try_html_then_pdf_link(self, context: Any, url: str, dest: Path) -> bool:
        """Navigate to a URL as HTML; if found, look for a PDF link and click.

        We use ``wait_until="domcontentloaded"`` (not ``networkidle``) here
        because publisher landing pages load endless analytics / ads scripts
        that never let ``networkidle`` fire within timeout. We don't need
        a fully quiet network to find a static ``<a href=...pdf>`` link.
        """
        page = context.new_page()
        try:
            try:
                response = page.goto(url, wait_until="domcontentloaded", timeout=30000)
            except Exception:
                return False
            if response is None or not response.ok:
                return False

            ctype = (response.headers.get("content-type") or "").lower()
            if "application/pdf" in ctype:
                # Inline-rendered PDF — grab the bytes directly
                body = response.body()
                if body[:5] == b"%PDF-":
                    dest.write_bytes(body)
                    return True
                return False

            # HTML page — find a PDF link
            pdf_link = self._find_pdf_link_in_page(page)
            if not pdf_link:
                return False
        finally:
            import contextlib
            with contextlib.suppress(Exception):
                page.close()

        # Got a link — try it as a download (preserves session cookies because
        # we reuse the same context).
        return self._try_capture_download(context, pdf_link, dest)

    @staticmethod
    def _find_pdf_link_in_page(page: Any) -> str | None:
        """Find the first ``<a href=...pdf...>`` on the current page."""
        try:
            href = page.evaluate(
                """() => {
                    const links = document.querySelectorAll('a[href]');
                    for (const a of links) {
                        const h = a.getAttribute('href') || '';
                        if (h.match(/\\.pdf($|\\?)/i)) return new URL(h, location.href).href;
                    }
                    return null;
                }"""
            )
            return str(href) if href else None
        except Exception:  # noqa: BLE001
            return None

    # ------------------------------------------------------------------ #
    # Cache layout
    # ------------------------------------------------------------------ #

    def _cache_path(self, doi: str) -> Path:
        digest = hashlib.sha256(doi.encode("utf-8")).hexdigest()[:16]
        return self._cache_dir / f"{digest}.pdf"


# --------------------------------------------------------------------------- #
# Module-level helpers
# --------------------------------------------------------------------------- #


def _is_pdf_file(path: Path) -> bool:
    """Quick check that a downloaded file actually starts with PDF magic."""
    try:
        with path.open("rb") as fh:
            return fh.read(5) == b"%PDF-"
    except OSError:
        return False


def _url_quote(s: str) -> str:
    """URL-encode for use in a query string."""
    from urllib.parse import quote_plus

    return quote_plus(s)


def _normalize_doi(doi: str) -> str:
    """Strip URL prefixes and whitespace to produce a bare DOI string."""
    if not doi:
        return ""
    s = doi.strip()
    # Common prefixes
    for prefix in (
        "https://doi.org/",
        "http://doi.org/",
        "https://dx.doi.org/",
        "http://dx.doi.org/",
        "doi:",
    ):
        if s.lower().startswith(prefix):
            s = s[len(prefix) :]
            break
    return s.strip()


def _resolve_relative(base: str, href: str) -> str:
    """Turn a relative ``href`` into an absolute URL relative to ``base``."""
    from urllib.parse import urljoin

    return urljoin(base, href)
