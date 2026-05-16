# Eval Report: litqa2

- **Pipeline:** `anthropic/claude-haiku-4-5 | bge-small | hybrid(BM25+lance) | min_tokens=100 | bge-rerank-v2-m3 | retrieve=80/rerank=8 | no-verifier | loose`
- **Run at:** 2026-05-16 02:36:17
- **Questions:** 186
- **Errors:** 1

## Aggregate metrics

| Metric | Value |
|---|---|
| `citation_precision` | 0.688 |
| `citation_recall` | 0.489 |
| `citation_f1` | 0.402 |
| `coverage` | 0.638 |
| `localization_accuracy` | 0.362 |
| `abstention_precision` | 0.000 |
| `abstention_recall` | 1.000 |
| `abstention_f1` | 0.000 |
| `mc_correct` | 55.000 |
| `mc_wrong` | 4.000 |
| `mc_unanswered` | 126.000 |
| `mc_accuracy_over_answered` | 0.932 |
| `mc_accuracy_over_all` | 0.297 |

## Per-question results

| ID | Refused | Should refuse | Cited ∩ Gold | Cited | Gold | Faith |
|---|---|---|---|---|---|---|
| `e3b5a4af-41d9-48db-becf-29a08d0ad28e` | ✗ | ✗ | 0 | 2 | 0 | 0.98 |
| `76184ccf-4bf0-469e-a442-11d04b4ff8b0` | ✓ | ✗ | 0 | 0 | 1 | 0.31 |
| `39129e1c-096f-4414-bf4f-37fadbbe364c` | ✗ | ✗ | 1 | 1 | 5 | 0.45 |
| `27234279-f50c-4cfc-86e2-af68364a8f94` | ✓ | ✗ | 0 | 0 | 3 | 0.33 |
| `517e7cf8-c5d2-4391-9e2a-235b79d93050` | ✗ | ✗ | 1 | 1 | 1 | 0.70 |
| `cb710074-73a8-4407-b0c7-7dc868f1bc76` | ✓ | ✗ | 0 | 0 | 14 | 0.75 |
| `5c4c602c-9624-4eae-ac44-efe4c0dd10e6` | ✗ | ✗ | 1 | 1 | 1 | 0.55 |
| `c9bdb9b5-28c1-44da-93b6-b1fc9d8bf369` | ✗ | ✗ | 1 | 1 | 9 | 0.90 |
| `e6b0f9e5-e976-47dc-b839-0b2fca967e9e` | ✗ | ✗ | 1 | 1 | 12 | 0.69 |
| `247eeb85-a552-4b87-b83e-327538fcb8a9` | ✗ | ✗ | 0 | 0 | 0 | 0.81 |
| `a214f5f8-0de8-43cf-82e0-7930003e4a0c` | ✗ | ✗ | 1 | 1 | 7 | 0.34 |
| `a43e5166-d0e8-48f8-a113-648acac7ed59` | ✗ | ✗ | 1 | 1 | 1 | 0.62 |
| `dd29920d-cb70-440f-961c-3e1103776c4f` | ✗ | ✗ | 1 | 1 | 1 | 0.87 |
| `7d805bb8-4c7c-431f-b068-acf5e5459985` | ✗ | ✗ | 0 | 3 | 1 | 0.98 |
| `8d7fa642-ee46-4a13-8ea9-61cc2d4f4ddd` | ✗ | ✗ | 1 | 1 | 6 | 0.84 |
| `487539f9-2f17-4009-aa4a-c41322445f11` | ✗ | ✗ | 0 | 0 | 0 | 0.72 |
| `5049c648-b1bb-4624-8824-9d93dfb04e51` | ✗ | ✗ | 1 | 2 | 1 | 0.60 |
| `a18883e9-218a-4719-8d2c-cf94d740de1a` | ✓ | ✗ | 0 | 0 | 3 | 0.88 |
| `d7833c0f-2a16-40d2-b6a0-6764aa3003a6` | ✗ | ✗ | 0 | 0 | 0 | 0.97 |
| `1ccdc348-50e1-4941-9151-5e50411a2b41` | ✗ | ✗ | 1 | 1 | 1 | 0.97 |
| `1e5f5199-84f4-4133-ab87-2372fa6ca722` | ✓ | ✗ | 0 | 0 | 0 | 0.59 |
| `d2860d38-dfb9-4b80-905f-812c32573915` | ✗ | ✗ | 1 | 1 | 1 | 0.48 |
| `77a41274-cd9c-48bc-a347-e0746907840d` | ✗ | ✗ | 1 | 4 | 2 | 0.78 |
| `5a2128ad-3127-4595-b810-db128d1a2335` | ✓ | ✗ | 0 | 0 | 4 | 0.40 |
| `d65103ae-c881-4116-a0a7-1b233eb6275a` | ✗ | ✗ | 1 | 1 | 5 | 0.36 |
| `ab5eb050-d134-4445-9307-6faa08be7474` | ✗ | ✗ | 1 | 1 | 7 | 0.23 |
| `82de3e92-abe2-46ac-ad17-23417b9c4da7` | ✗ | ✗ | 1 | 1 | 4 | 0.91 |
| `7cf0fcde-fea8-420c-8531-2f2fe9e38980` | ✗ | ✗ | 2 | 4 | 3 | 0.32 |
| `da5b2a8f-ba08-4692-851f-2e0bf142a02f` | ✗ | ✗ | 0 | 3 | 1 | 0.84 |
| `e2fb56b7-08cd-4dc0-bc63-b45931a74fc9` | ✓ | ✗ | 0 | 0 | 1 | 0.66 |
| `eda34fde-798e-43a1-a9d3-a804d3d8ee4e` | ✓ | ✗ | 0 | 0 | 5 | 0.93 |
| `0eede7a8-fe1f-42d3-a2c6-478083648644` | ✗ | ✗ | 2 | 2 | 2 | 0.94 |
| `d1307e50-3c03-4c76-81ee-2decb5de5f14` | ✓ | ✗ | 0 | 0 | 0 | 0.19 |
| `10cece36-a507-4a93-9600-13f3e0e677f8` | ✗ | ✗ | 1 | 4 | 2 | 0.51 |
| `f5a84803-3917-43eb-801b-8dc0c5400da1` | ✗ | ✗ | 1 | 5 | 1 | 0.88 |
| `c47dd378-dde3-4a45-9184-6abfa6163717` | ✗ | ✗ | 1 | 2 | 1 | 0.81 |
| `0bac8974-554c-439a-a9a2-22fa509c8d5d` | ✗ | ✗ | 1 | 3 | 2 | 0.69 |
| `aaa85379-1e4b-4642-9ec4-e1a6d6c29c3b` | ✗ | ✗ | 0 | 2 | 0 | 0.96 |
| `aa1835b2-2b1c-4986-b7af-e174da0124b0` | ✗ | ✗ | 1 | 1 | 1 | 0.48 |
| `5a9c6697-a65c-49c0-9e02-38b2a276fde7` | ✗ | ✗ | 1 | 1 | 1 | 0.83 |
| `37a4d007-793e-4a89-922a-c1b05f4f82c1` | ✓ | ✗ | 0 | 0 | 1 | 0.28 |
| `c9baf8e0-c4c7-4ba3-b5c4-18e9af8b2df1` | ✗ | ✗ | 0 | 1 | 2 | 0.66 |
| `d0f69626-66ee-4807-937d-c3a024441812` | ✗ | ✗ | 0 | 1 | 4 | 0.92 |
| `462a9f38-7cbe-4e12-a6e2-b1d7028c3a8b` | ✗ | ✗ | 1 | 1 | 1 | 0.65 |
| `86f111e5-402b-4ef5-b101-8be1bf5be7c6` | ✗ | ✗ | 1 | 1 | 1 | 0.84 |
| `cbe93a43-09cd-4cb4-9edd-f22fe8c28415` | ✗ | ✗ | 0 | 1 | 2 | 0.40 |
| `7a88e6f7-fb8e-4a24-b08d-9b7a6edafe57` | ✗ | ✗ | 0 | 0 | 0 | 0.77 |
| `91387526-9268-4a3c-9abe-73819707d0b0` | ✗ | ✗ | 1 | 1 | 1 | 0.93 |
| `7b98796f-25be-4c58-a52a-4e366c0ffd95` | ✗ | ✗ | 1 | 1 | 4 | 0.86 |
| `5e20e26d-6192-4563-abb3-a4857e3dbc7c` | ✗ | ✗ | 1 | 1 | 2 | 0.84 |
| `b105af85-833e-48bc-ac78-48f73c9673fd` | ✗ | ✗ | 1 | 4 | 5 | 0.70 |
| `5b6d6f82-a585-4aa8-9fe6-e7d35f7cb2ae` | ✓ | ✗ | 0 | 0 | 0 | 0.53 |
| `12321eab-6ad6-4218-8815-18bc51c14544` | ✗ | ✗ | 1 | 2 | 1 | 0.85 |
| `c33446f6-fbff-4186-8a51-28a17f68bd40` | ✗ | ✗ | 1 | 5 | 2 | 0.55 |
| `b1d5a5f5-6e89-4dfb-b60d-5a9824b015f3` | ✗ | ✗ | 0 | 3 | 0 | 0.89 |
| `6aa10957-bdd9-4dab-a4e1-234a17cb87dd` | ✗ | ✗ | 1 | 1 | 1 | 0.77 |
| `28ebecdf-949e-4d20-aca9-5989b7a9d6e9` | ✓ | ✗ | 0 | 0 | 2 | 0.88 |
| `dbb51a1c-f9a2-4960-a93c-118957659790` | ✗ | ✗ | 1 | 1 | 7 | 0.39 |
| `85c67ef3-322c-42b4-b745-c05e07e7b8ac` | ✗ | ✗ | 1 | 1 | 6 | 0.82 |
| `653635b7-3bc6-4a7b-98c7-c02038c0e928` | ✗ | ✗ | 1 | 1 | 1 | 0.44 |
| `100b570f-1c4f-4214-8402-f1b15f9989b4` | ✗ | ✗ | 1 | 1 | 4 | 0.48 |
| `0a9d6516-95ef-4d7b-a28d-d7cde27b7b55` | ✗ | ✗ | 1 | 2 | 1 | 0.67 |
| `8d61a14b-60ef-43b0-8003-b60cb6657428` | ✓ | ✗ | 0 | 0 | 0 | 0.08 |
| `4d4cb121-9525-499a-9475-9b212465c72d` | ✓ | ✗ | 0 | 0 | 0 | 0.26 |
| `ca4c9d21-b842-4875-9a6a-bcb9f6c55073` | ✗ | ✗ | 0 | 1 | 7 | 1.00 |
| `c3816cb5-8c87-4946-b133-43f415ab6b2a` | ✓ | ✗ | 0 | 0 | 16 | 0.12 |
| `59745f75-52bf-4815-905c-3dfad1ef8923` | ✓ | ✗ | 0 | 0 | 0 | 0.03 |
| `26691c84-514b-4712-a43e-09705d681e45` | ✓ | ✗ | 0 | 0 | 1 | 0.59 |
| `0e53a08c-4252-4a84-962b-5b396f9740aa` | ✓ | ✗ | 0 | 0 | 0 | 0.00 |
| `8ade3e3a-4792-4965-b9d9-05e528ebbfa0` | ✗ | ✗ | 0 | 2 | 0 | 0.31 |
| `f5a4b449-e647-4ae0-8419-c221792482c9` | ✗ | ✗ | 0 | 3 | 5 | 0.53 |
| `5806ed2a-1005-44f1-8d70-332048fea8f4` | ✗ | ✗ | 0 | 2 | 1 | 0.62 |
| `6fff0994-6d02-470a-9d61-8e35420412b6` | ✗ | ✗ | 1 | 1 | 5 | 0.74 |
| `8266ac61-92d6-423d-8e7a-fe47b3a7e885` | ✗ | ✗ | 1 | 1 | 12 | 0.98 |
| `322454df-45a8-41b3-9b0a-4e808144023c` | ✓ | ✗ | 0 | 0 | 0 | 0.47 |
| `3c9f23e2-fdd0-431b-aca7-4f9556c78f1f` | ✗ | ✗ | 0 | 0 | 0 | 0.00 ⚠️ InternalServerError: litellm.InternalServerError: AnthropicError - {"type":"error","error":{"type":"overloaded_error","message":"Overloaded"},"request_id":"req_011Cb5skjDnGunFxtSK4Pg9S"} |
| `983f1ef5-fc7d-4f4a-8f48-e704641eae12` | ✗ | ✗ | 1 | 1 | 2 | 0.51 |
| `7d2c8d44-ecf3-40d2-ab69-b6195c46ffe9` | ✗ | ✗ | 1 | 6 | 1 | 0.75 |
| `720e20c2-9ad1-4d98-9f01-8b7fb3782a46` | ✗ | ✗ | 0 | 1 | 3 | 0.84 |
| `dbfbae3d-62f6-4710-8d13-8ce4c8485567` | ✗ | ✗ | 1 | 1 | 1 | 0.31 |
| `7a42c784-7ae0-48fe-a71f-0a547b8fabb3` | ✗ | ✗ | 0 | 0 | 0 | 0.25 |
| `0708b62f-9652-49eb-8ba6-28878afa7445` | ✓ | ✗ | 0 | 0 | 4 | 0.84 |
| `5b3b7d05-9e54-445c-b374-d4c6b60923b4` | ✗ | ✗ | 1 | 1 | 1 | 0.21 |
| `623a831f-41ee-4e0e-936a-87f93d96369e` | ✗ | ✗ | 0 | 1 | 0 | 0.81 |
| `0b1d5537-db47-420c-984b-9b56d38e6d98` | ✓ | ✗ | 0 | 0 | 1 | 0.34 |
| `ade96656-7ed1-4e21-b009-b7a73e13bff5` | ✗ | ✗ | 0 | 3 | 0 | 0.52 |
| `78a2c1d2-f035-4c7d-a7ee-40dfd95ca88a` | ✗ | ✗ | 1 | 1 | 1 | 0.91 |
| `224efcd7-3652-47f8-84dd-15b4c6fafae2` | ✗ | ✗ | 1 | 1 | 2 | 0.81 |
| `55187fb4-e7ee-4027-b74f-cab50f328442` | ✗ | ✗ | 1 | 3 | 1 | 0.81 |
| `25a9cf59-1c28-4ddf-b797-f43efb9349e6` | ✗ | ✗ | 1 | 2 | 11 | 0.64 |
| `12a20d8d-cd49-47eb-9a19-6a38519ee3dc` | ✗ | ✗ | 1 | 1 | 1 | 0.83 |
| `4bb69c9d-2485-42d2-b8aa-aa647b407ca4` | ✗ | ✗ | 0 | 2 | 0 | 0.65 |
| `8c833521-56c4-458d-8c65-2bbf66190cae` | ✗ | ✗ | 1 | 1 | 1 | 0.74 |
| `255fd5fb-9623-4030-8bf2-253247df7c82` | ✗ | ✗ | 1 | 1 | 1 | 0.82 |
| `38ada695-2c79-459b-8e68-dbed734c74f9` | ✗ | ✗ | 1 | 1 | 1 | 0.80 |
| `e763edaa-b112-460a-a564-d58a6685e639` | ✗ | ✗ | 0 | 4 | 1 | 0.89 |
| `8af900bb-5794-40db-910e-10d5857ce5bd` | ✗ | ✗ | 2 | 2 | 2 | 0.50 |
| `6194ebfc-2d5c-4ccc-8883-da7c471b61e6` | ✗ | ✗ | 0 | 1 | 1 | 0.33 |
| `1f1b07d7-39ce-4665-9b70-4ab77e3c87aa` | ✗ | ✗ | 0 | 1 | 4 | 0.23 |
| `55668039-396e-488a-b2c3-bbe840550433` | ✗ | ✗ | 1 | 1 | 1 | 0.38 |
| `4f050bf3-27cd-4a14-8422-45df5e2bb079` | ✗ | ✗ | 1 | 1 | 1 | 0.74 |
| `cff00d08-5655-4214-97ac-8fa9504c1165` | ✓ | ✗ | 0 | 0 | 2 | 0.97 |
| `0eeb7ea9-fc80-4dee-9418-1c328c3ab653` | ✗ | ✗ | 1 | 1 | 2 | 0.87 |
| `658f7050-d137-477e-8693-26609080cecd` | ✗ | ✗ | 1 | 1 | 2 | 0.40 |
| `8696273a-7fea-411a-b6c6-0e826e1e02b5` | ✗ | ✗ | 1 | 1 | 1 | 0.78 |
| `ce6dd5f7-0706-41dd-a383-9b0d22ef00a1` | ✗ | ✗ | 1 | 1 | 1 | 0.35 |
| `400786c1-e6c6-4f46-a501-86fdd048ed88` | ✗ | ✗ | 1 | 3 | 2 | 0.97 |
| `e820cbcf-6df1-4c1c-b985-c02f39f52781` | ✗ | ✗ | 1 | 3 | 1 | 0.63 |
| `230dec20-cd02-4613-a7b1-e28058ed46fe` | ✗ | ✗ | 1 | 1 | 2 | 0.84 |
| `7975ddb0-a784-4f85-a297-c80e1cb5dcf2` | ✓ | ✗ | 0 | 0 | 0 | 0.08 |
| `a1d01019-d2b1-4619-92ec-7ea38578819f` | ✗ | ✗ | 1 | 1 | 2 | 0.75 |
| `fe074387-3765-4020-8f5d-e395d1094121` | ✗ | ✗ | 0 | 1 | 0 | 0.72 |
| `f0b6cea0-e005-47bc-be0d-9a10b219cae6` | ✓ | ✗ | 0 | 0 | 3 | 0.99 |
| `ae02d0e9-edf5-4c39-a215-3cbc8f4c565d` | ✗ | ✗ | 2 | 3 | 4 | 0.47 |
| `fd60a0e7-ba64-49a9-843a-6f5cb17c5fa9` | ✗ | ✗ | 0 | 4 | 4 | 0.27 |
| `14fd2b75-76fb-4c29-a21d-c557b2bcf2ff` | ✗ | ✗ | 1 | 1 | 4 | 0.94 |
| `e9f142f0-8ef6-47cd-b846-7283a93308d4` | ✗ | ✗ | 1 | 1 | 15 | 0.85 |
| `398ebac1-fd2d-45b1-9415-d82db4b4d83c` | ✓ | ✗ | 0 | 0 | 0 | 0.46 |
| `7e7150d6-bc73-4a29-a5b3-4ef8399ed947` | ✗ | ✗ | 1 | 1 | 1 | 0.27 |
| `58b39fab-337b-452d-b74f-84f9a188ce88` | ✓ | ✗ | 0 | 0 | 25 | 0.30 |
| `80e6571e-8f5d-496a-8ba3-9c9f5b783f5d` | ✗ | ✗ | 2 | 3 | 5 | 0.92 |
| `154e7b14-4ed5-4cf3-9149-0c4843fc62cc` | ✗ | ✗ | 1 | 1 | 1 | 0.36 |
| `a71ef7a2-31a2-460d-9ff4-32d7722353c3` | ✗ | ✗ | 1 | 1 | 1 | 0.09 |
| `c624ed31-214f-4c80-9544-5514a096b1d3` | ✓ | ✗ | 0 | 0 | 0 | 0.79 |
| `bcd2f213-c6c6-4660-af35-a7bd1c6a1170` | ✓ | ✗ | 0 | 0 | 0 | 0.45 |
| `24fae97b-03f3-48b8-b623-abf07faee02e` | ✓ | ✗ | 0 | 0 | 0 | 0.80 |
| `ce93661b-e3c4-4a7a-96b6-87492259c501` | ✓ | ✗ | 0 | 0 | 0 | 0.83 |
| `941c04dc-c89d-4a90-87b0-930625268a38` | ✗ | ✗ | 1 | 1 | 2 | 0.85 |
| `ea4ce240-2864-4ee5-9ffc-2dbda0f8f550` | ✗ | ✗ | 1 | 1 | 10 | 0.88 |
| `cff68274-4bbe-4fa0-a181-36a9af3cc0f1` | ✓ | ✗ | 0 | 0 | 0 | 0.14 |
| `2c262f91-52b6-421d-8341-8748f923459e` | ✓ | ✗ | 0 | 0 | 0 | 0.10 |
| `6f8a51e2-f7ad-4033-b43d-370348e4809f` | ✗ | ✗ | 2 | 4 | 2 | 0.76 |
| `9a0b82cb-6a99-4e50-83fc-3ef2ebd277cc` | ✓ | ✗ | 0 | 0 | 2 | 0.91 |
| `8b665114-7729-4dac-a64f-4862a5397b82` | ✗ | ✗ | 2 | 2 | 14 | 0.95 |
| `5c808548-92c4-4ae7-990c-e2df81e3c2ae` | ✓ | ✗ | 0 | 0 | 24 | 0.09 |
| `564e715f-8d30-410b-bdb5-0dc5206589a7` | ✓ | ✗ | 0 | 0 | 0 | 0.32 |
| `e90ea0fc-4659-4b20-acae-75dc4b97a101` | ✗ | ✗ | 4 | 4 | 8 | 0.82 |
| `c246753c-27d2-4ae4-8630-b9b4077ba6f6` | ✗ | ✗ | 1 | 2 | 1 | 0.73 |
| `22306bd7-7e84-415d-aebb-11c6312eb081` | ✓ | ✗ | 0 | 0 | 1 | 0.78 |
| `7d71dffb-b591-4b88-b0c6-e125a1b083b4` | ✓ | ✗ | 0 | 0 | 1 | 0.32 |
| `fca26d7c-05cf-40b0-9fd6-a63ed7950909` | ✗ | ✗ | 1 | 3 | 1 | 0.42 |
| `c6e11fac-8f9c-4cf1-aa6e-4d25731ba74f` | ✓ | ✗ | 0 | 0 | 1 | 0.59 |
| `bace5737-ba26-422a-8706-0fb1e92b689f` | ✓ | ✗ | 0 | 0 | 0 | 0.07 |
| `ff7328e2-4954-46a2-8ea3-d40b4df0c0ea` | ✗ | ✗ | 0 | 1 | 0 | 0.51 |
| `76bcaeeb-93bd-4951-99b9-cf4613de1a37` | ✗ | ✗ | 1 | 1 | 1 | 0.78 |
| `850f86d3-0139-43df-89fd-e606c30aaa8b` | ✗ | ✗ | 0 | 4 | 1 | 0.85 |
| `df061613-2591-4faa-be03-791c76375cb5` | ✗ | ✗ | 1 | 2 | 1 | 0.93 |
| `634f6745-f3b3-4cb1-9859-96ffb954b98a` | ✓ | ✗ | 0 | 0 | 0 | 0.02 |
| `d1eabedb-656f-4f89-a65f-4ed89478ba9f` | ✗ | ✗ | 0 | 2 | 2 | 0.57 |
| `58f69c8d-cb94-4021-a84f-c549a7b976e1` | ✗ | ✗ | 0 | 0 | 0 | 0.82 |
| `20980744-f9ff-4e39-a08d-106eada6900c` | ✓ | ✗ | 0 | 0 | 0 | 0.14 |
| `a6622141-68d6-418f-8e30-7a5eff3d4fa8` | ✓ | ✗ | 0 | 0 | 5 | 0.38 |
| `9fe3ff3b-60cf-472d-ab1a-2bda1868f1b4` | ✗ | ✗ | 1 | 1 | 8 | 0.66 |
| `9088251a-99fe-4b91-b6a9-375154ec4f58` | ✗ | ✗ | 1 | 1 | 1 | 0.26 |
| `b8ec372b-ae29-473e-96bc-86ff1ead24ea` | ✗ | ✗ | 1 | 4 | 34 | 0.02 |
| `a45c277e-55d9-4e7f-b1de-37fc2e19daf6` | ✗ | ✗ | 0 | 0 | 0 | 0.37 |
| `a8aa19cc-e4d1-4aa1-8c4e-2a518b4c99d6` | ✓ | ✗ | 0 | 0 | 0 | 0.23 |
| `2c3ba95c-47d5-4798-9911-ffdb11c940e4` | ✓ | ✗ | 0 | 0 | 6 | 0.92 |
| `49d2630e-9d26-4e12-89a3-3050a609abf5` | ✓ | ✗ | 0 | 0 | 0 | 0.27 |
| `c758f685-ba4a-4bf0-bd85-567c60ff1508` | ✗ | ✗ | 0 | 1 | 0 | 0.83 |
| `fd54d745-447c-4fcd-80de-463fcd3de6a4` | ✓ | ✗ | 0 | 0 | 1 | 0.51 |
| `4d11258d-ee8c-4bc7-91a8-613c7a41f139` | ✗ | ✗ | 0 | 0 | 0 | 0.88 |
| `1ff2b2e4-492e-4e35-bf33-f0fb53ab938c` | ✗ | ✗ | 1 | 1 | 6 | 0.96 |
| `178a5e56-340f-4ba8-a3e5-f024ca016f40` | ✗ | ✗ | 1 | 1 | 3 | 0.92 |
| `c75879f4-9329-4594-8f6a-c4d421f2439f` | ✗ | ✗ | 1 | 3 | 1 | 0.96 |
| `f7346ea0-5f1b-45e9-a1d6-493c754159c1` | ✗ | ✗ | 0 | 4 | 1 | 0.76 |
| `3d3fea17-c8ee-4005-94cb-d8798be696c3` | ✗ | ✗ | 1 | 3 | 5 | 0.10 |
| `ab58e166-f0b5-49ae-ac56-c38b5d6e8aad` | ✗ | ✗ | 1 | 2 | 1 | 0.46 |
| `a73b2c2d-a3ac-49e6-8e2e-44b4c1e6de94` | ✗ | ✗ | 1 | 1 | 21 | 0.74 |
| `04dbe07d-8b2c-4daf-b5b2-ef0e93f1fd2a` | ✗ | ✗ | 2 | 2 | 5 | 0.95 |
| `4a6705b5-85e5-44c1-8444-65be30192802` | ✗ | ✗ | 0 | 3 | 2 | 0.78 |
| `08397294-3d99-4790-915c-b8bcb1e9e661` | ✓ | ✗ | 0 | 0 | 2 | 0.86 |
| `837b2489-723a-4099-9b68-c2a9ea688f4d` | ✗ | ✗ | 2 | 2 | 2 | 0.20 |
| `745f5a0d-5f8f-405e-bb46-f37b3d1f0678` | ✗ | ✗ | 1 | 3 | 2 | 0.92 |
| `bca1be77-208b-4d57-ac29-05aa6d58bdbf` | ✗ | ✗ | 0 | 2 | 2 | 0.58 |
| `2dc20a2f-de54-4bfe-a34f-1ba395f342cf` | ✗ | ✗ | 1 | 3 | 6 | 0.91 |
| `afb36e40-0836-4810-909e-eabfe17dcd8b` | ✗ | ✗ | 0 | 0 | 0 | 0.92 |
| `c6f097c9-2216-4e98-af45-8101681b38ec` | ✓ | ✗ | 0 | 0 | 0 | 0.05 |
| `9f797d29-9f3a-481d-b2fe-326cbc686273` | ✗ | ✗ | 1 | 1 | 4 | 0.78 |
| `0d5cf8a7-a240-4a8f-be4e-c16712f90d79` | ✗ | ✗ | 0 | 1 | 0 | 0.52 |
| `40400348-eabb-4b25-90d1-e33589d3e5a4` | ✗ | ✗ | 3 | 4 | 4 | 0.69 |
| `ebe57888-662f-488f-ade1-c0aaffe638b1` | ✗ | ✗ | 1 | 1 | 1 | 0.81 |
| `ef07d562-fc18-43c9-8201-7a189d76eeb9` | ✗ | ✗ | 1 | 1 | 2 | 0.87 |
| `b331480e-dfc7-4e92-931a-c71f491c4795` | ✗ | ✗ | 0 | 1 | 5 | 0.84 |
| `58950824-2665-445d-939b-9512d5d01a2b` | ✓ | ✗ | 0 | 0 | 0 | 0.36 |
| `8d12cb90-73c6-4cc1-9f83-0fa9fd822e92` | ✗ | ✗ | 1 | 1 | 1 | 0.32 |

