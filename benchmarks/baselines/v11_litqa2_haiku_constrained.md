# Eval Report: litqa2

- **Pipeline:** `anthropic/claude-haiku-4-5 | cohere-embed-v3 | hybrid(BM25+lance) | min_tokens=100 | cohere-rerank-v3 | retrieve=100/rerank=10 | no-verifier | loose | gen=constrained`
- **Run at:** 2026-05-17 17:10:14
- **Questions:** 186
- **Errors:** 1

## Aggregate metrics

| Metric | Value |
|---|---|
| `citation_precision` | 0.590 |
| `citation_recall` | 0.602 |
| `citation_f1` | 0.481 |
| `coverage` | 0.828 |
| `localization_accuracy` | 0.211 |
| `abstention_precision` | 0.176 |
| `abstention_recall` | 0.750 |
| `abstention_f1` | 0.286 |
| `mc_correct` | 161.000 |
| `mc_wrong` | 7.000 |
| `mc_unanswered` | 17.000 |
| `mc_accuracy_over_answered` | 0.958 |
| `mc_accuracy_over_all` | 0.870 |

## Per-question results

| ID | Refused | Should refuse | Cited ∩ Gold | Cited | Gold | Faith |
|---|---|---|---|---|---|---|
| `e3b5a4af-41d9-48db-becf-29a08d0ad28e` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `76184ccf-4bf0-469e-a442-11d04b4ff8b0` | ✗ | ✗ | 1 | 1 | 1 | 0.10 |
| `39129e1c-096f-4414-bf4f-37fadbbe364c` | ✗ | ✗ | 1 | 1 | 5 | 0.48 |
| `27234279-f50c-4cfc-86e2-af68364a8f94` | ✗ | ✗ | 1 | 1 | 3 | 0.26 |
| `517e7cf8-c5d2-4391-9e2a-235b79d93050` | ✗ | ✗ | 1 | 1 | 1 | 0.81 |
| `cb710074-73a8-4407-b0c7-7dc868f1bc76` | ✗ | ✗ | 2 | 4 | 14 | 0.72 |
| `5c4c602c-9624-4eae-ac44-efe4c0dd10e6` | ✗ | ✗ | 1 | 1 | 1 | 0.68 |
| `c9bdb9b5-28c1-44da-93b6-b1fc9d8bf369` | ✗ | ✗ | 2 | 3 | 9 | 0.92 |
| `e6b0f9e5-e976-47dc-b839-0b2fca967e9e` | ✗ | ✗ | 1 | 1 | 12 | 0.25 |
| `247eeb85-a552-4b87-b83e-327538fcb8a9` | ✗ | ✗ | 3 | 3 | 12 | 0.87 |
| `a214f5f8-0de8-43cf-82e0-7930003e4a0c` | ✗ | ✗ | 2 | 2 | 7 | 0.35 |
| `a43e5166-d0e8-48f8-a113-648acac7ed59` | ✗ | ✗ | 1 | 1 | 1 | 0.64 |
| `dd29920d-cb70-440f-961c-3e1103776c4f` | ✗ | ✗ | 1 | 1 | 1 | 0.97 |
| `7d805bb8-4c7c-431f-b068-acf5e5459985` | ✗ | ✗ | 0 | 1 | 1 | 1.00 |
| `8d7fa642-ee46-4a13-8ea9-61cc2d4f4ddd` | ✗ | ✗ | 2 | 3 | 6 | 0.80 |
| `487539f9-2f17-4009-aa4a-c41322445f11` | ✗ | ✗ | 4 | 13 | 6 | 0.96 |
| `5049c648-b1bb-4624-8824-9d93dfb04e51` | ✗ | ✗ | 1 | 3 | 1 | 0.89 |
| `a18883e9-218a-4719-8d2c-cf94d740de1a` | ✗ | ✗ | 0 | 4 | 3 | 0.98 |
| `d7833c0f-2a16-40d2-b6a0-6764aa3003a6` | ✗ | ✗ | 0 | 12 | 5 | 0.99 |
| `1ccdc348-50e1-4941-9151-5e50411a2b41` | ✗ | ✗ | 1 | 1 | 1 | 1.00 |
| `1e5f5199-84f4-4133-ab87-2372fa6ca722` | ✗ | ✗ | 0 | 16 | 2 | 0.99 |
| `d2860d38-dfb9-4b80-905f-812c32573915` | ✗ | ✗ | 1 | 3 | 1 | 0.75 |
| `77a41274-cd9c-48bc-a347-e0746907840d` | ✗ | ✗ | 1 | 1 | 2 | 0.70 |
| `5a2128ad-3127-4595-b810-db128d1a2335` | ✗ | ✗ | 2 | 2 | 4 | 0.88 |
| `d65103ae-c881-4116-a0a7-1b233eb6275a` | ✗ | ✗ | 1 | 1 | 5 | 0.37 |
| `ab5eb050-d134-4445-9307-6faa08be7474` | ✗ | ✗ | 1 | 1 | 7 | 0.15 |
| `82de3e92-abe2-46ac-ad17-23417b9c4da7` | ✗ | ✗ | 2 | 2 | 4 | 0.99 |
| `7cf0fcde-fea8-420c-8531-2f2fe9e38980` | ✗ | ✗ | 2 | 3 | 3 | 0.49 |
| `da5b2a8f-ba08-4692-851f-2e0bf142a02f` | ✗ | ✗ | 0 | 3 | 1 | 0.95 |
| `e2fb56b7-08cd-4dc0-bc63-b45931a74fc9` | ✗ | ✗ | 0 | 6 | 1 | 0.65 |
| `eda34fde-798e-43a1-a9d3-a804d3d8ee4e` | ✗ | ✗ | 2 | 4 | 5 | 1.00 |
| `0eede7a8-fe1f-42d3-a2c6-478083648644` | ✗ | ✗ | 2 | 3 | 2 | 0.97 |
| `d1307e50-3c03-4c76-81ee-2decb5de5f14` | ✓ | ✗ | 0 | 0 | 4 | 0.86 |
| `10cece36-a507-4a93-9600-13f3e0e677f8` | ✗ | ✗ | 1 | 3 | 2 | 0.62 |
| `f5a84803-3917-43eb-801b-8dc0c5400da1` | ✗ | ✗ | 1 | 3 | 1 | 1.00 |
| `c47dd378-dde3-4a45-9184-6abfa6163717` | ✗ | ✗ | 1 | 2 | 1 | 0.99 |
| `0bac8974-554c-439a-a9a2-22fa509c8d5d` | ✗ | ✗ | 2 | 4 | 2 | 1.00 |
| `aaa85379-1e4b-4642-9ec4-e1a6d6c29c3b` | ✗ | ✗ | 4 | 7 | 5 | 0.96 |
| `aa1835b2-2b1c-4986-b7af-e174da0124b0` | ✗ | ✗ | 1 | 3 | 1 | 0.44 |
| `5a9c6697-a65c-49c0-9e02-38b2a276fde7` | ✗ | ✗ | 1 | 1 | 1 | 0.90 |
| `37a4d007-793e-4a89-922a-c1b05f4f82c1` | ✗ | ✗ | 1 | 2 | 1 | 0.20 |
| `c9baf8e0-c4c7-4ba3-b5c4-18e9af8b2df1` | ✗ | ✗ | 2 | 3 | 2 | 0.62 |
| `d0f69626-66ee-4807-937d-c3a024441812` | ✗ | ✗ | 0 | 1 | 4 | 0.98 |
| `462a9f38-7cbe-4e12-a6e2-b1d7028c3a8b` | ✗ | ✗ | 1 | 1 | 1 | 0.96 |
| `86f111e5-402b-4ef5-b101-8be1bf5be7c6` | ✗ | ✗ | 1 | 1 | 1 | 0.93 |
| `cbe93a43-09cd-4cb4-9edd-f22fe8c28415` | ✗ | ✗ | 0 | 1 | 2 | 0.36 |
| `7a88e6f7-fb8e-4a24-b08d-9b7a6edafe57` | ✗ | ✗ | 2 | 3 | 3 | 0.99 |
| `91387526-9268-4a3c-9abe-73819707d0b0` | ✗ | ✗ | 1 | 1 | 1 | 0.84 |
| `7b98796f-25be-4c58-a52a-4e366c0ffd95` | ✗ | ✗ | 1 | 1 | 4 | 0.99 |
| `5e20e26d-6192-4563-abb3-a4857e3dbc7c` | ✗ | ✗ | 1 | 1 | 2 | 0.71 |
| `b105af85-833e-48bc-ac78-48f73c9673fd` | ✗ | ✗ | 1 | 1 | 5 | 0.91 |
| `5b6d6f82-a585-4aa8-9fe6-e7d35f7cb2ae` | ✗ | ✗ | 2 | 6 | 2 | 0.26 |
| `12321eab-6ad6-4218-8815-18bc51c14544` | ✗ | ✗ | 1 | 3 | 1 | 0.83 |
| `c33446f6-fbff-4186-8a51-28a17f68bd40` | ✗ | ✗ | 2 | 3 | 2 | 0.29 |
| `b1d5a5f5-6e89-4dfb-b60d-5a9824b015f3` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `6aa10957-bdd9-4dab-a4e1-234a17cb87dd` | ✗ | ✗ | 1 | 2 | 1 | 0.97 |
| `28ebecdf-949e-4d20-aca9-5989b7a9d6e9` | ✗ | ✗ | 1 | 1 | 2 | 0.99 |
| `dbb51a1c-f9a2-4960-a93c-118957659790` | ✗ | ✗ | 1 | 1 | 7 | 0.82 |
| `85c67ef3-322c-42b4-b745-c05e07e7b8ac` | ✗ | ✗ | 1 | 3 | 6 | 0.97 |
| `653635b7-3bc6-4a7b-98c7-c02038c0e928` | ✗ | ✗ | 1 | 2 | 1 | 0.35 |
| `100b570f-1c4f-4214-8402-f1b15f9989b4` | ✗ | ✗ | 1 | 1 | 4 | 0.37 |
| `0a9d6516-95ef-4d7b-a28d-d7cde27b7b55` | ✗ | ✗ | 0 | 3 | 1 | 0.71 |
| `8d61a14b-60ef-43b0-8003-b60cb6657428` | ✗ | ✗ | 0 | 2 | 0 | 0.09 |
| `4d4cb121-9525-499a-9475-9b212465c72d` | ✗ | ✗ | 0 | 4 | 0 | 0.08 |
| `ca4c9d21-b842-4875-9a6a-bcb9f6c55073` | ✗ | ✗ | 0 | 2 | 7 | 1.00 |
| `c3816cb5-8c87-4946-b133-43f415ab6b2a` | ✓ | ✓ | 0 | 0 | 0 | 0.24 |
| `59745f75-52bf-4815-905c-3dfad1ef8923` | ✓ | ✗ | 0 | 0 | 0 | 0.00 |
| `26691c84-514b-4712-a43e-09705d681e45` | ✗ | ✗ | 1 | 2 | 1 | 0.42 |
| `0e53a08c-4252-4a84-962b-5b396f9740aa` | ✓ | ✗ | 0 | 0 | 0 | 0.00 |
| `8ade3e3a-4792-4965-b9d9-05e528ebbfa0` | ✗ | ✗ | 0 | 3 | 0 | 0.35 |
| `f5a4b449-e647-4ae0-8419-c221792482c9` | ✗ | ✗ | 0 | 6 | 5 | 0.39 |
| `5806ed2a-1005-44f1-8d70-332048fea8f4` | ✗ | ✗ | 0 | 4 | 1 | 0.69 |
| `6fff0994-6d02-470a-9d61-8e35420412b6` | ✗ | ✗ | 1 | 2 | 5 | 0.99 |
| `8266ac61-92d6-423d-8e7a-fe47b3a7e885` | ✗ | ✗ | 1 | 1 | 12 | 1.00 |
| `322454df-45a8-41b3-9b0a-4e808144023c` | ✓ | ✗ | 0 | 0 | 0 | 0.50 |
| `3c9f23e2-fdd0-431b-aca7-4f9556c78f1f` | ✓ | ✗ | 0 | 0 | 0 | 0.00 |
| `983f1ef5-fc7d-4f4a-8f48-e704641eae12` | ✗ | ✗ | 2 | 2 | 2 | 0.74 |
| `7d2c8d44-ecf3-40d2-ab69-b6195c46ffe9` | ✗ | ✗ | 1 | 2 | 1 | 0.93 |
| `720e20c2-9ad1-4d98-9f01-8b7fb3782a46` | ✗ | ✗ | 1 | 2 | 3 | 0.94 |
| `dbfbae3d-62f6-4710-8d13-8ce4c8485567` | ✗ | ✗ | 1 | 1 | 1 | 0.12 |
| `7a42c784-7ae0-48fe-a71f-0a547b8fabb3` | ✗ | ✗ | 6 | 21 | 6 | 0.48 |
| `0708b62f-9652-49eb-8ba6-28878afa7445` | ✗ | ✗ | 1 | 1 | 4 | 0.99 |
| `5b3b7d05-9e54-445c-b374-d4c6b60923b4` | ✗ | ✗ | 1 | 1 | 1 | 0.74 |
| `623a831f-41ee-4e0e-936a-87f93d96369e` | ✗ | ✗ | 5 | 7 | 30 | 0.89 |
| `0b1d5537-db47-420c-984b-9b56d38e6d98` | ✗ | ✗ | 1 | 2 | 1 | 0.71 |
| `ade96656-7ed1-4e21-b009-b7a73e13bff5` | ✗ | ✗ | 0 | 3 | 0 | 0.42 |
| `78a2c1d2-f035-4c7d-a7ee-40dfd95ca88a` | ✗ | ✗ | 1 | 2 | 1 | 0.99 |
| `224efcd7-3652-47f8-84dd-15b4c6fafae2` | ✗ | ✗ | 1 | 1 | 2 | 0.93 |
| `55187fb4-e7ee-4027-b74f-cab50f328442` | ✗ | ✗ | 1 | 2 | 1 | 0.94 |
| `25a9cf59-1c28-4ddf-b797-f43efb9349e6` | ✗ | ✗ | 1 | 2 | 11 | 0.56 |
| `12a20d8d-cd49-47eb-9a19-6a38519ee3dc` | ✗ | ✗ | 1 | 10 | 1 | 0.86 |
| `4bb69c9d-2485-42d2-b8aa-aa647b407ca4` | ✗ | ✗ | 5 | 7 | 7 | 0.80 |
| `8c833521-56c4-458d-8c65-2bbf66190cae` | ✗ | ✗ | 0 | 3 | 1 | 0.85 |
| `255fd5fb-9623-4030-8bf2-253247df7c82` | ✗ | ✗ | 1 | 3 | 1 | 0.96 |
| `38ada695-2c79-459b-8e68-dbed734c74f9` | ✗ | ✗ | 1 | 1 | 1 | 0.93 |
| `e763edaa-b112-460a-a564-d58a6685e639` | ✗ | ✗ | 0 | 3 | 1 | 0.88 |
| `8af900bb-5794-40db-910e-10d5857ce5bd` | ✗ | ✗ | 2 | 3 | 2 | 0.47 |
| `6194ebfc-2d5c-4ccc-8883-da7c471b61e6` | ✗ | ✗ | 1 | 3 | 1 | 0.16 |
| `1f1b07d7-39ce-4665-9b70-4ab77e3c87aa` | ✗ | ✗ | 1 | 2 | 4 | 0.24 |
| `55668039-396e-488a-b2c3-bbe840550433` | ✗ | ✗ | 1 | 1 | 1 | 0.32 |
| `4f050bf3-27cd-4a14-8422-45df5e2bb079` | ✗ | ✗ | 1 | 2 | 1 | 0.67 |
| `cff00d08-5655-4214-97ac-8fa9504c1165` | ✗ | ✗ | 2 | 2 | 2 | 0.98 |
| `0eeb7ea9-fc80-4dee-9418-1c328c3ab653` | ✗ | ✗ | 1 | 1 | 2 | 0.97 |
| `658f7050-d137-477e-8693-26609080cecd` | ✗ | ✗ | 1 | 1 | 2 | 0.25 |
| `8696273a-7fea-411a-b6c6-0e826e1e02b5` | ✗ | ✗ | 1 | 2 | 1 | 0.69 |
| `ce6dd5f7-0706-41dd-a383-9b0d22ef00a1` | ✗ | ✗ | 1 | 1 | 1 | 0.85 |
| `400786c1-e6c6-4f46-a501-86fdd048ed88` | ✗ | ✗ | 1 | 3 | 2 | 1.00 |
| `e820cbcf-6df1-4c1c-b985-c02f39f52781` | ✗ | ✗ | 1 | 3 | 1 | 0.70 |
| `230dec20-cd02-4613-a7b1-e28058ed46fe` | ✗ | ✗ | 1 | 2 | 2 | 0.90 |
| `7975ddb0-a784-4f85-a297-c80e1cb5dcf2` | ✓ | ✗ | 0 | 0 | 0 | 0.00 |
| `a1d01019-d2b1-4619-92ec-7ea38578819f` | ✗ | ✗ | 1 | 1 | 2 | 0.93 |
| `fe074387-3765-4020-8f5d-e395d1094121` | ✗ | ✗ | 0 | 2 | 0 | 0.47 |
| `f0b6cea0-e005-47bc-be0d-9a10b219cae6` | ✗ | ✗ | 1 | 1 | 3 | 1.00 |
| `ae02d0e9-edf5-4c39-a215-3cbc8f4c565d` | ✗ | ✗ | 3 | 3 | 4 | 0.66 |
| `fd60a0e7-ba64-49a9-843a-6f5cb17c5fa9` | ✗ | ✗ | 1 | 4 | 4 | 0.29 |
| `14fd2b75-76fb-4c29-a21d-c557b2bcf2ff` | ✗ | ✗ | 1 | 1 | 4 | 0.87 |
| `e9f142f0-8ef6-47cd-b846-7283a93308d4` | ✗ | ✗ | 2 | 3 | 15 | 0.94 |
| `398ebac1-fd2d-45b1-9415-d82db4b4d83c` | ✗ | ✗ | 2 | 6 | 2 | 0.59 |
| `7e7150d6-bc73-4a29-a5b3-4ef8399ed947` | ✗ | ✗ | 1 | 2 | 1 | 0.40 |
| `58b39fab-337b-452d-b74f-84f9a188ce88` | ✓ | ✓ | 0 | 0 | 0 | 0.62 |
| `80e6571e-8f5d-496a-8ba3-9c9f5b783f5d` | ✗ | ✗ | 2 | 4 | 5 | 0.88 |
| `154e7b14-4ed5-4cf3-9149-0c4843fc62cc` | ✗ | ✗ | 1 | 1 | 1 | 0.22 |
| `a71ef7a2-31a2-460d-9ff4-32d7722353c3` | ✗ | ✗ | 1 | 2 | 1 | 0.23 |
| `c624ed31-214f-4c80-9544-5514a096b1d3` | ✗ | ✗ | 2 | 2 | 23 | 0.97 |
| `bcd2f213-c6c6-4660-af35-a7bd1c6a1170` | ✓ | ✗ | 0 | 0 | 0 | 0.49 |
| `24fae97b-03f3-48b8-b623-abf07faee02e` | ✗ | ✗ | 3 | 4 | 5 | 0.85 |
| `ce93661b-e3c4-4a7a-96b6-87492259c501` | ✗ | ✗ | 4 | 4 | 9 | 0.61 |
| `941c04dc-c89d-4a90-87b0-930625268a38` | ✗ | ✗ | 1 | 1 | 2 | 0.94 |
| `ea4ce240-2864-4ee5-9ffc-2dbda0f8f550` | ✗ | ✗ | 1 | 1 | 10 | 0.93 |
| `cff68274-4bbe-4fa0-a181-36a9af3cc0f1` | ✓ | ✗ | 0 | 0 | 0 | 0.16 |
| `2c262f91-52b6-421d-8341-8748f923459e` | ✓ | ✗ | 0 | 0 | 0 | 0.14 |
| `6f8a51e2-f7ad-4033-b43d-370348e4809f` | ✗ | ✗ | 1 | 1 | 2 | 1.00 |
| `9a0b82cb-6a99-4e50-83fc-3ef2ebd277cc` | ✗ | ✗ | 1 | 5 | 2 | 0.96 |
| `8b665114-7729-4dac-a64f-4862a5397b82` | ✗ | ✗ | 2 | 2 | 14 | 0.99 |
| `5c808548-92c4-4ae7-990c-e2df81e3c2ae` | ✓ | ✓ | 0 | 0 | 0 | 0.10 |
| `564e715f-8d30-410b-bdb5-0dc5206589a7` | ✗ | ✗ | 4 | 4 | 25 | 0.59 |
| `e90ea0fc-4659-4b20-acae-75dc4b97a101` | ✗ | ✗ | 4 | 4 | 8 | 0.99 |
| `c246753c-27d2-4ae4-8630-b9b4077ba6f6` | ✗ | ✗ | 0 | 0 | 1 | 0.00 ⚠️ RateLimitError: litellm.RateLimitError: AnthropicException - {"type":"error","error":{"type":"rate_limit_error","message":"This request would exceed your organization's rate limit of 50,000 input tokens per minute (org: ac37d026-8a94-437f-87a7-e20cfa6cefa5, model: claude-haiku-4-5-20251001). For details, refer to: https://docs.claude.com/en/api/rate-limits. You can see the response headers for current usage. Please reduce the prompt length or the maximum tokens requested, or try again later. You may also contact sales at https://claude.com/contact-sales to discuss your options for a rate limit increase."},"request_id":"req_011Cb93g8jvUgUYoVU99psv6"} |
| `22306bd7-7e84-415d-aebb-11c6312eb081` | ✗ | ✗ | 1 | 1 | 1 | 0.92 |
| `7d71dffb-b591-4b88-b0c6-e125a1b083b4` | ✗ | ✗ | 0 | 2 | 1 | 0.22 |
| `fca26d7c-05cf-40b0-9fd6-a63ed7950909` | ✗ | ✗ | 1 | 4 | 1 | 0.55 |
| `c6e11fac-8f9c-4cf1-aa6e-4d25731ba74f` | ✗ | ✗ | 1 | 1 | 1 | 0.90 |
| `bace5737-ba26-422a-8706-0fb1e92b689f` | ✓ | ✗ | 0 | 0 | 0 | 0.02 |
| `ff7328e2-4954-46a2-8ea3-d40b4df0c0ea` | ✗ | ✗ | 2 | 7 | 7 | 0.48 |
| `76bcaeeb-93bd-4951-99b9-cf4613de1a37` | ✗ | ✗ | 1 | 1 | 1 | 0.98 |
| `850f86d3-0139-43df-89fd-e606c30aaa8b` | ✗ | ✗ | 0 | 5 | 1 | 0.65 |
| `df061613-2591-4faa-be03-791c76375cb5` | ✗ | ✗ | 1 | 2 | 1 | 0.98 |
| `634f6745-f3b3-4cb1-9859-96ffb954b98a` | ✓ | ✗ | 0 | 0 | 0 | 0.00 |
| `d1eabedb-656f-4f89-a65f-4ed89478ba9f` | ✗ | ✗ | 0 | 5 | 2 | 0.95 |
| `58f69c8d-cb94-4021-a84f-c549a7b976e1` | ✗ | ✗ | 4 | 8 | 44 | 0.96 |
| `20980744-f9ff-4e39-a08d-106eada6900c` | ✓ | ✗ | 0 | 0 | 0 | 0.06 |
| `a6622141-68d6-418f-8e30-7a5eff3d4fa8` | ✗ | ✗ | 4 | 6 | 5 | 0.73 |
| `9fe3ff3b-60cf-472d-ab1a-2bda1868f1b4` | ✗ | ✗ | 2 | 2 | 8 | 0.94 |
| `9088251a-99fe-4b91-b6a9-375154ec4f58` | ✗ | ✗ | 1 | 2 | 1 | 0.94 |
| `b8ec372b-ae29-473e-96bc-86ff1ead24ea` | ✗ | ✓ | 0 | 3 | 0 | 0.39 |
| `a45c277e-55d9-4e7f-b1de-37fc2e19daf6` | ✗ | ✗ | 1 | 2 | 1 | 0.25 |
| `a8aa19cc-e4d1-4aa1-8c4e-2a518b4c99d6` | ✗ | ✗ | 0 | 7 | 0 | 0.62 |
| `2c3ba95c-47d5-4798-9911-ffdb11c940e4` | ✗ | ✗ | 2 | 2 | 6 | 0.98 |
| `49d2630e-9d26-4e12-89a3-3050a609abf5` | ✓ | ✗ | 0 | 0 | 0 | 0.33 |
| `c758f685-ba4a-4bf0-bd85-567c60ff1508` | ✗ | ✗ | 5 | 7 | 8 | 0.94 |
| `fd54d745-447c-4fcd-80de-463fcd3de6a4` | ✗ | ✗ | 1 | 1 | 1 | 0.78 |
| `4d11258d-ee8c-4bc7-91a8-613c7a41f139` | ✗ | ✗ | 4 | 12 | 16 | 0.96 |
| `1ff2b2e4-492e-4e35-bf33-f0fb53ab938c` | ✗ | ✗ | 1 | 1 | 6 | 0.99 |
| `178a5e56-340f-4ba8-a3e5-f024ca016f40` | ✗ | ✗ | 1 | 1 | 3 | 1.00 |
| `c75879f4-9329-4594-8f6a-c4d421f2439f` | ✗ | ✗ | 1 | 2 | 1 | 1.00 |
| `f7346ea0-5f1b-45e9-a1d6-493c754159c1` | ✗ | ✗ | 1 | 10 | 1 | 0.99 |
| `3d3fea17-c8ee-4005-94cb-d8798be696c3` | ✗ | ✗ | 1 | 5 | 5 | 0.00 |
| `ab58e166-f0b5-49ae-ac56-c38b5d6e8aad` | ✗ | ✗ | 1 | 2 | 1 | 0.45 |
| `a73b2c2d-a3ac-49e6-8e2e-44b4c1e6de94` | ✗ | ✗ | 2 | 2 | 21 | 0.83 |
| `04dbe07d-8b2c-4daf-b5b2-ef0e93f1fd2a` | ✗ | ✗ | 3 | 3 | 5 | 0.99 |
| `4a6705b5-85e5-44c1-8444-65be30192802` | ✗ | ✗ | 0 | 4 | 2 | 0.99 |
| `08397294-3d99-4790-915c-b8bcb1e9e661` | ✗ | ✗ | 2 | 4 | 2 | 0.98 |
| `837b2489-723a-4099-9b68-c2a9ea688f4d` | ✗ | ✗ | 2 | 4 | 2 | 0.70 |
| `745f5a0d-5f8f-405e-bb46-f37b3d1f0678` | ✗ | ✗ | 1 | 2 | 2 | 0.71 |
| `bca1be77-208b-4d57-ac29-05aa6d58bdbf` | ✗ | ✗ | 2 | 3 | 2 | 0.77 |
| `2dc20a2f-de54-4bfe-a34f-1ba395f342cf` | ✗ | ✗ | 2 | 5 | 6 | 1.00 |
| `afb36e40-0836-4810-909e-eabfe17dcd8b` | ✗ | ✗ | 3 | 17 | 6 | 0.97 |
| `c6f097c9-2216-4e98-af45-8101681b38ec` | ✓ | ✗ | 0 | 0 | 0 | 0.01 |
| `9f797d29-9f3a-481d-b2fe-326cbc686273` | ✗ | ✗ | 1 | 2 | 4 | 0.84 |
| `0d5cf8a7-a240-4a8f-be4e-c16712f90d79` | ✗ | ✗ | 6 | 11 | 12 | 0.28 |
| `40400348-eabb-4b25-90d1-e33589d3e5a4` | ✗ | ✗ | 3 | 4 | 4 | 0.95 |
| `ebe57888-662f-488f-ade1-c0aaffe638b1` | ✗ | ✗ | 1 | 2 | 1 | 0.82 |
| `ef07d562-fc18-43c9-8201-7a189d76eeb9` | ✗ | ✗ | 1 | 2 | 2 | 0.90 |
| `b331480e-dfc7-4e92-931a-c71f491c4795` | ✗ | ✗ | 1 | 3 | 5 | 0.76 |
| `58950824-2665-445d-939b-9512d5d01a2b` | ✗ | ✗ | 0 | 4 | 0 | 0.74 |
| `8d12cb90-73c6-4cc1-9f83-0fa9fd822e92` | ✗ | ✗ | 1 | 1 | 1 | 0.12 |

