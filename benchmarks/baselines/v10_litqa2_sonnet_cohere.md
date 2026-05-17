# Eval Report: litqa2

- **Pipeline:** `anthropic/claude-sonnet-4-6 | cohere-embed-v3 | hybrid(BM25+lance) | min_tokens=100 | cohere-rerank-v3 | retrieve=100/rerank=10 | no-verifier | loose`
- **Run at:** 2026-05-17 13:15:11
- **Questions:** 186

## Aggregate metrics

| Metric | Value |
|---|---|
| `citation_precision` | 0.677 |
| `citation_recall` | 0.491 |
| `citation_f1` | 0.427 |
| `coverage` | 0.703 |
| `localization_accuracy` | 0.258 |
| `abstention_precision` | 0.069 |
| `abstention_recall` | 0.500 |
| `abstention_f1` | 0.121 |
| `mc_correct` | 143.000 |
| `mc_wrong` | 8.000 |
| `mc_unanswered` | 35.000 |
| `mc_accuracy_over_answered` | 0.947 |
| `mc_accuracy_over_all` | 0.769 |

## Per-question results

| ID | Refused | Should refuse | Cited ∩ Gold | Cited | Gold | Faith |
|---|---|---|---|---|---|---|
| `e3b5a4af-41d9-48db-becf-29a08d0ad28e` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `76184ccf-4bf0-469e-a442-11d04b4ff8b0` | ✗ | ✗ | 1 | 1 | 1 | 0.12 |
| `39129e1c-096f-4414-bf4f-37fadbbe364c` | ✗ | ✗ | 1 | 1 | 5 | 0.48 |
| `27234279-f50c-4cfc-86e2-af68364a8f94` | ✗ | ✗ | 1 | 1 | 3 | 0.26 |
| `517e7cf8-c5d2-4391-9e2a-235b79d93050` | ✗ | ✗ | 1 | 1 | 1 | 0.81 |
| `cb710074-73a8-4407-b0c7-7dc868f1bc76` | ✗ | ✗ | 2 | 2 | 14 | 0.72 |
| `5c4c602c-9624-4eae-ac44-efe4c0dd10e6` | ✗ | ✗ | 1 | 1 | 1 | 0.68 |
| `c9bdb9b5-28c1-44da-93b6-b1fc9d8bf369` | ✗ | ✗ | 1 | 1 | 9 | 0.92 |
| `e6b0f9e5-e976-47dc-b839-0b2fca967e9e` | ✗ | ✗ | 1 | 1 | 12 | 0.25 |
| `247eeb85-a552-4b87-b83e-327538fcb8a9` | ✗ | ✗ | 1 | 1 | 12 | 0.87 |
| `a214f5f8-0de8-43cf-82e0-7930003e4a0c` | ✗ | ✗ | 2 | 2 | 7 | 0.35 |
| `a43e5166-d0e8-48f8-a113-648acac7ed59` | ✗ | ✗ | 1 | 1 | 1 | 0.64 |
| `dd29920d-cb70-440f-961c-3e1103776c4f` | ✗ | ✗ | 1 | 1 | 1 | 0.97 |
| `7d805bb8-4c7c-431f-b068-acf5e5459985` | ✗ | ✗ | 0 | 1 | 1 | 1.00 |
| `8d7fa642-ee46-4a13-8ea9-61cc2d4f4ddd` | ✗ | ✗ | 1 | 1 | 6 | 0.80 |
| `487539f9-2f17-4009-aa4a-c41322445f11` | ✗ | ✗ | 1 | 1 | 6 | 0.96 |
| `5049c648-b1bb-4624-8824-9d93dfb04e51` | ✗ | ✗ | 1 | 3 | 1 | 0.89 |
| `a18883e9-218a-4719-8d2c-cf94d740de1a` | ✗ | ✗ | 0 | 3 | 3 | 0.98 |
| `d7833c0f-2a16-40d2-b6a0-6764aa3003a6` | ✗ | ✗ | 1 | 5 | 5 | 0.99 |
| `1ccdc348-50e1-4941-9151-5e50411a2b41` | ✗ | ✗ | 1 | 1 | 1 | 1.00 |
| `1e5f5199-84f4-4133-ab87-2372fa6ca722` | ✗ | ✗ | 0 | 3 | 2 | 0.99 |
| `d2860d38-dfb9-4b80-905f-812c32573915` | ✗ | ✗ | 1 | 2 | 1 | 0.75 |
| `77a41274-cd9c-48bc-a347-e0746907840d` | ✗ | ✗ | 1 | 1 | 2 | 0.70 |
| `5a2128ad-3127-4595-b810-db128d1a2335` | ✗ | ✗ | 2 | 2 | 4 | 0.88 |
| `d65103ae-c881-4116-a0a7-1b233eb6275a` | ✗ | ✗ | 1 | 1 | 5 | 0.37 |
| `ab5eb050-d134-4445-9307-6faa08be7474` | ✗ | ✗ | 1 | 1 | 7 | 0.15 |
| `82de3e92-abe2-46ac-ad17-23417b9c4da7` | ✓ | ✗ | 0 | 0 | 4 | 0.99 |
| `7cf0fcde-fea8-420c-8531-2f2fe9e38980` | ✗ | ✗ | 2 | 4 | 3 | 0.49 |
| `da5b2a8f-ba08-4692-851f-2e0bf142a02f` | ✗ | ✗ | 0 | 2 | 1 | 0.95 |
| `e2fb56b7-08cd-4dc0-bc63-b45931a74fc9` | ✗ | ✗ | 0 | 2 | 1 | 0.65 |
| `eda34fde-798e-43a1-a9d3-a804d3d8ee4e` | ✗ | ✗ | 3 | 3 | 5 | 1.00 |
| `0eede7a8-fe1f-42d3-a2c6-478083648644` | ✗ | ✗ | 2 | 3 | 2 | 0.97 |
| `d1307e50-3c03-4c76-81ee-2decb5de5f14` | ✓ | ✗ | 0 | 0 | 4 | 0.86 |
| `10cece36-a507-4a93-9600-13f3e0e677f8` | ✗ | ✗ | 1 | 3 | 2 | 0.62 |
| `f5a84803-3917-43eb-801b-8dc0c5400da1` | ✗ | ✗ | 1 | 2 | 1 | 1.00 |
| `c47dd378-dde3-4a45-9184-6abfa6163717` | ✗ | ✗ | 1 | 2 | 1 | 0.99 |
| `0bac8974-554c-439a-a9a2-22fa509c8d5d` | ✗ | ✗ | 1 | 3 | 2 | 1.00 |
| `aaa85379-1e4b-4642-9ec4-e1a6d6c29c3b` | ✗ | ✗ | 1 | 1 | 5 | 0.96 |
| `aa1835b2-2b1c-4986-b7af-e174da0124b0` | ✗ | ✗ | 1 | 1 | 1 | 0.47 |
| `5a9c6697-a65c-49c0-9e02-38b2a276fde7` | ✗ | ✗ | 1 | 1 | 1 | 0.90 |
| `37a4d007-793e-4a89-922a-c1b05f4f82c1` | ✗ | ✗ | 1 | 1 | 1 | 0.20 |
| `c9baf8e0-c4c7-4ba3-b5c4-18e9af8b2df1` | ✗ | ✗ | 1 | 1 | 2 | 0.62 |
| `d0f69626-66ee-4807-937d-c3a024441812` | ✗ | ✗ | 0 | 1 | 4 | 0.98 |
| `462a9f38-7cbe-4e12-a6e2-b1d7028c3a8b` | ✗ | ✗ | 1 | 1 | 1 | 0.96 |
| `86f111e5-402b-4ef5-b101-8be1bf5be7c6` | ✗ | ✗ | 1 | 1 | 1 | 0.93 |
| `cbe93a43-09cd-4cb4-9edd-f22fe8c28415` | ✗ | ✗ | 0 | 1 | 2 | 0.37 |
| `7a88e6f7-fb8e-4a24-b08d-9b7a6edafe57` | ✗ | ✗ | 1 | 1 | 3 | 0.99 |
| `91387526-9268-4a3c-9abe-73819707d0b0` | ✓ | ✗ | 0 | 0 | 1 | 0.86 |
| `7b98796f-25be-4c58-a52a-4e366c0ffd95` | ✗ | ✗ | 1 | 1 | 4 | 0.99 |
| `5e20e26d-6192-4563-abb3-a4857e3dbc7c` | ✗ | ✗ | 1 | 1 | 2 | 0.71 |
| `b105af85-833e-48bc-ac78-48f73c9673fd` | ✓ | ✗ | 0 | 0 | 5 | 0.91 |
| `5b6d6f82-a585-4aa8-9fe6-e7d35f7cb2ae` | ✓ | ✗ | 0 | 0 | 2 | 0.26 |
| `12321eab-6ad6-4218-8815-18bc51c14544` | ✗ | ✗ | 1 | 3 | 1 | 0.83 |
| `c33446f6-fbff-4186-8a51-28a17f68bd40` | ✗ | ✗ | 1 | 2 | 2 | 0.29 |
| `b1d5a5f5-6e89-4dfb-b60d-5a9824b015f3` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `6aa10957-bdd9-4dab-a4e1-234a17cb87dd` | ✗ | ✗ | 1 | 1 | 1 | 0.97 |
| `28ebecdf-949e-4d20-aca9-5989b7a9d6e9` | ✗ | ✗ | 1 | 1 | 2 | 0.99 |
| `dbb51a1c-f9a2-4960-a93c-118957659790` | ✓ | ✗ | 0 | 0 | 7 | 0.82 |
| `85c67ef3-322c-42b4-b745-c05e07e7b8ac` | ✗ | ✗ | 1 | 1 | 6 | 0.97 |
| `653635b7-3bc6-4a7b-98c7-c02038c0e928` | ✗ | ✗ | 1 | 1 | 1 | 0.35 |
| `100b570f-1c4f-4214-8402-f1b15f9989b4` | ✗ | ✗ | 1 | 1 | 4 | 0.37 |
| `0a9d6516-95ef-4d7b-a28d-d7cde27b7b55` | ✗ | ✗ | 1 | 3 | 1 | 0.71 |
| `8d61a14b-60ef-43b0-8003-b60cb6657428` | ✗ | ✗ | 0 | 1 | 0 | 0.09 |
| `4d4cb121-9525-499a-9475-9b212465c72d` | ✗ | ✗ | 0 | 4 | 0 | 0.08 |
| `ca4c9d21-b842-4875-9a6a-bcb9f6c55073` | ✗ | ✗ | 0 | 1 | 7 | 1.00 |
| `c3816cb5-8c87-4946-b133-43f415ab6b2a` | ✓ | ✓ | 0 | 0 | 0 | 0.25 |
| `59745f75-52bf-4815-905c-3dfad1ef8923` | ✓ | ✗ | 0 | 0 | 0 | 0.00 |
| `26691c84-514b-4712-a43e-09705d681e45` | ✗ | ✗ | 1 | 2 | 1 | 0.42 |
| `0e53a08c-4252-4a84-962b-5b396f9740aa` | ✓ | ✗ | 0 | 0 | 0 | 0.00 |
| `8ade3e3a-4792-4965-b9d9-05e528ebbfa0` | ✗ | ✗ | 0 | 3 | 0 | 0.35 |
| `f5a4b449-e647-4ae0-8419-c221792482c9` | ✗ | ✗ | 0 | 3 | 5 | 0.39 |
| `5806ed2a-1005-44f1-8d70-332048fea8f4` | ✗ | ✗ | 0 | 1 | 1 | 0.69 |
| `6fff0994-6d02-470a-9d61-8e35420412b6` | ✗ | ✗ | 2 | 2 | 5 | 0.99 |
| `8266ac61-92d6-423d-8e7a-fe47b3a7e885` | ✗ | ✗ | 1 | 1 | 12 | 1.00 |
| `322454df-45a8-41b3-9b0a-4e808144023c` | ✓ | ✗ | 0 | 0 | 0 | 0.50 |
| `3c9f23e2-fdd0-431b-aca7-4f9556c78f1f` | ✗ | ✗ | 0 | 1 | 0 | 0.00 |
| `983f1ef5-fc7d-4f4a-8f48-e704641eae12` | ✗ | ✗ | 1 | 1 | 2 | 0.74 |
| `7d2c8d44-ecf3-40d2-ab69-b6195c46ffe9` | ✗ | ✗ | 1 | 1 | 1 | 0.93 |
| `720e20c2-9ad1-4d98-9f01-8b7fb3782a46` | ✓ | ✗ | 0 | 0 | 3 | 0.94 |
| `dbfbae3d-62f6-4710-8d13-8ce4c8485567` | ✗ | ✗ | 1 | 1 | 1 | 0.12 |
| `7a42c784-7ae0-48fe-a71f-0a547b8fabb3` | ✗ | ✗ | 1 | 2 | 6 | 0.48 |
| `0708b62f-9652-49eb-8ba6-28878afa7445` | ✗ | ✗ | 1 | 1 | 4 | 0.99 |
| `5b3b7d05-9e54-445c-b374-d4c6b60923b4` | ✗ | ✗ | 1 | 1 | 1 | 0.74 |
| `623a831f-41ee-4e0e-936a-87f93d96369e` | ✗ | ✗ | 1 | 2 | 30 | 0.89 |
| `0b1d5537-db47-420c-984b-9b56d38e6d98` | ✗ | ✗ | 1 | 1 | 1 | 0.71 |
| `ade96656-7ed1-4e21-b009-b7a73e13bff5` | ✗ | ✗ | 0 | 2 | 0 | 0.42 |
| `78a2c1d2-f035-4c7d-a7ee-40dfd95ca88a` | ✗ | ✗ | 1 | 1 | 1 | 0.99 |
| `224efcd7-3652-47f8-84dd-15b4c6fafae2` | ✗ | ✗ | 1 | 1 | 2 | 0.93 |
| `55187fb4-e7ee-4027-b74f-cab50f328442` | ✗ | ✗ | 1 | 1 | 1 | 0.94 |
| `25a9cf59-1c28-4ddf-b797-f43efb9349e6` | ✗ | ✗ | 1 | 2 | 11 | 0.57 |
| `12a20d8d-cd49-47eb-9a19-6a38519ee3dc` | ✗ | ✗ | 1 | 2 | 1 | 0.86 |
| `4bb69c9d-2485-42d2-b8aa-aa647b407ca4` | ✗ | ✗ | 1 | 1 | 7 | 0.80 |
| `8c833521-56c4-458d-8c65-2bbf66190cae` | ✗ | ✗ | 0 | 1 | 1 | 0.85 |
| `255fd5fb-9623-4030-8bf2-253247df7c82` | ✗ | ✗ | 1 | 1 | 1 | 0.96 |
| `38ada695-2c79-459b-8e68-dbed734c74f9` | ✗ | ✗ | 1 | 1 | 1 | 0.93 |
| `e763edaa-b112-460a-a564-d58a6685e639` | ✗ | ✗ | 0 | 3 | 1 | 0.88 |
| `8af900bb-5794-40db-910e-10d5857ce5bd` | ✗ | ✗ | 2 | 2 | 2 | 0.47 |
| `6194ebfc-2d5c-4ccc-8883-da7c471b61e6` | ✗ | ✗ | 0 | 1 | 1 | 0.16 |
| `1f1b07d7-39ce-4665-9b70-4ab77e3c87aa` | ✗ | ✗ | 0 | 1 | 4 | 0.24 |
| `55668039-396e-488a-b2c3-bbe840550433` | ✗ | ✗ | 1 | 1 | 1 | 0.30 |
| `4f050bf3-27cd-4a14-8422-45df5e2bb079` | ✗ | ✗ | 1 | 1 | 1 | 0.67 |
| `cff00d08-5655-4214-97ac-8fa9504c1165` | ✗ | ✗ | 1 | 1 | 2 | 0.98 |
| `0eeb7ea9-fc80-4dee-9418-1c328c3ab653` | ✗ | ✗ | 1 | 1 | 2 | 0.97 |
| `658f7050-d137-477e-8693-26609080cecd` | ✗ | ✗ | 1 | 1 | 2 | 0.25 |
| `8696273a-7fea-411a-b6c6-0e826e1e02b5` | ✗ | ✗ | 1 | 2 | 1 | 0.69 |
| `ce6dd5f7-0706-41dd-a383-9b0d22ef00a1` | ✗ | ✗ | 1 | 1 | 1 | 0.88 |
| `400786c1-e6c6-4f46-a501-86fdd048ed88` | ✗ | ✗ | 1 | 2 | 2 | 1.00 |
| `e820cbcf-6df1-4c1c-b985-c02f39f52781` | ✗ | ✗ | 1 | 3 | 1 | 0.70 |
| `230dec20-cd02-4613-a7b1-e28058ed46fe` | ✗ | ✗ | 1 | 2 | 2 | 0.90 |
| `7975ddb0-a784-4f85-a297-c80e1cb5dcf2` | ✓ | ✗ | 0 | 0 | 0 | 0.00 |
| `a1d01019-d2b1-4619-92ec-7ea38578819f` | ✗ | ✗ | 1 | 1 | 2 | 0.93 |
| `fe074387-3765-4020-8f5d-e395d1094121` | ✗ | ✗ | 0 | 1 | 0 | 0.46 |
| `f0b6cea0-e005-47bc-be0d-9a10b219cae6` | ✗ | ✗ | 1 | 1 | 3 | 1.00 |
| `ae02d0e9-edf5-4c39-a215-3cbc8f4c565d` | ✗ | ✗ | 2 | 2 | 4 | 0.66 |
| `fd60a0e7-ba64-49a9-843a-6f5cb17c5fa9` | ✗ | ✗ | 0 | 3 | 4 | 0.29 |
| `14fd2b75-76fb-4c29-a21d-c557b2bcf2ff` | ✗ | ✗ | 1 | 1 | 4 | 0.87 |
| `e9f142f0-8ef6-47cd-b846-7283a93308d4` | ✗ | ✗ | 1 | 2 | 15 | 0.93 |
| `398ebac1-fd2d-45b1-9415-d82db4b4d83c` | ✗ | ✗ | 1 | 4 | 2 | 0.59 |
| `7e7150d6-bc73-4a29-a5b3-4ef8399ed947` | ✗ | ✗ | 1 | 1 | 1 | 0.40 |
| `58b39fab-337b-452d-b74f-84f9a188ce88` | ✓ | ✓ | 0 | 0 | 0 | 0.63 |
| `80e6571e-8f5d-496a-8ba3-9c9f5b783f5d` | ✗ | ✗ | 1 | 3 | 5 | 0.88 |
| `154e7b14-4ed5-4cf3-9149-0c4843fc62cc` | ✗ | ✗ | 1 | 1 | 1 | 0.22 |
| `a71ef7a2-31a2-460d-9ff4-32d7722353c3` | ✗ | ✗ | 0 | 1 | 1 | 0.23 |
| `c624ed31-214f-4c80-9544-5514a096b1d3` | ✗ | ✗ | 1 | 1 | 23 | 0.97 |
| `bcd2f213-c6c6-4660-af35-a7bd1c6a1170` | ✓ | ✗ | 0 | 0 | 0 | 0.50 |
| `24fae97b-03f3-48b8-b623-abf07faee02e` | ✗ | ✗ | 1 | 1 | 5 | 0.85 |
| `ce93661b-e3c4-4a7a-96b6-87492259c501` | ✗ | ✗ | 1 | 1 | 9 | 0.61 |
| `941c04dc-c89d-4a90-87b0-930625268a38` | ✗ | ✗ | 1 | 1 | 2 | 0.94 |
| `ea4ce240-2864-4ee5-9ffc-2dbda0f8f550` | ✓ | ✗ | 0 | 0 | 10 | 0.93 |
| `cff68274-4bbe-4fa0-a181-36a9af3cc0f1` | ✓ | ✗ | 0 | 0 | 0 | 0.16 |
| `2c262f91-52b6-421d-8341-8748f923459e` | ✓ | ✗ | 0 | 0 | 0 | 0.14 |
| `6f8a51e2-f7ad-4033-b43d-370348e4809f` | ✗ | ✗ | 1 | 1 | 2 | 1.00 |
| `9a0b82cb-6a99-4e50-83fc-3ef2ebd277cc` | ✓ | ✗ | 0 | 0 | 2 | 0.96 |
| `8b665114-7729-4dac-a64f-4862a5397b82` | ✗ | ✗ | 1 | 1 | 14 | 0.99 |
| `5c808548-92c4-4ae7-990c-e2df81e3c2ae` | ✗ | ✓ | 0 | 1 | 0 | 0.10 |
| `564e715f-8d30-410b-bdb5-0dc5206589a7` | ✓ | ✗ | 0 | 0 | 25 | 0.59 |
| `e90ea0fc-4659-4b20-acae-75dc4b97a101` | ✗ | ✗ | 4 | 4 | 8 | 0.99 |
| `c246753c-27d2-4ae4-8630-b9b4077ba6f6` | ✗ | ✗ | 1 | 2 | 1 | 0.99 |
| `22306bd7-7e84-415d-aebb-11c6312eb081` | ✗ | ✗ | 1 | 1 | 1 | 0.92 |
| `7d71dffb-b591-4b88-b0c6-e125a1b083b4` | ✗ | ✗ | 0 | 2 | 1 | 0.22 |
| `fca26d7c-05cf-40b0-9fd6-a63ed7950909` | ✗ | ✗ | 0 | 2 | 1 | 0.55 |
| `c6e11fac-8f9c-4cf1-aa6e-4d25731ba74f` | ✗ | ✗ | 1 | 1 | 1 | 0.90 |
| `bace5737-ba26-422a-8706-0fb1e92b689f` | ✓ | ✗ | 0 | 0 | 0 | 0.02 |
| `ff7328e2-4954-46a2-8ea3-d40b4df0c0ea` | ✓ | ✗ | 0 | 0 | 7 | 0.48 |
| `76bcaeeb-93bd-4951-99b9-cf4613de1a37` | ✗ | ✗ | 1 | 1 | 1 | 0.98 |
| `850f86d3-0139-43df-89fd-e606c30aaa8b` | ✗ | ✗ | 0 | 2 | 1 | 0.65 |
| `df061613-2591-4faa-be03-791c76375cb5` | ✓ | ✗ | 0 | 0 | 1 | 0.98 |
| `634f6745-f3b3-4cb1-9859-96ffb954b98a` | ✓ | ✗ | 0 | 0 | 0 | 0.00 |
| `d1eabedb-656f-4f89-a65f-4ed89478ba9f` | ✗ | ✗ | 0 | 3 | 2 | 0.95 |
| `58f69c8d-cb94-4021-a84f-c549a7b976e1` | ✗ | ✗ | 2 | 3 | 44 | 0.96 |
| `20980744-f9ff-4e39-a08d-106eada6900c` | ✓ | ✗ | 0 | 0 | 0 | 0.07 |
| `a6622141-68d6-418f-8e30-7a5eff3d4fa8` | ✓ | ✗ | 0 | 0 | 5 | 0.73 |
| `9fe3ff3b-60cf-472d-ab1a-2bda1868f1b4` | ✗ | ✗ | 2 | 2 | 8 | 0.94 |
| `9088251a-99fe-4b91-b6a9-375154ec4f58` | ✗ | ✗ | 1 | 2 | 1 | 0.94 |
| `b8ec372b-ae29-473e-96bc-86ff1ead24ea` | ✗ | ✓ | 0 | 2 | 0 | 0.39 |
| `a45c277e-55d9-4e7f-b1de-37fc2e19daf6` | ✗ | ✗ | 0 | 1 | 1 | 0.25 |
| `a8aa19cc-e4d1-4aa1-8c4e-2a518b4c99d6` | ✗ | ✗ | 0 | 1 | 0 | 0.62 |
| `2c3ba95c-47d5-4798-9911-ffdb11c940e4` | ✗ | ✗ | 2 | 2 | 6 | 0.98 |
| `49d2630e-9d26-4e12-89a3-3050a609abf5` | ✓ | ✗ | 0 | 0 | 0 | 0.33 |
| `c758f685-ba4a-4bf0-bd85-567c60ff1508` | ✗ | ✗ | 2 | 2 | 8 | 0.94 |
| `fd54d745-447c-4fcd-80de-463fcd3de6a4` | ✗ | ✗ | 1 | 1 | 1 | 0.78 |
| `4d11258d-ee8c-4bc7-91a8-613c7a41f139` | ✗ | ✗ | 0 | 0 | 16 | 0.96 |
| `1ff2b2e4-492e-4e35-bf33-f0fb53ab938c` | ✓ | ✗ | 0 | 0 | 6 | 0.99 |
| `178a5e56-340f-4ba8-a3e5-f024ca016f40` | ✓ | ✗ | 0 | 0 | 3 | 1.00 |
| `c75879f4-9329-4594-8f6a-c4d421f2439f` | ✗ | ✗ | 1 | 1 | 1 | 1.00 |
| `f7346ea0-5f1b-45e9-a1d6-493c754159c1` | ✗ | ✗ | 1 | 5 | 1 | 0.99 |
| `3d3fea17-c8ee-4005-94cb-d8798be696c3` | ✗ | ✗ | 1 | 3 | 5 | 0.00 |
| `ab58e166-f0b5-49ae-ac56-c38b5d6e8aad` | ✗ | ✗ | 1 | 2 | 1 | 0.45 |
| `a73b2c2d-a3ac-49e6-8e2e-44b4c1e6de94` | ✗ | ✗ | 1 | 3 | 21 | 0.83 |
| `04dbe07d-8b2c-4daf-b5b2-ef0e93f1fd2a` | ✗ | ✗ | 1 | 1 | 5 | 0.99 |
| `4a6705b5-85e5-44c1-8444-65be30192802` | ✗ | ✗ | 0 | 4 | 2 | 0.99 |
| `08397294-3d99-4790-915c-b8bcb1e9e661` | ✗ | ✗ | 1 | 2 | 2 | 0.98 |
| `837b2489-723a-4099-9b68-c2a9ea688f4d` | ✗ | ✗ | 1 | 1 | 2 | 0.70 |
| `745f5a0d-5f8f-405e-bb46-f37b3d1f0678` | ✗ | ✗ | 1 | 2 | 2 | 0.71 |
| `bca1be77-208b-4d57-ac29-05aa6d58bdbf` | ✗ | ✗ | 2 | 3 | 2 | 0.77 |
| `2dc20a2f-de54-4bfe-a34f-1ba395f342cf` | ✗ | ✗ | 3 | 4 | 6 | 1.00 |
| `afb36e40-0836-4810-909e-eabfe17dcd8b` | ✗ | ✗ | 2 | 5 | 6 | 0.97 |
| `c6f097c9-2216-4e98-af45-8101681b38ec` | ✓ | ✗ | 0 | 0 | 0 | 0.01 |
| `9f797d29-9f3a-481d-b2fe-326cbc686273` | ✗ | ✗ | 1 | 1 | 4 | 0.84 |
| `0d5cf8a7-a240-4a8f-be4e-c16712f90d79` | ✗ | ✗ | 1 | 1 | 12 | 0.28 |
| `40400348-eabb-4b25-90d1-e33589d3e5a4` | ✗ | ✗ | 2 | 3 | 4 | 0.95 |
| `ebe57888-662f-488f-ade1-c0aaffe638b1` | ✗ | ✗ | 1 | 1 | 1 | 0.82 |
| `ef07d562-fc18-43c9-8201-7a189d76eeb9` | ✗ | ✗ | 1 | 2 | 2 | 0.90 |
| `b331480e-dfc7-4e92-931a-c71f491c4795` | ✗ | ✗ | 0 | 2 | 5 | 0.76 |
| `58950824-2665-445d-939b-9512d5d01a2b` | ✗ | ✗ | 0 | 2 | 0 | 0.74 |
| `8d12cb90-73c6-4cc1-9f83-0fa9fd822e92` | ✗ | ✗ | 1 | 1 | 1 | 0.12 |