## Per-question answers

### `e3b5a4af-41d9-48db-becf-29a08d0ad28e`
> Based on the provided sources, Acinetobacter lwoffii evolved in the lab to be resistant to ciprofloxacin only. The sources indicate that "for A. lwoffii, clinical resistance was seen only for ciprofloxacin." Additionally, "A. lwoffii has a reduced capacity to evolve resistance to antibiotics compared to A. baumannii, where it only evolved resistance to ciprofloxacin."

Cited: 6795e9ad5fae6fe1-b687cf6e::s278, 6795e9ad5fae6fe1-b687cf6e::s383

### `76184ccf-4bf0-469e-a442-11d04b4ff8b0`
_Refused._

### `39129e1c-096f-4414-bf4f-37fadbbe364c`
> The majority of gene disruption phenotypes (61% of total gene phenotypes) were detected by 4 cell divisions in human neural stem cells. However, the question asks specifically about "Cas9-disrupted loci" more broadly. If the question is asking about all disrupted loci (both genes and enhancers combined), the sources do not provide a single combined fraction for that metric. The sources separately report that 61% of gene disruption phenotypes were apparent after 4 cell divisions, while 30% of enhancer disruption phenotypes were detected at this early time point.

Cited: aca6b37101ab6098-3101659e::s135

