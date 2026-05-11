# Eval Report: harry_potter_micro

- **Pipeline:** `groq/llama-3.3-70b-versatile | bge-small | hybrid(BM25+lance) | min_tokens=150 | top_k=15 | loose`
- **Run at:** 2026-05-10 23:01:51
- **Questions:** 15
- **Errors:** 15

## Aggregate metrics

| Metric | Value |
|---|---|
| `citation_precision` | 1.000 |
| `citation_recall` | 1.000 |
| `citation_f1` | 1.000 |
| `coverage` | 1.000 |
| `localization_accuracy` | 0.000 |
| `abstention_precision` | 1.000 |
| `abstention_recall` | 1.000 |
| `abstention_f1` | 1.000 |

## Per-question results

| ID | Refused | Should refuse | Cited ∩ Gold | Cited | Gold | Faith |
|---|---|---|---|---|---|---|
| `hp_quidditch_basics` | ✗ | ✗ | 0 | 0 | 3 | 0.00 ⚠️ RateLimitError: litellm.RateLimitError: RateLimitError: GroqException - {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kr2sdwkqf1396h731pjeyc0q` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 91386, Requested 9381. Please try again in 11m2.688s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing","type":"tokens","code":"rate_limit_exceeded"}}
 |
| `hp_voldemort_killed_parents` | ✗ | ✗ | 0 | 0 | 4 | 0.00 ⚠️ RateLimitError: litellm.RateLimitError: RateLimitError: GroqException - {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kr2sdwkqf1396h731pjeyc0q` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 91371, Requested 10836. Please try again in 31m46.848s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing","type":"tokens","code":"rate_limit_exceeded"}}
 |
| `hp_three_headed_dog_name` | ✗ | ✗ | 0 | 0 | 5 | 0.00 ⚠️ RateLimitError: litellm.RateLimitError: RateLimitError: GroqException - {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kr2sdwkqf1396h731pjeyc0q` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 91357, Requested 9781. Please try again in 16m23.232s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing","type":"tokens","code":"rate_limit_exceeded"}}
 |
| `hp_hagrid_dragon_name` | ✗ | ✗ | 0 | 0 | 3 | 0.00 ⚠️ RateLimitError: litellm.RateLimitError: RateLimitError: GroqException - {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kr2sdwkqf1396h731pjeyc0q` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 91342, Requested 10818. Please try again in 31m6.24s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing","type":"tokens","code":"rate_limit_exceeded"}}
 |
| `hp_mirror_of_erised` | ✗ | ✗ | 0 | 0 | 3 | 0.00 ⚠️ RateLimitError: litellm.RateLimitError: RateLimitError: GroqException - {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kr2sdwkqf1396h731pjeyc0q` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 91327, Requested 10337. Please try again in 23m57.696s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing","type":"tokens","code":"rate_limit_exceeded"}}
 |
| `hp_why_famous` | ✗ | ✗ | 0 | 0 | 4 | 0.00 ⚠️ RateLimitError: litellm.RateLimitError: RateLimitError: GroqException - {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kr2sdwkqf1396h731pjeyc0q` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 91312, Requested 10987. Please try again in 33m6.336s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing","type":"tokens","code":"rate_limit_exceeded"}}
 |
| `hp_hagrid_reveals_wizard` | ✗ | ✗ | 0 | 0 | 2 | 0.00 ⚠️ RateLimitError: litellm.RateLimitError: RateLimitError: GroqException - {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kr2sdwkqf1396h731pjeyc0q` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 91297, Requested 10060. Please try again in 19m32.448s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing","type":"tokens","code":"rate_limit_exceeded"}}
 |
| `hp_platform` | ✗ | ✗ | 0 | 0 | 4 | 0.00 ⚠️ RateLimitError: litellm.RateLimitError: RateLimitError: GroqException - {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kr2sdwkqf1396h731pjeyc0q` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 91282, Requested 11175. Please try again in 35m22.848s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing","type":"tokens","code":"rate_limit_exceeded"}}
 |
| `hp_sorcerers_stone` | ✗ | ✗ | 0 | 0 | 3 | 0.00 ⚠️ RateLimitError: litellm.RateLimitError: RateLimitError: GroqException - {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kr2sdwkqf1396h731pjeyc0q` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 91267, Requested 10914. Please try again in 31m24.384s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing","type":"tokens","code":"rate_limit_exceeded"}}
 |
| `hp_sorting_hat_not_slytherin` | ✗ | ✗ | 0 | 0 | 2 | 0.00 ⚠️ RateLimitError: litellm.RateLimitError: RateLimitError: GroqException - {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kr2sdwkqf1396h731pjeyc0q` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 91252, Requested 9392. Please try again in 9m16.416s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing","type":"tokens","code":"rate_limit_exceeded"}}
 |
| `hp_potter_called_sorting` | ✗ | ✗ | 0 | 0 | 1 | 0.00 ⚠️ RateLimitError: litellm.RateLimitError: RateLimitError: GroqException - {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kr2sdwkqf1396h731pjeyc0q` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 91237, Requested 10472. Please try again in 24m36.576s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing","type":"tokens","code":"rate_limit_exceeded"}}
 |
| `hp_lily_james` | ✗ | ✗ | 0 | 0 | 2 | 0.00 ⚠️ RateLimitError: litellm.RateLimitError: RateLimitError: GroqException - {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kr2sdwkqf1396h731pjeyc0q` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 91222, Requested 11033. Please try again in 32m28.32s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing","type":"tokens","code":"rate_limit_exceeded"}}
 |
| `hp_refuse_favorite_color` | ✗ | ✓ | 0 | 0 | 0 | 0.00 ⚠️ RateLimitError: litellm.RateLimitError: RateLimitError: GroqException - {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kr2sdwkqf1396h731pjeyc0q` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 91207, Requested 11041. Please try again in 32m22.272s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing","type":"tokens","code":"rate_limit_exceeded"}}
 |
| `hp_refuse_triwizard` | ✗ | ✓ | 0 | 0 | 0 | 0.00 ⚠️ RateLimitError: litellm.RateLimitError: RateLimitError: GroqException - {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kr2sdwkqf1396h731pjeyc0q` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 91192, Requested 10943. Please try again in 30m44.64s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing","type":"tokens","code":"rate_limit_exceeded"}}
 |
| `hp_refuse_horcrux` | ✗ | ✓ | 0 | 0 | 0 | 0.00 ⚠️ RateLimitError: litellm.RateLimitError: RateLimitError: GroqException - {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kr2sdwkqf1396h731pjeyc0q` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 91178, Requested 10607. Please try again in 25m42.24s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing","type":"tokens","code":"rate_limit_exceeded"}}
 |

## Per-question answers

### `hp_quidditch_basics`
**Error:** RateLimitError: litellm.RateLimitError: RateLimitError: GroqException - {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kr2sdwkqf1396h731pjeyc0q` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 91386, Requested 9381. Please try again in 11m2.688s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing","type":"tokens","code":"rate_limit_exceeded"}}


### `hp_voldemort_killed_parents`
**Error:** RateLimitError: litellm.RateLimitError: RateLimitError: GroqException - {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kr2sdwkqf1396h731pjeyc0q` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 91371, Requested 10836. Please try again in 31m46.848s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing","type":"tokens","code":"rate_limit_exceeded"}}


### `hp_three_headed_dog_name`
**Error:** RateLimitError: litellm.RateLimitError: RateLimitError: GroqException - {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kr2sdwkqf1396h731pjeyc0q` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 91357, Requested 9781. Please try again in 16m23.232s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing","type":"tokens","code":"rate_limit_exceeded"}}


### `hp_hagrid_dragon_name`
**Error:** RateLimitError: litellm.RateLimitError: RateLimitError: GroqException - {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kr2sdwkqf1396h731pjeyc0q` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 91342, Requested 10818. Please try again in 31m6.24s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing","type":"tokens","code":"rate_limit_exceeded"}}


### `hp_mirror_of_erised`
**Error:** RateLimitError: litellm.RateLimitError: RateLimitError: GroqException - {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kr2sdwkqf1396h731pjeyc0q` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 91327, Requested 10337. Please try again in 23m57.696s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing","type":"tokens","code":"rate_limit_exceeded"}}


### `hp_why_famous`
**Error:** RateLimitError: litellm.RateLimitError: RateLimitError: GroqException - {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kr2sdwkqf1396h731pjeyc0q` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 91312, Requested 10987. Please try again in 33m6.336s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing","type":"tokens","code":"rate_limit_exceeded"}}


### `hp_hagrid_reveals_wizard`
**Error:** RateLimitError: litellm.RateLimitError: RateLimitError: GroqException - {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kr2sdwkqf1396h731pjeyc0q` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 91297, Requested 10060. Please try again in 19m32.448s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing","type":"tokens","code":"rate_limit_exceeded"}}


### `hp_platform`
**Error:** RateLimitError: litellm.RateLimitError: RateLimitError: GroqException - {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kr2sdwkqf1396h731pjeyc0q` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 91282, Requested 11175. Please try again in 35m22.848s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing","type":"tokens","code":"rate_limit_exceeded"}}


### `hp_sorcerers_stone`
**Error:** RateLimitError: litellm.RateLimitError: RateLimitError: GroqException - {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kr2sdwkqf1396h731pjeyc0q` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 91267, Requested 10914. Please try again in 31m24.384s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing","type":"tokens","code":"rate_limit_exceeded"}}


### `hp_sorting_hat_not_slytherin`
**Error:** RateLimitError: litellm.RateLimitError: RateLimitError: GroqException - {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kr2sdwkqf1396h731pjeyc0q` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 91252, Requested 9392. Please try again in 9m16.416s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing","type":"tokens","code":"rate_limit_exceeded"}}


### `hp_potter_called_sorting`
**Error:** RateLimitError: litellm.RateLimitError: RateLimitError: GroqException - {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kr2sdwkqf1396h731pjeyc0q` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 91237, Requested 10472. Please try again in 24m36.576s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing","type":"tokens","code":"rate_limit_exceeded"}}


### `hp_lily_james`
**Error:** RateLimitError: litellm.RateLimitError: RateLimitError: GroqException - {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kr2sdwkqf1396h731pjeyc0q` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 91222, Requested 11033. Please try again in 32m28.32s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing","type":"tokens","code":"rate_limit_exceeded"}}


### `hp_refuse_favorite_color`
**Error:** RateLimitError: litellm.RateLimitError: RateLimitError: GroqException - {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kr2sdwkqf1396h731pjeyc0q` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 91207, Requested 11041. Please try again in 32m22.272s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing","type":"tokens","code":"rate_limit_exceeded"}}


### `hp_refuse_triwizard`
**Error:** RateLimitError: litellm.RateLimitError: RateLimitError: GroqException - {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kr2sdwkqf1396h731pjeyc0q` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 91192, Requested 10943. Please try again in 30m44.64s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing","type":"tokens","code":"rate_limit_exceeded"}}


### `hp_refuse_horcrux`
**Error:** RateLimitError: litellm.RateLimitError: RateLimitError: GroqException - {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kr2sdwkqf1396h731pjeyc0q` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 91178, Requested 10607. Please try again in 25m42.24s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing","type":"tokens","code":"rate_limit_exceeded"}}