## Per-question answers

### `e3b5a4af-41d9-48db-becf-29a08d0ad28e`
> *Acinetobacter lwoffii* was evolved in the lab to be resistant to ciprofloxacin. This is the only antibiotic for which clinical resistance was observed in *A. lwoffii* during the laboratory evolution experiments, as it did not evolve resistance to meropenem or gentamicin.

Cited: 6795e9ad5fae6fe1-b687cf6e::s278, 6795e9ad5fae6fe1-b687cf6e::s383

### `76184ccf-4bf0-469e-a442-11d04b4ff8b0`
> Active olfactory receptor genes increase their contacts with Greek Island regions by 2.7-fold in mouse olfactory neurons.

Cited: a8d467f77e70f70d-553b632a::s175

### `39129e1c-096f-4414-bf4f-37fadbbe364c`
> The majority of gene disruption phenotypes (61% of total gene phenotypes) were detected by 4 cell divisions. The best answer is **61% of gene loci**.

Cited: aca6b37101ab6098-3101659e::s135

### `27234279-f50c-4cfc-86e2-af68364a8f94`
> The sources report that the method detected 12,309 mandarin-specific insertion loci (ILs) across 57 mandarin accessions. Therefore, the best answer from the provided options is **12,300** (the closest approximation to 12,309 unique transposable element insertion loci in the mandarin genome).