## Per-question answers

### `e3b5a4af-41d9-48db-becf-29a08d0ad28e`
> **ciproflaxin** A. lwoffii evolved resistance to ciprofloxacin in laboratory experiments, as indicated by the statement that 'clinical resistance was seen only for ciprofloxacin' when A. lwoffii was evolved in the lab. The mutant evolution experiments clearly show that A. lwoffii only evolved resistance to ciprofloxacin, not to the other antibiotics tested. In the one instance where A. lwoffii evolved resistance, to ciprofloxacin, drug target mutations were also observed.

Cited: 6795e9ad5fae6fe1-b687cf6e::s278, 6795e9ad5fae6fe1-b687cf6e::s370, 6795e9ad5fae6fe1-b687cf6e::s383

### `76184ccf-4bf0-469e-a442-11d04b4ff8b0`
> **2.7 fold** Furthermore, total contacts made to GIs showed that whereas the active OR gene significantly increased its contacts to GIs by 2.7-fold, both inactive OR genes and other GIs significantly decreased their GI contacts.

Cited: a8d467f77e70f70d-553b632a::s175

### `39129e1c-096f-4414-bf4f-37fadbbe364c`
> **61% of gene loci** The majority of gene disruption phenotypes (61% of total gene phenotypes) were detected by 4 cell divisions.

Cited: aca6b37101ab6098-3101659e::s135

### `27234279-f50c-4cfc-86e2-af68364a8f94`
> **12,300** Our method detected 4,850 SWO-specific ILs, 12,309 mandarin-specific ILs, and 4,900 pummelo-specific ILs in them.

Cited: c322ce6575cc1c3a-d56b589a::s181

### `517e7cf8-c5d2-4391-9e2a-235b79d93050`
> **80%** H3.3 K36R mutants complete development and eclose at a frequency of ~80%, which is nearly identical to that of H3.3 Ctrl animals.

Cited: 116c0e949dd415fc-61f4295b::s281

### `cb710074-73a8-4407-b0c7-7dc868f1bc76`
> **10%** The acute heat stress assay was performed with animals exposed to 35°C for 6 hours, and survival was assessed after 14 hours of recovery at 20°C. Only 10% of adr mutant animals die after the same 35°C stress, which includes adr-1(-), adr-2(-), and adr-1(-);adr-2(-) animals.

Cited: 1c5f1e074ba072b8-31d0ed90::s437, 1c5f1e074ba072b8-31d0ed90::s438, 1c5f1e074ba072b8-31d0ed90::s79, 1c5f1e074ba072b8-31d0ed90::s80

### `5c4c602c-9624-4eae-ac44-efe4c0dd10e6`
> **Asn326** A large oligosaccharide density was observed in the cryo-EM map of Nav1.6, attaching to Asn326.

Cited: d79480166f4ab0e3-4297b383::s79

### `c9bdb9b5-28c1-44da-93b6-b1fc9d8bf369`
> **evening** The overall number of TILs was highly dependent on the time of day of tumor harvest, with total leukocyte numbers peaking in the evening (ZT13). We confirmed these data by immunofluorescence staining of tumor sections, showing higher T cell numbers in the evening (ZT13) compared with the morning (ZT1). Leukocyte trafficking to the tumor was strongly time-of-day dependent, with more cells reaching the tumor in the evening, in line with the infiltration block data.

Cited: 40349a281d8b56ff-7979b34d::s110, 40349a281d8b56ff-7979b34d::s112, 40349a281d8b56ff-7979b34d::s132

### `e6b0f9e5-e976-47dc-b839-0b2fca967e9e`
> **cell–matrix interactions** Myotendinous junction myonuclei exhibited enrichment in genes associated with cell-matrix interactions (COL22A1, ADGBR4), whereas NMJ myonuclei showed enrichment in genes linked to synaptic transmission responses (PHLDB2, CHRNE).