### `27234279-f50c-4cfc-86e2-af68364a8f94`
_Refused._

### `517e7cf8-c5d2-4391-9e2a-235b79d93050`
> H3.3 K36R mutants complete development and eclose at a frequency of ~80%.

Cited: 116c0e949dd415fc-61f4295b::s281

### `cb710074-73a8-4407-b0c7-7dc868f1bc76`
_Refused._

### `5c4c602c-9624-4eae-ac44-efe4c0dd10e6`
> A large oligosaccharide density was observed in the cryo-EM map of Nav1.6, attaching to Asn326.

Cited: d79480166f4ab0e3-4297b383::s79

### `c9bdb9b5-28c1-44da-93b6-b1fc9d8bf369`
> The number of tumor-infiltrating leukocytes is highest in the evening. Specifically, total leukocyte numbers peak at zeitgeber time 13 (ZT13), which corresponds to the evening time point.

Cited: 40349a281d8b56ff-7979b34d::s110

### `e6b0f9e5-e976-47dc-b839-0b2fca967e9e`
> Based on the single-nuclei RNA sequencing data, myotendinous junction myonuclei are enriched for genes involved in cell-matrix interactions.

Cited: f7c3d31ee5706405-5f6af1d3::s122

### `247eeb85-a552-4b87-b83e-327538fcb8a9`
> Based on the provided sources, 5.3% of ER+ MBC patients showed AR-negative status when evaluated by IHC.

### `a214f5f8-0de8-43cf-82e0-7930003e4a0c`
> Beta-amyrin synthase from *Saponaria vaccaria* produced the highest yield of beta-amyrin from squalene. Among the beta-amyrin synthases from *Artemisia annua*, *Arabidopsis thaliana*, *Glycyrrhiza glabra*, and *Saponaria vaccaria* that were tested, the BAS homologue from *S. vaccaria* (SvBAS) yielded the highest titre of β-amyrin.

Cited: e35c8530af941f04-9a7975aa::s100

### `a43e5166-d0e8-48f8-a113-648acac7ed59`
> From P6 to P15, TC synapse density increases 5-fold in the anterior cingulate cortex in wild-type mice.

Cited: c0b69d2af9f2e018-845b5d60::s271

### `dd29920d-cb70-440f-961c-3e1103776c4f`
> Cells with the anti-CD19 synNotch → sIL-2 circuit locally expanded by a factor of ~100 within the target tumor.

Cited: 34f4e70030aa5d35-a24b74ef::s130

### `7d805bb8-4c7c-431f-b068-acf5e5459985`
> MLH1dn expression increases editing efficiency of the PE2 editing system by 3.2-fold on average in HEK293T cells. However, when assessed across a broader range of single-base substitution edits at different genomic loci in HEK293T cells, PE4 (PE2 with MLH1dn) improved editing efficiency over PE2 by 2.0-fold on average. In MMR-proficient cell types, the PE4 system enhanced editing efficiency over PE2 by an average of 7.7-fold.

Cited: fa808d37a77e6019-79d6e54c::s256, fa808d37a77e6019-79d6e54c::s263, fa808d37a77e6019-79d6e54c::s96

### `8d7fa642-ee46-4a13-8ea9-61cc2d4f4ddd`
> A version of Apollo with a deletion of amino acids 344-360 (Apollo/Delta1 PK) had a reduced interaction with DNA-PKcs in 293T cells.

Cited: cea2facf97f5150c-660a07bf::s407

### `487539f9-2f17-4009-aa4a-c41322445f11`
> Deleting the N-terminal 53 amino acids of COSA-1 would most likely affect its ability to recruit MSH5 and ZHP3. More specifically, the N-terminal intrinsically disordered region spanning residue 1–50 is critical for this interaction. Within this region, six conserved amino acids are particularly important: P43, K44, E50, F53, P51, and D52. Mutation of all six of these residues to alanine (COSA-1-6A) nearly abolished the interactions with MSH-5 and ZHP-3.

### `5049c648-b1bb-4624-8824-9d93dfb04e51`
> Disruption of MTF1 expression in Chlamydomonas results in depletion of the entire photosynthetic apparatus. Loss of MTF1 expression had the strongest phenotype: the disruption of this gene resulted in the depletion of the entire photosynthetic apparatus and most of the chloroplast-expressed proteins. Genetic rescue of the mtf1 mutant alleviated the observed growth defect to nearly wild-type growth under high-light conditions and recovered expression of chloroplast-expressed proteins.

Cited: 9afb8ab3b1d5ff95-b03dfb72::s238, 9afb8ab3b1d5ff95-b03dfb72::s239

### `a18883e9-218a-4719-8d2c-cf94d740de1a`
_Refused._

### `d7833c0f-2a16-40d2-b6a0-6764aa3003a6`
> Yes, according to the sources, metabolic glycan labeling does both immobilize dendritic cell membrane and enhance antitumor efficacy of dendritic cell vaccine.

Metabolic glycan labeling immobilizes dendritic cell membrane: "metabolic glycan labeling can reduce the membrane mobility of DCs, which activates DCs and improves the antigen presentation and subsequent T cell priming property of DCs." More specifically, "DCs treated with azido-sugars exhibit a reduced membrane mobility" , and "stiffer membranes may contribute to receptor clustering and the activation of downstream signaling pathways." Metabolic glycan labeling enhances antitumor efficacy of dendritic cell vaccine: "Metabolic glycan labeling itself can enhance the antitumor efficacy of DC vaccines." Additionally, "azido-labeled antigen-pulsed DCs also result in improved CTL response and antitumor efficacy compared to unlabeled DCs in both prophylactic and therapeutic settings."

### `1ccdc348-50e1-4941-9151-5e50411a2b41`
> In all 17 CRISPRi screens, the average effect sizes of sgRNAs targeting coding strands within gene bodies were more than twofold higher than those targeting the template strands.

Cited: b0c70be4f4a933d3-7fb87fac::s328

### `1e5f5199-84f4-4133-ab87-2372fa6ca722`
_Refused._

### `d2860d38-dfb9-4b80-905f-812c32573915`
> Engineered strains of *Staphylococcus epidermidis* can stimulate T cells specific for non-native epitopes.