Cited: c322ce6575cc1c3a-d56b589a::s181

### `517e7cf8-c5d2-4391-9e2a-235b79d93050`
> H3.3 K36R mutants complete development and eclose at a frequency of approximately 80%, which is nearly identical to that of H3.3 Ctrl animals. The best answer is **80%**.

Cited: 116c0e949dd415fc-61f4295b::s281

### `cb710074-73a8-4407-b0c7-7dc868f1bc76`
> The question asks about survival after exposure to **36°C** for 6 hours, but the sources describe an experiment performed at **35°C** for 6 hours with 14 hours of recovery at 20°C. At 35°C, approximately 10% of adr mutant animals (including adr-1(-), adr-2(-), and adr-1(-);adr-2(-)) die after the acute heat stress, meaning approximately 90% survive. Since the question specifies 36°C rather than 35°C, there is a discrepancy. However, the closest and most directly supported answer from the sources regarding the percentage that **die** among adr mutant animals under the described conditions (35°C, 6h, recovery 14h at 20°C) is approximately **10%**. The best answer is **10%**.

Cited: 1c5f1e074ba072b8-31d0ed90::s78, 1c5f1e074ba072b8-31d0ed90::s79

### `5c4c602c-9624-4eae-ac44-efe4c0dd10e6`
> A large oligosaccharide density was observed in the cryo-EM map of Nav1.6, attaching to Asn326.

Cited: d79480166f4ab0e3-4297b383::s79

### `c9bdb9b5-28c1-44da-93b6-b1fc9d8bf369`
> The number of tumor-infiltrating leukocytes (TILs) was highest in the evening (ZT13, which is 13 hours after light onset) in experiments using B16-F10-OVA melanoma cells injected into mice. The best answer is **evening**.

Cited: 40349a281d8b56ff-7979b34d::s110

### `e6b0f9e5-e976-47dc-b839-0b2fca967e9e`
> Myotendinous junction myonuclei exhibited enrichment in genes associated with cell–matrix interactions (such as COL22A1 and ADGBR4). The best answer is **cell–matrix interactions**.

Cited: f7c3d31ee5706405-5f6af1d3::s122

### `247eeb85-a552-4b87-b83e-327538fcb8a9`
> The percentage of AR-negative patients among ER+ MBC patients was 5.3%, compared to 17.4% in FBC samples. The correct answer is **5.3%**. Results showed that the percentage of AR-negative patients was significantly lower in MBC than in FBC samples (5.3% vs. 17.4% in MBC and FBC samples, respectively).

Cited: 476ba9a9e8ea9c14-b5e5878b::s495

### `a214f5f8-0de8-43cf-82e0-7930003e4a0c`
> Beta-amyrin synthases from four plants (Artemisia annua, Arabidopsis thaliana, Glycyrrhiza glabra, and Saponaria vaccaria) were compared for their ability to produce β-amyrin from squalene. Among these candidates, the BAS homologue from Saponaria vaccaria (SvBAS) yielded the highest titre of β-amyrin. The answer is **Saponaria vaccaria**.

Cited: e35c8530af941f04-9a7975aa::s100, e35c8530af941f04-9a7975aa::s99

### `a43e5166-d0e8-48f8-a113-648acac7ed59`
> From P6 to P15, thalamocortical (TC) synapse density in the anterior cingulate cortex increases 5-fold in wild-type mice. The best answer is **5x**.

Cited: c0b69d2af9f2e018-845b5d60::s271

### `dd29920d-cb70-440f-961c-3e1103776c4f`
> T cells with the anti-CD19 synNotch → sIL-2 circuit locally expanded by a factor of ~100 within the CD19+ target tumor in the NSG mouse model. The best answer is **100**.

Cited: 34f4e70030aa5d35-a24b74ef::s130

### `7d805bb8-4c7c-431f-b068-acf5e5459985`
> MLH1dn expression increases editing efficiency of the PE2 system (as part of the PE4 system) by an average of 7.7-fold across six MMR-proficient cell types. The best answer is **7.7x**.

Cited: fa808d37a77e6019-79d6e54c::s96

### `8d7fa642-ee46-4a13-8ea9-61cc2d4f4ddd`
> The best answer is **residues 344–360**.

A version of Apollo with a deletion of amino acids 344–360 (Apollo/Delta1 PK), removing the residues most similar to those of the Artemis DNA-PK interaction motif, had a reduced interaction with DNA-PKcs in 293T cells.

Cited: cea2facf97f5150c-660a07bf::s360

### `487539f9-2f17-4009-aa4a-c41322445f11`
> The best answer is **aa 31-40**.

The sources describe a series of N-terminal truncations of COSA-1 tested by yeast two-hybrid assay, where COSA-1 truncations retaining residues 1–10, 1–20, and 1–30 could still interact with MSH-5 and ZHP-3, but COSA-1 truncated to residues 1–40 showed dramatically decreased interactions with these two proteins. This means that the region spanning approximately amino acids 31–40 is critical, as its deletion (going from the 1–30 truncation to the 1–40 truncation) causes the dramatic loss of interaction with MSH-5 and ZHP-3.

Cited: 4c0f27bd833d0295-e8c8a393::s638

### `5049c648-b1bb-4624-8824-9d93dfb04e51`
> The best answer is **Depletion of photosynthetic machinery**.

Disruption of MTF1 expression in Chlamydomonas results in the depletion of the entire photosynthetic apparatus and most chloroplast-expressed proteins. MTF1 is required for translation of nearly all chloroplast-encoded proteins, and its loss causes a severe photosynthetic phenotype. Specifically, chloroplast-expressed subunits of photosynthetic complexes tend to be more depleted than their nuclear-expressed counterparts in the mtf1 mutant, with the depletion of nuclear-expressed subunits being a secondary effect due to degradation of incompletely assembled complexes.

Cited: 9afb8ab3b1d5ff95-b03dfb72::s237, 9afb8ab3b1d5ff95-b03dfb72::s238, 9afb8ab3b1d5ff95-b03dfb72::s247

### `a18883e9-218a-4719-8d2c-cf94d740de1a`
> Yes, hair cells (hair follicles) do regenerate in wounds treated with verteporfin in mouse models. By POD 30, verteporfin-treated wounds regrew levels of hair follicles and glands comparable with those in unwounded skin, whereas control wounds formed bare, fibrotic scars. A striking difference between PBS- and verteporfin-treated wounds was the emergence of regenerated hair follicles in the latter within 30 days, while control wounds formed bare areas. This regenerative effect is consistent with the mechanism by which blocking mechanotransduction via verteporfin (a YAP inhibitor) prevents fibroblast conversion and yields ENF-mediated regeneration, defined in part by the restoration of dermal appendages such as hair follicles.

Cited: 7dead537a45e92bd-e35471f4::s253, 7dead537a45e92bd-e35471f4::s72, 7dead537a45e92bd-e35471f4::s89

### `d7833c0f-2a16-40d2-b6a0-6764aa3003a6`
> Yes. Metabolic glycan labeling immobilizes the dendritic cell membrane and enhances the antitumor efficacy of dendritic cell vaccines. Specifically, metabolic glycan labeling reduces the membrane mobility of DCs, which activates DCs and improves antigen presentation and subsequent T cell priming. DCs treated with azido-sugars exhibit a reduced membrane mobility compared to control DCs without azido-sugar treatment. Metabolic glycan labeling itself can enhance the antitumor efficacy of DC vaccines. In vivo, azido-labeled antigen-pulsed DCs result in improved CTL response and antitumor efficacy compared to unlabeled DCs in both prophylactic and therapeutic settings.

Cited: 6f59dd139145c891-36c60054::s16, 6f59dd139145c891-36c60054::s19, 6f59dd139145c891-36c60054::s2, 6f59dd139145c891-36c60054::s749, 6f59dd139145c891-36c60054::s760

### `1ccdc348-50e1-4941-9151-5e50411a2b41`
> Targeting sgRNAs to the **coding strand** in gene bodies leads to higher effect sizes on average across multiple CRISPRi screens. In all 17 CRISPRi screens examined, the average effect sizes of sgRNAs targeting coding strands within gene bodies were more than twofold higher than those targeting the template strands.

Cited: b0c70be4f4a933d3-7fb87fac::s328

### `1e5f5199-84f4-4133-ab87-2372fa6ca722`
> The protein encoded by TDRD1 recognizes and binds **symmetrical dimethylarginine (sDMA)** modifications on other proteins (such as MILI and MIWI); TDRD1 itself is the reader of these marks, not the substrate. The sources describe TDRD1's Tudor domains as specifically binding symmetrically dimethylated arginine residues on piRNA pathway proteins. The conserved aromatic cage of the Tudor domain of TDRD1 is responsible for specifically binding the symmetrically dimethylated arginine side chain. The best answer is: **Symmetrical dimethylarginine modifications** — specifically, TDRD1's extended Tudor domains recognize and bind symmetrically dimethylated arginine (sDMA) marks.

Cited: aa268cf616154b07-7384f4cb::s183, aa268cf616154b07-7384f4cb::s184, aa268cf616154b07-7384f4cb::s329

### `d2860d38-dfb9-4b80-905f-812c32573915`
> The correct answer is **S. epidermis** (S. epidermidis).

Engineered strains of S. epidermidis stimulate T cells specific for non-native epitopes under physiologic conditions of colonization. Specifically, S. epidermidis was engineered to express non-native antigens, and these engineered strains could stimulate antigen-specific T cells both in vitro and in vivo.

Cited: 8e4b7872a7579d54-cb6467cd::s89, 8e4b7872a7579d54-cb6467cd::s93

### `77a41274-cd9c-48bc-a347-e0746907840d`
> The best answer is **Enlarged granular cells**.

Expression of HsMOR with the N-terminal αPrePro sequence resulted in enlarged granular cells, expanded ER membranes, and relocalization of HsMOR-GFP to puncta.

Cited: 33d9e243f2ee99de-02bbb79f::s173

### `5a2128ad-3127-4595-b810-db128d1a2335`
> The homology-based structure predicted by ColabFold had particularly good predictions for helices TM1, TM6, and TM7, but was weak in the extracellular TM2-TM3 loop region and did not predict the partial unwinding of TM3 at the extracellular end. Therefore, the best answer is **TM3**, as the homology model had a poor prediction for the partial unwinding of TM3 at the extracellular end in HcKCR1.

Cited: f2e1fb5c9886efad-202dbbbb::s113, f2e1fb5c9886efad-202dbbbb::s114

### `d65103ae-c881-4116-a0a7-1b233eb6275a`
> The gene for which regulation occurs in the coding sequence is **gp02**.

Whereas regulation of the three host genes (rpoS, cyaA, and petA) all involved sequestration of the target ribosome-binding site, regulation of gp02 occurs in the coding sequence, indicating that target regulation might be accompanied by ribonuclease recruitment.

Cited: d1ef96583ec64586-195f7c93::s219

### `ab5eb050-d134-4445-9307-6faa08be7474`
> Formation of the DarR dimer results in the burial of approximately 1300 Å² of surface from solvent. The best answer is **1300 Å²**.

Cited: 405dcaff86bce126-c6c89512::s68

### `82de3e92-abe2-46ac-ad17-23417b9c4da7`
_Refused._

### `7cf0fcde-fea8-420c-8531-2f2fe9e38980`
> Yes, this has been assessed. Researchers explored the possibility of tagmenting cDNA products directly after preamplification without cleaning, quantifying, or normalizing the cDNA first, a strategy they termed Smart-seq3xpress. Specifically, they found that cDNA products after preamplification at fewer cycles could directly be tagmented without concentration measurements, bioanalyzer QC traces, or cDNA amount normalization steps. However, when using the standard KAPA PCR buffer, the resulting libraries were heavily biased towards 5' reads, indicating inefficient tagmentation due to the high salt concentration in the PCR buffer interfering with the tagmentation reaction. Testing alternative PCR polymerases resolved this issue, with five other PCR polymerases found to be compatible with direct tagmentation in terms of library quality and complexity.