Cited: f7c3d31ee5706405-5f6af1d3::s122

### `247eeb85-a552-4b87-b83e-327538fcb8a9`
> **5.3%** Results showed that the percentage of AR-negative patients was significantly lower in MBC than in FBC samples (5.3% vs. 17.4% in MBC and FBC samples, respectively)

Cited: 476ba9a9e8ea9c14-b5e5878b::s495, 476ba9a9e8ea9c14-b5e5878b::s496, 476ba9a9e8ea9c14-b5e5878b::s497

### `a214f5f8-0de8-43cf-82e0-7930003e4a0c`
> **Saponaria vaccaria** β-Amyrin synthases (BASs) of various plant origins (Artemisia annua, Arabidopsis thaliana, Glycyrrhiza glabra and Saponaria vaccaria) were integrated into JWY601 to quantify the production of β-amyrin from squalene by gas chromatography-mass spectrometry (GC-MS). Among these candidates, the BAS homologue from S. vaccaria (SvBAS) yielded the highest titre of β-amyrin, the production of which was further confirmed by efficient consumption of squalene compared to the parent strain.

Cited: e35c8530af941f04-9a7975aa::s100, e35c8530af941f04-9a7975aa::s99

### `a43e5166-d0e8-48f8-a113-648acac7ed59`
> **5x** From P6 to P15, TC synapse density increases 5-fold in wild-type mice.

Cited: c0b69d2af9f2e018-845b5d60::s271

### `dd29920d-cb70-440f-961c-3e1103776c4f`
> **100** Cells with the synthetic IL-2 circuit autonomously identified the target tumor (CD19 + /right) and locally expanded by a factor of ~100 within this tumor.

Cited: 34f4e70030aa5d35-a24b74ef::s130

### `7d805bb8-4c7c-431f-b068-acf5e5459985`
> **7.7x** In six MMR-proficient cell types, including induced pluripotent stem cells (iPSCs) and primary T cells, these PE4 (PE2+MLH1dn) and PE5 (PE3+MLH1dn) systems enhanced editing efficiency over PE2 and PE3 by an average of 7.7-fold and 2.0-fold, respectively, and increased edit/indel ratios (outcome purity) by 3.4fold.

Cited: fa808d37a77e6019-79d6e54c::s96

### `8d7fa642-ee46-4a13-8ea9-61cc2d4f4ddd`
> **residues 344–360** A version of Apollo with a deletion of amino acids 344-360 (Apollo/Delta1 PK), removing the residues most similar to those of the Artemis DNA-PK interaction motif, had a reduced interaction with DNA-PKcs in 293T cells. A domain in Apollo (amino acids 344-360) promotes Apollo's interaction with DNA-PK and is required for Apollo function at telomeres.

Cited: cea2facf97f5150c-660a07bf::s360, cea2facf97f5150c-660a07bf::s407, cea2facf97f5150c-660a07bf::s61

### `487539f9-2f17-4009-aa4a-c41322445f11`
> **aa 31-40** The N-terminus of COSA-1 mediates the interaction with MSH-5 and ZHP-3. COSA-1 has a long N-terminus containing an intrinsically disordered region (IDR) spanning residue 1–50. Truncated COSA-1 1–10, COSA-1 1–20, and COSA-1 1–30 could interact with MSH-5 and ZHP-3, while COSA-1 1-40 showed dramatically decreased interactions with these two proteins. The N-terminal 53 amino acids of COSA-1 play a vital role in the interactions with MSH-5 and ZHP-3.

Cited: 4c0f27bd833d0295-e8c8a393::s612, 4c0f27bd833d0295-e8c8a393::s613, 4c0f27bd833d0295-e8c8a393::s625, 4c0f27bd833d0295-e8c8a393::s626, 4c0f27bd833d0295-e8c8a393::s627, 4c0f27bd833d0295-e8c8a393::s628, 4c0f27bd833d0295-e8c8a393::s638, 4c0f27bd833d0295-e8c8a393::s639, 4c0f27bd833d0295-e8c8a393::s640, 4c0f27bd833d0295-e8c8a393::s641, 4c0f27bd833d0295-e8c8a393::s645, 4c0f27bd833d0295-e8c8a393::s646, 4c0f27bd833d0295-e8c8a393::s647

### `5049c648-b1bb-4624-8824-9d93dfb04e51`
> **Depletion of photosynthetic machinery** MTF1 is the chloroplast's MTF and is required for translation of nearly all chloroplast-encoded proteins, and its mutant shows a severe photosynthetic phenotype. Loss of MTF1 expression resulted in the depletion of the entire photosynthetic apparatus and most of the chloroplast-expressed proteins. Disruption of the poorly characterized genes PMR1 and MTF1 led to the depletion of the entire photosynthetic apparatus.

Cited: 9afb8ab3b1d5ff95-b03dfb72::s180, 9afb8ab3b1d5ff95-b03dfb72::s237, 9afb8ab3b1d5ff95-b03dfb72::s238

### `a18883e9-218a-4719-8d2c-cf94d740de1a`
> **Yes** A striking difference between PBS- and verteporfin-treated wounds was the emergence of regenerated HF in the latter within 30 days; control wounds formed bare areas. By POD 30, verteporfin-treated wounds regrew levels of HF and glands comparable with those in unwounded skin and had less-dense, more randomly oriented ECM fibers. Blocking mechanotransduction (verteporfin, YAP inhibitor) prevents conversion and yields regeneration, defined by the restoration of dermal appendages (hair follicles).

Cited: 7dead537a45e92bd-e35471f4::s253, 7dead537a45e92bd-e35471f4::s72, 7dead537a45e92bd-e35471f4::s73, 7dead537a45e92bd-e35471f4::s89

### `d7833c0f-2a16-40d2-b6a0-6764aa3003a6`
> **Yes** Metabolic glycan labeling can reduce the membrane mobility of DCs, which activates DCs and improves the antigen presentation and subsequent T cell priming property of DCs. Metabolic glycan labeling itself can enhance the antitumor efficacy of DC vaccines. DCs treated with azido-sugars exhibit a reduced membrane mobility compared to control DCs without azido-sugar treatment. Azido-labeled antigen-pulsed DCs result in improved CTL response and antitumor efficacy compared to unlabeled DCs in both prophylactic and therapeutic settings.

Cited: 6f59dd139145c891-36c60054::s16, 6f59dd139145c891-36c60054::s17, 6f59dd139145c891-36c60054::s18, 6f59dd139145c891-36c60054::s19, 6f59dd139145c891-36c60054::s20, 6f59dd139145c891-36c60054::s748, 6f59dd139145c891-36c60054::s749, 6f59dd139145c891-36c60054::s750, 6f59dd139145c891-36c60054::s760, 6f59dd139145c891-36c60054::s761, 6f59dd139145c891-36c60054::s762, 6f59dd139145c891-36c60054::s763

### `1ccdc348-50e1-4941-9151-5e50411a2b41`
> **coding strand** In all 17 CRISPRi screens, the average effect sizes of sgRNAs targeting coding strands within gene bodies were more than twofold higher than those targeting the template strands.

Cited: b0c70be4f4a933d3-7fb87fac::s328

### `1e5f5199-84f4-4133-ab87-2372fa6ca722`
> **No dimethylarginine** The protein encoded by TDRD1 itself does not have dimethylarginine modifications. Rather, TDRD1 is a Tudor domain-containing protein that binds to other proteins that contain symmetrical dimethylarginine (sDMA) modifications. The study examined the binding of TDRD1's Tudor domains to endogenous murine proteins MILI and MIWI, which are reported to contain sDMAs, not TDRD1 itself. MVH (mouse Vasa homolog) is reported to carry both symmetrical and asymmetrical dimethylarginine modifications and associates with TDRD1, but this describes MVH, not TDRD1 itself.

Cited: aa268cf616154b07-7384f4cb::s1160, aa268cf616154b07-7384f4cb::s1161, aa268cf616154b07-7384f4cb::s1162, aa268cf616154b07-7384f4cb::s1163, aa268cf616154b07-7384f4cb::s1171, aa268cf616154b07-7384f4cb::s1172, aa268cf616154b07-7384f4cb::s1173, aa268cf616154b07-7384f4cb::s1174, aa268cf616154b07-7384f4cb::s1175, aa268cf616154b07-7384f4cb::s1178, aa268cf616154b07-7384f4cb::s1179, aa268cf616154b07-7384f4cb::s1180, aa268cf616154b07-7384f4cb::s21, aa268cf616154b07-7384f4cb::s22, aa268cf616154b07-7384f4cb::s23, aa268cf616154b07-7384f4cb::s24

### `d2860d38-dfb9-4b80-905f-812c32573915`
> **S. epidermis** Engineered S. epidermidis strains stimulate T cells specific for non-native epitopes under physiologic conditions of colonization. OT-I- or OT-II-expressing S. epidermidis could prime OVA-specific CD8+ or CD4+ T cells, respectively, without any barrier breach or skin inflammation. The engineered strains of S. epidermidis could stimulate antigen-specific T cells in vitro and in vivo.

Cited: 8e4b7872a7579d54-cb6467cd::s89, 8e4b7872a7579d54-cb6467cd::s92, 8e4b7872a7579d54-cb6467cd::s93

### `77a41274-cd9c-48bc-a347-e0746907840d`
> **Enlarged granular cells** The α PrePro and Ost1ssα Pro sequences resulted in enlarged granular cells, expanded ER membranes, and relocalization of HsMOR-GFP to puncta.

Cited: 33d9e243f2ee99de-02bbb79f::s173

### `5a2128ad-3127-4595-b810-db128d1a2335`
> **TM2** The homology models were weak in the extracellular TM2-TM3 loop region and did not predict partial unwinding of TM3 at the extracellular end, an unusual feature of Hc ChRs that they share with ChRmine. In contrast, models were particularly good for helices TM1, TM6, and TM7.

Cited: f2e1fb5c9886efad-202dbbbb::s113, f2e1fb5c9886efad-202dbbbb::s114

### `d65103ae-c881-4116-a0a7-1b233eb6275a`
> **gp02** Whereas regulation of the three host genes all involved sequestration of the target ribosome-binding site, regulation of gp02 occurs in the coding sequence, indicating that target regulation might be accompanied by ribonuclease recruitment.

Cited: d1ef96583ec64586-195f7c93::s219

### `ab5eb050-d134-4445-9307-6faa08be7474`
> **1300 anstrom^2** Formation of the DarR dimer by interaction of the two monomers results in the burial of ~1300 Å 2 of surface from solvent.

Cited: 405dcaff86bce126-c6c89512::s68

### `82de3e92-abe2-46ac-ad17-23417b9c4da7`
> **increases** To assess the role of ECL3 in A3AR, we engineered chimeric receptors by grafting ECL3 from A3AR onto the backbones of other adenosine receptors. The three ECL3-chimeric receptors gained the ability to bind CF101 and CF102 with increased efficacy or potency.

Cited: 23f9c4bad2271b89-675be55a::s146, 23f9c4bad2271b89-675be55a::s148

### `7cf0fcde-fea8-420c-8531-2f2fe9e38980`
> **Yes** Having demonstrated robust tagmentation over large ranges of cDNA, Tn5 and reaction volumes, we realized an opportunity to exclude several time-consuming and expensive experimental steps, including excessive cDNA preamplification, concentration measurements, bioanalyzer QC traces and cDNA amount normalization. Instead, cDNA products after preamplification at fewer cycles could directly be tagmented without the abovementioned steps - this strategy we termed Smart-seq3xpress. To explore this potential, we first generated libraries with low-volume RT (300 nL lysis volume) from HEK293FT cells and using a range of PCR preamplification cycles (10 to 20), that strikingly, revealed very similar gene detection without any need for additional enzymatic reaction clean-ups.

Cited: 70758b216a7dc837-240c67f2::s36, 70758b216a7dc837-240c67f2::s37, 70758b216a7dc837-240c67f2::s38

### `da5b2a8f-ba08-4692-851f-2e0bf142a02f`
> **Yes** We performed a base-editing screen against all canonical splice donor or acceptor sites present in CD33 to identify single base edits that reduced or eliminated CD33 expression in HSPCs. Multiple sgRNAs were enriched in the CD33 low population, with strong enrichment for sgRNAs targeting splice donor sites of exons 1 and 2. We performed another systematic mutagenesis screen of CD33 splice sites, as was done with ABE8e, but with evoFERNY protein instead.

Cited: 6acd5496cc0d3cfd-49391314::s129, 6acd5496cc0d3cfd-49391314::s131, 6acd5496cc0d3cfd-49391314::s249

### `e2fb56b7-08cd-4dc0-bc63-b45931a74fc9`
> **More diffuse** In LatC, upper somata tended to focus their axonal terminations in a small area, whereas deep somata tended to project more diffusely, with middle somata exhibiting an intermediate pattern. Upper somata are located in layer 1 and 2/3, middle somata in layer 4 to upper layer 5, and deep somata in lower layer 5 and layer 6. IT cells can have focal or sparse patterns in their contralateral projections, with sparse projections originating from deep-layer cells and targeting deep layers, while focal projections originated from upper-middle layer cells.

Cited: 56e5853498f0abb3-aaa4ebb4::s308, 56e5853498f0abb3-aaa4ebb4::s316, 56e5853498f0abb3-aaa4ebb4::s317, 56e5853498f0abb3-aaa4ebb4::s318, 56e5853498f0abb3-aaa4ebb4::s400, 56e5853498f0abb3-aaa4ebb4::s401

### `eda34fde-798e-43a1-a9d3-a804d3d8ee4e`
> **They maintain a negative bias** The negative bias in decision-making persisted after effective microstimulation, with negative biases in decision-making sustained in the Follow-up block. During the Follow-up block, the behavioral effects of microstimulation persisted, but the microstimulation did not directly influence the network. The attenuated signal flow in the FCS network could induce persistent negative bias observed in the effective sessions.

Cited: f476506231a1bcfd-731d4d10::s132, f476506231a1bcfd-731d4d10::s134, f476506231a1bcfd-731d4d10::s260, f476506231a1bcfd-731d4d10::s267

### `0eede7a8-fe1f-42d3-a2c6-478083648644`
> **subtle increase** Both SNVs lead to a subtle increase in relative affinity of ETS-A to 0.24 and 0.26 respectively. Both human variants cause a similar subtle increase in the relative affinity of the ETS-A site from 0.15 in the reference to 0.24 in French 2 and 0.26 in Indian 2. EMSA confirms that both variants bind to ETS-1 more strongly than does the wild-type (WT) ETS-A.

Cited: ebc08bec41d51153-ab2b3568::s102, ebc08bec41d51153-ab2b3568::s83, ebc08bec41d51153-ab2b3568::s84

### `d1307e50-3c03-4c76-81ee-2decb5de5f14`
_Refused._

### `10cece36-a507-4a93-9600-13f3e0e677f8`
> **strong increase** Removal of DNA methylation dramatically increased repeat-derived RNA, in particular from IAP elements, in DNMT-TKO neurons. This resulted in a 200-fold induction of IAP elements, which comprise one-third of repeat-derived RNA in DNMT-TKO neurons. The absence of DNA methylation causes rampant transcription of retrotransposons specifically in neurons.

Cited: 45a7bf5a940e82ae-b0a29e9c::s186, 45a7bf5a940e82ae-b0a29e9c::s187, 45a7bf5a940e82ae-b0a29e9c::s55

### `f5a84803-3917-43eb-801b-8dc0c5400da1`
> **Increases dephosphorylation** From an initial panel of thirteen inhibitors, we found two related compounds, pexmetinib and BIRB796, that increased the rate of pT180 dephosphorylation 10-fold and 2-fold, respectively. Pexmetinib is a conformation-selective p38α inhibitor that stimulates threonine dephosphorylation of the p38α activation loop by WIP1. The compounds do not directly control WIP1 activity, but instead act through binding to p38α-2p to modulate the rate of WIP1 catalyzed p38α dephosphorylation.

Cited: 1f689965a0b8b875-14dc08ae::s54, 1f689965a0b8b875-14dc08ae::s59, 1f689965a0b8b875-14dc08ae::s61