Cited: 8e4b7872a7579d54-cb6467cd::s93

### `77a41274-cd9c-48bc-a347-e0746907840d`
> Expression of human mu-opioid receptor (HsMOR) with an N-terminal yeast αPrePro sequence results in enlarged granular cells, expanded ER membranes, and relocalization of HsMOR-GFP to puncta. Additionally, removal of the RxR motif and the N-glycosylation sites decreased the percent of cells signaling by up to 40 and 28% respectively. The yeast-based αPrePro sequence dramatically decreased the maximum size of the signaling population by 72%. These cellular disruptions are suggested to result from partial HsMOR-GFP misfolding, which may be associated with premature ER exit.

Cited: 33d9e243f2ee99de-02bbb79f::s151, 33d9e243f2ee99de-02bbb79f::s173, 33d9e243f2ee99de-02bbb79f::s175, 33d9e243f2ee99de-02bbb79f::s248

### `5a2128ad-3127-4595-b810-db128d1a2335`
_Refused._

### `d65103ae-c881-4116-a0a7-1b233eb6275a`
> Regulation of gp02 occurs in the coding sequence.

Cited: d1ef96583ec64586-195f7c93::s219

### `ab5eb050-d134-4445-9307-6faa08be7474`
> Formation of the DarR dimer by interaction of the two monomers results in the burial of ~1300 Å² of surface from solvent.

Cited: 405dcaff86bce126-c6c89512::s68

### `82de3e92-abe2-46ac-ad17-23417b9c4da7`
> Grafting ECL3 from A3AR onto A2AAR (as part of chimeric receptors) caused the resulting chimeric receptors to gain the ability to bind CF101 with increased efficacy.

Cited: 23f9c4bad2271b89-675be55a::s148

### `7cf0fcde-fea8-420c-8531-2f2fe9e38980`
> Yes, researchers have assessed doing tagmentation of cDNA directly in the PCR mix without cleaning and quantifying the cDNA first. Specifically, "cDNA products after preamplification at fewer cycles could directly be tagmented without the abovementioned steps - this strategy we termed Smart-seq3xpress." The abovementioned steps that were excluded included "excessive cDNA preamplification, concentration measurements, bioanalyzer QC traces and cDNA amount normalization." In initial experiments, "we first generated libraries with low-volume RT (300 nL lysis volume) from HEK293FT cells and using a range of PCR preamplification cycles (10 to 20), that strikingly, revealed very similar gene detection without any need for additional enzymatic reaction clean-ups." However, this initial approach had limitations: "the resulting libraries were heavily biased towards 5' reads that contain the UMI at the expense of the internal reads important for full-length scRNAseq as for the established Smart-seq3 protocol, thus the resulting libraries had diminished the full-transcript coverage."

Cited: 70758b216a7dc837-240c67f2::s36, 70758b216a7dc837-240c67f2::s37, 70758b216a7dc837-240c67f2::s38, 70758b216a7dc837-240c67f2::s39

### `da5b2a8f-ba08-4692-851f-2e0bf142a02f`
> Yes, a base editing screen against splice sites in CD33 has been performed. The researchers "performed a base-editing screen against all canonical splice donor or acceptor sites present in CD33 to identify single base edits that reduced or eliminated CD33 expression in HSPCs." Multiple sgRNAs were enriched in the CD33 low population, with strong enrichment for sgRNAs targeting splice donor sites of exons 1 and 2. Additionally, "a systematic mutagenesis screen of CD33 splice sites" was performed with a different base editor protein (evoFERNY) as well.

Cited: 6acd5496cc0d3cfd-49391314::s129, 6acd5496cc0d3cfd-49391314::s131, 6acd5496cc0d3cfd-49391314::s249

### `e2fb56b7-08cd-4dc0-bc63-b45931a74fc9`
_Refused._

### `eda34fde-798e-43a1-a9d3-a804d3d8ee4e`
_Refused._

### `0eede7a8-fe1f-42d3-a2c6-478083648644`
> Both human SNVs French 2 and Indian 2 increase the affinity of the transcription factor ETS-1 to DNA. Specifically, both variants cause a subtle increase in the relative affinity of the ETS-A site from 0.15 in the reference to 0.24 in French 2 and 0.26 in Indian 2. EMSA confirms that both variants bind to ETS-1 more strongly than does the wild-type ETS-A.

Cited: ebc08bec41d51153-ab2b3568::s83, ebc08bec41d51153-ab2b3568::s84

### `d1307e50-3c03-4c76-81ee-2decb5de5f14`
_Refused._

### `10cece36-a507-4a93-9600-13f3e0e677f8`
> Removal of DNA methylation dramatically increased repeat-derived RNA, in particular from IAP elements, in DNMT-TKO neurons. Due to this 200-fold induction, IAPs comprise one-third of repeat-derived RNA, which impacts the expression of neighboring genes. The absence of DNA methylation causes rampant transcription of retrotransposons specifically in neurons. This entails reorganization of the accessibility landscape by transcription factors that are methylation sensitive, driving both genic and repeat upregulation.

Cited: 45a7bf5a940e82ae-b0a29e9c::s186, 45a7bf5a940e82ae-b0a29e9c::s187, 45a7bf5a940e82ae-b0a29e9c::s55, 45a7bf5a940e82ae-b0a29e9c::s56

### `f5a84803-3917-43eb-801b-8dc0c5400da1`
> Pexmetinib increases the rate of threonine dephosphorylation by WIP1 phosphatase 10-fold. This increase occurs because pexmetinib flips the activation loop of p38α to present pT180 for dephosphorylation by WIP1. The flipped conformation is stabilized through interactions between pexmetinib and the conserved DFG motif, where the carbonyl oxygen of pexmetinib coordinates D168 through hydrogen bonding while the indazole moiety makes hydrophobic interactions with F169. Additionally, the phosphate of pY182 makes hydrogen bonds to the sidechains of R186 and H174, and the backbone of T175, further anchoring the flipped activation loop. The flipped conformation exposes pT180 to solvent, rendering it accessible for phosphatase attack.

Cited: 1f689965a0b8b875-14dc08ae::s59, 1f689965a0b8b875-14dc08ae::s68, 1f689965a0b8b875-14dc08ae::s70, 1f689965a0b8b875-14dc08ae::s72, 1f689965a0b8b875-14dc08ae::s74

### `c47dd378-dde3-4a45-9184-6abfa6163717`
> When p300 catalytic activity is inhibited, rTetR-VP48 chromatin occupancy does not decrease. Specifically, p300 inhibition "did not observe a decrease in TF binding" compared to control conditions. BAF inhibition decreases average TF occupancy while p300 inhibition has little to no effect.

Cited: 3e070f56a44a20e5-f3eb62ec::s178, 3e070f56a44a20e5-f3eb62ec::s246

### `0bac8974-554c-439a-a9a2-22fa509c8d5d`
> Bempegaldesleukin is designed to overcome Treg affinity for IL-2 through several mechanisms:

Bempegaldesleukin is "designed to have an extended half-life, providing controlled and sustained signaling through the heterodimeric IL-2 receptor pathway (IL-2R βγ) to preferentially activate and expand effector CD8+ T and NK" cells. The drug "activates the powerful IL-2 receptor system in a controlled and biased way, tilting the balance in the tumor microenvironment toward effector T cells and away from Treg activity." Additionally, "preclinical evidence from mouse tumor models indicates that bempegaldesleukin limits intratumoral Treg proliferation and survival by way of promoting apoptosis, thereby polarizing the TME toward CD8+ T cells and consequently driving a very high CD8+/Treg ratio."

Cited: f297ec065068a1fb-b871f9c0::s109, f297ec065068a1fb-b871f9c0::s152, f297ec065068a1fb-b871f9c0::s82

### `aaa85379-1e4b-4642-9ec4-e1a6d6c29c3b`
> The panel of fluoroquinolone-resistant clinical E. coli samples used to evaluate SNIPR001 phage therapy comprised 72 strains. These strains were isolated from either fecal samples or perianal swabs of hematological cancer patients hospitalized for hematopoietic cell transplantation.

Cited: 5b90612d4398fbee-f46e1738::s1713, 5b90612d4398fbee-f46e1738::s1714

### `aa1835b2-2b1c-4986-b7af-e174da0124b0`
> In primary neurons cultured from LSL-CRISPRi mice, AAVs delivering sgHspa5 led to marked Cre-dependent neuronal death within 2 weeks of expression.

Cited: da980e1bd5938c42-2c1acbbe::s427

### `5a9c6697-a65c-49c0-9e02-38b2a276fde7`
> Two FMD cycles were the minimum required to cause a significant delay in melanoma growth.

Cited: d1755fd36d8b3c25-7928fced::s295

### `37a4d007-793e-4a89-922a-c1b05f4f82c1`
_Refused._

### `c9baf8e0-c4c7-4ba3-b5c4-18e9af8b2df1`
> The dendrogram clustered the 238 proteins into 20 unique structural clades.

Cited: 635912ff7732db5a-d3b4f268::s212

### `d0f69626-66ee-4807-937d-c3a024441812`
> There were 3,601 differential H3K27ac peaks between the queens and workers.

Cited: d37934bbe3d8f67c-d961c2b7::s111

### `462a9f38-7cbe-4e12-a6e2-b1d7028c3a8b`
> Inspection of TnG-repeat-like elements in the Homo sapiens genome revealed 18,164 distinct sites containing TnG repeats (>29 nucleotides).

Cited: 676ba1096cbf511b-b1513bb8::s209

### `86f111e5-402b-4ef5-b101-8be1bf5be7c6`
> At Braak V/VI compared to control (Braak 0), 19,638 promoters of 5,765 genes were found to be differentially methylated.

Cited: c8bdc674e9741afa-093821ac::s239

### `cbe93a43-09cd-4cb4-9edd-f22fe8c28415`
> On FORSK treatment, 7,875 phospho-sites were regulated (FDR < 0.05).

Cited: c090173e7e65c0e3-514e4135::s180

### `7a88e6f7-fb8e-4a24-b08d-9b7a6edafe57`
> Using the algorithm G4 hunter, 80 putative G4-forming sequences (PQSs) were identified within the TMPRSS2 gene.

### `91387526-9268-4a3c-9abe-73819707d0b0`
> A katE mutant strain of Acinetobacter baumannii was about 5-fold more sensitive to desiccation than the wild type.

Cited: c2cda5b607346e60-ae8acc05::s156

### `7b98796f-25be-4c58-a52a-4e366c0ffd95`
> The LIMK PDZ domain from human LIMK1 (residues 159-258) and human LIMK2 (residues 147-239) are 47% identical.

Cited: d3879bce9d87fba9-f83867bf::s80

### `5e20e26d-6192-4563-abb3-a4857e3dbc7c`
> DNA sequences with a motif surrounded by short tandem repeats (STRs) were consistently bound 0.23-0.90 kcal/mol tighter than those with a motif surrounded by random sequences.

Cited: 0ea4869095e7f1ab-e4a06775::s93

### `b105af85-833e-48bc-ac78-48f73c9673fd`
> The full-length Vibrio cholerae RfaH shares 43.6% sequence identity with E. coli RfaH. In full-length Vc RfaH, the KOW domain exhibits secondary structure elements that perfectly match the pattern of autoinhibited Ec RfaH, suggesting similar tertiary structures for Ec RfaH and Vc RfaH. However, helix α3* is 1.5 turns longer in Vc RfaH compared to Ec RfaH. Additionally, Vc RfaH has a disulfide bridge connecting strand β3* and helix α3*, which stabilizes this helix, a feature not present in Ec RfaH. These two structural features imply a stabilization of the domain interface and thus an increased affinity between the domains as compared to Ec RfaH.

Cited: f5f69f4f8c501c4d-1b1d2b64::s151, f5f69f4f8c501c4d-1b1d2b64::s153, f5f69f4f8c501c4d-1b1d2b64::s611, f5f69f4f8c501c4d-1b1d2b64::s612