Cited: 70758b216a7dc837-240c67f2::s36, 70758b216a7dc837-240c67f2::s37, 70758b216a7dc837-240c67f2::s41, 70758b216a7dc837-240c67f2::s42

### `da5b2a8f-ba08-4692-851f-2e0bf142a02f`
> Yes, a base editing screen against splice sites in CD33 has been performed before. Specifically, a base-editing screen was performed against all canonical splice donor or acceptor sites present in CD33 to identify single base edits that reduced or eliminated CD33 expression in HSPCs. Multiple sgRNAs were enriched in the CD33-low population, with strong enrichment for sgRNAs targeting splice donor sites of exons 1 and 2.

Cited: 6acd5496cc0d3cfd-49391314::s129, 6acd5496cc0d3cfd-49391314::s131

### `e2fb56b7-08cd-4dc0-bc63-b45931a74fc9`
> The best answer is **More diffuse**.

Deep (lower layer 5/layer 6) IT neurons tend to project more diffusely within a target area, whereas upper (layer 2-4) IT neurons tend to focus their axonal terminations in a small, focal area. This is further supported by the finding that sparse (diffuse) projections originate from deep-layer cells, while focal projections originate from upper-middle layer cells.

Cited: 56e5853498f0abb3-aaa4ebb4::s308, 56e5853498f0abb3-aaa4ebb4::s400

### `eda34fde-798e-43a1-a9d3-a804d3d8ee4e`
> The best answer is **They maintain a negative bias**.

Microstimulations in the subgenual anterior cingulate cortex (sgACC) of monkeys induced a negative bias in decision-making that persisted after the stimulation ended. Specifically, the mean increase in avoidance choices (% Δ Av) for the Stim-on and Follow-up blocks was significantly larger than the 5% threshold in negative effective sessions, indicating that negative biases in decision-making were sustained in the Follow-up block. By contrast, when the stimulation was ineffective, the monkeys did not change their decision-making in either the Stim-on or Follow-up blocks.

Cited: f476506231a1bcfd-731d4d10::s132, f476506231a1bcfd-731d4d10::s134, f476506231a1bcfd-731d4d10::s136

### `0eede7a8-fe1f-42d3-a2c6-478083648644`
> The human SNVs French 2 and Indian 2 cause a subtle increase in the affinity of ETS-1 to the ETS-A site. Specifically, both variants increase the relative affinity of the ETS-A site from 0.15 in the reference sequence to 0.24 (French 2) and 0.26 (Indian 2), representing approximately a 1.6-fold increase. EMSA confirms that both variants bind to ETS-1 more strongly than does the wild-type ETS-A sequence. The best answer is: **subtle increase**

Cited: ebc08bec41d51153-ab2b3568::s102, ebc08bec41d51153-ab2b3568::s83, ebc08bec41d51153-ab2b3568::s84

### `d1307e50-3c03-4c76-81ee-2decb5de5f14`
_Refused._

### `10cece36-a507-4a93-9600-13f3e0e677f8`
> The best answer is **strong increase**.

Removal of DNA methylation (via DNMT triple knockout) dramatically increased repeat-derived RNA in neurons, particularly from IAP elements. This increase was approximately 200-fold for IAP elements, causing them to comprise one-third of all repeat-derived RNA in DNMT-TKO neurons. In contrast, knocking out MBD proteins showed no significant increase in repeat expression, indicating that the strong derepression is specifically attributable to the loss of DNA methylation itself.

Cited: 45a7bf5a940e82ae-b0a29e9c::s185, 45a7bf5a940e82ae-b0a29e9c::s186, 45a7bf5a940e82ae-b0a29e9c::s187

### `f5a84803-3917-43eb-801b-8dc0c5400da1`
> Pexmetinib increases the rate of threonine dephosphorylation by WIP1 phosphatase. Specifically, pexmetinib increased the rate of pT180 dephosphorylation 10-fold relative to the DMSO-treated control. This effect occurs through binding to p38α and flipping the activation loop conformation, which presents pT180 for dephosphorylation by WIP1, rather than by directly altering WIP1 activity. The best answer is: **Increases dephosphorylation**

Cited: 1f689965a0b8b875-14dc08ae::s59, 1f689965a0b8b875-14dc08ae::s61

### `c47dd378-dde3-4a45-9184-6abfa6163717`
> The chromatin occupancy of rTetR-VP48 shows no change when p300 is inhibited. Specifically, inhibiting p300 catalytic activity with A485 did not result in a decrease in TF binding compared to rTetR-VP48 without inhibitors. This is further supported by the quantification showing that BAF inhibition decreases average TF occupancy while p300 inhibition has little to no effect. The best answer is: **no change**

Cited: 3e070f56a44a20e5-f3eb62ec::s178, 3e070f56a44a20e5-f3eb62ec::s246

### `0bac8974-554c-439a-a9a2-22fa509c8d5d`
> The best answer is: **Preferentially binding to b2b3 complex over b1b2b3 complex**.

Bempegaldesleukin was designed to signal preferentially through the heterodimeric IL-2 receptor (IL-2Rβγ, i.e., the β2γ/CD122 complex) rather than the heterotrimeric IL-2Rαβγ complex, which is preferentially expressed on Tregs. Specifically, PEGylation sites are located at the interface of IL-2 with IL-2Rα, sterically blocking binding to the trimeric (αβγ) receptor complex that Tregs preferentially express. This CD122-preferential (βγ) agonism allows bempegaldesleukin to preferentially activate and expand effector CD8+ T and NK cells over Tregs in the tumor microenvironment. As a result, preclinical evidence shows that bempegaldesleukin limits intratumoral Treg proliferation and survival, driving a very high CD8+/Treg ratio.

Cited: f297ec065068a1fb-b871f9c0::s109, f297ec065068a1fb-b871f9c0::s114, f297ec065068a1fb-b871f9c0::s82

### `aaa85379-1e4b-4642-9ec4-e1a6d6c29c3b`
> The panel of fluoroquinolone-resistant clinical E. coli samples used to evaluate SNIPR001 consisted of 72 strains.

Cited: 5b90612d4398fbee-f46e1738::s879

### `aa1835b2-2b1c-4986-b7af-e174da0124b0`
> Mouse neurons cultured from LSL-CRISPRi mice and transduced with sgHspa5 showed marked Cre-dependent neuronal death within 2 weeks of expression. The best answer from the provided options is **14 days**, as the sources indicate neuronal death occurs "within 2 weeks" following CRISPR inactivation of Hspa5.

Cited: da980e1bd5938c42-2c1acbbe::s427

### `5a9c6697-a65c-49c0-9e02-38b2a276fde7`
> Two FMD cycles were the minimum required to cause a significant delay in melanoma growth in mice. The best answer is **2**.

Cited: d1755fd36d8b3c25-7928fced::s295

### `37a4d007-793e-4a89-922a-c1b05f4f82c1`
> C1QTNF1 encodes CTRP1 (also known as mCTRP1 in mice), which is an adiponectin paralog. There are a total of 14 Gly-X-Y repeats in the collagenous domain of mCTRP1. The answer is **14**.

Cited: f265b292c35123ad-a2a40b50::s124

### `c9baf8e0-c4c7-4ba3-b5c4-18e9af8b2df1`
> Adenosine deaminases (A_deamin, PF02137) were grouped together into a single A_deamin-clade using structure-based clustering. The best answer is **1**.

Cited: 635912ff7732db5a-d3b4f268::s245

### `d0f69626-66ee-4807-937d-c3a024441812`
> There were 3,601 differential H3K27ac peaks between queens and workers, with more peaks up-regulated in the queen, distributed in intron and promoter regions.

Cited: d37934bbe3d8f67c-d961c2b7::s111

### `462a9f38-7cbe-4e12-a6e2-b1d7028c3a8b`
> The human genome contains 18,164 distinct sites with TnG-repeat-like elements (>29 nucleotides). The best answer is **18164**.

Cited: 676ba1096cbf511b-b1513bb8::s209

### `86f111e5-402b-4ef5-b101-8be1bf5be7c6`
> At Braak V/VI compared to control (Braak 0), 19,638 promoters of 5,765 genes were found to be differentially methylated for 5mC. The best answer is **5765**, as this is the number of genes showing changes in 5mC methylation of their promoter regions in Alzheimer's patients at Braak stages V/VI compared to control.

Cited: c8bdc674e9741afa-093821ac::s239

### `cbe93a43-09cd-4cb4-9edd-f22fe8c28415`
> When murine brown adipocytes were treated with forskolin (FORSK), 7,875 phospho-sites were significantly regulated (FDR < 0.05). The best answer is **7875**.

Cited: c090173e7e65c0e3-514e4135::s180

### `7a88e6f7-fb8e-4a24-b08d-9b7a6edafe57`
> Using the G4 Hunter algorithm, 80 putative G4-forming sequences (PQSs) were identified within the TMPRSS2 gene. The best answer is **80**.

Cited: 4cbe11308ab2309d-80cecb52::s238

### `91387526-9268-4a3c-9abe-73819707d0b0`
_Refused._

### `7b98796f-25be-4c58-a52a-4e366c0ffd95`
> The LIMK PDZ domain of human LIMK1 and human LIMK2 are 47% identical. The best answer is **47**.

Cited: d3879bce9d87fba9-f83867bf::s80

### `5e20e26d-6192-4563-abb3-a4857e3dbc7c`
> DNA sequences with a motif surrounded by STRs were consistently bound 0.23-0.90 kcal/mol tighter than those with a motif surrounded by random sequences. The best answer is **0.23-0.9 kcal/mol**.

Cited: 0ea4869095e7f1ab-e4a06775::s93

### `b105af85-833e-48bc-ac78-48f73c9673fd`
_Refused._

### `5b6d6f82-a585-4aa8-9fe6-e7d35f7cb2ae`
_Refused._

### `12321eab-6ad6-4218-8815-18bc51c14544`
> The best answer is **You need 10x less**.

On soft 0.5 kPa substrates, complete inhibition of proliferation was observed at roughly 1/10th the concentration required to arrest cell proliferation on plastic. This is further supported by the observation that fibroblasts on 0.5 kPa substrates showed near-total growth arrest at 1/20th the required dose of plastic (with 250 nM bleomycin producing only a modest 44% increase in cell number compared to nearly 200% on plastic). Thus, culturing fibroblasts on a 0.5 kPa soft surface increases their propensity to enter a senescent, non-proliferative state, meaning you need approximately 10x less bleomycin compared to plastic to inhibit cell growth.

Cited: 9fcf84b83327fac1-12161dc6::s81, 9fcf84b83327fac1-12161dc6::s82, 9fcf84b83327fac1-12161dc6::s83

### `c33446f6-fbff-4186-8a51-28a17f68bd40`
> The constraints for Wyckoff sites are implemented as Lagrange multiplier constraints. Specifically, a particle occupying a Wyckoff position must stay in that position at all times, and this can be accomplished via traditional constrained molecular dynamics of Lagrange multipliers. Therefore, the best answer from the provided options is **Lagrange multiplier constraints**.

Cited: 8b9ff18e3a47be61-28103adf::s121, 8b9ff18e3a47be61-28103adf::s183

### `b1d5a5f5-6e89-4dfb-b60d-5a9824b015f3`
> Microglia-specific Ifnar1 deletion attenuates the loss of post-synaptic terminals in 5XFAD mice. Specifically, PSD95+ puncta density (a post-synaptic marker) was restored in 5XFAD;MKO mice (microglia-specific Ifnar1 knockout), whereas synaptophysin+ (pre-synaptic) density was not rescued. This selective rescue of post-synaptic terminals is consistent with the finding that microglial IFN-I signaling drives preferential engulfment of PSD95+ post-synaptic puncta, and that this engulfment is necessarily and exclusively mediated by IFN-I signaling in microglia. **The best answer is: attenuation of loss.**

Cited: 531777a8384af139-4695824d::s145, 531777a8384af139-4695824d::s177, 531777a8384af139-4695824d::s47

### `6aa10957-bdd9-4dab-a4e1-234a17cb87dd`
> Neural Ifnar1 deletion (in 5XFAD;NKO mice) restored pre-synaptic terminals, as synaptophysin⁺ puncta density was rescued in these mice. The best answer is: **restoration**

Cited: 531777a8384af139-4695824d::s47

### `28ebecdf-949e-4d20-aca9-5989b7a9d6e9`
> CWC15 was shown to interact with PAB1, PAG1, and PBA1, but not PBE1, among the four selected 20S proteasome subunits tested in the BiFC assay. Therefore, the 20S proteasome subunit that CWC15 has **not** been shown to interact with in its role promoting degradation of Serrate is **PBE1**.

Cited: 4fe437fb33178a64-5db8a7b0::s244

### `dbb51a1c-f9a2-4960-a93c-118957659790`
_Refused._

### `85c67ef3-322c-42b4-b745-c05e07e7b8ac`
> The best answer is **3-4 days**.

Cells committed to senescence after 3-4 days of ERK activation remained committed even if ERK signaling was brought back to basal levels using inhibitors.

Cited: 039834c95dd3a676-7b222494::s98

### `653635b7-3bc6-4a7b-98c7-c02038c0e928`
> STK11 mutation was positively associated with the CD8⁻/IFNG⁺ immune phenotype in lung adenocarcinoma (LUAD). The best answer is **CD8-/IGNF+**.

Cited: 01604c16c5a26a1f-157aef00::s369

### `100b570f-1c4f-4214-8402-f1b15f9989b4`
> The MIRAS knock-in mice show a 30% decrease in rotarod performance at 12 months of age compared with control mice.