### `c47dd378-dde3-4a45-9184-6abfa6163717`
> **no change** When p300 catalytic activity was inhibited with the small molecule A485, no decrease in TF binding was observed despite a marked reduction in H3K27 acetylation. p300 inhibition has little to no effect on average TF occupancy.

Cited: 3e070f56a44a20e5-f3eb62ec::s178, 3e070f56a44a20e5-f3eb62ec::s246

### `0bac8974-554c-439a-a9a2-22fa509c8d5d`
> **Preferentially binding to b2b3 complex over b1b2b3 complex** Based in part on the discovery that the heterotrimeric IL-2R αβγ is preferentially expressed on Tregs, we developed bempegaldesleukin, an engineered cytokine designed to improve the efficacy, tolerability, and pharmacokinetics of IL-2. Specifically, we designed it to have an extended half-life, providing controlled and sustained signaling through the heterodimeric IL-2 receptor pathway (IL-2R βγ) to preferentially activate and expand effector CD8+ T and NK cells over Tregs in the tumor microenvironment. Preclinical evidence from mouse tumor models indicates that bempegaldesleukin limits intratumoral Treg proliferation and survival by way of promoting apoptosis, thereby polarizing the TME toward CD8+ T cells and consequently driving a very high CD8+/Treg ratio.

Cited: f297ec065068a1fb-b871f9c0::s109, f297ec065068a1fb-b871f9c0::s81, f297ec065068a1fb-b871f9c0::s82, f297ec065068a1fb-b871f9c0::s92

### `aaa85379-1e4b-4642-9ec4-e1a6d6c29c3b`
> **72** Finally, we validated SNIPR001 on a clinical panel (n = 72) of fluoroquinolone-resistant E. coli strains that were isolated from either a fecal sample or a perianal swab from hematological cancer patients. The panel comprising 72 fluoroquinolone-resistant E. coli strains is isolated from either fecal samples or perianal swabs of hematological cancer patients hospitalized for hematopoietic cell transplantation.

Cited: 5b90612d4398fbee-f46e1738::s1713, 5b90612d4398fbee-f46e1738::s1714, 5b90612d4398fbee-f46e1738::s1715, 5b90612d4398fbee-f46e1738::s1716, 5b90612d4398fbee-f46e1738::s879, 5b90612d4398fbee-f46e1738::s880, 5b90612d4398fbee-f46e1738::s881

### `aa1835b2-2b1c-4986-b7af-e174da0124b0`
> **14 days** In primary neurons cultured from LSL-CRISPRi mice, AAVs delivering sgHspa5 led to marked Cre-dependent neuronal death within 2 weeks of expression. Survival was determined by counting GFP+ nuclei over time and normalized to peak fluorescence, which occurred at day 8, with representative images shown at 16 days post transduction.

Cited: da980e1bd5938c42-2c1acbbe::s1454, da980e1bd5938c42-2c1acbbe::s1455, da980e1bd5938c42-2c1acbbe::s427

### `5a9c6697-a65c-49c0-9e02-38b2a276fde7`
> **2** Two FMD cycles were the minimum required to cause a significant delay in melanoma growth.

Cited: d1755fd36d8b3c25-7928fced::s295

### `37a4d007-793e-4a89-922a-c1b05f4f82c1`
> **34** C1QTNF1 is the gene encoding CTRP2 (C1q/TNF-related protein 2), which is one of the adiponectin paralogs identified in mice. There are a total of 14, 34, 23, 23, 14, and 34 Gly-X-Y repeats in the collagenous domain of mCTRP1, mCTRP2, mCTRP3, mCTRP5, mCTRP6, and mCTRP7, respectively.

Cited: f265b292c35123ad-a2a40b50::s121, f265b292c35123ad-a2a40b50::s124

### `c9baf8e0-c4c7-4ba3-b5c4-18e9af8b2df1`
> **2** Adenosine deaminases (A_deamin, PF02137 in InterPro database), enzymes involved in purine metabolism, were split into different clades when using structure-based clustering. When using amino acid sequence-based clustering methods, adenosine deaminases were grouped together into a single A_deamin-clade, but were all grouped together into a single A_deamin-clade using structure-based clustering approach. Structure-based hierarchical clustering showed that different clades reflected unique structures, implying distinct catalytic functions and properties.

Cited: 635912ff7732db5a-d3b4f268::s214, 635912ff7732db5a-d3b4f268::s216, 635912ff7732db5a-d3b4f268::s245

### `d0f69626-66ee-4807-937d-c3a024441812`
> **3601** There were 3,601 differential peaks between the queens and workers, and more peaks were up-regulated in the queen, which were distributed in the intron and promoter regions.

Cited: d37934bbe3d8f67c-d961c2b7::s111

### `462a9f38-7cbe-4e12-a6e2-b1d7028c3a8b`
> **18164** Inspection of TnG-repeat-like elements in the Homo sapiens and Danio rerio genomes revealed 18,164 and 5,517 distinct sites containing TnG repeats (>29 nucleotides), respectively, in comparison to the 46,574 sites in the M. musculus genome.

Cited: 676ba1096cbf511b-b1513bb8::s209

### `86f111e5-402b-4ef5-b101-8be1bf5be7c6`
> **5765** 19,638 promoters of 5,765 genes were found to be differentially methylated at Braak V/VI compared to Braak 0.

Cited: c8bdc674e9741afa-093821ac::s239

### `cbe93a43-09cd-4cb4-9edd-f22fe8c28415`
> **7875** On FORSK and inosine treatment, 7,875 and 8,613 phospho-sites were regulated (FDR < 0.05), respectively, with 2,535 phospho-sites being significantly regulated in both treatments.

Cited: c090173e7e65c0e3-514e4135::s180

### `7a88e6f7-fb8e-4a24-b08d-9b7a6edafe57`
> **80** Using the algorithm G4 hunter, we identified 80 putative G4-forming sequences (PQSs) within TMPRSS2 gene.

Cited: 4cbe11308ab2309d-80cecb52::s238, 4cbe11308ab2309d-80cecb52::s239, 4cbe11308ab2309d-80cecb52::s240

### `91387526-9268-4a3c-9abe-73819707d0b0`
> **5-fold** We found that katE, ABUW_2639, and ABUW_2724 mutants were about 5-fold more sensitive to desiccation than the wild type.

Cited: c2cda5b607346e60-ae8acc05::s156

### `7b98796f-25be-4c58-a52a-4e366c0ffd95`
> **47** The LIMK PDZ domain between human LIMK1 and human LIMK2 are 47% identical and 81% similar.

Cited: d3879bce9d87fba9-f83867bf::s80

### `5e20e26d-6192-4563-abb3-a4857e3dbc7c`
> **0.23-0.9** DNA sequences with a motif surrounded by STRs were consistently bound 0.23-0.90 kcal/mol tighter than those with a motif surrounded by random sequences.

Cited: 0ea4869095e7f1ab-e4a06775::s93

### `b105af85-833e-48bc-ac78-48f73c9673fd`
> **43.6** The full-length Vibrio cholerae RfaH shares 43.6% sequence identity with E. coli RfaH.

Cited: f5f69f4f8c501c4d-1b1d2b64::s151

### `5b6d6f82-a585-4aa8-9fe6-e7d35f7cb2ae`
> **Above 40%** Formulations with over 40% substitution with PEG-maleimide showed no detectable levels of transfection. MH42 at 0.15% (10% of total PEG), 0.3% (20% of total PEG), and 0.6% (40% of total PEG) showed Müller glia transfection after intravitreal administration.

Cited: 57be1424a3665e9d-92cfef3b::s552, 57be1424a3665e9d-92cfef3b::s553, 57be1424a3665e9d-92cfef3b::s554, 57be1424a3665e9d-92cfef3b::s556, 57be1424a3665e9d-92cfef3b::s557, 57be1424a3665e9d-92cfef3b::s558

### `12321eab-6ad6-4218-8815-18bc51c14544`
> **You need 10x less** Complete inhibition of proliferation was observed at roughly 1/10th the concentration required to arrest cell proliferation on plastic. On the softest matrix (0.5 kPa), fibroblasts treated with 250 nM bleomycin experienced a modest 44% increase in cell number over three days compared to nearly 200% for plastic, a near total growth arrest at 1/20th the required dose of plastic. Fibroblasts exposed to senescence-inducing drug bleomycin have a higher propensity towards entering a non-proliferative, senescent like state on softer substrates (0.5-25 kPa) compared to stiff tissue-culture plastic.

Cited: 9fcf84b83327fac1-12161dc6::s81, 9fcf84b83327fac1-12161dc6::s82, 9fcf84b83327fac1-12161dc6::s83

### `c33446f6-fbff-4186-8a51-28a17f68bd40`
> **Lagrange multiplier constraints** The constraints for Wyckoff sites are implemented as Lagrange multiplier constraints. To perform constrained molecular dynamics of particle occupying a Wyckoff position, particles must stay in a Wyckoff position at all times, which can be accomplished via traditional constrained molecular dynamics of Lagrange multipliers.

Cited: 8b9ff18e3a47be61-28103adf::s120, 8b9ff18e3a47be61-28103adf::s121, 8b9ff18e3a47be61-28103adf::s183

### `b1d5a5f5-6e89-4dfb-b60d-5a9824b015f3`
> **attenuation of loss** Microglia-specific Ifnar1 deletion attenuated the loss of post-synaptic terminals by selective engulfment. While both pre- and post-synapses were reduced in normal 5XFAD brains, PSD95+ puncta density, but not synaptophysin+, was restored in 5XFAD;MKO mice. Independent analysis of Vglut1 and GluR, another pair of excitatory pre- and post-synaptic markers, respectively, showed reestablishment of GluR, but not Vglut1, in 5XFAD;MKO mice, corroborating a selective effect of microglial IFN-I signaling on post-terminals of excitatory synapses.

Cited: 531777a8384af139-4695824d::s145, 531777a8384af139-4695824d::s147, 531777a8384af139-4695824d::s47

### `6aa10957-bdd9-4dab-a4e1-234a17cb87dd`
> **restoration** Neural Ifnar1 deletion restored pre-synaptic terminals in 5XFAD mice. In 5XFAD;NKO mice (neural Ifnar1 deletion), synaptophysin+ puncta density, which labels pre-synaptic terminals, was restored, whereas it was not restored in 5XFAD;MKO (microglia-specific deletion).

Cited: 531777a8384af139-4695824d::s163, 531777a8384af139-4695824d::s47

### `28ebecdf-949e-4d20-aca9-5989b7a9d6e9`
> **PBE1** Among four selected 20 S proteasome subunits known to interact with SE, CWC15 interacted with PAB1, PAG1 and PBA1, but not PBE1, in the nucleus.

Cited: 4fe437fb33178a64-5db8a7b0::s244

### `dbb51a1c-f9a2-4960-a93c-118957659790`
> **-8** According to the degron index model, a Ser residue at position -8 is predicted to favor degradation (CDI ≤ 40).

Cited: 93344b73bc0f6720-3f6b52f2::s125

### `85c67ef3-322c-42b4-b745-c05e07e7b8ac`
> **3-4 days** Stimulation of RAS-MAPK signaling with 4OHT for ≥3 days engaged the cells to a stable proliferation arrest, whereas shorter stimulation did not. Cells induced for ≥3 days were senescence-associated β-galactosidase positive 6 days after ending ERK stimulation, whereas cells induced for 1, 1.5, or 2 days were not, indicating that they are fully senescent. Cells committed to senescence after 3-4 days of ERK activation remained committed even if ERK signaling was brought back to basal levels using inhibitors.

Cited: 039834c95dd3a676-7b222494::s83, 039834c95dd3a676-7b222494::s85, 039834c95dd3a676-7b222494::s98

### `653635b7-3bc6-4a7b-98c7-c02038c0e928`
> **CD8+/IGNF +** STK11 mutation was positively associated with CD8+/IFNG+ and downregulated its RNA and protein expression in LUAD (p < 0.05). Protein levels of STK11 were significantly reduced in CD8+/IFNG+ compared with other subtypes.

Cited: 01604c16c5a26a1f-157aef00::s369, 01604c16c5a26a1f-157aef00::s370

### `100b570f-1c4f-4214-8402-f1b15f9989b4`
> **30%** Mice with a homozygous knock-in MIRAS allele show a 30% decrease in rotarod performance at 12 months of age.

Cited: 09768e5cf98b5291-c38b8d49::s203

### `0a9d6516-95ef-4d7b-a28d-d7cde27b7b55`
> **40 hours** In pre-commitment cells (24 or 40 h -E2), reactivation of ER-HOXA9 successfully re-established a pattern of gene expression that was nearly indistinguishable from the transcriptome of naive +E2 progenitor cells. In contrast, in cells withdrawn from E2 for 72 h, reactivation of ER-HOXA9 was unable to reverse the global induction of differentiation. By 72 h -E2, the cells had passed a key commitment point, beyond which their phenotype was maintained in the absence of the originating stimulus.

Cited: aef60484f35c4136-1379b717::s205, aef60484f35c4136-1379b717::s206, aef60484f35c4136-1379b717::s208

### `8d61a14b-60ef-43b0-8003-b60cb6657428`
> **Neu5Ac** The glycan probe used in the ARPLA method contains a Neu5Ac aptamer as one of its three sections.

Cited: 170f8322198d6069-0c88279c::s38, 170f8322198d6069-0c88279c::s39

### `4d4cb121-9525-499a-9475-9b212465c72d`
> **symmetric sampling of the SDE/ODE (analytical conditioning)** We began by considering analytic conditioners that can control protein backbone geometry. We found that conditioning on the symmetry of protein complexes can readily generate samples under arbitrary symmetry groups. The paper explored symmetrize complexes under arbitrary symmetry groups as one of several conditioner primitives. Sampling oligomeric structures with arbitrary chain symmetries is possible by using a conditioner that tessellates an asymmetric subunit in the energy function.

Cited: 6223b4c58a3e1894-0f5f8dde::s100, 6223b4c58a3e1894-0f5f8dde::s139, 6223b4c58a3e1894-0f5f8dde::s140, 6223b4c58a3e1894-0f5f8dde::s161

### `ca4c9d21-b842-4875-9a6a-bcb9f6c55073`
> **48** The LungMAP Human Lung CellRef contains a total of 347,970 cells and 48 well-defined lung cell types, covering major cellular heterogeneity in the four regions: trachea, bronchi, SMG, and lung parenchyma. In total, 8080 seed cells were identified for 48 normal human lung cell types.

Cited: 0bd1ca4800d9e08e-ed49ee6f::s342, 0bd1ca4800d9e08e-ed49ee6f::s542

### `c3816cb5-8c87-4946-b133-43f415ab6b2a`
_Refused._

### `59745f75-52bf-4815-905c-3dfad1ef8923`
_Refused._

### `26691c84-514b-4712-a43e-09705d681e45`
> **SIN3 histone deacetylation** Inactivation of genes encoding members of the TP53 signaling pathway (TFDP1 and HIPK2), SAGA H3 acetylation complex components (KAT2A, TRRAP, TADA3, TAF5L, TADA2B, SGF29 and TADA1), and the Fanconi Anemia complex (FANCA, FANCC, FANCE, FANCF, FANCG, FANCL and FAAP100), all implicated in DNA damage repair, resulted in resistance to colchicine. Inactivation of members of the SIN3 histone deacetylase (SIN3B, SINHCAF and ARID4B) resulted in palbociclib sensitivity, not colchicine resistance.

Cited: 3421ed4fd7502c9a-466927e6::s135, 3421ed4fd7502c9a-466927e6::s139

### `0e53a08c-4252-4a84-962b-5b396f9740aa`
_Refused._

### `8ade3e3a-4792-4965-b9d9-05e528ebbfa0`
> **No** Doublecortin (DCX), a widely accepted marker of newly generated granule cells, was detected in diverse human neurons, but it did not define immature neuron populations. Other studies have reported varied amounts of cells expressing doublecortin (DCX; a widely adopted marker of neuroblasts and immature neurons) in the adult human DG, and around 75% of DCX-expressing cells were colocalized with NeuN, a marker of mature granule cells, suggesting that most DCX-expressing cells might actually be mature granule cells or interneurons rather than newly generated immature cells.

Cited: e7d33e6c5033c2e2-30e83b44::s393, e7d33e6c5033c2e2-30e83b44::s61, e7d33e6c5033c2e2-30e83b44::s76