### `5b6d6f82-a585-4aa8-9fe6-e7d35f7cb2ae`
_Refused._

### `12321eab-6ad6-4218-8815-18bc51c14544`
> Complete inhibition of proliferation was observed at roughly 1/10th the concentration required to arrest cell proliferation on plastic. More specifically, on the softest matrix (0.5 kPa), fibroblasts treated with 250 nM bleomycin experienced a near total growth arrest at 1/20th the required dose of plastic.

Cited: 9fcf84b83327fac1-12161dc6::s81, 9fcf84b83327fac1-12161dc6::s82

### `c33446f6-fbff-4186-8a51-28a17f68bd40`
> To perform constrained molecular dynamics of particles occupying Wyckoff positions, a subgroup G′ is defined that contains the elements of G which do not leave the particle position invariant plus an identity group element. The identity of this subgroup is not the identity transform but instead a transform that projects from a general position into the Wyckoff position. The group orbit is similarly defined on the subgroup, and the other procedures apply. To ensure particles stay in a Wyckoff position at all times, this can be accomplished via traditional constrained molecular dynamics of Lagrange multipliers. The constraints for Wyckoff sites are implemented as Lagrange multiplier constraints, and the terms can be computed analytically at each step.

Cited: 8b9ff18e3a47be61-28103adf::s115, 8b9ff18e3a47be61-28103adf::s116, 8b9ff18e3a47be61-28103adf::s119, 8b9ff18e3a47be61-28103adf::s121, 8b9ff18e3a47be61-28103adf::s183

### `b1d5a5f5-6e89-4dfb-b60d-5a9824b015f3`
> Microglia-specific Ifnar1 deletion attenuated the loss of post-synaptic terminals by selective engulfment. More specifically, while both pre- and post-synapses were reduced in normal 5XFAD brains, PSD95+ puncta density, but not synaptophysin+, was restored in 5XFAD;MKO mice. Independent analysis of another pair of excitatory pre- and post-synaptic markers showed reestablishment of GluR, but not Vglut1, in 5XFAD;MKO mice, corroborating a selective effect of microglial IFN-I signaling on post-terminals of excitatory synapses.

Cited: 531777a8384af139-4695824d::s145, 531777a8384af139-4695824d::s147, 531777a8384af139-4695824d::s47

### `6aa10957-bdd9-4dab-a4e1-234a17cb87dd`
> Neural Ifnar1 deletion restored pre-synaptic terminals in 5XFAD mice.

Cited: 531777a8384af139-4695824d::s47

### `28ebecdf-949e-4d20-aca9-5989b7a9d6e9`
_Refused._

### `dbb51a1c-f9a2-4960-a93c-118957659790`
> According to the degron index model, a Serine residue at position 3 or -8 is predicted to favor degradation in a short peptide obtained from the C-termini of a human protein sequence.

Cited: 93344b73bc0f6720-3f6b52f2::s125

### `85c67ef3-322c-42b4-b745-c05e07e7b8ac`
> In human fibroblasts, cells committed to senescence after 3-4 days of ERK activation remained committed even if ERK signaling was brought back to basal levels using inhibitors.

Cited: 039834c95dd3a676-7b222494::s98

### `653635b7-3bc6-4a7b-98c7-c02038c0e928`
> In lung adenocarcinoma, STK11 mutation was positively associated with the CD8+/IFNG+ cancer immune phenotype.

Cited: 01604c16c5a26a1f-157aef00::s369

### `100b570f-1c4f-4214-8402-f1b15f9989b4`
> The mice show a 30% decrease in rotarod performance at 12 months of age.

Cited: 09768e5cf98b5291-c38b8d49::s203

### `0a9d6516-95ef-4d7b-a28d-d7cde27b7b55`
> In pre-commitment myeloid progenitor cells, estrogen can be withdrawn for 24 or 40 hours before the cells can no longer return to their progenitor state. After inactivating ER-HOXA9 for >72 h, the cells were stably committed to differentiation and could no longer be returned to the progenitor state upon ER-HOXA9 reactivation.

Cited: aef60484f35c4136-1379b717::s191, aef60484f35c4136-1379b717::s192

### `8d61a14b-60ef-43b0-8003-b60cb6657428`
_Refused._

### `4d4cb121-9525-499a-9475-9b212465c72d`
_Refused._

### `ca4c9d21-b842-4875-9a6a-bcb9f6c55073`
> The LungMAP Human Lung CellRef identifies 48 cell types in a normal human lung.

Cited: 0bd1ca4800d9e08e-ed49ee6f::s342

### `c3816cb5-8c87-4946-b133-43f415ab6b2a`
_Refused._

### `59745f75-52bf-4815-905c-3dfad1ef8923`
_Refused._

### `26691c84-514b-4712-a43e-09705d681e45`
_Refused._

### `0e53a08c-4252-4a84-962b-5b396f9740aa`
_Refused._

### `8ade3e3a-4792-4965-b9d9-05e528ebbfa0`
> No, doublecortin is not a unique marker of newly generated granule cells in the hippocampus. Doublecortin (DCX), a widely accepted marker of newly generated granule cells, was detected in diverse human neurons, but it did not define immature neuron populations. Additionally, DCX expression was found in granule cells across species beyond just newly generated cells. DCX expression with at least one unique molecular identifier (UMI) was found in granule cells across species, with humans showing the scarcest expression.

Cited: e7d33e6c5033c2e2-30e83b44::s170, e7d33e6c5033c2e2-30e83b44::s61

### `f5a4b449-e647-4ae0-8419-c221792482c9`
> CifA is a ribonuclease (RNase) that depletes a spermatocyte lncRNA important for the histone-to-protamine transition of spermiogenesis. The specific lncRNA is the AAGAG lncRNA. lncRNA knockdown enhances cytoplasmic incompatibility, and mutagenesis links lncRNA depletion and subsequent sperm chromatin integrity changes to embryonic DNA damage and CI.

Cited: c1799acd1f08346b-7a1ba0f8::s17, c1799acd1f08346b-7a1ba0f8::s19, c1799acd1f08346b-7a1ba0f8::s76

### `5806ed2a-1005-44f1-8d70-332048fea8f4`
> Neonatal male mice injected with NIF show a significant reduction in microglial phagocytic capacity and engulfment of VGlut2. VGlut2 is a vesicular glutamate transporter, which is the neurotransmitter transporter in question.

Cited: c0b69d2af9f2e018-845b5d60::s375, c0b69d2af9f2e018-845b5d60::s377

### `6fff0994-6d02-470a-9d61-8e35420412b6`
> The causative mutation of the snog1a mutant of Physcomitrium patens is located on chromosome 8.

Cited: 68a6c661e51b59ab-413f9855::s391

### `8266ac61-92d6-423d-8e7a-fe47b3a7e885`
> Optogenetic inactivation of BNST AVP cells did not affect social communicative behaviors. Specifically, inhibition of BNST AVP cells did not affect social communicative behaviors (i.e., urine marking and ultrasonic vocalizations) in males or in females.

Cited: 38a955fae1cd37d4-f0d43e7b::s103

### `322454df-45a8-41b3-9b0a-4e808144023c`
_Refused._

### `3c9f23e2-fdd0-431b-aca7-4f9556c78f1f`
**Error:** InternalServerError: litellm.InternalServerError: AnthropicError - {"type":"error","error":{"type":"overloaded_error","message":"Overloaded"},"request_id":"req_011Cb5skjDnGunFxtSK4Pg9S"}

### `983f1ef5-fc7d-4f4a-8f48-e704641eae12`
> Relative to the common S288C strain of yeast, the Wyeast 3068 brewing strain has several deleted genes that are enriched for processes of flocculation, carbohydrate transmembrane transport, asparagine catabolism, and transposition.

Cited: 74a92b882343d335-0d4fcaac::s194

### `7d2c8d44-ecf3-40d2-ab69-b6195c46ffe9`
> Relative to wild type zebrafish embryos, those with Kif9 knocked down display the following ciliary phenotypes:

Kif9 KD embryos displayed beat defects that ranged from complete paralysis of cilia, to reduced beat frequency and disrupted waveforms. Cilia that did beat did so more slowly. Kif9 KD embryos also had shorter cilia than controls. Kif9 KD embryos displayed loss of radial spoke, inner dynein arm and outer dynein arm placement in the distal ends of cilia. The normal axonemal localization of Rsph10b was disrupted after Kif9 KD, with this defect restricted to the distal ends of the cilia. Loss of Kif9 leads to loss of the Spef1 distal tip domain.

Cited: 8061d302c8a858a8-d1033cab::s127, 8061d302c8a858a8-d1033cab::s131, 8061d302c8a858a8-d1033cab::s133, 8061d302c8a858a8-d1033cab::s201, 8061d302c8a858a8-d1033cab::s343, 8061d302c8a858a8-d1033cab::s90

### `720e20c2-9ad1-4d98-9f01-8b7fb3782a46`
> Removal of the sialic acid moieties from T-cell surfaces decreases the binding of Siglec-15 to human T cells. Specifically, the observed decrease in Siglec-15 binding upon neuraminidase A desialylation was comparable to that measured in the case of deglycosylation, indicating that the sialic acid moiety is the key unit for the binding of Siglec-15 to human T cells.

Cited: 66609914f1843fd6-9d104250::s99

### `dbfbae3d-62f6-4710-8d13-8ce4c8485567`
> SLC14A1 (solute carrier family 14 member 1) appears to be a specific marker for endothelial cells in the heart.

Cited: 83a86f1f96eceb6e-73d94b3b::s104

### `7a42c784-7ae0-48fe-a71f-0a547b8fabb3`
> All Fanzor proteins and TnpBs with a loss of the canonical glutamic acid in RuvC-II contained an alternative conserved glutamate approximately 45 residues away. For ApmFNuc specifically, this alternative conserved glutamate is E467, which was found to be in close proximity with the catalytic residues in the RuvC-I and RuvC-III motifs, suggesting that this alternative, conserved glutamate compensates for the mutation in RuvC-II.

### `0708b62f-9652-49eb-8ba6-28878afa7445`
_Refused._

### `5b3b7d05-9e54-445c-b374-d4c6b60923b4`
> The average speed of the jet for cicadas is around 0.6 to 3.16 m/s.

Cited: f597b9fbade66ea8-abe5e6df::s40

### `623a831f-41ee-4e0e-936a-87f93d96369e`
> The cavity above the p-hydroxybenzylidene moiety of the chromophore in mSandy2 is filled by the mp rotamer of Leucine at position 63. The mp rotamer is defined by the dihedral angles χ1 = gauche(−) and χ2 = gauche(+). This rotamer fills the cavity by packing tightly against it. In contrast, the alternate pt rotamer (χ1 = gauche(+), χ2 = trans) does not fill the cavity.

Cited: 9fa80155de882a7c-15748f57::s591

### `0b1d5537-db47-420c-984b-9b56d38e6d98`
_Refused._

### `ade96656-7ed1-4e21-b009-b7a73e13bff5`
> The reemergence of prenatal cellular programs is mediated by Mac2 macrophages via the chemokine CXCL8 (IL-8) interacting with ACKR1 on VE3 vascular endothelial cells in diseased skin. CellPhoneDB receptor-ligand database predicted a significant enrichment for ACKR1 on VE3 to interact with CXCL8 (IL-8) on Mac2. ACKR1 is the venular capillary marker that characterizes VE3. A re-emergence of prenatal vascular endothelial cell and macrophage cellular programs occurs in atopic dermatitis and psoriasis lesional skin.

Cited: 98bfd461c77d2ddb-abe7e939::s221, 98bfd461c77d2ddb-abe7e939::s234, 98bfd461c77d2ddb-abe7e939::s99

### `78a2c1d2-f035-4c7d-a7ee-40dfd95ca88a`
> The putative ETS transcription factor binding sites in the FoxF enhancer bind ETS with low relative affinities ranging from 0.09 to 0.24.

Cited: d344be98a61d850f-3c8cc77a::s102