Cited: 09768e5cf98b5291-c38b8d49::s203

### `0a9d6516-95ef-4d7b-a28d-d7cde27b7b55`
> In pre-commitment myeloid progenitor cells, estrogen can be withdrawn for up to 40 hours and the cells can still return to their progenitor state upon reactivation of ER-HOXA9. After estrogen is withdrawn for 72 hours or more, the cells have passed the commitment point and can no longer be returned to the progenitor state. Therefore, the best answer is **40 hours** — estrogen can be withdrawn for up to 40 hours before the cells can no longer return to their progenitor state (with the commitment point occurring between 40 and 72 hours).

Cited: aef60484f35c4136-1379b717::s192, aef60484f35c4136-1379b717::s205, aef60484f35c4136-1379b717::s444

### `8d61a14b-60ef-43b0-8003-b60cb6657428`
> The aptamer in the ARPLA glycan probe binds Neu5Ac.

Cited: 170f8322198d6069-0c88279c::s39

### `4d4cb121-9525-499a-9475-9b212465c72d`
> The best answer is **symmetric sampling of the SDE/ODE (analytical conditioning)**.

In the Chroma (Ingraham 2022) paper, symmetry conditioning was achieved through analytic conditioners applied within the diffusion process itself. Specifically, the framework uses a diffusion-conditioner approach that allows sampling from arbitrary mixtures of hard constraints and soft penalties, including a conditioner that symmetrizes complexes under arbitrary symmetry groups. This works by tessellating an asymmetric subunit in the energy function during the sampling process, forcing all generated configurations to respect the desired symmetry group. These microscopic diffusion steps are biased or constrained by user-specified symmetry requirements to produce a new conditional diffusion process at design time, which corresponds to analytical conditioning of the SDE/ODE.

Cited: 6223b4c58a3e1894-0f5f8dde::s100, 6223b4c58a3e1894-0f5f8dde::s139, 6223b4c58a3e1894-0f5f8dde::s161, 6223b4c58a3e1894-0f5f8dde::s98

### `ca4c9d21-b842-4875-9a6a-bcb9f6c55073`
> The LungMAP Human Lung CellRef identifies 48 well-defined cell types in a normal human lung. The best answer is **48**.

Cited: 0bd1ca4800d9e08e-ed49ee6f::s342

### `c3816cb5-8c87-4946-b133-43f415ab6b2a`
_Refused._

### `59745f75-52bf-4815-905c-3dfad1ef8923`
_Refused._

### `26691c84-514b-4712-a43e-09705d681e45`
> The answer is **SIN3 histone deacetylation**.

According to the sources, inactivation of genes encoding members of the TP53 signaling pathway, SAGA H3 acetylation complex components, and the Fanconi Anemia complex all resulted in resistance to colchicine in HAP1 cells. In contrast, inactivation of members of the SIN3 histone deacetylase complex (SIN3B, SINHCAF and ARID4B) resulted in sensitivity to palbociclib, not resistance to colchicine. There is no source indicating that SIN3 histone deacetylation complex inactivation results in resistance to colchicine, making it the complex whose inactivation does NOT result in colchicine resistance in HAP1 cells.

Cited: 3421ed4fd7502c9a-466927e6::s135, 3421ed4fd7502c9a-466927e6::s139

### `0e53a08c-4252-4a84-962b-5b396f9740aa`
_Refused._

### `8ade3e3a-4792-4965-b9d9-05e528ebbfa0`
> The best answer is **No**.

Doublecortin (DCX), while widely accepted as a marker of newly generated granule cells, was detected in diverse human neurons and did not define immature neuron populations. Approximately 75% of DCX-immunolabeled cells were colocalized with NeuN, a marker of mature granule cells, and 91% were positive for PROX1, suggesting that most DCX-expressing cells in humans may actually be mature granule cells or interneurons rather than newly generated neurons. Furthermore, cross-species transcriptomic analysis identified robust neurogenic trajectories in mouse, pig, and macaque but not in humans, despite DCX RNA expression being detectable in the adult human hippocampus, indicating that DCX expression alone is not a unique or reliable marker of newly generated granule cells.

Cited: e7d33e6c5033c2e2-30e83b44::s393, e7d33e6c5033c2e2-30e83b44::s398, e7d33e6c5033c2e2-30e83b44::s61

### `f5a4b449-e647-4ae0-8419-c221792482c9`
> The correct answer is **AAGAG lncRNA**.

CifA, encoded by prophage WO of *Wolbachia*, acts as a ribonuclease that depletes the AAGAG lncRNA in primary spermatocytes, and this depletion promotes cytoplasmic incompatibility during embryogenesis. Specifically, knockdown of the AAGAG lncRNA in the presence of *Wolbachia* (wMel) enhanced CI approximately threefold compared to controls, demonstrating a causal interaction between CifA-mediated AAGAG lncRNA depletion and CI. The AAGAG lncRNA is derived from tandem repeats in heterochromatic regions, is highly expressed in primary spermatocytes, and its depletion results in a defective histone-to-protamine transition during sperm chromatin organization, which is central to the CI mechanism.

Cited: c1799acd1f08346b-7a1ba0f8::s76, c1799acd1f08346b-7a1ba0f8::s89, c1799acd1f08346b-7a1ba0f8::s93

### `5806ed2a-1005-44f1-8d70-332048fea8f4`
> NIF injections in neonatal male mice significantly reduced microglial phagocytic capacity and engulfment of VGlut2. The best answer is **VGlut2**.

Cited: c0b69d2af9f2e018-845b5d60::s377

### `6fff0994-6d02-470a-9d61-8e35420412b6`
> The causative mutation in the snog1a mutant is located on chromosome 8. Specifically, bulk segregant analysis revealed a peak of the expected allele frequency on chromosome 8, pointing to the gene Pp3c8_19720 as the site of the causative mutation. The best answer is **Chromosome 8**.

Cited: 68a6c661e51b59ab-413f9855::s391, 68a6c661e51b59ab-413f9855::s392

### `8266ac61-92d6-423d-8e7a-fe47b3a7e885`
> The best answer is **No difference in social communicative behaviors**.

Optogenetic inhibition of BNST AVP cells did not affect social communicative behaviors (urine marking and ultrasonic vocalizations) in males or females.

Cited: 38a955fae1cd37d4-f0d43e7b::s103

### `322454df-45a8-41b3-9b0a-4e808144023c`
_Refused._

### `3c9f23e2-fdd0-431b-aca7-4f9556c78f1f`
> The best answer is **CD38**.

CD38 controls NAD+ local concentration by metabolizing it into ADPR, meaning that increased abundance of CD38 is associated with the decline of NAD+ levels. Although the sources do not explicitly mention TNFα treatment of reactive astrocytes in this context, CD38 is the molecule whose relative abundance is directly linked to NAD+ decline through its enzymatic activity.

Cited: 7de06dcdff06813d-2aa4a31e::s451

### `983f1ef5-fc7d-4f4a-8f48-e704641eae12`
> The best answer is **Flocculation**.

Relative to the S288C reference strain, several genes found in Wyeast 3068 were deleted, and these deleted genes were enriched for processes including flocculation (P ≤ 4.59 × 10⁻⁵, involving FLO5, FLO9, FLO1, and FLO10), among other functions.

Cited: 74a92b882343d335-0d4fcaac::s194

### `7d2c8d44-ecf3-40d2-ab69-b6195c46ffe9`
> The best answer is **Shorter cilia**.

Kif9 knockdown embryos had shorter cilia than controls, and this phenotype was rescued by re-expression of Kif9-GFP.

Cited: 8061d302c8a858a8-d1033cab::s133

### `720e20c2-9ad1-4d98-9f01-8b7fb3782a46`
_Refused._

### `dbfbae3d-62f6-4710-8d13-8ce4c8485567`
> SLC14A1 (solute carrier family 14 member 1) appears to be a specific marker for endothelial cells in the heart. The best answer is **heart**.

Cited: 83a86f1f96eceb6e-73d94b3b::s104

### `7a42c784-7ae0-48fe-a71f-0a547b8fabb3`
> The alternative conserved glutamate in ApmFNuc (a Fanzor nuclease) that compensates for the loss of the canonical glutamate in RuvC-II is E467. This was confirmed experimentally, as the E467A mutant abolished ApmFNuc cleavage activity, demonstrating that this alternative glutamate is essential for nuclease function. The best answer is **E467**.

Cited: 2626aa23d080eaee-35590d07::s1111, 2626aa23d080eaee-35590d07::s1127

### `0708b62f-9652-49eb-8ba6-28878afa7445`
> The NCAN C-terminal (which contains the ELS domain) colocalizes with 75% of inhibitory synapses, as determined by STED microscopy. The best answer is **75%**.

Cited: f8498fdbd6c2acbf-3a73e8c9::s392

### `5b3b7d05-9e54-445c-b374-d4c6b60923b4`
> The average speed of cicada urine jets is around 0.6 to 3.16 m/s, which falls within the range of 0.6–3.16 m/s.

Cited: f597b9fbade66ea8-abe5e6df::s40

### `623a831f-41ee-4e0e-936a-87f93d96369e`
> The cavity above the p-hydroxybenzylidene moiety of the chromophore in mSandy2 is filled by the **mp** rotamer of Leucine 63. Specifically, the mp rotamer (χ1 = gauche(−), χ2 = gauche(+)) fills the cavity above the p-hydroxybenzylidene moiety of the chromophore by packing tightly against it, whereas the alternate pt rotamer does not.

Cited: 9fa80155de882a7c-15748f57::s512, 9fa80155de882a7c-15748f57::s591

### `0b1d5537-db47-420c-984b-9b56d38e6d98`
> The human proteasome core subunit α6 (Hs α6) shows a temperature-sensitive phenotype when expressed alone in yeast, but co-expression with the neighboring humanized α7 gene rescues this phenotype. Therefore, the best answer is **Hs α7**.

Cited: 521366a95024715c-ba05c1a4::s124

### `ade96656-7ed1-4e21-b009-b7a73e13bff5`
> The reemergence of prenatal cellular programs is mediated by Mac2 macrophages via CXCL8 interacting with ACKR1 on VE3 vascular endothelial cells in diseased skin. Specifically, CellPhoneDB receptor-ligand analysis predicted a significant enrichment for ACKR1 on VE3 to interact with CXCL8 (IL-8) on Mac2 in AD and psoriasis skin. ACKR1 is characterized as a venular capillary marker highly expressed on VE3 cells. The best answer is **ACKR1**.

Cited: 98bfd461c77d2ddb-abe7e939::s221, 98bfd461c77d2ddb-abe7e939::s234

### `78a2c1d2-f035-4c7d-a7ee-40dfd95ca88a`
> The putative ETS sites within the FoxF enhancer bind ETS with low relative affinities ranging from 0.09 to 0.24. The best answer is **0.09-0.24**.

Cited: d344be98a61d850f-3c8cc77a::s102

### `224efcd7-3652-47f8-84dd-15b4c6fafae2`
> FOXP3 has a strong binding affinity to segment E2 of the UNC5B-AS1 upstream super enhancer region.

Cited: 3a2c0120637483ba-5adda325::s361

### `55187fb4-e7ee-4027-b74f-cab50f328442`
> The upregulated gene CXCL17 was strongly positively correlated (Spearman coefficient >= 0.25) with Club cells as part of the Relapse signature, making it the most associated chemokine with that signature among the options listed. The best answer is **CXCL17**.

Cited: 129870223e3a57d6-aed81b74::s137

### `25a9cf59-1c28-4ddf-b797-f43efb9349e6`
> The cellular feature displaying the greatest difference in morphology between apoptotic and control cells as measured by Cell Painting assays is **mitochondria**.

When comparing apoptosis and control group cells, 367 differential morphology features were identified, with most morphology changes coming from the mitochondria and nuclei. This is further supported by the summary statement that apoptosis had more morphology feature changes, mostly impacting mitochondria.

Cited: 324908523a45ed3e-0832d3f2::s126, 324908523a45ed3e-0832d3f2::s204

### `12a20d8d-cd49-47eb-9a19-6a38519ee3dc`
> The best answer is **No effect**.

OT-1 T-cells cultured for 24 hours in stromal cell-conditioned medium (SCM) did not exhibit significant alterations in their surface expression of the CD8α co-receptor compared to unconditioned medium (UCM), with the p-value for UCM vs. SCM being 0.7383, indicating no statistically significant difference. Specifically, the CD8α comparison between UCM and SCM yielded P = 0.7383, confirming the absence of a significant effect of bone marrow stromal cell-conditioned media on CD8α expression.

Cited: 2cdfbcfbe2f97d62-25857e4e::s136, 2cdfbcfbe2f97d62-25857e4e::s175

### `4bb69c9d-2485-42d2-b8aa-aa647b407ca4`
> The correct answer is **Decrease**.

Expression of the ATPase-deficient Spn-E-EQ mutant in BmN4 silkworm cells caused a reduction of mature piR1712 and piR2986, with a concomitant accumulation of longer RNA signals corresponding to their pre-piRNA precursors.

Cited: 6f9603c4a7dfa9ed-8ee6647e::s354

### `8c833521-56c4-458d-8c65-2bbf66190cae`
> Infection of A. thaliana plants with an avrE single knockout strain of Pst DC3000 has no effect on NCED3 expression, as expression levels of the ABA biosynthesis marker gene NCED3 were found to be unaltered in Arabidopsis plants infected with an effector-less strain in which AvrPto and AvrPtoB have been reintegrated (which serves as a comparable control context). The best answer is: **No effect**.

Cited: ff5bb438eb6b3659-38bb2e97::s344