### `f5a4b449-e647-4ae0-8419-c221792482c9`
> **AAGAG lncRNA** CifA is a ribonuclease (RNase) that depletes a spermatocyte lncRNA important for the histone-to-protamine transition of spermiogenesis. lncRNA knockdown enhances CI, and mutagenesis links lncRNA depletion and subsequent sperm chromatin integrity changes to embryonic DNA damage and CI. To directly test the involvement of the lncRNA in CI, we used transgenic flies with RNA interference (RNAi)-mediated knockdown of the AAGAG lncRNA. AAGAG-knockdown males (AAGAG_KD+) induced approximately threefold more CI (median embryonic hatching = 11.8%) upon mating with uninfected (wMel-) females compared with control males, indicating causal interaction between Wolbachia and AAGAG lncRNA depletion on CI. The role of CifA in depleting AAGAG lncRNA suggests that CifA RNase activity is central to establishing the CI modification during early sperm development.

Cited: c1799acd1f08346b-7a1ba0f8::s17, c1799acd1f08346b-7a1ba0f8::s19, c1799acd1f08346b-7a1ba0f8::s85, c1799acd1f08346b-7a1ba0f8::s89, c1799acd1f08346b-7a1ba0f8::s90, c1799acd1f08346b-7a1ba0f8::s93

### `5806ed2a-1005-44f1-8d70-332048fea8f4`
> **VGlut2** NIF, a glycoprotein produced by a canine hookworm, is a selective antagonist of the CR3-CD11b subunit, preventing the recognition of its endogenous ligands. Neonatal male mice received bilateral microinjections of PBS or NIF (200 ng) into the ACC at P7, and brain tissue was collected 24 h later. Microglia from animals microinjected with NIF had a significant reduction in the phagocytic index (~50%) and a significant decrease in the total lysosomal content within each microglia. NIF injections at P7 effectively reduce microglial phagocytic capacity and engulfment of VGlut2, which induces an abnormal increase in VGlut2 synapse density.

Cited: c0b69d2af9f2e018-845b5d60::s370, c0b69d2af9f2e018-845b5d60::s372, c0b69d2af9f2e018-845b5d60::s374, c0b69d2af9f2e018-845b5d60::s377

### `6fff0994-6d02-470a-9d61-8e35420412b6`
> **Chromosome 8** When the allele frequencies for the mutant individuals were plotted across all 27 chromosomes in the P. patens genome assembly, a peak of the expected allele frequency was revealed on chromosome 8, which provided a region of the genome to interrogate for causative mutations. Gene candidates identified following interrogation of the genomic locus on chromosome 8.

Cited: 68a6c661e51b59ab-413f9855::s1416, 68a6c661e51b59ab-413f9855::s391

### `8266ac61-92d6-423d-8e7a-fe47b3a7e885`
> **No difference in social communicative behaviors** Inhibition of BNST AVP cells did not affect social communicative behaviors (i.e., urine marking and ultrasonic vocalizations) in males or in females, which produced little to no urine marks and vocalizations in any condition.

Cited: 38a955fae1cd37d4-f0d43e7b::s103

### `322454df-45a8-41b3-9b0a-4e808144023c`
_Refused._

### `3c9f23e2-fdd0-431b-aca7-4f9556c78f1f`
_Refused._

### `983f1ef5-fc7d-4f4a-8f48-e704641eae12`
> **Flocculation** Several genes found in the reference laboratory strain were deleted in Wyeast 3068, and deleted genes were enriched for processes of flocculation (P ≤ 4.59 × 10^-5, FLO5, FLO9, FLO1, FLO10), carbohydrate transmembrane transport, asparagine catabolism, and transposition.

Cited: 74a92b882343d335-0d4fcaac::s193, 74a92b882343d335-0d4fcaac::s194

### `7d2c8d44-ecf3-40d2-ab69-b6195c46ffe9`
> **Shorter cilia** Kif9 KD embryos also had shorter cilia than controls (P<0.0001). This phenotype was also rescued by expression of Kif9-GFP, demonstrating the specificity of the effect.

Cited: 8061d302c8a858a8-d1033cab::s133, 8061d302c8a858a8-d1033cab::s134

### `720e20c2-9ad1-4d98-9f01-8b7fb3782a46`
> **decreases** Removal of sialic acid moieties from T cell surfaces through neuraminidase treatment resulted in a decrease in Siglec-15 binding comparable to that measured in the case of complete deglycosylation. The sialic acid moiety is the key unit for the binding of Siglec-15 to human T cells. Sialic acid moieties on α(2,3) and α(2,6) sialoglycans were specifically removed from the surface of T cells through the action of neuraminidase, demonstrating the importance of these structures for Siglec-15 binding.

Cited: 66609914f1843fd6-9d104250::s98, 66609914f1843fd6-9d104250::s99

### `dbfbae3d-62f6-4710-8d13-8ce4c8485567`
> **heart** SLC14A1 (solute carrier family 14 member 1) appears to be a specific marker for endothelial cells in the heart, whose expression was independently validated with data from the Human Protein Atlas.

Cited: 83a86f1f96eceb6e-73d94b3b::s104

### `7a42c784-7ae0-48fe-a71f-0a547b8fabb3`
> **E467** All Fanzor proteins and TnpBs with a loss of the canonical glutamic acid in RuvC-II contained an alternative conserved glutamate approximately 45 residues away. The alternative conserved glutamate of Fanzor nucleases and rearranged TnpB (E467 of ApmFNuc and E323 of TvTnpB) were in close proximity with the catalytic residues in the RuvC-I and RuvC-III motifs, suggesting that these alternative, conserved glutamates compensate for the mutation in RuvC-II. The alternative Fanzor glutamate is indeed essential for the nuclease activity, as both RuvC-I and RuvC-II mutants (including E467A) abolished ApmFNuc cleavage activity.

Cited: 2626aa23d080eaee-35590d07::s1093, 2626aa23d080eaee-35590d07::s1094, 2626aa23d080eaee-35590d07::s1095, 2626aa23d080eaee-35590d07::s1108, 2626aa23d080eaee-35590d07::s1109, 2626aa23d080eaee-35590d07::s1110, 2626aa23d080eaee-35590d07::s1111, 2626aa23d080eaee-35590d07::s1112, 2626aa23d080eaee-35590d07::s1113, 2626aa23d080eaee-35590d07::s1114, 2626aa23d080eaee-35590d07::s1115, 2626aa23d080eaee-35590d07::s1116, 2626aa23d080eaee-35590d07::s1117, 2626aa23d080eaee-35590d07::s1118, 2626aa23d080eaee-35590d07::s1119, 2626aa23d080eaee-35590d07::s1125, 2626aa23d080eaee-35590d07::s1126, 2626aa23d080eaee-35590d07::s1127, 2626aa23d080eaee-35590d07::s1128, 2626aa23d080eaee-35590d07::s1129, 2626aa23d080eaee-35590d07::s1130

### `0708b62f-9652-49eb-8ba6-28878afa7445`
> **75%** Using STED, we found that NCAN C-terminal colocalizes with 75% of inhibitory synapses and 40% of excitatory synapses.

Cited: f8498fdbd6c2acbf-3a73e8c9::s392

### `5b3b7d05-9e54-445c-b374-d4c6b60923b4`
> **0.6-3.16m/s** The average speed of the jet for cicadas is around (u 0.6 to 3.16 m/s) and the total volume per excretion event ranges from (6 to 574 L).

Cited: f597b9fbade66ea8-abe5e6df::s40

### `623a831f-41ee-4e0e-936a-87f93d96369e`
> **mp** The cavity above the p-hydroxybenzylidene moiety of the chromophore in mSandy2 is filled by the mp rotamer of Leucine at position 63. The mp rotamer is defined as having χ1 = gauche(-) and χ2 = gauche(+), and it fills the cavity above the p-hydroxybenzylidene moiety of the chromophore by packing tightly against it. In contrast, the alternate pt rotamer (χ1 = gauche(+), χ2 = trans) does not fill the cavity.

Cited: 9fa80155de882a7c-15748f57::s512, 9fa80155de882a7c-15748f57::s513, 9fa80155de882a7c-15748f57::s591, 9fa80155de882a7c-15748f57::s593, 9fa80155de882a7c-15748f57::s594, 9fa80155de882a7c-15748f57::s607, 9fa80155de882a7c-15748f57::s608

### `0b1d5537-db47-420c-984b-9b56d38e6d98`
> **Hs α7** While a single-humanized Hs α6 strain is temperature sensitive (TS) at 37°C, a combination with the neighboring humanized α7 gene rescues the phenotype. MERGE revealed the fitness of paired-humanized genotypes similar to synthetic genetic interactions, showing that Hs α6 can functionally replace its yeast ortholog when co-expressed with Hs α7.

Cited: 521366a95024715c-ba05c1a4::s124, 521366a95024715c-ba05c1a4::s126

### `ade96656-7ed1-4e21-b009-b7a73e13bff5`
> **ACKR1** VE3, which forms ~2% of endothelial cells, is characterized by gamma synuclein (SNCG) and high expression of the venular capillary marker ACKR1. CellPhoneDB analysis predicted a significant enrichment for ACKR1 on VE3 to interact with CXCL8 (IL-8) on Mac2. The reemergence of prenatal vascular endothelial cell and macrophage cellular programs occurs in atopic dermatitis and psoriasis lesional skin.

Cited: 98bfd461c77d2ddb-abe7e939::s221, 98bfd461c77d2ddb-abe7e939::s234, 98bfd461c77d2ddb-abe7e939::s99

### `78a2c1d2-f035-4c7d-a7ee-40dfd95ca88a`
> **0.09-0.24** The putative ETS sites within the FoxF enhancer bind ETS with low relative affinities ranging from 0.09 to 0.24. These affinities are calculated as the ratio of each 8-mer's fluorescence to the fluorescence of CCGGAAGT, the 8-mer with the highest affinity for ETS1.

Cited: d344be98a61d850f-3c8cc77a::s101, d344be98a61d850f-3c8cc77a::s102

### `224efcd7-3652-47f8-84dd-15b4c6fafae2`
> **E2** ChIP-qPCR experiments using H3K27ac (Histone 3 Lysine 27 Acetylation, super-enhancer marker), H3K4me1 (Histone 3 Lysine 4 Monomethylation, enhancer marker), and FOXP3 antibodies revealed that FOXP3 had a strong binding affinity to segment E2 of the UNC5B-AS1 upstream super enhancer region.

Cited: 3a2c0120637483ba-5adda325::s361

### `55187fb4-e7ee-4027-b74f-cab50f328442`
> **CXCL17** For the Relapse signature, the upregulated genes LCN2, LTF, SAA1, SAA2, CXCL17 were strongly (Spearman coefficient [sCC] >= 0.25) and the genes GABRP, IGHG3, IHGH4, IGLC7, MUC5B, CCL19, CXCL2, CXCL5 were weakly (sCC >= 0.15) positively correlated with Club cells. LCN2, LTF, MUC5B, CXCL1, CXCL6, and CXCL17 are enriched in so called effector Club cells of the lung tissue playing a crucial role in the first line of immune response.

Cited: 129870223e3a57d6-aed81b74::s137, 129870223e3a57d6-aed81b74::s148

### `25a9cf59-1c28-4ddf-b797-f43efb9349e6`
> **mitochondria** We identified 367 differential morphology features between apoptosis and control group cells, with most morphology changes from the mitochondria and nuclei. Apoptosis had more morphology feature changes, mostly impacting mitochondria.

Cited: 324908523a45ed3e-0832d3f2::s126, 324908523a45ed3e-0832d3f2::s204

### `12a20d8d-cd49-47eb-9a19-6a38519ee3dc`
> **No effect** OT-1 T-cells were cultured for 24 hours in UCM, SCM or ACM (without stimulation). We found that T-cells did not exhibit significant alterations in their surface expression of the TCR nor the CD8α co-receptor, although a trend towards increased surface expression was noted in ACM. CD8α expression of OT-1 T-cells after a 24 hr treatment with UCM, SCM or ACM showed no significant differences, with statistical comparisons showing: UCM v. SCM P = 0.7383, UCM v. ACM P = 0.9964, SCM v. ACM P = 0.7830.

Cited: 2cdfbcfbe2f97d62-25857e4e::s134, 2cdfbcfbe2f97d62-25857e4e::s135, 2cdfbcfbe2f97d62-25857e4e::s136, 2cdfbcfbe2f97d62-25857e4e::s137, 2cdfbcfbe2f97d62-25857e4e::s138, 2cdfbcfbe2f97d62-25857e4e::s139, 2cdfbcfbe2f97d62-25857e4e::s140, 2cdfbcfbe2f97d62-25857e4e::s141, 2cdfbcfbe2f97d62-25857e4e::s174, 2cdfbcfbe2f97d62-25857e4e::s175

### `4bb69c9d-2485-42d2-b8aa-aa647b407ca4`
> **Decrease** Compared to wild-type Spn-E, Spn-E-EQ caused a reduction of mature piR1712 and piR2986 and a concomitant accumulation of longer RNA signals that correspond to the lengths of their pre-piRNAs. piR1712 and piR2986 are representative Siwi-bound piRNAs generated by BmAgo3-mediated cleavage, and their levels were detected in BmN4 cells expressing Spn-E-EQ by northern blotting.

Cited: 6f9603c4a7dfa9ed-8ee6647e::s350, 6f9603c4a7dfa9ed-8ee6647e::s351, 6f9603c4a7dfa9ed-8ee6647e::s352, 6f9603c4a7dfa9ed-8ee6647e::s353, 6f9603c4a7dfa9ed-8ee6647e::s354, 6f9603c4a7dfa9ed-8ee6647e::s355, 6f9603c4a7dfa9ed-8ee6647e::s356

### `8c833521-56c4-458d-8c65-2bbf66190cae`
> **Insufficient information to answer** The sources discuss NCED3 expression in response to avrPtoB mutant and effector-less strains, but do not specifically address the effect of avrE single knockout on NCED3 expression. While the sources extensively discuss how HopM1 and AvrE1 together induce ABA biosynthesis pathways and affect ABA-related gene expression, there is no specific data provided about NCED3 expression in response to avrE single knockout Pst DC3000.

Cited: ff5bb438eb6b3659-38bb2e97::s339, ff5bb438eb6b3659-38bb2e97::s340, ff5bb438eb6b3659-38bb2e97::s344

### `255fd5fb-9623-4030-8bf2-253247df7c82`
> **Increased expression** A. thaliana plants infected with Pst DC3000, hopM1−, and avrE1− single mutants, but not with h−/a− double mutant, showed significantly higher expression levels of the ABA biosynthesis marker gene NCED3 than mock-infected plants. HopM1 and AvrE1 act redundantly in affecting the Arabidopsis transcriptome, with an important induction of genes associated with ABA-related pathways when comparing WT Pst versus Pst lacking HopM1 and AvrE1.

Cited: ff5bb438eb6b3659-38bb2e97::s339, ff5bb438eb6b3659-38bb2e97::s340, ff5bb438eb6b3659-38bb2e97::s97

### `38ada695-2c79-459b-8e68-dbed734c74f9`
> **Increased expression** A. thaliana plants infected with Pst DC3000, hopM1−, and avrE1− single mutants, but not with h−/a− double mutant, showed significantly higher expression levels of the ABA biosynthesis marker gene NCED3 than mock-infected plants. The hopM1− single mutant (lacking only HopM1) still induced significantly higher NCED3 expression compared to mock-infected plants, indicating that loss of HopM1 alone does not prevent NCED3 induction.

Cited: ff5bb438eb6b3659-38bb2e97::s97

### `e763edaa-b112-460a-a564-d58a6685e639`
> **increased heterogeneity** To determine if prenatal DEP + MS exposure modifies the relative abundance of these microglial subtypes, we quantified the percentage of Iba1 hi P2ry12 lo or Iba1 lo P2ry12 hi microglia, which we termed here as microglial heterogeneity. However, microglial heterogeneity was strikingly enhanced in DEP + MS male offspring ACC compared with CON, both at P8 and P15. Our data indicate that subtypes of microglia are present during early ACC development and that prenatal DEP + MS insult increases the relative abundance of heterogeneity.