### `224efcd7-3652-47f8-84dd-15b4c6fafae2`
> FOXP3 had a strong binding affinity to segment E2 of the UNC5B-AS1 upstream super enhancer region.

Cited: 3a2c0120637483ba-5adda325::s361

### `55187fb4-e7ee-4027-b74f-cab50f328442`
> Most of the upregulated genes in the Relapse signature were directly related to immune response processes. Specifically, the upregulated genes LCN2, LTF, SAA1, SAA2, and CXCL17 were strongly positively correlated with Club cells. Additionally, cells of myeloid lineage were strongly positively correlated with LTF, CCL19, and some of the immunoglobulins upregulated in the Relapse signature (IGHG3, IGKC, IGLC2).

Cited: 129870223e3a57d6-aed81b74::s137, 129870223e3a57d6-aed81b74::s138, 129870223e3a57d6-aed81b74::s55

### `25a9cf59-1c28-4ddf-b797-f43efb9349e6`
> Based on the provided sources, when comparing apoptotic and control cells measured by Cell Painting assays, the cellular features displaying the greatest difference in morphology are the mitochondria and nuclei. "We identified 367 differential morphology features between apoptosis and control group cells, with most morphology changes from the mitochondria and nuclei." This is further supported by the finding that "apoptosis had more morphology feature changes, mostly impacting mitochondria."

Cited: 324908523a45ed3e-0832d3f2::s126, 324908523a45ed3e-0832d3f2::s204

### `12a20d8d-cd49-47eb-9a19-6a38519ee3dc`
> Bone marrow stromal cell-conditioned media (SCM) did not produce significant alterations in CD8α receptor expression on cultured OT-1 T cells. Specifically, when OT-1 T-cells were cultured for 24 hours in SCM without stimulation, T-cells "did not exhibit significant alterations in their surface expression of the TCR nor the CD8α co-receptor, although a trend towards increased surface expression was noted in ACM."

Cited: 2cdfbcfbe2f97d62-25857e4e::s175

### `4bb69c9d-2485-42d2-b8aa-aa647b407ca4`
> Expression of the ATPase-deficient Spn-E-EQ mutant in silkworm BmN4 cells caused a reduction of mature piR1712 and piR2986. Concomitantly, there was an accumulation of longer RNA signals that correspond to the lengths of their pre-piRNAs.

Cited: 6f9603c4a7dfa9ed-8ee6647e::s354, 6f9603c4a7dfa9ed-8ee6647e::s355

### `8c833521-56c4-458d-8c65-2bbf66190cae`
> A. thaliana plants infected with avrE1 single mutant showed significantly higher expression levels of the ABA biosynthesis marker gene NCED3 than mock-infected plants.

Cited: ff5bb438eb6b3659-38bb2e97::s97

### `255fd5fb-9623-4030-8bf2-253247df7c82`
> A. thaliana plants infected with the avrE/hopM1 double knockout (h/a) mutant of Pst DC3000 did not show significantly higher expression levels of NCED3 compared with mock-infected plants. In contrast, plants infected with Pst DC3000 or the single hopM1 or avrE1 mutants showed significantly higher NCED3 expression levels than mock-infected plants.

Cited: ff5bb438eb6b3659-38bb2e97::s97

### `38ada695-2c79-459b-8e68-dbed734c74f9`
> A. thaliana plants infected with Pst DC3000 hopM1 single mutant showed significantly higher expression levels of the ABA biosynthesis marker gene NCED3 than mock-infected plants.

Cited: ff5bb438eb6b3659-38bb2e97::s97

### `e763edaa-b112-460a-a564-d58a6685e639`
> Prenatal maternal stress and diesel exhaust particle (DEP + MS) exposure strongly enhance the functional heterogeneity of microglia in male mice. Specifically, microglial heterogeneity was strikingly enhanced in DEP + MS male offspring anterior cingulate cortex (ACC) compared with control animals, both at P8 and P15. This enhanced heterogeneity leads to an overabundance of one specific subtype of microglia with a severely diminished phagocytic activity that eliminated fewer thalamocortical (TC) synapses. Microglia from DEP + MS males were less phagocytic and engulfed fewer synapses overall. The Iba1 lo P2ry12 hi microglial subtype, which is more abundant in DEP + MS offspring, has diminished lysosomal content and engulfs fewer TC synapses.

Cited: c0b69d2af9f2e018-845b5d60::s327, c0b69d2af9f2e018-845b5d60::s339, c0b69d2af9f2e018-845b5d60::s421, c0b69d2af9f2e018-845b5d60::s423

### `8af900bb-5794-40db-910e-10d5857ce5bd`
> Based on the provided sources, I can answer this question about bipolar interneurons in human cortex:

In human temporal and frontal cortex, bipolar (BP) interneuron axons target other interneurons at a rate of 72%. This represents an increase from 56% in mouse.

Cited: 3039597cd03cb050-e2ba21eb::s121, 3039597cd03cb050-e2ba21eb::s122

### `6194ebfc-2d5c-4ccc-8883-da7c471b61e6`
> All dopaminergic neurons (DANs) in the mushroom body received input from all sensory modalities.

Cited: 0faff73a03a57dfe-cac59605::s994

### `1f1b07d7-39ce-4665-9b70-4ab77e3c87aa`
> Only 33% (with 5- or 8-hop cascades) of octopaminergic neurons (OANs) received input from all modalities.

Cited: 0faff73a03a57dfe-cac59605::s266

### `55668039-396e-488a-b2c3-bbe840550433`
> 694 (20%) isoforms could significantly alter pseudotime upon overexpression in hESC differentiation.

Cited: 0c23610f9819876e-1c7bceee::s145

### `4f050bf3-27cd-4a14-8422-45df5e2bb079`
> In the first FST analysis conducted among the four geographical-based Iranian populations, the east and southeast: northeast pair exhibited the highest FST value (FST= 0.09).

Cited: c5e2b39b87ce68c3-3e8a42d1::s444

### `cff00d08-5655-4214-97ac-8fa9504c1165`
_Refused._

### `0eeb7ea9-fc80-4dee-9418-1c328c3ab653`
> MtNCC1's N-terminal Atx1-like domain (MtNCC1₁₋₇₈) bound one Cu⁺ per molecule with an affinity constant of 2.45 pM⁻¹.

Cited: af470b1b1a34dd6b-0ba6ac3e::s257

### `658f7050-d137-477e-8693-26609080cecd`
> The long, slender stalk of the S. coelicolor Umbrella complex structure extended about 300 Å.

Cited: 0d71c9d2055299d4-2f967140::s162

### `8696273a-7fea-411a-b6c6-0e826e1e02b5`
> In mES cells, the contact probabilities of most (~75%) active promoters with the nearest TAD boundary are lower than 0.2.

Cited: 071eed17b15b184b-5393792c::s275

### `ce6dd5f7-0706-41dd-a383-9b0d22ef00a1`
> After knockout of the Ift122 gene in Tetrahymena, Pkdh1 expression shows a drastic decrease in abundance. This suggests that nonciliary Pkdh1 may be either degraded or downregulated in Ift122 ∆-mutant cells.

Cited: 9d1bda6cef59d705-b224f6d8::s148

### `400786c1-e6c6-4f46-a501-86fdd048ed88`
> Elevated Rpn14 levels suppress the turnover of phosphorylated αsyn in yeast. Specifically, significant accumulation of phosphorylated α-syn was observed upon elevated protein level of Rpn14. These results reveal that elevated levels of Rpn14 inhibit the turnover of phosphorylated α-syn.

Cited: a95e8580727af033-09043102::s385, a95e8580727af033-09043102::s386, a95e8580727af033-09043102::s391

### `e820cbcf-6df1-4c1c-b985-c02f39f52781`
> A number of domains that were lowly expressed on their own ablated KRAB function when paired with it. For example, the poorly expressed DHX16 OB_NTP and BAZ1A DDT domains inhibited KRAB function at 100 ng/mL dox. However, increasing the dox concentration to 1000 ng/mL dox permitted some silencing for KRAB-DHX16 and full silencing for KRAB-BAZ1A, consistent with the loss of function of these KRAB fusions coming from decreased protein abundance.

Cited: 71256a6d0f955156-f438b0cb::s272, 71256a6d0f955156-f438b0cb::s273, 71256a6d0f955156-f438b0cb::s274

### `230dec20-cd02-4613-a7b1-e28058ed46fe`
> The firing rate of SMAD1-deficient PV interneurons in response to current injections was significantly reduced in the barrel cortex of adult mice.

Cited: 3b1e01c90c47dd5d-850e00fc::s206

### `7975ddb0-a784-4f85-a297-c80e1cb5dcf2`
_Refused._

### `a1d01019-d2b1-4619-92ec-7ea38578819f`
> Based on the provided sources, the mechanism for expression of the EPRS1(N1) form of EPRS1 in humans is as follows:

A novel polyadenylation event, which introduces a new stop codon, generates the EPRS1(N1) variant with a truncated C-terminus.

Cited: 3ced378716ddecf0-3008c492::s137

### `fe074387-3765-4020-8f5d-e395d1094121`
> For time-lapse continuous data generated by 2pSAM, the net rate of 3D imaging can be increased to 30 volume/s by exploiting spatiotemporal continuity and estimating motions during reconstruction with a motion-correction algorithm.

Cited: 3022f334b06fe41f-49e3ab2b::s146

### `f0b6cea0-e005-47bc-be0d-9a10b219cae6`
_Refused._

### `ae02d0e9-edf5-4c39-a215-3cbc8f4c565d`
> The phylloxera X chromosome is the second-largest chromosome at 47.28 Mb. The phylloxera genome has a total chromosome-level length of 259.64 Mb across 5 chromosomes. This means the X chromosome represents approximately 18% of the total chromosome-level assembly, making it smaller than the largest autosome but larger than at least some of the other autosomes, as the 4 autosomes are ordered from longest to shortest.

Cited: d0e434519e92b617-6d9d1707::s70, d0e434519e92b617-6d9d1707::s83, d0e434519e92b617-6d9d1707::s86

### `fd60a0e7-ba64-49a9-843a-6f5cb17c5fa9`
> The N-terminal α1-helical extension in the PF03500 protein family drives the quaternary structure assembly of these proteins. The α1-helix guides the formation of different dimerization interfaces within the tetramer, with each interface burying about 822 Å² and contributing a free energy gain of approximately 10 kcal/mol to the quaternary structure. α1 dimerization is primarily driven by symmetric hydrophobic contacts between adjoining α1-helices, as well as a combination of hydrophobic and polar interactions with the protein core of the neighboring subunit. The presence of an N-terminal hydrophobic helix in BcsD could be used as a predictor of the protein's oligomeric state and opens the potential for engineering of BcsD variants with altered quaternary structure.

Cited: ec21473ce029219d-58061129::s207, ec21473ce029219d-58061129::s208, ec21473ce029219d-58061129::s213, ec21473ce029219d-58061129::s315

### `14fd2b75-76fb-4c29-a21d-c557b2bcf2ff`
> The CDRs of P1A4 form a deep, ~12-Å pocket between the heavy and light chains.

Cited: 09d92318a4a24d0d-b1ddf424::s100

### `e9f142f0-8ef6-47cd-b846-7283a93308d4`
> The non-specific effect observed for jAspSnFR3.mRuby3 was determined to be due to an unexpected interaction with the C-terminal histidine tag.

Cited: 64c8513d404bd086-2a7ec0cf::s62

### `398ebac1-fd2d-45b1-9415-d82db4b4d83c`
_Refused._

### `7e7150d6-bc73-4a29-a5b3-4ef8399ed947`
> Ddd1 showed preferences towards editing 5'-GC substrates.

Cited: 635912ff7732db5a-d3b4f268::s379

### `58b39fab-337b-452d-b74f-84f9a188ce88`
_Refused._