### `255fd5fb-9623-4030-8bf2-253247df7c82`
> Infection of A. thaliana plants with the avrE/hopM1 double knockout (h⁻/a⁻) Pst DC3000 results in reduced expression of NCED3 compared to wild-type Pst DC3000 infection, with only the single mutants (hopM1⁻ and avrE1⁻) and wild-type DC3000 showing significantly higher NCED3 expression than mock-infected plants. The best answer is **reduced expression**.

Cited: ff5bb438eb6b3659-38bb2e97::s97

### `38ada695-2c79-459b-8e68-dbed734c74f9`
> Infection of A. thaliana plants with hopM1 knockout Pst DC3000 results in increased expression of NCED3 compared to mock-infected plants, though at an intermediate level relative to wild-type Pst DC3000. The best answer is **Increased expression**.

Plants infected with the hopM1 single mutant showed significantly higher NCED3 expression than mock-infected plants, indicating that infection with hopM1 knockout Pst DC3000 still induces NCED3 expression (albeit at an intermediate level compared to wild-type Pst DC3000).

Cited: ff5bb438eb6b3659-38bb2e97::s97

### `e763edaa-b112-460a-a564-d58a6685e639`
> The best answer is **increased heterogeneity**.

Prenatal DEP + MS exposure strikingly enhanced microglial heterogeneity in male offspring ACC compared with controls, both at P8 and P15. Specifically, the data indicate that prenatal DEP + MS insult increases the relative abundance of microglial heterogeneity in male offspring. This increased heterogeneity was driven by an overabundance of one specific subtype of microglia (Iba1lo P2ry12hi) with severely diminished phagocytic activity that eliminated fewer thalamocortical synapses.

Cited: c0b69d2af9f2e018-845b5d60::s327, c0b69d2af9f2e018-845b5d60::s328, c0b69d2af9f2e018-845b5d60::s423

### `8af900bb-5794-40db-910e-10d5857ce5bd`
> In human temporal and frontal cortex, bipolar interneuron axons target other interneurons at a rate of 72% (225 IN targets out of 314 synapses, N=9 axons). This represents an increase from 56% IN targeting observed in mouse. The best answer is **72%**.

Cited: 3039597cd03cb050-e2ba21eb::s121, 3039597cd03cb050-e2ba21eb::s122

### `6194ebfc-2d5c-4ccc-8883-da7c471b61e6`
> All DANs (100%) received signals from all sensory modalities. The best answer is **100%**.

Cited: 0faff73a03a57dfe-cac59605::s994

### `1f1b07d7-39ce-4665-9b70-4ab77e3c87aa`
> 33% of octopaminergic neurons (OANs) in the mushroom body received input from all sensory modalities (with 5- or 8-hop cascades).

Cited: 0faff73a03a57dfe-cac59605::s266

### `55668039-396e-488a-b2c3-bbe840550433`
> The correct answer is **20%**.

According to the sources, 496 (27%) of TF genes encoding 694 (20%) isoforms could significantly alter pseudotime (Wilcoxon rank-sum test; FDR < 0.05). The question asks specifically about the fraction of transcription factor **isoforms** (not TF genes) that can significantly alter pseudotime upon overexpression, and the answer is **20%** of isoforms.

Cited: 0c23610f9819876e-1c7bceee::s145

### `4f050bf3-27cd-4a14-8422-45df5e2bb079`
> The greatest genetic differentiation parameter (FST) among geographical-based Iranian cannabis populations was observed for the **east and southeast: northeast** pair (FST = 0.09).

Cited: c5e2b39b87ce68c3-3e8a42d1::s444

### `cff00d08-5655-4214-97ac-8fa9504c1165`
> GLP-1-MK-801 produced a vehicle-corrected reduction in body fat mass of 45%, while GLP-1 induced a 22% decrease in body fat mass, yielding an absolute percent difference of 23%. The best answer is **23%**.

Cited: 8a63ec61b2075d5f-74d7d111::s170

### `0eeb7ea9-fc80-4dee-9418-1c328c3ab653`
> The affinity constant of MtNCC1 (specifically its N-terminal Atx1-like domain, MtNCC1₁₋₇₈) binding to Cu⁺ is 2.45 pM⁻¹.

Cited: af470b1b1a34dd6b-0ba6ac3e::s257

### `658f7050-d137-477e-8693-26609080cecd`
> The long, slender stalk of the S. coelicolor Umbrella complex particles extended about 300 Å. The best answer is **300 Å**.

Cited: 0d71c9d2055299d4-2f967140::s162

### `8696273a-7fea-411a-b6c6-0e826e1e02b5`
> The sources indicate that approximately 75% of active promoters in mESCs have contact probabilities with the nearest TAD boundary that are lower than 0.2. The distribution of contact probabilities between all active promoters in mES cells and the closest inner TAD boundary shows that the majority fall below 0.2, with shaded areas in the figure corresponding to promoters with contact probability below 0.2. Therefore, the best answer is **between 0 and 0.3**, as ~75% of active promoters have contact probabilities with the nearest TAD boundary lower than 0.2, placing the bulk of the distribution in the 0–0.3 range.

Cited: 071eed17b15b184b-5393792c::s275, 071eed17b15b184b-5393792c::s904

### `ce6dd5f7-0706-41dd-a383-9b0d22ef00a1`
> The best answer is **Large decrease**.

After knockout of the *Ift122* gene in *Tetrahymena*, Pkdh1 shows a drastic decrease in abundance in the *Ift122*-null strain, suggesting that nonciliary Pkdh1 may be either degraded or downregulated in *Ift122*∆-mutant cells.

Cited: 9d1bda6cef59d705-b224f6d8::s148

### `400786c1-e6c6-4f46-a501-86fdd048ed88`
> The best answer is **Inhibition**.

Elevated levels of Rpn14 cause significant accumulation of phosphorylated α-syn (pS129), indicating that Rpn14 suppresses pS129 α-syn turnover. This conclusion is directly confirmed by the statement that elevated levels of Rpn14 inhibit the turnover of phosphorylated α-syn.

Cited: a95e8580727af033-09043102::s386, a95e8580727af033-09043102::s391

### `e820cbcf-6df1-4c1c-b985-c02f39f52781`
> The best answer is **eliminates function**.

Domains that were lowly expressed on their own ablated KRAB function when paired with it. For example, the poorly expressed DHX16 OB_NTP and BAZ1A DDT domains inhibited KRAB function when concatenated with it. This loss of function was consistent with decreased protein abundance caused by the poorly expressed partner domain reducing overall expression of the fusion.

Cited: 71256a6d0f955156-f438b0cb::s272, 71256a6d0f955156-f438b0cb::s273, 71256a6d0f955156-f438b0cb::s274

### `230dec20-cd02-4613-a7b1-e28058ed46fe`
> The firing rate of parvalbumin-expressing interneurons in the barrel cortex of adult mice is significantly reduced when SMAD1 is deleted. The best answer from the provided options is **Greatly reduced**.

This reduced firing frequency is most likely explained by a reduction in input resistance in the SMAD1-deficient cells.

Cited: 3b1e01c90c47dd5d-850e00fc::s206, 3b1e01c90c47dd5d-850e00fc::s208

### `7975ddb0-a784-4f85-a297-c80e1cb5dcf2`
_Refused._

### `a1d01019-d2b1-4619-92ec-7ea38578819f`
> The mechanism for expression of the EPRS1(N1) form is **polyadenylation**.

A novel polyadenylation event, which introduces a new stop codon, generates an EPRS1 variant with a truncated C-terminus called EPRS1(N1).

Cited: 3ced378716ddecf0-3008c492::s137

### `fe074387-3765-4020-8f5d-e395d1094121`
> The net rate of 3D imaging for time-lapse continuous data generated by 2pSAM is 30 volume/s. By exploiting spatiotemporal continuity and estimating motions during reconstruction, a motion-correction algorithm was developed to increase reconstruction volumetric speed to 30 volume/s.

Cited: 3022f334b06fe41f-49e3ab2b::s146

### `f0b6cea0-e005-47bc-be0d-9a10b219cae6`
> The optimal GDP-binding temperature for the EF-1A protein from Asgard class Wukongarchaeia is 63.2 °C (90% CI: 54.8–65.6 °C). Therefore, the best answer from the provided options is **63.2**.

Cited: e2c5bba3431b7f0b-903142c2::s141

### `ae02d0e9-edf5-4c39-a215-3cbc8f4c565d`
> The phylloxera X chromosome is the second-largest chromosome, at 47.28 Mb. This was confirmed by sequencing read depth analysis showing that the second-largest scaffold had about half the normalized sequencing read depth ratio for males compared with other chromosomes. The best answer is: **Second longest**.

Cited: d0e434519e92b617-6d9d1707::s83, d0e434519e92b617-6d9d1707::s85

### `fd60a0e7-ba64-49a9-843a-6f5cb17c5fa9`
> The role of the N-terminal α1-helical extension in the PF03500 protein family is **α1-driven dimerization**.

The N-terminal α1-helical extension drives the formation of a specific dimerization interface within the tetramer, burying approximately 822 Å² and contributing a free energy gain of ~10 kcal/mol to the quaternary structure. This α1 dimerization is primarily driven by symmetric hydrophobic contacts between adjoining α1-helices, as well as hydrophobic and polar interactions with the protein core of the neighboring subunit. More broadly, the presence of this N-terminal α-helical extension (α1) is determined to drive the D2-symmetric, tetrahedron-like tetrameric quaternary structure assembly, and is likely conserved in the majority of bcsD-encoding β- and γ-Proteobacteria.

Cited: ec21473ce029219d-58061129::s207, ec21473ce029219d-58061129::s208, ec21473ce029219d-58061129::s315

### `14fd2b75-76fb-4c29-a21d-c557b2bcf2ff`
> The CDRs of P1A4 form a deep, ~12-Å pocket between the heavy and light chains that ARS1620 is able to access. The best answer is **12 Å**.

Cited: 09d92318a4a24d0d-b1ddf424::s100

### `e9f142f0-8ef6-47cd-b846-7283a93308d4`
> The non-specific effect observed for jAspSnFR3.mRuby3 is due to an interaction of amino acids with the C-terminal histidine tag. This was confirmed because the effect could be reproduced with other proteins containing mRuby3 purified via the same C-terminal histidine tag, and was absent when the histidine tag was removed. Therefore, the best answer is: **Interaction of amino acids with the C-terminal histidine tag**.

Cited: 64c8513d404bd086-2a7ec0cf::s62, 64c8513d404bd086-2a7ec0cf::s637

### `398ebac1-fd2d-45b1-9415-d82db4b4d83c`
> The best answer is **Shift equilibrium to super-open state**.

The A456V mutation in Human Glucokinase accelerates glucose binding by shifting the conformational equilibrium towards the super-open conformation, rather than the closed active state. Specifically, while most other hyperactive variants increase conversion to the closed state, p.A456V is the exception — all variants except p.A456V to some extent increased conversion to the closed state. This shift toward the super-open state is consistent with the finding that p.A456V mainly accelerates glucose binding rather than increasing conformational preference towards the active state. The mechanistic basis is that at low glucose levels, GCK shifts into the super-open conformation prior to binding a new glucose molecule, and by stabilizing this conformation, the enzyme is primed for glucose binding.

Cited: ff6d931c3e1942c1-312bdc4b::s147, ff6d931c3e1942c1-312bdc4b::s652, ff6d931c3e1942c1-312bdc4b::s657, ff6d931c3e1942c1-312bdc4b::s659

### `7e7150d6-bc73-4a29-a5b3-4ef8399ed947`
> The substrate preference of the Ddd1 deaminase is 5'-GC.

Cited: 635912ff7732db5a-d3b4f268::s379

### `58b39fab-337b-452d-b74f-84f9a188ce88`
_Refused._

### `80e6571e-8f5d-496a-8ba3-9c9f5b783f5d`
> The marker combination **CD38+CXCR6+** can be used to identify murine liver CD8+ tissue-resident memory T cells independent of CD69 during inflammatory conditions.

CXCR6 and CD38 expression by circulating memory T cells (TCIRCM) remained stable following viral challenge (VV-OVA), unlike CD69 which was dynamically induced, making CXCR6 and CD38 suitable for CD69-independent TRM cell identification. Specifically, CXCR6 and CD38 expression remained similar following VV-OVA infection, allowing for CD69-independent TRM cell identification in the liver. Thus, employing CXCR6 and CD38 for TRM cell identification enables the evaluation of their functionality during inflammation and antigen challenge, which cannot be achieved using CD69 expression alone.

Cited: 7de06dcdff06813d-2aa4a31e::s299, 7de06dcdff06813d-2aa4a31e::s303, 7de06dcdff06813d-2aa4a31e::s357

### `154e7b14-4ed5-4cf3-9149-0c4843fc62cc`
> Circular dichroism was used to demonstrate that PafA remains folded even after exposure to 4 M urea for 14 days.

Cited: 68c9c104777ac1ed-f6f095ce::s125

### `a71ef7a2-31a2-460d-9ff4-32d7722353c3`
> Endonuclease V from *Thermotoga maritima* (Tm EndoV) is inhibited by dNTP concentrations greater than 2 mM. Therefore, the best answer from the provided options is **2mM**, as this is the threshold concentration above which inhibition occurs.

Cited: f7415168f213937f-e85e09ae::s490

### `c624ed31-214f-4c80-9544-5514a096b1d3`
> 73% of genes with RNA editing in mouse retina cells also exhibited alternative splicing.

Cited: bd4a587f33a63d66-71a1a570::s814

### `bcd2f213-c6c6-4660-af35-a7bd1c6a1170`
_Refused._

### `24fae97b-03f3-48b8-b623-abf07faee02e`
> The top ten loci for Cp36 accounted for 11.4% of uniquely mapped reads in K562 cells. The best answer is **11.40%**.