Cited: c0b69d2af9f2e018-845b5d60::s321, c0b69d2af9f2e018-845b5d60::s327, c0b69d2af9f2e018-845b5d60::s328

### `8af900bb-5794-40db-910e-10d5857ce5bd`
> **72%** When mapping the synaptic target properties of bipolar interneurons in mouse vs. human, a fraction of bipolar INs with almost exclusive innervation of other INs in human was not found in mouse, with interneuron targeting by bipolar interneuron axons increasing from 56% in mouse to 72% in human. The 72% figure represents 225 interneuron targets out of 314 total synapses from 9 bipolar interneuron axons in human cortex.

Cited: 3039597cd03cb050-e2ba21eb::s121, 3039597cd03cb050-e2ba21eb::s122, 3039597cd03cb050-e2ba21eb::s123

### `6194ebfc-2d5c-4ccc-8883-da7c471b61e6`
> **100%** All DANs received signals from all sensory modalities. DANs received input from all sensory modalities, including from those that normally sense conditioned stimuli in learning tasks (e.g., olfactory) and from proprioceptive neurons. DANs also receive polysynaptic feedforward inputs from all sensory modalities.

Cited: 0faff73a03a57dfe-cac59605::s265, 0faff73a03a57dfe-cac59605::s448, 0faff73a03a57dfe-cac59605::s994

### `1f1b07d7-39ce-4665-9b70-4ab77e3c87aa`
> **33%** Only 33% (with 5- or 8-hop cascades) of octopaminergic neurons (OANs) received input from all modalities. All DANs, 33% of OANs, and 60% of other MBINs received signals from all sensory modalities.

Cited: 0faff73a03a57dfe-cac59605::s266, 0faff73a03a57dfe-cac59605::s994

### `55668039-396e-488a-b2c3-bbe840550433`
> **20%** 694 (20%) isoforms could significantly alter pseudotime upon overexpression in hESC differentiation

Cited: 0c23610f9819876e-1c7bceee::s145

### `4f050bf3-27cd-4a14-8422-45df5e2bb079`
> **East and southeast: northeast** In the first FST analysis conducted among the four geographical-based Iranian populations, the highest and lowest FST values were observed for the east and southeast: northeast pair (FST= 0.09) and northeast: west and northwest pair (FST= 0.024), respectively. A higher FST value indicates greater genetic differences between populations.

Cited: c5e2b39b87ce68c3-3e8a42d1::s444, c5e2b39b87ce68c3-3e8a42d1::s445

### `cff00d08-5655-4214-97ac-8fa9504c1165`
> **23%** GLP-1-MK-801 produced a vehicle-corrected reduction in body fat mass of 45%, accompanied by an 8% loss in lean mass. In comparison, GLP-1 induced a 22% decrease in body fat mass and a 4% reduction in lean mass. The absolute percent difference in body fat mass loss between GLP-1-MK-801 (45%) and GLP-1 (22%) is 23% (45% - 22% = 23%).

Cited: 8a63ec61b2075d5f-74d7d111::s170, 8a63ec61b2075d5f-74d7d111::s171

### `0eeb7ea9-fc80-4dee-9418-1c328c3ab653`
> **2.45 pM-1** MtNCC11-78 bound one Cu+ per molecule with an affinity constant of 2.45 pM-1

Cited: af470b1b1a34dd6b-0ba6ac3e::s257

### `658f7050-d137-477e-8693-26609080cecd`
> **300 Å** The long, slender stalk of these particles extended about 300 Å, whereas their crown had a width of around 250 Å.

Cited: 0d71c9d2055299d4-2f967140::s162

### `8696273a-7fea-411a-b6c6-0e826e1e02b5`
> **between 0 and 0.3** In mES cells, the contact probabilities of most (~75%) active promoters with the nearest TAD boundary are comparable to those experienced by the ectopic Sox2 promoter in our experiments (lower than 0.2). Contact probabilities steeply decayed with increasing genomic distance from the promoter, fell considerably while approaching TAD boundaries (from 1 to around 0.05) and further dropped by a factor of around 3 across boundaries.

Cited: 071eed17b15b184b-5393792c::s158, 071eed17b15b184b-5393792c::s275

### `ce6dd5f7-0706-41dd-a383-9b0d22ef00a1`
> **Large decrease** We observed a drastic decrease in Pkdh1 abundance in the Ift122-null strain, suggesting that nonciliary Pkdh1 may be either degraded or downregulated in Ift122 ∆-mutant cells.

Cited: 9d1bda6cef59d705-b224f6d8::s148

### `400786c1-e6c6-4f46-a501-86fdd048ed88`
> **Inhibition** Significant accumulation of phosphorylated α-syn was observed upon elevated protein level of Rpn14, independent of the expression level of Tet-RPT2. Rpn14 protein is linked to the accumulation of the pS129 fraction, indicating that Rpn14 suppresses pS129 α-syn turnover. These results reveal that elevated levels of Rpn14 inhibit the turnover of phosphorylated α-syn.

Cited: a95e8580727af033-09043102::s385, a95e8580727af033-09043102::s386, a95e8580727af033-09043102::s391

### `e820cbcf-6df1-4c1c-b985-c02f39f52781`
> **eliminates function** We found that a number of domains that were lowly expressed on their own ablated KRAB function when paired with it. For example, we verified that the poorly expressed DHX16 OB_NTP and BAZ1A DDT domains inhibited KRAB function at 100 ng/mL dox. KRAB maintained its repressive function when paired with most domains except ones that had decreased expression and a few domains from general TAFs and RNA polymerase.

Cited: 71256a6d0f955156-f438b0cb::s272, 71256a6d0f955156-f438b0cb::s273, 71256a6d0f955156-f438b0cb::s365

### `230dec20-cd02-4613-a7b1-e28058ed46fe`
> **Greatly reduced** The firing rate of SMAD1-deficient PV interneurons in response to current injections was significantly reduced in the barrel cortex of adult mice. This reduced firing frequency is most likely to be explained by a reduction in input resistance in the Smad1 ∆PV cells.

Cited: 3b1e01c90c47dd5d-850e00fc::s206, 3b1e01c90c47dd5d-850e00fc::s208

### `7975ddb0-a784-4f85-a297-c80e1cb5dcf2`
_Refused._

### `a1d01019-d2b1-4619-92ec-7ea38578819f`
> **polyadenylation** One study revealed that a novel polyadenylation event, which introduces a new stop codon, generates an EPRS1 variant with a truncated C-terminus called EPRS1(N1).

Cited: 3ced378716ddecf0-3008c492::s137

### `fe074387-3765-4020-8f5d-e395d1094121`
> **30 volume/s** For time-lapse continuous data, 2pSAM can increase temporal resolution with a sliding window during 3D deconvolution by exploiting spatiotemporal continuity and estimating motions during reconstruction, which increases reconstruction volumetric speed to 30 volume/s.

Cited: 3022f334b06fe41f-49e3ab2b::s145, 3022f334b06fe41f-49e3ab2b::s146

### `f0b6cea0-e005-47bc-be0d-9a10b219cae6`
> **63.2** Wukongarchaeia (63.2 °C, 90% CI: 54.8 -65.6 °C) is a moderate thermophile

Cited: e2c5bba3431b7f0b-903142c2::s141

### `ae02d0e9-edf5-4c39-a215-3cbc8f4c565d`
> **Second longest** The second-largest chromosome (47.28 Mb) showed extensive gene synteny with the pea aphid X chromosome. The second-largest scaffold had about half of the normalized sequencing read depth ratio for males when compared with other chromosomes, confirming that it is the X chromosome. We named the 4 autosomes as chromosomes 1 to 4, ordered from longest to shortest.

Cited: d0e434519e92b617-6d9d1707::s83, d0e434519e92b617-6d9d1707::s85, d0e434519e92b617-6d9d1707::s86

### `fd60a0e7-ba64-49a9-843a-6f5cb17c5fa9`
> **α1-driven dimerization.** The N-terminal α1-helical extension drives dimerization within the PF03500 protein family, with the α1-helix guiding the formation of different dimerization interfaces within the tetramer. The α1 dimerization is primarily driven by symmetric hydrophobic contacts between adjoining α1-helices, as well as a combination of hydrophobic and polar interactions with the protein core of the neighboring subunit. The quaternary structure assembly of BcsD homologs is driven by the presence of an N-terminal α-helical extension (α1), which is likely conserved in the majority of bcsD-encoding β- and γ-Proteobacteria.

Cited: ec21473ce029219d-58061129::s207, ec21473ce029219d-58061129::s208, ec21473ce029219d-58061129::s212, ec21473ce029219d-58061129::s315

### `14fd2b75-76fb-4c29-a21d-c557b2bcf2ff`
> **12 Å** The CDRs of P1A4 form a deep, ~12-Å pocket between the heavy and light chains that ARS1620 is able to access.

Cited: 09d92318a4a24d0d-b1ddf424::s100

### `e9f142f0-8ef6-47cd-b846-7283a93308d4`
> **Interaction of amino acids with the C-terminal histidine tag** The non-specific effect observed for jAspSnFR3.mRuby3 was determined to be due to an unexpected interaction with the C-terminal histidine tag. This non-specific signal was reproduced with other proteins containing mRuby3 and purified via the same C-terminal histidine tag, indicating that the histidine tag was responsible for the non-specific signal. Only amino acids interact with the histidine tag, as a structurally related non-amino acid compound, GABA, does not elicit a change in red fluorescence.

Cited: 64c8513d404bd086-2a7ec0cf::s62, 64c8513d404bd086-2a7ec0cf::s63, 64c8513d404bd086-2a7ec0cf::s639

### `398ebac1-fd2d-45b1-9415-d82db4b4d83c`
> **Shift equilibrium to super-open state** By examining enzyme kinetics, Heredia et al. found that p.T65I, p.Y215A and p.A456V mainly accelerate glucose binding, while p.W99R, p.Y214A, p.Y214C and p.V455M predominantly increase the conformational preference towards the active state. Consistently, p.A456V shifted the equilibrium towards the super-open conformation according to our stability predictions.

Cited: ff6d931c3e1942c1-312bdc4b::s652, ff6d931c3e1942c1-312bdc4b::s653, ff6d931c3e1942c1-312bdc4b::s654, ff6d931c3e1942c1-312bdc4b::s655, ff6d931c3e1942c1-312bdc4b::s659, ff6d931c3e1942c1-312bdc4b::s660

### `7e7150d6-bc73-4a29-a5b3-4ef8399ed947`
> **5'-GC** Ddd1 and Ddd9 showed preferences towards editing 5'-GC substrates. Ddd1 and Ddd9 had a much higher editing activity compared to DddA at 5'-GC motifs.

Cited: 635912ff7732db5a-d3b4f268::s373, 635912ff7732db5a-d3b4f268::s379

### `58b39fab-337b-452d-b74f-84f9a188ce88`
_Refused._

### `80e6571e-8f5d-496a-8ba3-9c9f5b783f5d`
> **CD38+CXCR6+** CXCR6 and CD38 expression by TCIRCM cells remained stable following VV-OVA challenge, in contrast to CD69 which was induced by inflammatory stimuli. CXCR6 and CD38 could be employed to demarcate TCIRCM from TRM cells independently of CD69 to better understand TRM cell functional contributions during inflammatory stress. CXCR6 and CD38 expression remained similar following VV-OVA infection or after using other reactivation methods, allowing for CD69-independent TRM cell identification. Liver CXCR6+ CD38+ cells were greatly enriched following TCIRCM cell depletion and were lost after NAD+ administration, validating CXCR6 and CD38 as TRM cell-defining markers.

Cited: 7de06dcdff06813d-2aa4a31e::s295, 7de06dcdff06813d-2aa4a31e::s299, 7de06dcdff06813d-2aa4a31e::s300, 7de06dcdff06813d-2aa4a31e::s303

### `154e7b14-4ed5-4cf3-9149-0c4843fc62cc`
> **circular dichroism** WT PafA is highly stable and remains folded, as inferred by circular dichroism (CD) spectra, even after exposure to 4 M urea for 14 days.

Cited: 68c9c104777ac1ed-f6f095ce::s125

### `a71ef7a2-31a2-460d-9ff4-32d7722353c3`
> **2mM** Tm EndoV endonuclease mediated hydrolysis was inhibited at dNTP concentrations >2.0 mM. The presence of a band corresponding to unreacted extended template (E1) indicates that Tm EndoV endonucleases are inhibited by dNTP concentrations >2 mM.

Cited: f7415168f213937f-e85e09ae::s490, f7415168f213937f-e85e09ae::s76

### `c624ed31-214f-4c80-9544-5514a096b1d3`
> **73%** By analyzing transcriptome data, we found that 73% of genes with RNA editing also exhibited alternative splicing.

Cited: bd4a587f33a63d66-71a1a570::s814, bd4a587f33a63d66-71a1a570::s815

### `bcd2f213-c6c6-4660-af35-a7bd1c6a1170`
_Refused._

### `24fae97b-03f3-48b8-b623-abf07faee02e`
> **11.40%** Using the integration site mapping assay, we identified over 2,000 unique integration sites for Cp36 with the top ten loci accounting for 8.27% and 11.4% of uniquely mapped reads in HEK293FT cells and K562 cells, respectively.

Cited: 168faa61f56dbad8-d9cdd41f::s1339, 168faa61f56dbad8-d9cdd41f::s1340, 168faa61f56dbad8-d9cdd41f::s1346, 168faa61f56dbad8-d9cdd41f::s1347

### `ce93661b-e3c4-4a7a-96b6-87492259c501`
> **50-80%** About 50–80% of fibroblasts resisted to up to 12 days of chemotherapy treatment with oxaliplatin. The study treated cultured colorectal cancer-associated fibroblasts (CAF1 and CAF2) as well as other cell types with oxaliplatin for 12 days to determine tumor cell response to chemotherapy over time.

Cited: 14e30d1f93ac281f-1feb8376::s175, 14e30d1f93ac281f-1feb8376::s176, 14e30d1f93ac281f-1feb8376::s177, 14e30d1f93ac281f-1feb8376::s181

### `941c04dc-c89d-4a90-87b0-930625268a38`
> **64%** In the E. coli Long Term Evolution Experiment at 50,000 generations, 64.0% of the non-genic windows were transcribed in at least one clone at a relaxed threshold of 1 transcript per million reads (TPM).

Cited: f9f1eafd2f81f280-86b6f479::s39

### `ea4ce240-2864-4ee5-9ffc-2dbda0f8f550`
> **48** During infections with T6SS-5-negative B. thailandensis, galectin-3 accumulation events were counted on average at 48 per 1,000 bacteria for the hcp-5 deletion strain.

Cited: 634344ce13dd73ac-d812341d::s381

### `cff68274-4bbe-4fa0-a181-36a9af3cc0f1`
_Refused._

### `2c262f91-52b6-421d-8341-8748f923459e`
_Refused._

### `6f8a51e2-f7ad-4033-b43d-370348e4809f`
> **R8 residue of MC1 and E878 residue of PSMD2** The neighboring MC1 R8 residue establishes a charge interaction with PSMD2E878 and hydrogen bonds with PSMD2H868.

Cited: 36e711a08612716e-caaa863d::s138

### `9a0b82cb-6a99-4e50-83fc-3ef2ebd277cc`
> **The gain is similar for all models** For the AAV2 (adeno-associated virus 2) landscape where a 28-residue window was mutated, fine-tuning was evaluated across the three protein language models. Only minor differences were found between the fine-tuned pLMs for the mutations landscape tasks, and the average performance was reported across all pLMs. Both Ankh models gained significantly by fine-tuning for the mutational landscape data sets (GFP, AAV and GB1), consistent with the general finding that fine-tuning improved performance for ESM2 and ProtT5 models on these tasks.

Cited: b2eec4bcf78447c8-c064fdfe::s120, b2eec4bcf78447c8-c064fdfe::s121, b2eec4bcf78447c8-c064fdfe::s125, b2eec4bcf78447c8-c064fdfe::s69, b2eec4bcf78447c8-c064fdfe::s70