### `80e6571e-8f5d-496a-8ba3-9c9f5b783f5d`
> CXCR6 and CD38 can be employed to demarcate tissue-resident memory T cells from circulating memory T cells independently of CD69 during inflammatory conditions in the murine liver. Unlike CD69, both CD38 and CXCR6 were stably expressed under inflammatory conditions, allowing for the faithful delineation of TRM cell effector capabilities. CXCR6 and CD38 expression remained similar following VV-OVA infection or after using other reactivation methods, allowing for CD69-independent TRM cell identification.

Cited: 7de06dcdff06813d-2aa4a31e::s300, 7de06dcdff06813d-2aa4a31e::s303, 7de06dcdff06813d-2aa4a31e::s449

### `154e7b14-4ed5-4cf3-9149-0c4843fc62cc`
> WT PafA is highly stable and remains folded, as inferred by circular dichroism (CD) spectra, even after exposure to 4 M urea for 14 days.

Cited: 68c9c104777ac1ed-f6f095ce::s125

### `a71ef7a2-31a2-460d-9ff4-32d7722353c3`
> Tm EndoV endonuclease mediated hydrolysis was inhibited at dNTP concentrations >2.0 mM.

Cited: f7415168f213937f-e85e09ae::s76

### `c624ed31-214f-4c80-9544-5514a096b1d3`
_Refused._

### `bcd2f213-c6c6-4660-af35-a7bd1c6a1170`
_Refused._

### `24fae97b-03f3-48b8-b623-abf07faee02e`
_Refused._

### `ce93661b-e3c4-4a7a-96b6-87492259c501`
_Refused._

### `941c04dc-c89d-4a90-87b0-930625268a38`
> At 50,000 generations in the E. coli Long Term Evolution Experiment lines, 64.0% of the non-genic windows were transcribed in at least one clone at a relaxed threshold of 1 transcript per million reads (TPM).

Cited: f9f1eafd2f81f280-86b6f479::s39

### `ea4ce240-2864-4ee5-9ffc-2dbda0f8f550`
> During infections with the T6SS-5-negative B. thailandensis (hcp-5 deletion), on average 48 galectin-3 accumulation events can be expected per 1,000 bacteria.

Cited: 634344ce13dd73ac-d812341d::s381

### `cff68274-4bbe-4fa0-a181-36a9af3cc0f1`
_Refused._

### `2c262f91-52b6-421d-8341-8748f923459e`
_Refused._

### `6f8a51e2-f7ad-4033-b43d-370348e4809f`
> MC1 H7 establishes polar contacts with the PSMD2 E336 side chain and the backbone carbonyls of PSMD2 P871 and PSMD2 L873. The neighboring MC1 R8 residue establishes a charge interaction with PSMD2 E878 and hydrogen bonds with PSMD2 H868. Residues Y9 and W10 hydrogen bond with the backbone carbonyl of PSMD2 K773 and PSMD2 N737, respectively. Finally, W12 establishes π-stacking interactions with PSMD2 H770.

Cited: 36e711a08612716e-caaa863d::s137, 36e711a08612716e-caaa863d::s138, 36e711a08612716e-caaa863d::s139, 36e711a08612716e-caaa863d::s140

### `9a0b82cb-6a99-4e50-83fc-3ef2ebd277cc`
_Refused._

### `8b665114-7729-4dac-a64f-4862a5397b82`
> Rv2780 was detected in the cytoplasm of mice peritoneal macrophages during M. tuberculosis infection. Additionally, Rv2780 was mainly detected in the cytoplasm, partially in mitochondria, very minimally in the endoplasmic reticulum (ER) or lysosome.

Cited: c31907b446aed1b3-79dfc999::s79, c31907b446aed1b3-79dfc999::s81

### `5c808548-92c4-4ae7-990c-e2df81e3c2ae`
_Refused._

### `564e715f-8d30-410b-bdb5-0dc5206589a7`
_Refused._

### `e90ea0fc-4659-4b20-acae-75dc4b97a101`
> Based on the provided sources, the CDH23 isoforms capable of localizing to the stereocilia are:

For the longest CDH23 isoform (V1), both CDH23(+68) and CDH23(-68) were localized to the stereocilia as well as in the cell body. For the second longest isoform (V2), both CDH23(+68) and CDH23(-68) were only detected in the cell body. For the shortest isoform (V3), when the HA tag was added to the N terminus, it was detected in the stereocilia as well as cell body in injectoporated hair cells. Together, V1 and V3 isoforms of CDH23 can localize to the stereocilia.

Cited: a322cf631e4099c8-c8d9416c::s145, a322cf631e4099c8-c8d9416c::s146, a322cf631e4099c8-c8d9416c::s149, a322cf631e4099c8-c8d9416c::s150

### `c246753c-27d2-4ae4-8630-b9b4077ba6f6`
> The N-terminal HORMA domain encompassing residues 1-149 is not important for yeast Rev7's interaction with the MRX complex. Cells expressing ScRev7 N-terminally truncated variants showed robust growth in selection medium similar to wild-type, indicating that they associate with the subunits of MRX complex.

Cited: 5a389cfe7cca76d2-437a07be::s321, 5a389cfe7cca76d2-437a07be::s322

### `22306bd7-7e84-415d-aebb-11c6312eb081`
_Refused._

### `7d71dffb-b591-4b88-b0c6-e125a1b083b4`
_Refused._

### `fca26d7c-05cf-40b0-9fd6-a63ed7950909`
> The SpyTag-SpyCatcher molecular glue peptide system is used to attach the INT tag to AAVs in the Vault AAV delivery system. Specifically, SpyTag003 (SpT3) was genetically inserted into the VP2 protein of AAV9, and a SpyCatcher003-INT (SpC3-INT) fusion protein was designed wherein a flexible linker connected the SpC3 and the INT peptide. AAV9-VP2-SpT3 was then mixed with SpC3-INT to induce spontaneous formation of AAV9-INT.

Cited: 2445404168635a55-0ad2b180::s153, 2445404168635a55-0ad2b180::s82, 2445404168635a55-0ad2b180::s86

### `c6e11fac-8f9c-4cf1-aa6e-4d25731ba74f`
_Refused._

### `bace5737-ba26-422a-8706-0fb1e92b689f`
_Refused._

### `ff7328e2-4954-46a2-8ea3-d40b4df0c0ea`
> Based on the provided sources, a **sodium ion** coordinates binding of cyclic tetra-adenylate to Csx23 in Vibrio cholerae. However, it should be noted that while a sodium ion is positioned at the centre of the cA₄ molecule, "it appears to make no direct or indirect interactions with cA₄ or Csx23 CTD."

Cited: 43ce81162fb1ab76-beaced53::s925

### `76bcaeeb-93bd-4951-99b9-cf4613de1a37`
> The only microcin homolog identified in all phylogroups was microcin V.

Cited: 58223b6183837ffb-65e8f6c9::s173

### `850f86d3-0139-43df-89fd-e606c30aaa8b`
> Based on the provided sources, the following mouse models of immunisation were used to demonstrate that CD90 could identify germinal center-resident follicular helper CD4+ T cells:

FoxP3 EGFP mice were footpad-immunized with 20 μg of NP-Ova+alum. S1pr2-RFP mice were footpad-immunized with 20 μg of NP-Ova+alum and treated with 5 mg tamoxifen (i.p.) at days 5-7 p.i. PAGFP Tg mice were footpad-immunized with 20 μg of NP-Ova+alum 11 days prior to analysis. B6 mice were immunized as described for immunofluorescence analysis 8 days p.i.

Cited: ee877dbbbd2e51e3-55e76368::s105, ee877dbbbd2e51e3-55e76368::s117, ee877dbbbd2e51e3-55e76368::s125, ee877dbbbd2e51e3-55e76368::s762

### `df061613-2591-4faa-be03-791c76375cb5`
> S2X35, a class I mAb, showed that each of the S371F, D405N, and R408S substitutions caused substantial decreases in binding, likely accounting for enhanced resistance of BA.2 to S2X35. In the BA.2 context, no single reversion restored S2X35 binding, suggesting an additive effect of S371F, D405N, and R408S mutations.

Cited: daca00c2dca36dc2-b25fdc82::s165, daca00c2dca36dc2-b25fdc82::s176

### `634f6745-f3b3-4cb1-9859-96ffb954b98a`
_Refused._

### `d1eabedb-656f-4f89-a65f-4ed89478ba9f`
> DILT is most effective at enhancing ER proteostasis and promoting functional, soluble forms of GCase in neurons among these three compounds. DANT and DHBP treatment elevated soluble GCase levels in cell models, although not as robustly as DILT.

Cited: f74e43a900ad6cb5-10c56ee5::s242, f74e43a900ad6cb5-10c56ee5::s244

### `58f69c8d-cb94-4021-a84f-c549a7b976e1`
> Based on the provided sources, **CXE (the optimized EXO editor) has the highest HDR efficiency among the designed DNA editors discussed**.

"The optimized EXO editor, CXE, in which hExo1 was fused to the downstream of Cas9 with XTEN linker, gave rise to the highest HDR efficiency and the lowest indel frequency." "CXE resulted in the highest HDR efficiency and lowest indel frequency among the four EXO editors and was even significantly superior to E4 and E1B." "The CXE editor enhanced the precise genome editing efficiency (relative HDR/indel ratio) up to 9.8-fold at AAVS1 locus and 2.5-fold at GAPDH locus relative to the canonical Cas9." However, if considering nickase variants, "CXE nickase editors could be a useful alternative tool for applications that require precise genome edits without DSBs," with even higher HDR/indel ratios of up to 453-fold at the AAVS1 locus.

### `20980744-f9ff-4e39-a08d-106eada6900c`
_Refused._

### `a6622141-68d6-418f-8e30-7a5eff3d4fa8`
_Refused._

### `9fe3ff3b-60cf-472d-ab1a-2bda1868f1b4`
> Based on the provided sources, when male VICs are cultured on larger polystyrene nanoparticles gels but not on smaller polystyrene nanoparticles gels, the following epigenetic change can be expected:

Increased acetylation can be expected in male VICs on larger particles, as "only larger particles affected the acetylation state" in males.

Cited: e44731dbd47b1ddf-5ac4257e::s268

### `9088251a-99fe-4b91-b6a9-375154ec4f58`
> Based on the provided sources, ZDHHC5 can lead to pyroptosis when it mediates palmitoylation of **GSDMD**.

"Recent studies have shown that ZDHHC5/9 mediates ROS-dependent palmitoylation of GSDMD at hC191/mC192 to promote plasma membrane localization, which is indispensable for pyroptosis."

Cited: de604c3de7db092a-c7360229::s415

### `b8ec372b-ae29-473e-96bc-86ff1ead24ea`
> Based on the provided sources, TNN (tenascin) interacts with the following genes/proteins:

TN-C and TN-R interact with fibronectin. TN-C and TN-R bind with high affinity to a class of extracellular chondroitin sulfate proteoglycans called the lecticans (aggrecan, versican, brevican, and neurocan). Tenascins bind to members of the integrin family of heterodimers, cell adhesion molecules (CAMs) of the immunoglobulin superfamily, phosphacan/RPTP z / b, and annexin II. Tenascins interact with and are cleaved by serine proteinases and matrix metalloproteinases. TN-C and TN-R interact with immunoglobulin-like CAMs including F11/contactin, axonin-1, and neurofascin.

Cited: dd641ef35dc94ec2-2545f939::s140, dd641ef35dc94ec2-2545f939::s141, dd641ef35dc94ec2-2545f939::s142, dd641ef35dc94ec2-2545f939::s152

### `a45c277e-55d9-4e7f-b1de-37fc2e19daf6`
> Ogfrl1 has been shown to be a highly specific marker for PV interneurons in the molecular and fusiform layers of the dorsal cochlear nucleus.

### `a8aa19cc-e4d1-4aa1-8c4e-2a518b4c99d6`
_Refused._

### `2c3ba95c-47d5-4798-9911-ffdb11c940e4`
_Refused._

### `49d2630e-9d26-4e12-89a3-3050a609abf5`
_Refused._