Cited: 168faa61f56dbad8-d9cdd41f::s1346

### `ce93661b-e3c4-4a7a-96b6-87492259c501`
> About 50–80% of fibroblasts resisted up to 12 days of oxaliplatin chemotherapy treatment in culture. The best answer is **50-80%**.

Cited: 14e30d1f93ac281f-1feb8376::s181

### `941c04dc-c89d-4a90-87b0-930625268a38`
> 64% of non-genic genomic region windows displayed some transcription at a relaxed threshold (1 TPM) in the E. coli LTEE lines at 50,000 generations.

Cited: f9f1eafd2f81f280-86b6f479::s39

### `ea4ce240-2864-4ee5-9ffc-2dbda0f8f550`
_Refused._

### `cff68274-4bbe-4fa0-a181-36a9af3cc0f1`
_Refused._

### `2c262f91-52b6-421d-8341-8748f923459e`
_Refused._

### `6f8a51e2-f7ad-4033-b43d-370348e4809f`
> The key residue interaction formed when MC1 binds to PSMD2 involves the R8 residue of MC1 establishing a charge interaction with E878 of PSMD2. The best answer is: **R8 residue of MC1 and E878 residue of PSMD2**

Cited: 36e711a08612716e-caaa863d::s138

### `9a0b82cb-6a99-4e50-83fc-3ef2ebd277cc`
_Refused._

### `8b665114-7729-4dac-a64f-4862a5397b82`
> Rv2780 was mainly detected in the cytoplasm of mice peritoneal macrophages during M. tuberculosis infection. The best answer is **Cytoplasm**.

Cited: c31907b446aed1b3-79dfc999::s81

### `5c808548-92c4-4ae7-990c-e2df81e3c2ae`
> The protein encoded by GARIN3 (also known as GAPR-1) localizes to lipid-enriched microdomains in the Golgi complex of mammalian cells. The best answer is: **lipid-enriched microdomains in the golgi apparatus**

Cited: bc47961c1b2fa94b-e60b4799::s294

### `564e715f-8d30-410b-bdb5-0dc5206589a7`
_Refused._

### `e90ea0fc-4659-4b20-acae-75dc4b97a101`
> The V1 and V3 isoforms of CDH23 are capable of localizing to the stereocilia. Specifically, for the V1 isoform, both CDH23(+68) and CDH23(−68) were localized to the stereocilia as well as in the cell body. For the V2 isoform, both CDH23(+68) and CDH23(−68) were only detected in the cell body, not the stereocilia. For the V3 isoform, when the HA tag was placed at the N-terminus (to avoid interference with localization), CDH23-V3 was detected in the stereocilia as well as the cell body. The best answer from the provided options is: **The V1 and V2 isoforms** — however, this is incorrect per the sources. The correct answer supported by the sources is **"and V3 isoforms"** (i.e., V1 and V3 isoforms), as directly stated: "V1 and V3 isoforms of CDH23 can localize to the stereocilia."

Cited: a322cf631e4099c8-c8d9416c::s145, a322cf631e4099c8-c8d9416c::s146, a322cf631e4099c8-c8d9416c::s149, a322cf631e4099c8-c8d9416c::s150

### `c246753c-27d2-4ae4-8630-b9b4077ba6f6`
> The best answer is **1-149**.

The N-terminal HORMA domain encompassing residues 1-149 of ScRev7 is dispensable for interaction with the MRX subunits, as cells expressing N-terminally truncated variants (lacking this region) showed robust growth in selection medium, indicating they still associate with the MRX complex. In contrast, the C-terminal 42-amino acid fragment (residues 203-245) is critical for binding to the MRX subunits, and its deletion abolished this interaction.

Cited: 5a389cfe7cca76d2-437a07be::s322, 5a389cfe7cca76d2-437a07be::s759

### `22306bd7-7e84-415d-aebb-11c6312eb081`
> The AMP-CpG formulated EBV vaccine generated gp350-specific antibodies of the IgA, IgM, IgG1, IgG2a, IgG2b, and IgG3 isotypes. Notably, IgE is not mentioned among the isotypes produced, making it the antibody isotype NOT produced by the AMP-CpG formulated EBV vaccine for gp350-specific antibodies. The answer is **IgE**.

Cited: 9ed823ba1e15f21e-9d83dcd0::s385

### `7d71dffb-b591-4b88-b0c6-e125a1b083b4`
> Lipopolysaccharide (LPS) has been shown to induce inflammation and facilitate lung metastasis in a breast cancer model via the prostaglandin E2-EP2 pathway. LPS is a structural component of Gram-negative bacterial cell walls, making **lipopolysaccharide** the correct answer.

Cited: 760a41458de0016f-45c84606::s724, 760a41458de0016f-45c84606::s835

### `fca26d7c-05cf-40b0-9fd6-a63ed7950909`
> The Vault AAV delivery system uses the SpyTag-SpyCatcher bioconjugation system to attach the INT tag to AAVs. Specifically, SpyTag003 (SpT3) is inserted into the VP2 capsid protein of AAV9, and a SpyCatcher003-INT (SpC3-INT) fusion protein is created, allowing covalent conjugation of the INT peptide to the AAV surface. Therefore, the best answer from the provided options is **Spytag003**.

Cited: 2445404168635a55-0ad2b180::s66, 2445404168635a55-0ad2b180::s74

### `c6e11fac-8f9c-4cf1-aa6e-4d25731ba74f`
> The most highly represented genes in Borg genomes encode glycosyltransferases. The best answer is **Glycosyltransferases**.

Cited: 01e0adaed8ffd463-38a7f893::s131

### `bace5737-ba26-422a-8706-0fb1e92b689f`
_Refused._

### `ff7328e2-4954-46a2-8ea3-d40b4df0c0ea`
_Refused._

### `76bcaeeb-93bd-4951-99b9-cf4613de1a37`
> The only microcin homolog identified in all E. coli phylogroups was microcin V.

Cited: 58223b6183837ffb-65e8f6c9::s173

### `850f86d3-0139-43df-89fd-e606c30aaa8b`
> The mouse model used to demonstrate that CD90 could identify germinal center-resident follicular helper CD4+ T cells was NP-OVA footpad immunization. PAGFP transgenic mice were footpad-immunized with 20 µg of NP-Ova+alum, and photoactivated GCTfh cells were found to express reduced levels of CD90 compared to resting naive CD4+ T cells. S1pr2-RFP mice were also footpad-immunized with 20 µg of NP-Ova+alum to confirm decreased CD90 expression in S1pr2-marked GCTfh cells. Therefore, the best answer is **NP-OVA (4-hydroxy-3-nitrophenylacetyl (NP)-ovalbumin (OVA)) footpad immunization**.

Cited: ee877dbbbd2e51e3-55e76368::s105, ee877dbbbd2e51e3-55e76368::s125

### `df061613-2591-4faa-be03-791c76375cb5`
_Refused._

### `634f6745-f3b3-4cb1-9859-96ffb954b98a`
_Refused._

### `d1eabedb-656f-4f89-a65f-4ed89478ba9f`
> DILT (diltiazem) is the most effective compound at enhancing ER proteostasis and promoting functional, soluble forms of GCase in neurons. While DANT and DHBP also elevated soluble GCase levels in cell models, they did not do so as robustly as DILT. DILT was validated to enhance chaperone function by increasing the binding activity of CANX to N-glycosylated proteins, and treatment of SNCA-3x neurons with DILT abrogated the buildup of insoluble GCase while concomitantly elevating soluble GCase. The best answer is **DILT**.

Cited: f74e43a900ad6cb5-10c56ee5::s236, f74e43a900ad6cb5-10c56ee5::s242, f74e43a900ad6cb5-10c56ee5::s244

### `58f69c8d-cb94-4021-a84f-c549a7b976e1`
> CXE (Cas9-XTEN-hExo1) resulted in the highest HDR efficiency among the four designed EXO editors. Specifically, CXE showed the highest HDR efficiency and lowest indel frequency among CXE, EXC, CTE, and ETC, and was even significantly superior to the positive controls E4 and E1B. The optimized EXO editor, CXE, in which hExo1 was fused to the downstream of Cas9 with XTEN linker, gave rise to the highest HDR efficiency and the lowest indel frequency.

Cited: 66aafadef9d913b8-311a2ec6::s1162, 66aafadef9d913b8-311a2ec6::s296, 66aafadef9d913b8-311a2ec6::s297

### `20980744-f9ff-4e39-a08d-106eada6900c`
_Refused._

### `a6622141-68d6-418f-8e30-7a5eff3d4fa8`
_Refused._

### `9fe3ff3b-60cf-472d-ab1a-2bda1868f1b4`
> The best answer is **Increased acetylation relative to female VICs**.

Male VICs showed a unique trend where only larger particles affected the acetylation state, while smaller particles did not produce this effect. Male VICs also displayed significantly higher acetylation states compared to female VICs across hydrogel conditions. Therefore, on larger polystyrene nanoparticle gels (but not smaller ones), male VICs can be expected to show increased acetylation relative to female VICs.

Cited: e44731dbd47b1ddf-5ac4257e::s268, e44731dbd47b1ddf-5ac4257e::s269

### `9088251a-99fe-4b91-b6a9-375154ec4f58`
> ZDHHC5 (together with ZDHHC9) mediates ROS-dependent palmitoylation of GSDMD, which is indispensable for pyroptosis. The sources indicate that ZDHHC5 specifically promotes palmitoylation of GSDMD to facilitate plasma membrane localization and pyroptosis, while GSDMB and GSDME palmitoylation by ZDHHC5 is not established — GSDME palmitoylation is mediated by ZDHHC2, 7, 11, and 15, and the enzymes responsible for GSDMB palmitoylation require further study. Therefore, the best answer is **GSDMD**.

Cited: de604c3de7db092a-c7360229::s413, de604c3de7db092a-c7360229::s415

### `b8ec372b-ae29-473e-96bc-86ff1ead24ea`
> The best answer is **ERK1 & ERK2**.

On denatured collagen, β3 integrin-dependent activation of ERK1 and ERK2 regulates TN-C in vascular smooth muscle cells. Specifically, the β3 integrins activate both ERK1 and ERK2 MAPKs, which in turn modify prx1 and prx2, leading to interaction with the TN-C gene promoter and induction of TN-C transcription.

Cited: dd641ef35dc94ec2-2545f939::s395, dd641ef35dc94ec2-2545f939::s414

### `a45c277e-55d9-4e7f-b1de-37fc2e19daf6`
> Ogfrl1 has been shown to be a highly specific marker for parvalbumin (PV) interneurons in the molecular and fusiform layers of the dorsal cochlear nucleus. The best answer is **Ogfrl1**.

Cited: 1d72af568ea9078d-b044a088::s227

### `a8aa19cc-e4d1-4aa1-8c4e-2a518b4c99d6`
> Rasgrf1 has been shown to have significant nonrandom spatial distribution within the granule cell layer of the cerebellum, with its expression localized to the anterior (dorsal) side of the puck — a pattern that is largely the opposite of Gprin3, Cemip, Syndig1l, and Mab21l2, which showed strong localization to the ventral (posterior) granule layer (lobules VIII–X). Therefore, the gene localized to granule cells **anterior** to the primary fissure is **Rasgrf1**.

Cited: 1d72af568ea9078d-b044a088::s233

### `2c3ba95c-47d5-4798-9911-ffdb11c940e4`
> JUND was identified as a stabilized RNA upon DDX3X depletion. Specifically, JUND RNA was stabilized after 24 h with knockdown of DDX3 and ActD treatment. Therefore, the best answer is **JUND**.

Cited: 56206a0d497c3922-fc28cbb0::s113, 56206a0d497c3922-fc28cbb0::s98

### `49d2630e-9d26-4e12-89a3-3050a609abf5`
_Refused._

### `c758f685-ba4a-4bf0-bd85-567c60ff1508`
> The answer is **p50**.

Nuclear expression of the cofactor p50 was enriched in TRAF3 LOF DLBCL cells, suggesting potential crosstalk between the two NF-κB branches. By contrast, nuclear localization of canonical NF-κB transcription factor subunits RelA and c-Rel was not affected by TRAF3 LOF.

Cited: 0ca36e794a547256-8b0b5a88::s289, 0ca36e794a547256-8b0b5a88::s293

### `fd54d745-447c-4fcd-80de-463fcd3de6a4`
> The answer is **MYB44**.

The sources confirm that ABA catabolic genes upregulated in dana1 knockout lines include CYP707A1, CYP707A2, CYP707A4, and UGT71B1, while MYB44 was found to be **downregulated** (not upregulated) in the dana1 mutant.

Cited: b372fd7f8558d5e0-ff2c7d15::s205

### `4d11258d-ee8c-4bc7-91a8-613c7a41f139`
> The K548R mutation in PARP1 has been shown to impair its interaction with MRE11 in immunoprecipitation assays. Specifically, FLAG-PARP1 WT, K548R, or Vector, together with GFP-MRE11, were transfected into HEK293T cells and subjected to FLAG affinity gel immunoprecipitation, where the K548R mutant showed reduced interaction with MRE11. The answer is **K548R**.

### `1ff2b2e4-492e-4e35-bf33-f0fb53ab938c`
_Refused._

### `178a5e56-340f-4ba8-a3e5-f024ca016f40`
_Refused._

### `c75879f4-9329-4594-8f6a-c4d421f2439f`
> The question asks which mutation *increases* interaction with SH3 (i.e., shows loss of specificity — stronger binding to SH3-containing proteins than wild-type).