### `8b665114-7729-4dac-a64f-4862a5397b82`
> **Cytoplasm** Rv2780 was mainly detected in the cytoplasm, partially in mitochondria, very minimally in the endoplasmic reticulum (ER) or lysosome. Rv2780 was detected in the cytoplasm of mice peritoneal macrophages (MPMs) during M. tuberculosis infection.

Cited: c31907b446aed1b3-79dfc999::s79, c31907b446aed1b3-79dfc999::s81

### `5c808548-92c4-4ae7-990c-e2df81e3c2ae`
_Refused._

### `564e715f-8d30-410b-bdb5-0dc5206589a7`
> **Bd-ASIA1** The copy number of the virus relative to the genome average varied between strains, ranging from 0.08 to 2.49, and was lower in Bd-BRAZIL and Bd-CAPE compared with Bd-ASIA1.

Cited: 1725c45090a9d29f-a741d85e::s226, 1725c45090a9d29f-a741d85e::s227, 1725c45090a9d29f-a741d85e::s228, 1725c45090a9d29f-a741d85e::s229

### `e90ea0fc-4659-4b20-acae-75dc4b97a101`
> **Both the V1 and V3 isoforms.** For the longest CDH23 isoform (V1), both CDH23(+68) and CDH23(-68) were localized to the stereocilia as well as in the cell body. For the second longest isoform (V2), both CDH23(+68) and CDH23(-68) were only detected in the cell body. The shortest isoform (V3) was detected in the stereocilia as well as cell body in injectoporated hair cells when the HA tag was added to the N terminus. Together, the data demonstrate that V1 and V3 isoforms of CDH23 can localize to the stereocilia.

Cited: a322cf631e4099c8-c8d9416c::s145, a322cf631e4099c8-c8d9416c::s146, a322cf631e4099c8-c8d9416c::s149, a322cf631e4099c8-c8d9416c::s150

### `c246753c-27d2-4ae4-8630-b9b4077ba6f6`
**Error:** RateLimitError: litellm.RateLimitError: AnthropicException - {"type":"error","error":{"type":"rate_limit_error","message":"This request would exceed your organization's rate limit of 50,000 input tokens per minute (org: ac37d026-8a94-437f-87a7-e20cfa6cefa5, model: claude-haiku-4-5-20251001). For details, refer to: https://docs.claude.com/en/api/rate-limits. You can see the response headers for current usage. Please reduce the prompt length or the maximum tokens requested, or try again later. You may also contact sales at https://claude.com/contact-sales to discuss your options for a rate limit increase."},"request_id":"req_011Cb93g8jvUgUYoVU99psv6"}

### `22306bd7-7e84-415d-aebb-11c6312eb081`
> **IgE** In this study antibody isotype analysis revealed AMP-CpG formulated EBV vaccine generated a mixture of IgA, IgM, IgG1, IgG2a, IgG2b, and IgG3 gp350-specific antibody isotypes.

Cited: 9ed823ba1e15f21e-9d83dcd0::s385

### `7d71dffb-b591-4b88-b0c6-e125a1b083b4`
> **lipopolysaccharide** Lipopolysaccharide induces inflammation and facilitates lung metastasis in a breast cancer model via the prostaglandin E2-EP2 pathway. LPS is a structural component of Gram-negative bacteria and can bind to toll-like receptor 4 (TLR4), activating several signaling mechanisms that may affect cell survival, including proliferation, inflammation, and apoptosis.

Cited: 760a41458de0016f-45c84606::s724, 760a41458de0016f-45c84606::s835

### `fca26d7c-05cf-40b0-9fd6-a63ed7950909`
> **Spytag003** As a way of site-specifically conjugating INT onto AAV, the researchers leveraged the molecular glue peptides SpyTag-SpyCatcher. They genetically inserted SpyTag003 (SpT3) into the VP2 protein of AAV9 and created a SpyCatcher003-INT (SpC3-INT) fusion protein to attach the INT tag to the AAV. The SpyTag-SpyCatcher molecular glue peptides were employed as a method of site-specific conjugation for the INT peptide, which binds vault interior and facilitates packaging.

Cited: 2445404168635a55-0ad2b180::s153, 2445404168635a55-0ad2b180::s81, 2445404168635a55-0ad2b180::s82, 2445404168635a55-0ad2b180::s84

### `c6e11fac-8f9c-4cf1-aa6e-4d25731ba74f`
> **Glycosyltransferases** The most highly represented Borg genes encode glycosyltransferases, which are proteins involved in DNA and RNA manipulation.

Cited: 01e0adaed8ffd463-38a7f893::s131

### `bace5737-ba26-422a-8706-0fb1e92b689f`
_Refused._

### `ff7328e2-4954-46a2-8ea3-d40b4df0c0ea`
> **Sodium** A single sodium ion is positioned at the centre of the cA4, which interacts with a water molecule, but appears to make no direct or indirect interactions with cA4 or Csx23 CTD. The cA4 molecule and a coordinating sodium ion are positioned at the centre of rotation for the 4-fold crystallographic symmetry in the Csx23 CTD tetramer structure.

Cited: 43ce81162fb1ab76-beaced53::s924, 43ce81162fb1ab76-beaced53::s925, 43ce81162fb1ab76-beaced53::s926, 43ce81162fb1ab76-beaced53::s984, 43ce81162fb1ab76-beaced53::s985, 43ce81162fb1ab76-beaced53::s986, 43ce81162fb1ab76-beaced53::s987

### `76bcaeeb-93bd-4951-99b9-cf4613de1a37`
> **Microcin V** The only microcin homolog identified in all phylogroups was microcin V; it was the most enriched in phylogroup A and the most depleted in phylogroup D.

Cited: 58223b6183837ffb-65e8f6c9::s173