### `c758f685-ba4a-4bf0-bd85-567c60ff1508`
> Nuclear expression of the cofactor p50 was enriched in TRAF3 loss of function DLBCL cells. Additionally, increased nuclear localization of the subunits RelB and p52 was observed in TRAF3 LOF cells, as compared to wild-type control clones.

Cited: 0ca36e794a547256-8b0b5a88::s293

### `fd54d745-447c-4fcd-80de-463fcd3de6a4`
_Refused._

### `4d11258d-ee8c-4bc7-91a8-613c7a41f139`
> Based on the provided sources, the K548R mutation in PARP1 has been shown to impair its interaction with MRE11 in immunoprecipitation assays.

"Similarly, we observed a reduced interaction of the PARP1-K548R mutant with MRE11 to a similar level to that seen in cells exposed to the PARP inhibitor AZD2281 (Fig. 4C and SI Appendix, Fig. S4D)."

### `1ff2b2e4-492e-4e35-bf33-f0fb53ab938c`
> The reversion mutation S446G in the BA.1 background increases the neutralization potency of both antibodies.

Cited: e3048b3df487004d-f5873c81::s217

### `178a5e56-340f-4ba8-a3e5-f024ca016f40`
> Based on the provided sources, the mutation **G56H** pulls the CDR2 loop closer to RBD in computational models.

"The mutation of Gly56 to His56 has imparted changes in the CDR2 loop and pulled Gly55 towards the Gly482 of RBD as observed in PyMol analysis."

Cited: d54befdeabd3bf9e-4573e6c1::s504

### `c75879f4-9329-4594-8f6a-c4d421f2439f`
> Three Pbs2 mutants increase interaction with SH3 containing proteins: Q82W, P97A, and L98F. However, Q82W displays a more complex pattern, as it "displayed both loss and gain of specificity with different SH3 containing proteins, suggesting a more general shift in the interaction profile rather than a simple loss or gain of specificity." In contrast, P97A and L98F are "mutations that only decrease specificity" and "are associated with decreases of interaction strength."

Cited: 667d94590e6616fe-e15f7eed::s535, 667d94590e6616fe-e15f7eed::s536, 667d94590e6616fe-e15f7eed::s539

### `f7346ea0-5f1b-45e9-a1d6-493c754159c1`
> Based on the provided sources, the S118L mutation of Kir6.2 impacts the following processes:

Channel assembly is impaired by the S118L mutation. Surface trafficking is affected, as the mutation prevents correct assembly and subsequent surface expression of the KATP channel. Protein degradation is impacted, as without correct assembly, SUR1 will be removed by the degradative machinery. Plasmalemmal KATP channel density is reduced by the mutation. In contrast, the S118L mutation does NOT impact ATP sensitivity and metabolic regulation.

Cited: e01d60f8ccaf1fbd-a4be292d::s315, e01d60f8ccaf1fbd-a4be292d::s320, e01d60f8ccaf1fbd-a4be292d::s321, e01d60f8ccaf1fbd-a4be292d::s322

### `3d3fea17-c8ee-4005-94cb-d8798be696c3`
> The total volume of UCYN-A and the total volume of its haptophyte host cell scale log-linearly. The total volume of B. bigelowii and the total chloroplast volume scale log-linearly. The total UCYN-A volume and the total chloroplast volume of its haptophyte host scale with a close-to-linear relationship.

Cited: b2aeda61ca908aaf-9486c25d::s139, b2aeda61ca908aaf-9486c25d::s142, b2aeda61ca908aaf-9486c25d::s79

### `ab58e166-f0b5-49ae-ac56-c38b5d6e8aad`
> Podoplanin (Pdpn) and integrin β4 (CD104) can be used to identify post-Aire mTECs. Specifically, the mTEC lo population separated into Pdpn+ CD104+ (pre-Aire) and Pdpn− CD104− (post-Aire) compartments. The mTEC lo could be divided into pre- and post-Aire compartments based on Pdpn and CD104 expression.

Cited: da7b856dfa32186d-1e1bf60f::s168, da7b856dfa32186d-1e1bf60f::s173

### `a73b2c2d-a3ac-49e6-8e2e-44b4c1e6de94`
> Based on the provided sources, among the Sm proteins tested with mutant Drosophila SMN D20V protein versus WT SMN, the five proteins that were most reduced are SmD1, D2, E, F, and G. However, the sources do not provide specific quantitative data comparing the individual fold-change values for each of these five proteins to definitively identify which single protein has the greatest reduction. The sources only indicate that these five proteins "were the most reduced in the D20V mutant pulldowns" as a group, while "SmB and D3 were the two least affected clients." To answer which specific protein among SmD1, D2, E, F, and G has the greatest reduction would require additional quantitative data not explicitly stated in the provided sources.

Cited: 7b3aeee153dea14b-f01a40db::s116

### `04dbe07d-8b2c-4daf-b5b2-ef0e93f1fd2a`
> For KBTBD4-PR, **Arg312** is the central residue that contributes to the expansion of the 2b-2c loop and is inserted into the narrow tunnel leading to the HDAC1 catalytic site. The expansion of the 2b-2c loop occurs as a net effect of the indel mutations in the PR mutant. The positively charged side chain of Arg312 reaches halfway into the tunnel.

Cited: 774bbc2bae82b5a7-82522eec::s145, 774bbc2bae82b5a7-82522eec::s148

### `4a6705b5-85e5-44c1-8444-65be30192802`
> RlmB has been found to promote large ribosomal subunit assembly even when expressed as a catalytically dead mutant. Specifically, the catalytically inactive RlmB variant RlmB(E198A) can stimulate 50S assembly. RlmB and RlmKL have functions in ribosome assembly independent of their modification activities. Additionally, some enzymes restore growth even though they are catalytically inactive, including RlmB and RlmKL.

Cited: 9a92b9f5adbd8f23-edc56ec0::s15, 9a92b9f5adbd8f23-edc56ec0::s199, 9a92b9f5adbd8f23-edc56ec0::s359

### `08397294-3d99-4790-915c-b8bcb1e9e661`
_Refused._

### `837b2489-723a-4099-9b68-c2a9ea688f4d`
> BUD40 produces the thickest fibers among the synthetically designed matrix proteins. The BUD40 material produces fibers that are, on average, 2.07± 0.56 microns thick. In comparison, the BUD60 forms fibers about 1.31± 0.23 microns thick, and the BUD80 forms fibers that are, on average, 1.07± 0.21 microns thick.

Cited: 7eb232e6cd269f4c-b14c15d4::s299, 7eb232e6cd269f4c-b14c15d4::s300

### `745f5a0d-5f8f-405e-bb46-f37b3d1f0678`
> Based on the provided sources, training characteristics within the target brain region do **not** explain inter-individual differences in clinical response to rtfMRI-NF in patients with major depressive disorder.

"Training characteristics within the target brain region, such as mean NF signal amplitude, mean left amygdala activation, and signal changes in the left amygdala, were not associated with changes in symptoms." Additionally, "within the active group, no significant associations were found between changes in MADRS scores and measures of NF training performance, including mean NF amplitude, average left amygdala response during regulation blocks, or changes in left amygdala response from the first to the last training runs." Instead, the sources indicate that "the amplitude of amygdala regulation alone is not the determinant of therapeutic success. Rather, it is the manner in which this regulation is executed that may account for the observed variability in treatment outcomes."

Cited: 06508579b3fd8baf-222782c2::s399, 06508579b3fd8baf-222782c2::s508, 06508579b3fd8baf-222782c2::s589

### `bca1be77-208b-4d57-ac29-05aa6d58bdbf`
> The transcription factor p50 most strongly promotes macrophage polarization towards a hypoxia state in glioma-associated TAMs. Specifically, "the identification of a p50-triggered hypoxia response program as a fundamental mechanism underlying Hypoxia-TAM polarization" has been established. Tumor cell-produced SPARC and hypoxia-induced lactate "concertedly promote Hypoxia-TAM polarization at least in part through activating p50."

Cited: e1671d32c95165a1-15d2b9a0::s251, e1671d32c95165a1-15d2b9a0::s364

### `2dc20a2f-de54-4bfe-a34f-1ba395f342cf`
> Distinct nuclear and cytoplasmic viscoelastic differences exist in immortalized human astrocytes (IHAs) but not in glioblastoma (GBM) cells. Specifically, the nucleus and cytoplasm of IHAs have distinct stiffness and relaxation times. In contrast, GBM cells do not appear to have significant differences in their nuclear and cytoplasmic viscoelastic properties.

Cited: edce53910698b365-47b1176a::s123, edce53910698b365-47b1176a::s171, edce53910698b365-47b1176a::s172

### `afb36e40-0836-4810-909e-eabfe17dcd8b`
> Based on the provided sources, several genes were **not** upregulated by 5-FU treatment in the HCT116 cell line:

Pol ι and pol κ were not significantly upregulated upon 5-FU treatment in HCT116 cell line. Pol δ was not significantly upregulated by the administration of 5-FU at either 1 or 10 μM. UDG and MBD4 were not upregulated upon 5-FU treatment within 72 h. Thymidylate synthase (TYMS) was not significantly upregulated upon the administration of 5-FU within 72 h.

### `c6f097c9-2216-4e98-af45-8101681b38ec`
_Refused._

### `9f797d29-9f3a-481d-b2fe-326cbc686273`
> Mn²⁺ had the strongest enhancing effect on the cleavage activity of endonuclease R.DraR1 from Deinococcus radiodurans.

Cited: 97736fa153fa784c-41306673::s223

### `0d5cf8a7-a240-4a8f-be4e-c16712f90d79`
> Substituting L522 to alanine in the minN region of Unkempt's intrinsically disordered region completely silenced transcriptional activity. Additionally, substituting W622 and F625 to alanines in the minC region completely silenced the activities of that region.

Cited: f56f5fb1f0922800-5c745f12::s207

### `40400348-eabb-4b25-90d1-e33589d3e5a4`
> FEXO, a low-cost over-the-counter antihistamine, has been found to have similar effects as anti-VISTA antibodies. When combined with ICB therapy, FEXO and the anti-VISTA antibody had similar efficacy in controlling primary tumor growth. However, FEXO+ICB was more effective than anti-VISTA+ICB for prolonging survival of mice because 50% of FEXO+ICB-treated mice had tumor-free survival but none of the anti-VISTA+ICB-treated mice survived. FEXO+ICB was also more potent than anti-VISTA+ICB in inhibiting lung metastasis.

Cited: 1e98838d3116281b-bac8d842::s252, 1e98838d3116281b-bac8d842::s254, 1e98838d3116281b-bac8d842::s255, 1e98838d3116281b-bac8d842::s256

### `ebe57888-662f-488f-ade1-c0aaffe638b1`
> Glial fibrillary acidic protein (GFAP) is a reactive astrocyte marker that has been shown to increase in expression in RhoANesKO mice.

Cited: d396d8edd4f389e6-d53cbbe3::s270

### `ef07d562-fc18-43c9-8201-7a189d76eeb9`
> The highest frequencies of KIR+ CD8+ T cells were found in patients with vasculitis or embolism and, to a lesser extent, in those with acute respiratory distress syndrome (ARDS).

Cited: 7f115cb9d0652622-d64852b9::s300

### `b331480e-dfc7-4e92-931a-c71f491c4795`
> The three residues with evolutionary divergence in the G domains of RAS isoforms that impose selectivity constraints on pan-KRAS non-covalent inhibition are H95, P121, and S122. H95 in the α3 helix exerts orthosteric effects. P121 and S122 in loop 8 exert allosteric (or indirect) effects.

Cited: 70973b3a4b0a193e-f334e23d::s135

### `58950824-2665-445d-939b-9512d5d01a2b`
_Refused._

### `8d12cb90-73c6-4cc1-9f83-0fa9fd822e92`
> Using acj6 and SoxN, the T4/T5 neurons of the optic lobe were identified and split into T4/T5a-b and T4/T5c-d subtypes by subclustering.

Cited: 010bab0784c5d05e-4d07cf2b::s185