Only three Pbs2 mutants (Q82W, P97A, and L98F) were found to interact with an SH3-containing protein more strongly than wild-type Pbs2, indicating a loss of specificity, while S83F, K85W, I87W, N92H, and N92S all interacted more weakly (gain of specificity). Among the answer options provided (I87W, K85W, N92H, N92S, P97A, S83F), only **P97A** is listed as a mutation that increases interaction with SH3-containing proteins (loss of specificity — stronger binding than wild-type). The best answer is **P97A**.

Cited: 667d94590e6616fe-e15f7eed::s535

### `f7346ea0-5f1b-45e9-a1d6-493c754159c1`
> The S118L mutation of Kir6.2 does not affect ATP sensitivity of the KATP channel. The S118L mutation does not affect channel stimulation by MgADP, as MgADP-induced increases in hetS118L and homS118L KATP currents were not significantly different from wild-type. Metabolic inhibition of hetS118L and homS118L channels was unaffected, with current amplitudes and rates of activation in response to azide being similar to wild-type. In contrast, membrane trafficking is impaired by the S118L mutation, with an approximately 40% reduction in surface expression of hetS118L and homS118L channels compared with wild-type. Therefore, of the listed processes, **membrane trafficking** is the process impacted by the S118L mutation.

Cited: e01d60f8ccaf1fbd-a4be292d::s199, e01d60f8ccaf1fbd-a4be292d::s203, e01d60f8ccaf1fbd-a4be292d::s208, e01d60f8ccaf1fbd-a4be292d::s245, e01d60f8ccaf1fbd-a4be292d::s315

### `3d3fea17-c8ee-4005-94cb-d8798be696c3`
> The sources report a remarkably consistent log-linear (log10-log10) relationship between the volume of UCYN-A (the nitroplast) and the volume of its haptophyte host cell. This relationship holds true within and across different UCYN-A sublineages, with a slope of approximately 1.0 and R² = 0.97. A similarly tight log-linear size relationship also exists between the volume of the host cell and the total chloroplast volume, further supporting that volume scales log-linearly in this symbiosis. The best answer is **Volume**.

Cited: b2aeda61ca908aaf-9486c25d::s139, b2aeda61ca908aaf-9486c25d::s79, b2aeda61ca908aaf-9486c25d::s80

### `ab58e166-f0b5-49ae-ac56-c38b5d6e8aad`
> Podoplanin (Pdpn) is downregulated in post-Aire mTECs, and by flow cytometry the mTEC lo population separates into Pdpn+ CD104+ (pre-Aire) and Pdpn− CD104− (post-Aire) compartments, meaning Pdpn expression (its absence) marks post-Aire mTECs. Therefore, among the listed options, **Pdpn** is the protein that can be used to identify post-Aire mTECs (specifically, post-Aire mTECs are Pdpn-negative, distinguishing them from pre-Aire mTECs that are Pdpn-positive).

Cited: da7b856dfa32186d-1e1bf60f::s168, da7b856dfa32186d-1e1bf60f::s173

### `a73b2c2d-a3ac-49e6-8e2e-44b4c1e6de94`
> The best answer is **SmD1**.

The five Sm proteins most reduced in D20V mutant pulldowns were SmD1, D2, E, F, and G, which correspond to the proteins that directly bind Gem2 during U-snRNP assembly. Among the answer options provided, SmD1 is the only Sm protein listed, and it was identified as one of the most reduced binding partners in the D20V mutant compared to WT SMN. By contrast, proteins such as Cul1 and SkpA (components of the SCF E3 ligase) were significantly enriched in SMN pulldowns but were not specifically noted as reduced in D20V mutants. HspA family members were noted to preferentially interact with SMA-causing alleles, suggesting increased rather than decreased association with mutant SMN.

Cited: 7b3aeee153dea14b-f01a40db::s116, 7b3aeee153dea14b-f01a40db::s135, 7b3aeee153dea14b-f01a40db::s34

### `04dbe07d-8b2c-4daf-b5b2-ef0e93f1fd2a`
> The residue of KBTBD4-PR that is inserted into the narrow tunnel leading to the HDAC1 catalytic site is Arg312, whose positively charged side chain reaches halfway into the tunnel. The best answer is **Arg312**.

Cited: 774bbc2bae82b5a7-82522eec::s148

### `4a6705b5-85e5-44c1-8444-65be30192802`
> The best answer is **RlmB**.

The catalytically inactive RlmB variant RlmB(E198A) can stimulate 50S assembly, demonstrating that RlmB has a modification-independent function in large ribosomal subunit assembly. In contrast, the catalytically inactive RlmN(C355A) variant does not stimulate ribosome assembly, indicating that RlmN's catalytic activity is required. Similarly, expression of the catalytically inactive RluC(D144A) does not improve ribosome assembly in the Δ10 strain, suggesting that the pseudouridines made by RluC are important for ribosome LSU assembly. RlmB (and RlmL) have functions in ribosome assembly independent of their modification activities, distinguishing them from RlmN and RluC, which require catalytic activity.

Cited: 9a92b9f5adbd8f23-edc56ec0::s15, 9a92b9f5adbd8f23-edc56ec0::s255, 9a92b9f5adbd8f23-edc56ec0::s262, 9a92b9f5adbd8f23-edc56ec0::s359

### `08397294-3d99-4790-915c-b8bcb1e9e661`
> The best answer is **DTD**.

When Drosophila lacking the Rev3 catalytic subunit of polymerase zeta were also mutated in the DTD domain of Rev1, the double mutants showed the greatest increase in MMS sensitivity among the domain-specific mutants tested. Specifically, Rev1-DTD rev3 double mutants showed a greater increase in sensitivity than either Rev1 ΔBRCT rev3 or Rev1-UBM rev3 double mutants, reaching a level equivalent to that of the rev1Δ null mutant. This indicates that the deoxycytidyl transferase activity of REV1 becomes critically important for MMS tolerance in the absence of pol ζ.

Cited: 1c2a0524c883d73f-f2d03f0c::s129, 1c2a0524c883d73f-f2d03f0c::s156

### `837b2489-723a-4099-9b68-c2a9ea688f4d`
> BUD40 produces the thickest fibers, averaging 2.07 ± 0.56 microns thick, compared to BUD60 (1.31 ± 0.23 microns) and BUD80 (1.07 ± 0.21 microns). The best answer is **BUD40**.

Cited: 7eb232e6cd269f4c-b14c15d4::s299

### `745f5a0d-5f8f-405e-bb46-f37b3d1f0678`
> The correct answer is **None of the above**.

Training characteristics within the target brain region — specifically mean NF signal amplitude, mean left amygdala activation, and signal changes in the left amygdala — were **not** associated with changes in symptoms and therefore could **not** explain interindividual differences in clinical response. Instead, it was whole-brain activation pattern subtypes (beyond the target region) that were significantly associated with interindividual variability in clinical efficacy.

Cited: 06508579b3fd8baf-222782c2::s507, 06508579b3fd8baf-222782c2::s508

### `bca1be77-208b-4d57-ac29-05aa6d58bdbf`
> The transcription factor p50 most strongly promotes macrophage polarization towards a hypoxia state in glioma-associated TAMs. Disruption of p50 (encoded by NFKB1), but not HIF1α or c-Jun, markedly decreased the expression of Hypoxia-TAM signature genes, identifying p50 as the key driver. These results confirm that p50, as a downstream transcription factor of NFκB signaling, is required for the Hypoxia-TAM signature. The best answer is **p50**.

Cited: e1671d32c95165a1-15d2b9a0::s246, e1671d32c95165a1-15d2b9a0::s247, e1671d32c95165a1-15d2b9a0::s364

### `2dc20a2f-de54-4bfe-a34f-1ba395f342cf`
> The best answer is: **The viscosity of nucleus is approximately the same as the viscosity of the cytoplasm.**

In IHAs, there is no statistical difference between the viscosity of the nucleus (2527 ± 871 Pa·min) and cytoplasm (4432 ± 1026 Pa·min), making this a property specific to IHAs. In contrast, IHAs show distinct differences in nuclear versus cytoplasmic stiffness (nucleus fourfold stiffer than cytoplasm) and relaxation time (nucleus significantly lower than cytoplasm), but these differences are also not conserved in GBM cells, meaning those properties are not unique to IHAs in the way the question asks. GBM cells do not have significant differences in cytoplasmic versus nuclear stiffness, viscosity, or relaxation time, so the similar viscosity between nucleus and cytoplasm is shared by both cell types. However, among the answer options provided, "the nucleus is more stiff than the cytoplasm" and "the relaxation time of the nucleus is higher than that of the cytoplasm" are contradicted by the sources (the nuclear relaxation time is *lower*, not higher, than cytoplasmic relaxation time in IHAs). The option that the viscosity of the nucleus is approximately the same as the viscosity of the cytoplasm is directly supported as a finding in IHAs, and since GBM cells also show no significant nuclear-cytoplasmic differences across all properties, this is the most specifically noted IHA property among the options.

Cited: edce53910698b365-47b1176a::s132, edce53910698b365-47b1176a::s133, edce53910698b365-47b1176a::s134, edce53910698b365-47b1176a::s155

### `afb36e40-0836-4810-909e-eabfe17dcd8b`
> TYMS was not upregulated by 5-FU treatment in the HCT116 cell line. Specifically, thymidylate synthase (TYMS) was not significantly upregulated upon the administration of 5-FU within 72 hours. In contrast, ITPA was upregulated >2-fold at 10 μM 5-FU in 72 hours. polB (pol β) was also upregulated >2-fold upon 5-FU administration in 72 hours. Rev1 was also upregulated in response to 5-FU treatment.

Cited: 0606f4a1026bae93-53471ae3::s1367, 0606f4a1026bae93-53471ae3::s1373, 0606f4a1026bae93-53471ae3::s1441, 0606f4a1026bae93-53471ae3::s1443, 0606f4a1026bae93-53471ae3::s1548

### `c6f097c9-2216-4e98-af45-8101681b38ec`
_Refused._

### `9f797d29-9f3a-481d-b2fe-326cbc686273`
> Mn2+ exhibited the most enhancing effect on the cleavage activity of R.DraR1, while Mg2+ had only minimal catalytic effect, and Ca2+, Zn2+, and Ni2+ were unable to catalyze the cleavage activity. The best answer is **Mn2+**.

Cited: 97736fa153fa784c-41306673::s223

### `0d5cf8a7-a240-4a8f-be4e-c16712f90d79`
> The answer is **L522**.

Substituting L522 in the minN region of UNK's IDR to alanine completely silenced the transcriptional activity of that region.

Cited: f56f5fb1f0922800-5c745f12::s207

### `40400348-eabb-4b25-90d1-e33589d3e5a4`
> The over-the-counter antihistamine found to be as effective as (and in some respects superior to) anti-VISTA antibodies when combined with ICB therapy is **Fexofenadine**.

FEXO (fexofenadine) monotherapy showed similar anti-tumor activity to that of VISTA antibodies, and when combined with ICB therapy, had similar efficacy in controlling primary tumor growth. Remarkably, FEXO+ICB was more effective than anti-VISTA+ICB for prolonging survival of mice, as 50% of FEXO+ICB-treated mice had tumor-free survival while none of the anti-VISTA+ICB-treated mice survived. FEXO+ICB was also more potent than anti-VISTA+ICB in inhibiting lung metastasis.

Cited: 1e98838d3116281b-bac8d842::s253, 1e98838d3116281b-bac8d842::s255, 1e98838d3116281b-bac8d842::s256

### `ebe57888-662f-488f-ade1-c0aaffe638b1`
> GFAP (glial fibrillary acidic protein) has been shown to increase in expression in RhoANesKO mice.

Cited: d396d8edd4f389e6-d53cbbe3::s270

### `ef07d562-fc18-43c9-8201-7a189d76eeb9`
> The highest levels of KIR+ CD8+ T cells in COVID-19 patients were found in those with vasculitis or embolism, and to a lesser extent in those with acute respiratory distress syndrome (ARDS). Among the provided answer options, **vasculitis** is the best answer, as the sources explicitly state that the highest frequencies of KIR+ CD8+ T cells were found in patients with vasculitis (or embolism), with ARDS being a secondary association. Elevated KIR+ CD8+ T cells, but not CD4+ regulatory T cells, were specifically noted to correlate with vasculitis in COVID-19 patients.

Cited: 7f115cb9d0652622-d64852b9::s300, 7f115cb9d0652622-d64852b9::s98

### `b331480e-dfc7-4e92-931a-c71f491c4795`
> The three residues with evolutionary divergence in the G domains of RAS isoforms that impose selectivity constraints on pan-KRAS non-covalent inhibition are H95, P121, and S122. The orthosteric effect is conferred by H95 in the α3 helix, while P121 and S122 in loop 8 contribute allosteric (indirect) effects. The triple substitution in HRAS (Q95H, A121P, and A122S) was required to render HRAS similarly sensitive to the pan-KRAS inhibitor as KRAS, confirming that all three residues (95, 121, and 122) together determine selectivity. The best answer is **95, 121, 122**.

Cited: 70973b3a4b0a193e-f334e23d::s129, 70973b3a4b0a193e-f334e23d::s135

### `58950824-2665-445d-939b-9512d5d01a2b`
> MEF2C has been identified as a central regulator and network hub in the context of muscle adaptation to endurance training, and was suggested to have increased activity in the TF enrichment analysis. MEF2C enrichment was confirmed in the TF enrichment analysis, and it is linked to both heart and skeletal muscle adaptations to endurance training in Rattus norvegicus rats. The best answer is **MEF2C**.

Cited: d55d01d52f893ef8-5b74c904::s1197, d55d01d52f893ef8-5b74c904::s1198

### `8d12cb90-73c6-4cc1-9f83-0fa9fd822e92`
> The two transcription factors used to identify the T4/T5 neuron subtypes in the optic lobe were acj6 and SoxN.

Cited: 010bab0784c5d05e-4d07cf2b::s185