### `850f86d3-0139-43df-89fd-e606c30aaa8b`
> **NP-OVA (4-hydroxy3-nitrophenylacetyl (NP)-ovalbumin (OVA) footpad immunization** Fluorescently labeled, GC-resident Tfh cells in different mouse models were distinguished by low expression of CD90. PAGFP Tg mice were footpad-immunized with 20 μg of NP-Ova+alum 11 days prior to analysis. S1pr2-RFP mice were footpad-immunized with 20 μg of NP-Ova+alum and treated with 5 mg tamoxifen (i.p.) at days 5-7 p.i. FoxP3 EGFP mice were footpad-immunized with 20 μg of NP-Ova+alum. Loss of CD90 on resident GCTfh cells was observed for multiple immunogens and in the chronic GCs of PPs.

Cited: ee877dbbbd2e51e3-55e76368::s105, ee877dbbbd2e51e3-55e76368::s125, ee877dbbbd2e51e3-55e76368::s37, ee877dbbbd2e51e3-55e76368::s373, ee877dbbbd2e51e3-55e76368::s437

### `df061613-2591-4faa-be03-791c76375cb5`
> **S371F, D405N, R408S** S2X35, a class I mAb, showed moderately reduced binding due to the E484A mutation. However, each of the S371F, D405N, and R408S substitutions caused substantial decreases in binding, likely accounting for enhanced resistance of BA.2 to S2X35. In the BA.2, no single reversion restored S2X35 binding, suggesting an additive effect of S371F, D405N, and R408S mutations.

Cited: daca00c2dca36dc2-b25fdc82::s165, daca00c2dca36dc2-b25fdc82::s176

### `634f6745-f3b3-4cb1-9859-96ffb954b98a`
_Refused._

### `d1eabedb-656f-4f89-a65f-4ed89478ba9f`
> **DILT** DILT could enhance chaperone function by measuring the binding activity of CANX to N-glycosylated proteins, and enhancing ER proteostasis with DILT can promote functional, soluble forms of GCase. DANT and DHBP treatment elevated soluble GCase levels in cell models, although not as robustly as DILT. Treatment of SNCA -3x neurons with DILT abrogated the buildup of insoluble GCase while concomitantly elevating soluble GCase, and DILT enhanced properly folded, functional GCase, as demonstrated by increased GCase activity.

Cited: f74e43a900ad6cb5-10c56ee5::s236, f74e43a900ad6cb5-10c56ee5::s239, f74e43a900ad6cb5-10c56ee5::s241, f74e43a900ad6cb5-10c56ee5::s242, f74e43a900ad6cb5-10c56ee5::s244

### `58f69c8d-cb94-4021-a84f-c549a7b976e1`
> **CXE (Cas9-XTEN-hExo1)** The optimized EXO editor, CXE, in which hExo1 was fused to the downstream of Cas9 with XTEN linker, gave rise to the highest HDR efficiency and the lowest indel frequency. Notably, CXE resulted in the highest HDR efficiency and lowest indel frequency among the four EXO editors and was even significantly superior to E4 and E1B.

Cited: 66aafadef9d913b8-311a2ec6::s1162, 66aafadef9d913b8-311a2ec6::s1163, 66aafadef9d913b8-311a2ec6::s1164, 66aafadef9d913b8-311a2ec6::s1165, 66aafadef9d913b8-311a2ec6::s296, 66aafadef9d913b8-311a2ec6::s297, 66aafadef9d913b8-311a2ec6::s298, 66aafadef9d913b8-311a2ec6::s299

### `20980744-f9ff-4e39-a08d-106eada6900c`
_Refused._

### `a6622141-68d6-418f-8e30-7a5eff3d4fa8`
> **Telaprevir** Split luciferase constructs containing dNS3 exhibit significant resistance to telaprevir, which is consistent with the drug's covalent binding mechanism to the catalytic Ser139, which is mutated in dNS3. Telaprevir did not dissociate dNS3-PMED complexes well, in contrast to grazoprevir, glecaprevir, and danoprevir which inhibit luciferase activity in a dose dependent manner. The NS3 S139A mutation ablates telaprevir sensitivity, leaving only sensitivity to grazoprevir among the three drugs tested.

Cited: ab2ec42d01d567c3-25987f26::s102, ab2ec42d01d567c3-25987f26::s139, ab2ec42d01d567c3-25987f26::s89, ab2ec42d01d567c3-25987f26::s90, ab2ec42d01d567c3-25987f26::s91, ab2ec42d01d567c3-25987f26::s92

### `9fe3ff3b-60cf-472d-ab1a-2bda1868f1b4`
> **Increased acetylation relative to female VICs** Interestingly, we did observe a unique trend in the males, where only larger particles affected the acetylation state. Male VICs also displayed significantly higher acetylation states in most of our blank and PS-NP hydrogel conditions, when compared to female VICs.

Cited: e44731dbd47b1ddf-5ac4257e::s268, e44731dbd47b1ddf-5ac4257e::s269

### `9088251a-99fe-4b91-b6a9-375154ec4f58`
> **GSDMD** Recent studies have shown that ZDHHC5/9 mediates ROS-dependent palmitoylation of GSDMD at hC191/mC192 to promote plasma membrane localization, which is indispensable for pyroptosis. ZDHHC5/9 facilitates GSDMD ROS-dependent palmitoylation at C191 human (C192 mouse), promoting plasma membrane localization.

Cited: de604c3de7db092a-c7360229::s255, de604c3de7db092a-c7360229::s415

### `b8ec372b-ae29-473e-96bc-86ff1ead24ea`
> **ERK1 & ERK2** The β3 integrins activate ERK1 and ERK2 MAPKs, which modify prx1 and prx2. In turn, activated prx1 and/or prx2 interact with an ATTA 'ECM-responsive element' in the TN-C gene promoter, located at position -57 bp upstream from the transcription start site. On denatured collagen, β3 integrin-dependent activation of ERK1 and ERK2 regulates TN-C in vascular SMCs.

Cited: dd641ef35dc94ec2-2545f939::s395, dd641ef35dc94ec2-2545f939::s396, dd641ef35dc94ec2-2545f939::s414

### `a45c277e-55d9-4e7f-b1de-37fc2e19daf6`
> **Ogfrl1** Ogfrl1 in particular to be a highly specific marker for PV interneurons in the molecular and fusiform layers of the dorsal cochlear nucleus

Cited: 1d72af568ea9078d-b044a088::s227, 1d72af568ea9078d-b044a088::s228

### `a8aa19cc-e4d1-4aa1-8c4e-2a518b4c99d6`
> **Rasgrf1** Rasgrf1 was identified as having significant nonrandom spatial distribution within the granule cell layer of the cerebellum. The researchers divided the cerebellar puck into anterior and ventral regions and identified genes with specific localization to the granule layer, with Rasgrf1 showing a pattern previously identified using ISH data.

Cited: 1d72af568ea9078d-b044a088::s233, 1d72af568ea9078d-b044a088::s234, 1d72af568ea9078d-b044a088::s235, 1d72af568ea9078d-b044a088::s236, 1d72af568ea9078d-b044a088::s237, 1d72af568ea9078d-b044a088::s239, 1d72af568ea9078d-b044a088::s240

### `2c3ba95c-47d5-4798-9911-ffdb11c940e4`
> **JUND** JUND was identified in our data as a stabilized RNA, while EIF2A as degraded. JUND RNA was stabilized after 24 h with knockdown of DDX3 and ActD treatment.

Cited: 56206a0d497c3922-fc28cbb0::s113, 56206a0d497c3922-fc28cbb0::s98

### `49d2630e-9d26-4e12-89a3-3050a609abf5`
_Refused._

### `c758f685-ba4a-4bf0-bd85-567c60ff1508`
> **p50** Nuclear expression of the cofactor p50, however, was enriched in TRAF3 LOF DLBCL cells, suggesting potential crosstalk between the two NF-κB branches. On the other hand, nuclear localization of canonical NF-κB transcription factor complex subunits RelA and c-Rel was not affected by TRAF3 LOF.

Cited: 0ca36e794a547256-8b0b5a88::s289, 0ca36e794a547256-8b0b5a88::s290, 0ca36e794a547256-8b0b5a88::s291, 0ca36e794a547256-8b0b5a88::s292, 0ca36e794a547256-8b0b5a88::s293, 0ca36e794a547256-8b0b5a88::s294, 0ca36e794a547256-8b0b5a88::s295

### `fd54d745-447c-4fcd-80de-463fcd3de6a4`
> **MYB44** We confirmed the upregulation in dana1 mutant of ABA catabolic genes, including CYP707A1, CYP707A2, CYP707A4, and UGT71B1, as well as the downregulation of MYB44 and NTL6. MYB44 is explicitly stated to be downregulated (not upregulated) in dana1 mutants, making it the gene that is NOT an ABA catabolism gene that is upregulated in DANA1 knockout lines.

Cited: b372fd7f8558d5e0-ff2c7d15::s205

### `4d11258d-ee8c-4bc7-91a8-613c7a41f139`
> **K548R** The PARP1-K548R mutant showed a reduced interaction with MRE11 in immunoprecipitation assays, similar to the level seen in cells exposed to the PARP inhibitor AZD2281. FLAG-PARP1 WT, K548R, or Vector were transfected into HEK293T cells together with GFP-MRE11, and the cells were subjected to FLAG affinity gel immunoprecipitation to analyze the interaction between PARP1 and MRE11.

Cited: 499208a4235c02b6-fe42dd36::s1444, 499208a4235c02b6-fe42dd36::s1445, 499208a4235c02b6-fe42dd36::s1446, 499208a4235c02b6-fe42dd36::s1447, 499208a4235c02b6-fe42dd36::s1448, 499208a4235c02b6-fe42dd36::s1449, 499208a4235c02b6-fe42dd36::s2147, 499208a4235c02b6-fe42dd36::s2148, 499208a4235c02b6-fe42dd36::s2149, 499208a4235c02b6-fe42dd36::s2150, 499208a4235c02b6-fe42dd36::s2151, 499208a4235c02b6-fe42dd36::s2152

### `1ff2b2e4-492e-4e35-bf33-f0fb53ab938c`
> **S446G** The reversion mutation S446G in the BA.1 background increases the neutralization potency of both antibodies (negative escape values in heatmaps) and probably contributes to greater neutralization potency to the BA.2 variant, which carries G446.

Cited: e3048b3df487004d-f5873c81::s217

### `178a5e56-340f-4ba8-a3e5-f024ca016f40`
> **G56H** The mutation of Gly56 to His56 has imparted changes in the CDR2 loop and pulled Gly55 towards the Gly482 of RBD as observed in PyMol analysis.

Cited: d54befdeabd3bf9e-4573e6c1::s504

### `c75879f4-9329-4594-8f6a-c4d421f2439f`
> **I87W** Only three Pbs2 mutants (Q82W, P97A and L98F) were found to interact with an SH3 containing protein more strongly than wild-type Pbs2 with the same protein, indicating a loss of specificity, while six Pbs2 mutants interacted with an SH3 containing protein more weakly than wild-type Pbs2 (Q82W, S83F, K85W, I87W, N92H and N92S), indicating a gain in specificity. I87W, which is the strongest interacting mutant measured, positions its side-chain such that it interacts with the hydrophobic pocket, and additionally forms a hydrogen bond with the aspartic acid in position 333 of the Sho1 sequence, potentially explaining its strong interaction strength relative to all other Pbs2 variants.

Cited: 667d94590e6616fe-e15f7eed::s535, 667d94590e6616fe-e15f7eed::s623

### `f7346ea0-5f1b-45e9-a1d6-493c754159c1`
> **membrane trafficking** The S118L mutation does not affect KATP channel ATP sensitivity, as there was no significant difference in the dose-response curves for ATP inhibition between wild-type and mutant channels. The S118L mutation does not affect KATP channel stimulation by MgADP, as the mean increases in hetS118L and homS118L KATP currents were not significantly different from that of the wild-type current. Metabolic inhibition of hetS118L and homS118L channels was unaffected, with neither the hetS118L nor homS118L current amplitude appreciably different from that of the wild-type current in control solution or in the presence of azide. Membrane trafficking of S118L channels is impaired, with an ~40% reduction in the surface expression of hetS118L and homS118L channels compared with wild-type channels, suggesting that the mutation disrupts surface trafficking and/or assembly of the KATP channel complex. The S118L mutation affects channel assembly, preventing surface trafficking, as the reduction in total SUR1 protein favours the idea that channel assembly is affected.

Cited: e01d60f8ccaf1fbd-a4be292d::s196, e01d60f8ccaf1fbd-a4be292d::s199, e01d60f8ccaf1fbd-a4be292d::s202, e01d60f8ccaf1fbd-a4be292d::s203, e01d60f8ccaf1fbd-a4be292d::s204, e01d60f8ccaf1fbd-a4be292d::s208, e01d60f8ccaf1fbd-a4be292d::s241, e01d60f8ccaf1fbd-a4be292d::s245, e01d60f8ccaf1fbd-a4be292d::s315, e01d60f8ccaf1fbd-a4be292d::s320

### `3d3fea17-c8ee-4005-94cb-d8798be696c3`
> **Volume** A remarkably consistent linear relationship was found between the total volume of the haptophyte cells and the volume occupied by UCYN-A within its host, expressed as log10(VUCYN-A) = 1.0 log10(Vhapto) - 1.2, which demonstrates log-linear scaling. Similarly, a tight size relationship exists between the volume of B. bigelowii and the total chloroplast volume, expressed as log10(Vchloro) = 1.1 log10(Vhapto) - 1.2, also showing log-linear scaling. The total UCYN-A volume and the total chloroplast volume of its haptophyte host also scale with a close-to-linear relationship in log-log space: log10(VUCYN-A) = 0.9 log10(Vhapto) + 0.01.

Cited: b2aeda61ca908aaf-9486c25d::s139, b2aeda61ca908aaf-9486c25d::s140, b2aeda61ca908aaf-9486c25d::s142, b2aeda61ca908aaf-9486c25d::s79, b2aeda61ca908aaf-9486c25d::s80

### `ab58e166-f0b5-49ae-ac56-c38b5d6e8aad`
> **Pdpn** By reanalyzing Aire-lineage-tracing RNA-seq data, two proteins, podoplanin (Pdpn) and integrin b 4 (CD104), were identified as being downregulated in post-Aire mTECs, and by flow cytometry, the mTEC lo population separated into Pdpn + CD104 + (pre-Aire) and Pdpn - CD104 - (post-Aire) compartments. mTEC lo could be divided into pre- and post-Aire compartments based on Pdpn and CD104 expression.

Cited: da7b856dfa32186d-1e1bf60f::s168, da7b856dfa32186d-1e1bf60f::s173

### `a73b2c2d-a3ac-49e6-8e2e-44b4c1e6de94`
> **SmD1** The five Sm proteins (SmD1, D2, E, F, G) were the most reduced in the D20V mutant pulldowns, whereas SmB and D3 were the two least affected clients. The D20V mutant co-purified considerably less Gem2 than did the WT construct, consistent with its reported reduction in binding affinity to Gem2.

Cited: 7b3aeee153dea14b-f01a40db::s114, 7b3aeee153dea14b-f01a40db::s116

### `04dbe07d-8b2c-4daf-b5b2-ef0e93f1fd2a`
> **Arg312** For KBTBD4-PR, the positively charged side chain of Arg312 reaches halfway into the tunnel and is accompanied by Arg314, which occupies a nearby outer vestibule at the tunnel's entrance. The net effects of these two mutations are the expansion of the 2b-2c loop by two amino acids and, in the case of TTYML, alteration of the amino acid composition. Despite their sequence diversity, both mutants insert the bulky side chain of a central residue into the narrow tunnel leading to the catalytic site of the enzyme.

Cited: 774bbc2bae82b5a7-82522eec::s145, 774bbc2bae82b5a7-82522eec::s147, 774bbc2bae82b5a7-82522eec::s148

### `4a6705b5-85e5-44c1-8444-65be30192802`
> **RlmB** The catalytically inactive RlmB variant RlmB(E198A) can stimulate 50S assembly, indicating that its function is reminiscent of RlmE, as both appear to have dual roles in ribosome large subunit assembly with both 2'-O methylation and a methylation-independent role. RlmB and RlmKL restore growth even though they are catalytically inactive, in contrast to RluC and RlmN which restore growth because they modify rRNA. RlmB has functions in ribosome assembly independent of their modification activities.

Cited: 9a92b9f5adbd8f23-edc56ec0::s15, 9a92b9f5adbd8f23-edc56ec0::s199, 9a92b9f5adbd8f23-edc56ec0::s359, 9a92b9f5adbd8f23-edc56ec0::s360

### `08397294-3d99-4790-915c-b8bcb1e9e661`
> **DTD** Rev1 ∆ BRCT rev3 and Rev1UBM rev3 double mutants were more sensitive to MMS than rev3 single mutants, while Rev1-DTD rev3 double mutants showed a greater increase in sensitivity, equivalent to that observed in the rev1 ∆ null mutant. The DTD domain can insert cytosine opposite damaged guanines and abasic sites, and in Drosophila, without pol ζ, there seems to be a critical role for REV1 deoxycytidyl transferase activity.

Cited: 1c2a0524c883d73f-f2d03f0c::s128, 1c2a0524c883d73f-f2d03f0c::s129, 1c2a0524c883d73f-f2d03f0c::s155, 1c2a0524c883d73f-f2d03f0c::s156

### `837b2489-723a-4099-9b68-c2a9ea688f4d`
> **BUD40** The BUD40 material produces fibers that are, on average, 2.07± 0.56 microns thick, while the BUD60 forms fibers about 1.31± 0.23 microns thick, and the BUD80 forms fibers that are, on average, 1.07± 0.21 microns thick. Statistical analysis using oneway ANOVA demonstrated a statistically significant difference between the width of the fibers formed by the BUD40 and the fibers formed by the BUD60 and the BUD80. Shortening the length of the ELP produces thicker fibers within the material.

Cited: 7eb232e6cd269f4c-b14c15d4::s299, 7eb232e6cd269f4c-b14c15d4::s300, 7eb232e6cd269f4c-b14c15d4::s301, 7eb232e6cd269f4c-b14c15d4::s302

### `745f5a0d-5f8f-405e-bb46-f37b3d1f0678`
> **None of the above** Training characteristics within the target brain region, such as mean NF signal amplitude, mean left amygdala activation, and signal changes in the left amygdala, were not associated with changes in symptoms. Our analysis revealed significant associations between changes in MADRS scores and subtypes of whole-brain activation patterns during the NF training.

Cited: 06508579b3fd8baf-222782c2::s507, 06508579b3fd8baf-222782c2::s508

### `bca1be77-208b-4d57-ac29-05aa6d58bdbf`
> **p50** Subsetting for the top 10 TFs with the highest regulon activity score for the Hypoxia-TAM cluster and a hypoxia response geneset from the GSEA Molecular Signatures Database (MSigDB) suggested p50, hypoxia-inducible factor-1 a (HIF1 a ), and c-Jun as core TFs regulating Hypoxia-TAM signature. Disruption of p50 (encoded by NFKB1 ), but not the other two TFs, markedly decreased the expression of Hypoxia-TAM signature genes. These results suggest that p50 as a downstream TF of NFk B signaling is required for Hypoxia-TAM signature.

Cited: e1671d32c95165a1-15d2b9a0::s244, e1671d32c95165a1-15d2b9a0::s246, e1671d32c95165a1-15d2b9a0::s247

### `2dc20a2f-de54-4bfe-a34f-1ba395f342cf`
> **The nucleus is more stiff than the cytoplasm.** The nucleus and cytoplasm of IHAs have distinct stiffness and relaxation times, with the average nuclear stiffness of IHAs being fourfold higher than the stiffness of the cytoplasm. In contrast, GBM cells do not have significant differences in their nuclear and cytoplasmic viscoelastic properties, including stiffness. IHAs maintain viscoelastic differences between the nucleus and cytoplasm, but these cellular compartments are not mechanically distinct in GBM cells.

Cited: edce53910698b365-47b1176a::s132, edce53910698b365-47b1176a::s135, edce53910698b365-47b1176a::s171, edce53910698b365-47b1176a::s172, edce53910698b365-47b1176a::s45

### `afb36e40-0836-4810-909e-eabfe17dcd8b`
> **TYMS** ITPA (inosine triphosphatase) was upregulated at 10 μM concentration of 5-FU, with upregulation > 2-fold in 72 h. Pol β (encoded by POLB gene) was upregulated > 2-fold upon 5-FU administration in 72 h. Rev1 was upregulated in response to 5-FU treatment in HCT116 cells, as other TLS enzymes including pol ι, pol κ or pol ζ were not upregulated significantly, except for Rev1. Thymidylate synthase (TYMS) was not significantly upregulated upon 5-FU treatment within 72 h in HCT116 cells.

Cited: 0606f4a1026bae93-53471ae3::s1364, 0606f4a1026bae93-53471ae3::s1366, 0606f4a1026bae93-53471ae3::s1367, 0606f4a1026bae93-53471ae3::s1372, 0606f4a1026bae93-53471ae3::s1373, 0606f4a1026bae93-53471ae3::s1381, 0606f4a1026bae93-53471ae3::s1439, 0606f4a1026bae93-53471ae3::s1440, 0606f4a1026bae93-53471ae3::s1441, 0606f4a1026bae93-53471ae3::s1442, 0606f4a1026bae93-53471ae3::s1443, 0606f4a1026bae93-53471ae3::s1444, 0606f4a1026bae93-53471ae3::s1546, 0606f4a1026bae93-53471ae3::s1547, 0606f4a1026bae93-53471ae3::s1548, 0606f4a1026bae93-53471ae3::s1549, 0606f4a1026bae93-53471ae3::s1550

### `c6f097c9-2216-4e98-af45-8101681b38ec`
_Refused._

### `9f797d29-9f3a-481d-b2fe-326cbc686273`
> **Mn2+** Mn2+ exhibited the most enhancing effect on R.DraR1, whereas Mg2+ had minimal catalytic effect on R.DraR1, differing from most REases. R.DraR1 exhibits its cleavage activity in the presence of either Mn2+ (high efficiency) or Mg2+ (low efficiency), rather than Ca2+, Zn2+, and Ni2+, suggesting that the structural domain of R.DraR1 is more suitable to Mn2+ than other divalent metal ions.

Cited: 97736fa153fa784c-41306673::s223, 97736fa153fa784c-41306673::s381

### `0d5cf8a7-a240-4a8f-be4e-c16712f90d79`
> **L522** Substituting L522 in minN or two residues in minC (W622 and F625) to alanines completely silenced the activities of either region. A combined mutant, UNK3M, encompassing L522A/W622A/F625A, silenced not only IDR but also the full-length UNK protein. L522 is located in the minN region of the intrinsically disordered region (IDR) of Unkempt.

Cited: f56f5fb1f0922800-5c745f12::s201, f56f5fb1f0922800-5c745f12::s202, f56f5fb1f0922800-5c745f12::s206, f56f5fb1f0922800-5c745f12::s207, f56f5fb1f0922800-5c745f12::s208, f56f5fb1f0922800-5c745f12::s209, f56f5fb1f0922800-5c745f12::s212, f56f5fb1f0922800-5c745f12::s213, f56f5fb1f0922800-5c745f12::s214, f56f5fb1f0922800-5c745f12::s215, f56f5fb1f0922800-5c745f12::s216

### `40400348-eabb-4b25-90d1-e33589d3e5a4`
> **Fexofenadine** FEXO, a low-cost OTC drug, was tested to determine whether it may have similar effects as anti-VISTA antibodies. When combined with ICB therapy, FEXO and the anti-VISTA antibody had similar efficacy in controlling primary tumor growth. FEXO+ICB was more effective than anti-VISTA+ICB for prolonging survival of mice because 50% of FEXO+ICB-treated mice had tumor-free survival but none of the anti-VISTA+ICB-treated mice survived. FEXO+ICB was also more potent than anti-VISTA+ICB in inhibiting lung metastasis.

Cited: 1e98838d3116281b-bac8d842::s252, 1e98838d3116281b-bac8d842::s254, 1e98838d3116281b-bac8d842::s255, 1e98838d3116281b-bac8d842::s256

### `ebe57888-662f-488f-ade1-c0aaffe638b1`
> **GFAP** A striking increase in expression of the reactive astrocyte marker glial fibrillary acidic protein (GFAP) was found after CNS injury in RhoANesKO mice compared with WT mice. RhoA ablation in astrocytes increased GFAP expression compared with WT astrocytes.

Cited: d396d8edd4f389e6-d53cbbe3::s270, d396d8edd4f389e6-d53cbbe3::s321

### `ef07d562-fc18-43c9-8201-7a189d76eeb9`
> **Vasculitis** The highest frequencies of KIR+ CD8+ T cells were found in patients with vasculitis or embolism and, to a lesser extent, in those with acute respiratory distress syndrome (ARDS). Increased levels of KIR+ CD8+ T cells correlated with disease severity and vasculitis in COVID-19 patients.

Cited: 7f115cb9d0652622-d64852b9::s300, 7f115cb9d0652622-d64852b9::s98

### `b331480e-dfc7-4e92-931a-c71f491c4795`
> **95, 121, 122** The data therefore indicate that three residues with evolutionary divergence in the G domains of RAS isoforms also impose selectivity constraints on KRAS inhibition. The latter is because of a combination of orthosteric effects by H95 in the α3 helix and allosteric (or indirect) effects by P121 and S122 in loop 8. Most notable was the substitution of H95 in the α3 helix of KRAS with L and Q in NRAS and HRAS, respectively.

Cited: 70973b3a4b0a193e-f334e23d::s118, 70973b3a4b0a193e-f334e23d::s134, 70973b3a4b0a193e-f334e23d::s135

### `58950824-2665-445d-939b-9512d5d01a2b`
> **MEF2C** MEF2C was suggested to have increased activity in our TF enrichment analysis and was identified as a putative central regulator and network hub in the largest cluster of genes significantly enriched for multiple muscle adaptation processes. The largest cluster was significantly enriched for multiple muscle adaptation processes, including mitochondrion organization and fusion, aerobic respiration, PPAR and insulin signaling, longevity, muscle contraction, and response to heat and a mechanical stimulus, with MEF2C identified as a putative central regulator.

Cited: d55d01d52f893ef8-5b74c904::s1195, d55d01d52f893ef8-5b74c904::s1196, d55d01d52f893ef8-5b74c904::s1197, d55d01d52f893ef8-5b74c904::s1198

### `8d12cb90-73c6-4cc1-9f83-0fa9fd822e92`
> **acj6, SoxN** Using acj6 and SoxN, we identified the T4/T5 neurons of the optic lobe that split in T4/T5a-b and T4/T5c-d subtypes by subclustering.

Cited: 010bab0784c5d05e-4d07cf2b::s185
