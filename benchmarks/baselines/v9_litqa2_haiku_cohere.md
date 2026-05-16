# Eval Report: litqa2

- **Pipeline:** `anthropic/claude-haiku-4-5 | cohere-embed-v3 | hybrid(BM25+lance) | min_tokens=100 | cohere-rerank-v3 | retrieve=100/rerank=10 | no-verifier | loose`
- **Run at:** 2026-05-16 16:00:33
- **Questions:** 186

## Aggregate metrics

| Metric | Value |
|---|---|
| `citation_precision` | 0.686 |
| `citation_recall` | 0.499 |
| `citation_f1` | 0.444 |
| `coverage` | 0.744 |
| `localization_accuracy` | 0.242 |
| `abstention_precision` | 0.000 |
| `abstention_recall` | 1.000 |
| `abstention_f1` | 0.000 |
| `mc_correct` | 103.000 |
| `mc_wrong` | 0.000 |
| `mc_unanswered` | 83.000 |
| `mc_accuracy_over_answered` | 1.000 |
| `mc_accuracy_over_all` | 0.554 |

## Per-question results

| ID | Refused | Should refuse | Cited ∩ Gold | Cited | Gold | Faith |
|---|---|---|---|---|---|---|
| `e3b5a4af-41d9-48db-becf-29a08d0ad28e` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `76184ccf-4bf0-469e-a442-11d04b4ff8b0` | ✗ | ✗ | 1 | 1 | 1 | 0.12 |
| `39129e1c-096f-4414-bf4f-37fadbbe364c` | ✗ | ✗ | 2 | 2 | 5 | 0.49 |
| `27234279-f50c-4cfc-86e2-af68364a8f94` | ✗ | ✗ | 1 | 1 | 3 | 0.26 |
| `517e7cf8-c5d2-4391-9e2a-235b79d93050` | ✗ | ✗ | 1 | 1 | 1 | 0.81 |
| `cb710074-73a8-4407-b0c7-7dc868f1bc76` | ✓ | ✗ | 0 | 0 | 14 | 0.72 |
| `5c4c602c-9624-4eae-ac44-efe4c0dd10e6` | ✗ | ✗ | 1 | 1 | 1 | 0.68 |
| `c9bdb9b5-28c1-44da-93b6-b1fc9d8bf369` | ✗ | ✗ | 3 | 3 | 9 | 0.92 |
| `e6b0f9e5-e976-47dc-b839-0b2fca967e9e` | ✗ | ✗ | 1 | 1 | 12 | 0.25 |
| `247eeb85-a552-4b87-b83e-327538fcb8a9` | ✗ | ✗ | 0 | 0 | 12 | 0.87 |
| `a214f5f8-0de8-43cf-82e0-7930003e4a0c` | ✗ | ✗ | 1 | 1 | 7 | 0.35 |
| `a43e5166-d0e8-48f8-a113-648acac7ed59` | ✗ | ✗ | 1 | 1 | 1 | 0.64 |
| `dd29920d-cb70-440f-961c-3e1103776c4f` | ✗ | ✗ | 1 | 1 | 1 | 0.97 |
| `7d805bb8-4c7c-431f-b068-acf5e5459985` | ✗ | ✗ | 0 | 1 | 1 | 1.00 |
| `8d7fa642-ee46-4a13-8ea9-61cc2d4f4ddd` | ✗ | ✗ | 1 | 2 | 6 | 0.80 |
| `487539f9-2f17-4009-aa4a-c41322445f11` | ✗ | ✗ | 0 | 0 | 6 | 0.96 |
| `5049c648-b1bb-4624-8824-9d93dfb04e51` | ✗ | ✗ | 1 | 1 | 1 | 0.89 |
| `a18883e9-218a-4719-8d2c-cf94d740de1a` | ✗ | ✗ | 0 | 2 | 3 | 0.98 |
| `d7833c0f-2a16-40d2-b6a0-6764aa3003a6` | ✗ | ✗ | 0 | 0 | 5 | 0.99 |
| `1ccdc348-50e1-4941-9151-5e50411a2b41` | ✗ | ✗ | 1 | 1 | 1 | 1.00 |
| `1e5f5199-84f4-4133-ab87-2372fa6ca722` | ✓ | ✗ | 0 | 0 | 2 | 0.99 |
| `d2860d38-dfb9-4b80-905f-812c32573915` | ✗ | ✗ | 1 | 2 | 1 | 0.75 |
| `77a41274-cd9c-48bc-a347-e0746907840d` | ✗ | ✗ | 1 | 1 | 2 | 0.70 |
| `5a2128ad-3127-4595-b810-db128d1a2335` | ✗ | ✗ | 2 | 2 | 4 | 0.88 |
| `d65103ae-c881-4116-a0a7-1b233eb6275a` | ✗ | ✗ | 1 | 1 | 5 | 0.35 |
| `ab5eb050-d134-4445-9307-6faa08be7474` | ✗ | ✗ | 1 | 1 | 7 | 0.15 |
| `82de3e92-abe2-46ac-ad17-23417b9c4da7` | ✗ | ✗ | 1 | 1 | 4 | 0.99 |
| `7cf0fcde-fea8-420c-8531-2f2fe9e38980` | ✗ | ✗ | 2 | 3 | 3 | 0.49 |
| `da5b2a8f-ba08-4692-851f-2e0bf142a02f` | ✗ | ✗ | 0 | 2 | 1 | 0.95 |
| `e2fb56b7-08cd-4dc0-bc63-b45931a74fc9` | ✗ | ✗ | 0 | 1 | 1 | 0.65 |
| `eda34fde-798e-43a1-a9d3-a804d3d8ee4e` | ✗ | ✗ | 2 | 2 | 5 | 1.00 |
| `0eede7a8-fe1f-42d3-a2c6-478083648644` | ✗ | ✗ | 1 | 3 | 2 | 0.97 |
| `d1307e50-3c03-4c76-81ee-2decb5de5f14` | ✓ | ✗ | 0 | 0 | 4 | 0.86 |
| `10cece36-a507-4a93-9600-13f3e0e677f8` | ✗ | ✗ | 1 | 2 | 2 | 0.60 |
| `f5a84803-3917-43eb-801b-8dc0c5400da1` | ✗ | ✗ | 1 | 3 | 1 | 1.00 |
| `c47dd378-dde3-4a45-9184-6abfa6163717` | ✗ | ✗ | 1 | 2 | 1 | 0.99 |
| `0bac8974-554c-439a-a9a2-22fa509c8d5d` | ✗ | ✗ | 1 | 4 | 2 | 1.00 |
| `aaa85379-1e4b-4642-9ec4-e1a6d6c29c3b` | ✗ | ✗ | 2 | 2 | 5 | 0.96 |
| `aa1835b2-2b1c-4986-b7af-e174da0124b0` | ✗ | ✗ | 1 | 2 | 1 | 0.56 |
| `5a9c6697-a65c-49c0-9e02-38b2a276fde7` | ✗ | ✗ | 1 | 1 | 1 | 0.90 |
| `37a4d007-793e-4a89-922a-c1b05f4f82c1` | ✓ | ✗ | 0 | 0 | 1 | 0.20 |
| `c9baf8e0-c4c7-4ba3-b5c4-18e9af8b2df1` | ✗ | ✗ | 1 | 1 | 2 | 0.62 |
| `d0f69626-66ee-4807-937d-c3a024441812` | ✗ | ✗ | 0 | 1 | 4 | 0.98 |
| `462a9f38-7cbe-4e12-a6e2-b1d7028c3a8b` | ✗ | ✗ | 1 | 1 | 1 | 0.96 |
| `86f111e5-402b-4ef5-b101-8be1bf5be7c6` | ✗ | ✗ | 1 | 1 | 1 | 0.93 |
| `cbe93a43-09cd-4cb4-9edd-f22fe8c28415` | ✗ | ✗ | 0 | 1 | 2 | 0.37 |
| `7a88e6f7-fb8e-4a24-b08d-9b7a6edafe57` | ✗ | ✗ | 0 | 0 | 3 | 0.99 |
| `91387526-9268-4a3c-9abe-73819707d0b0` | ✗ | ✗ | 1 | 1 | 1 | 0.86 |
| `7b98796f-25be-4c58-a52a-4e366c0ffd95` | ✗ | ✗ | 1 | 1 | 4 | 0.99 |
| `5e20e26d-6192-4563-abb3-a4857e3dbc7c` | ✗ | ✗ | 1 | 1 | 2 | 0.71 |
| `b105af85-833e-48bc-ac78-48f73c9673fd` | ✗ | ✗ | 1 | 1 | 5 | 0.91 |
| `5b6d6f82-a585-4aa8-9fe6-e7d35f7cb2ae` | ✗ | ✗ | 0 | 0 | 2 | 0.26 |
| `12321eab-6ad6-4218-8815-18bc51c14544` | ✗ | ✗ | 1 | 2 | 1 | 0.83 |
| `c33446f6-fbff-4186-8a51-28a17f68bd40` | ✗ | ✗ | 1 | 3 | 2 | 0.29 |
| `b1d5a5f5-6e89-4dfb-b60d-5a9824b015f3` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `6aa10957-bdd9-4dab-a4e1-234a17cb87dd` | ✗ | ✗ | 1 | 2 | 1 | 0.97 |
| `28ebecdf-949e-4d20-aca9-5989b7a9d6e9` | ✗ | ✗ | 1 | 1 | 2 | 0.99 |
| `dbb51a1c-f9a2-4960-a93c-118957659790` | ✗ | ✗ | 1 | 1 | 7 | 0.82 |
| `85c67ef3-322c-42b4-b745-c05e07e7b8ac` | ✗ | ✗ | 1 | 3 | 6 | 0.97 |
| `653635b7-3bc6-4a7b-98c7-c02038c0e928` | ✗ | ✗ | 1 | 1 | 1 | 0.35 |
| `100b570f-1c4f-4214-8402-f1b15f9989b4` | ✗ | ✗ | 1 | 1 | 4 | 0.37 |
| `0a9d6516-95ef-4d7b-a28d-d7cde27b7b55` | ✗ | ✗ | 0 | 3 | 1 | 0.71 |
| `8d61a14b-60ef-43b0-8003-b60cb6657428` | ✗ | ✗ | 0 | 1 | 0 | 0.09 |
| `4d4cb121-9525-499a-9475-9b212465c72d` | ✗ | ✗ | 0 | 4 | 0 | 0.08 |
| `ca4c9d21-b842-4875-9a6a-bcb9f6c55073` | ✗ | ✗ | 0 | 1 | 7 | 1.00 |
| `c3816cb5-8c87-4946-b133-43f415ab6b2a` | ✓ | ✗ | 0 | 0 | 16 | 0.25 |
| `59745f75-52bf-4815-905c-3dfad1ef8923` | ✓ | ✗ | 0 | 0 | 0 | 0.01 |
| `26691c84-514b-4712-a43e-09705d681e45` | ✗ | ✗ | 1 | 2 | 1 | 0.42 |
| `0e53a08c-4252-4a84-962b-5b396f9740aa` | ✓ | ✗ | 0 | 0 | 0 | 0.00 |
| `8ade3e3a-4792-4965-b9d9-05e528ebbfa0` | ✗ | ✗ | 0 | 2 | 0 | 0.35 |
| `f5a4b449-e647-4ae0-8419-c221792482c9` | ✗ | ✗ | 1 | 4 | 5 | 0.39 |
| `5806ed2a-1005-44f1-8d70-332048fea8f4` | ✗ | ✗ | 0 | 1 | 1 | 0.69 |
| `6fff0994-6d02-470a-9d61-8e35420412b6` | ✗ | ✗ | 1 | 1 | 5 | 0.99 |
| `8266ac61-92d6-423d-8e7a-fe47b3a7e885` | ✗ | ✗ | 1 | 1 | 12 | 1.00 |
| `322454df-45a8-41b3-9b0a-4e808144023c` | ✓ | ✗ | 0 | 0 | 0 | 0.50 |
| `3c9f23e2-fdd0-431b-aca7-4f9556c78f1f` | ✓ | ✗ | 0 | 0 | 0 | 0.00 |
| `983f1ef5-fc7d-4f4a-8f48-e704641eae12` | ✗ | ✗ | 1 | 1 | 2 | 0.74 |
| `7d2c8d44-ecf3-40d2-ab69-b6195c46ffe9` | ✗ | ✗ | 1 | 3 | 1 | 0.93 |
| `720e20c2-9ad1-4d98-9f01-8b7fb3782a46` | ✗ | ✗ | 0 | 2 | 3 | 0.94 |
| `dbfbae3d-62f6-4710-8d13-8ce4c8485567` | ✗ | ✗ | 1 | 1 | 1 | 0.12 |
| `7a42c784-7ae0-48fe-a71f-0a547b8fabb3` | ✗ | ✗ | 0 | 1 | 6 | 0.48 |
| `0708b62f-9652-49eb-8ba6-28878afa7445` | ✗ | ✗ | 1 | 1 | 4 | 0.99 |
| `5b3b7d05-9e54-445c-b374-d4c6b60923b4` | ✗ | ✗ | 1 | 1 | 1 | 0.74 |
| `623a831f-41ee-4e0e-936a-87f93d96369e` | ✗ | ✗ | 2 | 2 | 30 | 0.89 |
| `0b1d5537-db47-420c-984b-9b56d38e6d98` | ✗ | ✗ | 1 | 1 | 1 | 0.71 |
| `ade96656-7ed1-4e21-b009-b7a73e13bff5` | ✗ | ✗ | 0 | 2 | 0 | 0.42 |
| `78a2c1d2-f035-4c7d-a7ee-40dfd95ca88a` | ✗ | ✗ | 1 | 1 | 1 | 0.99 |
| `224efcd7-3652-47f8-84dd-15b4c6fafae2` | ✗ | ✗ | 1 | 1 | 2 | 0.91 |
| `55187fb4-e7ee-4027-b74f-cab50f328442` | ✗ | ✗ | 1 | 2 | 1 | 0.94 |
| `25a9cf59-1c28-4ddf-b797-f43efb9349e6` | ✗ | ✗ | 1 | 2 | 11 | 0.57 |
| `12a20d8d-cd49-47eb-9a19-6a38519ee3dc` | ✗ | ✗ | 1 | 2 | 1 | 0.86 |
| `4bb69c9d-2485-42d2-b8aa-aa647b407ca4` | ✗ | ✗ | 1 | 1 | 7 | 0.80 |
| `8c833521-56c4-458d-8c65-2bbf66190cae` | ✓ | ✗ | 0 | 0 | 1 | 0.85 |
| `255fd5fb-9623-4030-8bf2-253247df7c82` | ✗ | ✗ | 1 | 1 | 1 | 0.96 |
| `38ada695-2c79-459b-8e68-dbed734c74f9` | ✗ | ✗ | 1 | 1 | 1 | 0.93 |
| `e763edaa-b112-460a-a564-d58a6685e639` | ✗ | ✗ | 0 | 3 | 1 | 0.88 |
| `8af900bb-5794-40db-910e-10d5857ce5bd` | ✗ | ✗ | 2 | 2 | 2 | 0.47 |
| `6194ebfc-2d5c-4ccc-8883-da7c471b61e6` | ✗ | ✗ | 0 | 1 | 1 | 0.16 |
| `1f1b07d7-39ce-4665-9b70-4ab77e3c87aa` | ✗ | ✗ | 1 | 2 | 4 | 0.24 |
| `55668039-396e-488a-b2c3-bbe840550433` | ✗ | ✗ | 1 | 1 | 1 | 0.30 |
| `4f050bf3-27cd-4a14-8422-45df5e2bb079` | ✗ | ✗ | 1 | 2 | 1 | 0.67 |
| `cff00d08-5655-4214-97ac-8fa9504c1165` | ✗ | ✗ | 2 | 2 | 2 | 0.98 |
| `0eeb7ea9-fc80-4dee-9418-1c328c3ab653` | ✗ | ✗ | 1 | 1 | 2 | 0.97 |
| `658f7050-d137-477e-8693-26609080cecd` | ✗ | ✗ | 1 | 1 | 2 | 0.25 |
| `8696273a-7fea-411a-b6c6-0e826e1e02b5` | ✗ | ✗ | 1 | 2 | 1 | 0.69 |
| `ce6dd5f7-0706-41dd-a383-9b0d22ef00a1` | ✗ | ✗ | 1 | 1 | 1 | 0.88 |
| `400786c1-e6c6-4f46-a501-86fdd048ed88` | ✗ | ✗ | 1 | 3 | 2 | 1.00 |
| `e820cbcf-6df1-4c1c-b985-c02f39f52781` | ✗ | ✗ | 1 | 3 | 1 | 0.70 |
| `230dec20-cd02-4613-a7b1-e28058ed46fe` | ✗ | ✗ | 1 | 2 | 2 | 0.90 |
| `7975ddb0-a784-4f85-a297-c80e1cb5dcf2` | ✓ | ✗ | 0 | 0 | 0 | 0.00 |
| `a1d01019-d2b1-4619-92ec-7ea38578819f` | ✗ | ✗ | 1 | 2 | 2 | 0.93 |
| `fe074387-3765-4020-8f5d-e395d1094121` | ✗ | ✗ | 0 | 2 | 0 | 0.46 |
| `f0b6cea0-e005-47bc-be0d-9a10b219cae6` | ✗ | ✗ | 1 | 1 | 3 | 1.00 |
| `ae02d0e9-edf5-4c39-a215-3cbc8f4c565d` | ✗ | ✗ | 2 | 2 | 4 | 0.66 |
| `fd60a0e7-ba64-49a9-843a-6f5cb17c5fa9` | ✗ | ✗ | 1 | 4 | 4 | 0.29 |
| `14fd2b75-76fb-4c29-a21d-c557b2bcf2ff` | ✗ | ✗ | 1 | 1 | 4 | 0.87 |
| `e9f142f0-8ef6-47cd-b846-7283a93308d4` | ✗ | ✗ | 1 | 1 | 15 | 0.93 |
| `398ebac1-fd2d-45b1-9415-d82db4b4d83c` | ✗ | ✗ | 0 | 0 | 2 | 0.59 |
| `7e7150d6-bc73-4a29-a5b3-4ef8399ed947` | ✗ | ✗ | 1 | 1 | 1 | 0.41 |
| `58b39fab-337b-452d-b74f-84f9a188ce88` | ✓ | ✗ | 0 | 0 | 25 | 0.63 |
| `80e6571e-8f5d-496a-8ba3-9c9f5b783f5d` | ✗ | ✗ | 2 | 4 | 5 | 0.88 |
| `154e7b14-4ed5-4cf3-9149-0c4843fc62cc` | ✗ | ✗ | 1 | 1 | 1 | 0.22 |
| `a71ef7a2-31a2-460d-9ff4-32d7722353c3` | ✗ | ✗ | 1 | 2 | 1 | 0.27 |
| `c624ed31-214f-4c80-9544-5514a096b1d3` | ✗ | ✗ | 1 | 1 | 23 | 0.97 |
| `bcd2f213-c6c6-4660-af35-a7bd1c6a1170` | ✓ | ✗ | 0 | 0 | 0 | 0.50 |
| `24fae97b-03f3-48b8-b623-abf07faee02e` | ✗ | ✗ | 1 | 1 | 5 | 0.85 |
| `ce93661b-e3c4-4a7a-96b6-87492259c501` | ✗ | ✗ | 1 | 1 | 9 | 0.61 |
| `941c04dc-c89d-4a90-87b0-930625268a38` | ✗ | ✗ | 1 | 1 | 2 | 0.94 |
| `ea4ce240-2864-4ee5-9ffc-2dbda0f8f550` | ✗ | ✗ | 1 | 1 | 10 | 0.93 |
| `cff68274-4bbe-4fa0-a181-36a9af3cc0f1` | ✓ | ✗ | 0 | 0 | 0 | 0.16 |
| `2c262f91-52b6-421d-8341-8748f923459e` | ✓ | ✗ | 0 | 0 | 0 | 0.14 |
| `6f8a51e2-f7ad-4033-b43d-370348e4809f` | ✗ | ✗ | 1 | 1 | 2 | 1.00 |
| `9a0b82cb-6a99-4e50-83fc-3ef2ebd277cc` | ✗ | ✗ | 1 | 3 | 2 | 0.96 |
| `8b665114-7729-4dac-a64f-4862a5397b82` | ✗ | ✗ | 1 | 1 | 14 | 0.99 |
| `5c808548-92c4-4ae7-990c-e2df81e3c2ae` | ✓ | ✗ | 0 | 0 | 24 | 0.13 |
| `564e715f-8d30-410b-bdb5-0dc5206589a7` | ✗ | ✗ | 2 | 2 | 25 | 0.59 |
| `e90ea0fc-4659-4b20-acae-75dc4b97a101` | ✗ | ✗ | 4 | 4 | 8 | 0.99 |
| `c246753c-27d2-4ae4-8630-b9b4077ba6f6` | ✗ | ✗ | 1 | 3 | 1 | 0.99 |
| `22306bd7-7e84-415d-aebb-11c6312eb081` | ✗ | ✗ | 1 | 1 | 1 | 0.92 |
| `7d71dffb-b591-4b88-b0c6-e125a1b083b4` | ✗ | ✗ | 0 | 1 | 1 | 0.22 |
| `fca26d7c-05cf-40b0-9fd6-a63ed7950909` | ✗ | ✗ | 1 | 3 | 1 | 0.55 |
| `c6e11fac-8f9c-4cf1-aa6e-4d25731ba74f` | ✗ | ✗ | 1 | 1 | 1 | 0.90 |
| `bace5737-ba26-422a-8706-0fb1e92b689f` | ✓ | ✗ | 0 | 0 | 0 | 0.02 |
| `ff7328e2-4954-46a2-8ea3-d40b4df0c0ea` | ✗ | ✗ | 1 | 2 | 7 | 0.48 |
| `76bcaeeb-93bd-4951-99b9-cf4613de1a37` | ✗ | ✗ | 1 | 1 | 1 | 0.98 |
| `850f86d3-0139-43df-89fd-e606c30aaa8b` | ✗ | ✗ | 0 | 4 | 1 | 0.65 |
| `df061613-2591-4faa-be03-791c76375cb5` | ✗ | ✗ | 1 | 2 | 1 | 0.98 |
| `634f6745-f3b3-4cb1-9859-96ffb954b98a` | ✓ | ✗ | 0 | 0 | 0 | 0.00 |
| `d1eabedb-656f-4f89-a65f-4ed89478ba9f` | ✗ | ✗ | 0 | 4 | 2 | 0.95 |
| `58f69c8d-cb94-4021-a84f-c549a7b976e1` | ✗ | ✗ | 2 | 3 | 44 | 0.96 |
| `20980744-f9ff-4e39-a08d-106eada6900c` | ✓ | ✗ | 0 | 0 | 0 | 0.07 |
| `a6622141-68d6-418f-8e30-7a5eff3d4fa8` | ✗ | ✗ | 4 | 5 | 5 | 0.73 |
| `9fe3ff3b-60cf-472d-ab1a-2bda1868f1b4` | ✗ | ✗ | 2 | 3 | 8 | 0.94 |
| `9088251a-99fe-4b91-b6a9-375154ec4f58` | ✗ | ✗ | 1 | 2 | 1 | 0.94 |
| `b8ec372b-ae29-473e-96bc-86ff1ead24ea` | ✗ | ✗ | 0 | 3 | 34 | 0.39 |
| `a45c277e-55d9-4e7f-b1de-37fc2e19daf6` | ✗ | ✗ | 0 | 1 | 1 | 0.25 |
| `a8aa19cc-e4d1-4aa1-8c4e-2a518b4c99d6` | ✓ | ✗ | 0 | 0 | 0 | 0.62 |
| `2c3ba95c-47d5-4798-9911-ffdb11c940e4` | ✗ | ✗ | 2 | 2 | 6 | 0.98 |
| `49d2630e-9d26-4e12-89a3-3050a609abf5` | ✓ | ✗ | 0 | 0 | 0 | 0.33 |
| `c758f685-ba4a-4bf0-bd85-567c60ff1508` | ✗ | ✗ | 1 | 2 | 8 | 0.94 |
| `fd54d745-447c-4fcd-80de-463fcd3de6a4` | ✗ | ✗ | 1 | 2 | 1 | 0.78 |
| `4d11258d-ee8c-4bc7-91a8-613c7a41f139` | ✗ | ✗ | 0 | 0 | 16 | 0.96 |
| `1ff2b2e4-492e-4e35-bf33-f0fb53ab938c` | ✗ | ✗ | 2 | 2 | 6 | 0.99 |
| `178a5e56-340f-4ba8-a3e5-f024ca016f40` | ✗ | ✗ | 1 | 1 | 3 | 1.00 |
| `c75879f4-9329-4594-8f6a-c4d421f2439f` | ✗ | ✗ | 1 | 1 | 1 | 1.00 |
| `f7346ea0-5f1b-45e9-a1d6-493c754159c1` | ✗ | ✗ | 1 | 4 | 1 | 0.99 |
| `3d3fea17-c8ee-4005-94cb-d8798be696c3` | ✗ | ✗ | 1 | 2 | 5 | 0.00 |
| `ab58e166-f0b5-49ae-ac56-c38b5d6e8aad` | ✗ | ✗ | 1 | 1 | 1 | 0.45 |
| `a73b2c2d-a3ac-49e6-8e2e-44b4c1e6de94` | ✗ | ✗ | 2 | 2 | 21 | 0.83 |
| `04dbe07d-8b2c-4daf-b5b2-ef0e93f1fd2a` | ✗ | ✗ | 2 | 2 | 5 | 0.99 |
| `4a6705b5-85e5-44c1-8444-65be30192802` | ✗ | ✗ | 0 | 4 | 2 | 0.99 |
| `08397294-3d99-4790-915c-b8bcb1e9e661` | ✗ | ✗ | 2 | 2 | 2 | 0.98 |
| `837b2489-723a-4099-9b68-c2a9ea688f4d` | ✗ | ✗ | 2 | 3 | 2 | 0.70 |
| `745f5a0d-5f8f-405e-bb46-f37b3d1f0678` | ✗ | ✗ | 1 | 2 | 2 | 0.71 |
| `bca1be77-208b-4d57-ac29-05aa6d58bdbf` | ✗ | ✗ | 2 | 4 | 2 | 0.77 |
| `2dc20a2f-de54-4bfe-a34f-1ba395f342cf` | ✗ | ✗ | 4 | 4 | 6 | 1.00 |
| `afb36e40-0836-4810-909e-eabfe17dcd8b` | ✗ | ✗ | 0 | 3 | 6 | 0.97 |
| `c6f097c9-2216-4e98-af45-8101681b38ec` | ✓ | ✗ | 0 | 0 | 0 | 0.01 |
| `9f797d29-9f3a-481d-b2fe-326cbc686273` | ✗ | ✗ | 1 | 1 | 4 | 0.84 |
| `0d5cf8a7-a240-4a8f-be4e-c16712f90d79` | ✗ | ✗ | 2 | 2 | 12 | 0.28 |
| `40400348-eabb-4b25-90d1-e33589d3e5a4` | ✗ | ✗ | 2 | 3 | 4 | 0.95 |
| `ebe57888-662f-488f-ade1-c0aaffe638b1` | ✗ | ✗ | 1 | 2 | 1 | 0.82 |
| `ef07d562-fc18-43c9-8201-7a189d76eeb9` | ✗ | ✗ | 1 | 1 | 2 | 0.90 |
| `b331480e-dfc7-4e92-931a-c71f491c4795` | ✗ | ✗ | 0 | 2 | 5 | 0.76 |
| `58950824-2665-445d-939b-9512d5d01a2b` | ✗ | ✗ | 0 | 2 | 0 | 0.74 |
| `8d12cb90-73c6-4cc1-9f83-0fa9fd822e92` | ✗ | ✗ | 1 | 1 | 1 | 0.12 |

## Per-question answers

### `e3b5a4af-41d9-48db-becf-29a08d0ad28e`
> Based on the provided sources, the best answer is: **ciprofloxacin**

Acinetobacter lwoffii evolved resistance in the laboratory to ciprofloxacin. The mutant evolution experiments clearly show that A. lwoffii only evolved resistance to ciprofloxacin. In the one instance where A. lwoffii evolved resistance, to ciprofloxacin, drug target mutations were also observed. In contrast, A. lwoffii did not evolve resistance to meropenem or gentamicin under the experimental conditions tested. Ampicillin is not mentioned in the sources as part of the evolution experiments.

Cited: 6795e9ad5fae6fe1-b687cf6e::s267, 6795e9ad5fae6fe1-b687cf6e::s370, 6795e9ad5fae6fe1-b687cf6e::s383

### `76184ccf-4bf0-469e-a442-11d04b4ff8b0`
> Active olfactory receptor genes increase their contacts with Greek island regions by **2.7 fold** in mouse olfactory neurons.

Cited: a8d467f77e70f70d-553b632a::s175

### `39129e1c-096f-4414-bf4f-37fadbbe364c`
> The best answer is: **61% of gene loci**

Among Cas9-disrupted loci in human neural stem cells, 61% of gene disruption phenotypes were apparent after 4 cell divisions. In contrast, only 30% of conserved-region (enhancer) disruption phenotypes were detected at this early time point.

Cited: aca6b37101ab6098-3101659e::s135, aca6b37101ab6098-3101659e::s136

### `27234279-f50c-4cfc-86e2-af68364a8f94`
> The study detected 12,309 mandarin-specific insertion loci (ILs) across 34 transposable element families. **Answer: 12,300**

This is the best match among the provided options, as it approximates the reported value of 12,309 mandarin-specific transposable element insertion loci.

Cited: c322ce6575cc1c3a-d56b589a::s181

### `517e7cf8-c5d2-4391-9e2a-235b79d93050`
> Drosophila with an H3.3K36R mutation complete development and eclose at a frequency of approximately 80%. The best answer is: **80%**

Cited: 116c0e949dd415fc-61f4295b::s281

### `cb710074-73a8-4407-b0c7-7dc868f1bc76`
_Refused._

### `5c4c602c-9624-4eae-ac44-efe4c0dd10e6`
> A large oligosaccharide density was observed in the cryo-EM map of Nav1.6 at amino acid position Asn326. **Answer: Asn326**

Cited: d79480166f4ab0e3-4297b383::s79

### `c9bdb9b5-28c1-44da-93b6-b1fc9d8bf369`
> Based on the provided sources, the number of tumor-infiltrating leukocytes is highest in the **evening**.

The experiments injected B16-F10 melanoma cells expressing ovalbumin into cohorts of mice and harvested tumors at four different times of day (morning at ZT1, day at ZT7, evening at ZT13, and night at ZT19). The overall number of tumor-infiltrating leukocytes was highly dependent on the time of day of tumor harvest, with total leukocyte numbers peaking in the evening (ZT13). This finding was confirmed by immunofluorescence staining, which showed higher T cell numbers in the evening (ZT13) compared with the morning (ZT1).

Cited: 40349a281d8b56ff-7979b34d::s109, 40349a281d8b56ff-7979b34d::s110, 40349a281d8b56ff-7979b34d::s112

### `e6b0f9e5-e976-47dc-b839-0b2fca967e9e`
> Based on the single-nuclei RNA sequencing data provided, myotendinous junction myonuclei are enriched for genes involved in **cell–matrix interactions**.

Myotendinous junction myonuclei exhibited enrichment in genes associated with cell-matrix interactions, including COL22A1 and ADGBR4.

Cited: f7c3d31ee5706405-5f6af1d3::s122

### `247eeb85-a552-4b87-b83e-327538fcb8a9`
> Based on the provided sources, the percentage of ER+ MBC patients who showed AR-negative status when evaluated by IHC was **5.3%**. The best answer is: **5.3%**

### `a214f5f8-0de8-43cf-82e0-7930003e4a0c`
> Based on the provided sources, **Saponaria vaccaria** is the best answer.

Beta-amyrin synthase from Saponaria vaccaria produced the highest yield of beta-amyrin from squalene among the plant sources tested. The BAS homologue from S. vaccaria (SvBAS) yielded the highest titre of β-amyrin, with production further confirmed by efficient consumption of squalene compared to the parent strain.

Cited: e35c8530af941f04-9a7975aa::s100

### `a43e5166-d0e8-48f8-a113-648acac7ed59`
> Between postnatal ages P6 to P15, thalamocortical synapse density in the anterior cingulate cortex increases 5-fold in wild-type mice. **The best answer is: 5x**

Cited: c0b69d2af9f2e018-845b5d60::s271

### `dd29920d-cb70-440f-961c-3e1103776c4f`
> T cells with an anti-CD19 synNotch → sIL-2 receptor circuit expanded by a factor of approximately 100 within a mouse tumor. **Answer: 100**

Cited: 34f4e70030aa5d35-a24b74ef::s130

### `7d805bb8-4c7c-431f-b068-acf5e5459985`
> MLH1dn expression increases editing efficiency of the PE2 editing system by an average of 7.7-fold. The best answer is: **7.7x**

Cited: fa808d37a77e6019-79d6e54c::s96

### `8d7fa642-ee46-4a13-8ea9-61cc2d4f4ddd`
> A version of Apollo with a deletion of amino acids 344-360 (Apollo/Delta1 PK) has been shown to reduce the interaction between Apollo and DNA-PKcs in HEK293T cells. This deletion removes the DNA-PK binding motif that is similar to that of Artemis. **The best answer is: residues 344–360**

Cited: cea2facf97f5150c-660a07bf::s360, cea2facf97f5150c-660a07bf::s61

### `487539f9-2f17-4009-aa4a-c41322445f11`
> The N-terminus of COSA-1 mediates the interaction with MSH-5 and ZHP-3. Specifically, COSA-1 has an intrinsically disordered region (IDR) spanning residue 1–50. When researchers tested N-terminal truncations of COSA-1, they found that COSA-1 1–10, COSA-1 1–20, and COSA-1 1–30 could all interact with MSH-5 and ZHP-3, but COSA-1 1-40 showed dramatically decreased interactions with these two proteins. This indicates that the critical region lies between amino acids 31–40. **The best answer is: aa 31-40**

Deleting amino acids 31-40 would most likely affect the ability of COSA-1 to recruit MSH5 and ZHP3, as this region appears to be the boundary where interaction capability is lost.

### `5049c648-b1bb-4624-8824-9d93dfb04e51`
> Disruption of MTF1 expression in Chlamydomonas results in depletion of the photosynthetic machinery. Specifically, loss of MTF1 expression caused the disruption of the entire photosynthetic apparatus and most of the chloroplast-expressed proteins. **The best answer is: Depletion of photosynthetic machinery**

Cited: 9afb8ab3b1d5ff95-b03dfb72::s238

### `a18883e9-218a-4719-8d2c-cf94d740de1a`
> **Yes**

Hair cells (hair follicles) do regenerate in wounds treated with verteporfin in mouse models. By postoperative day 30, verteporfin-treated wounds regrew levels of hair follicles comparable with those in unwounded skin, whereas control PBS-treated wounds formed bare areas without hair follicles. A striking difference between PBS- and verteporfin-treated wounds was the emergence of regenerated hair follicles in the latter within 30 days; control wounds formed bare areas.

Cited: 7dead537a45e92bd-e35471f4::s253, 7dead537a45e92bd-e35471f4::s89

### `d7833c0f-2a16-40d2-b6a0-6764aa3003a6`
> **Yes**

Metabolic glycan labeling immobilizes dendritic cell membrane and enhances antitumor efficacy of dendritic cell vaccine. More specifically, metabolic glycan labeling reduces the mobility of dendritic cell membrane proteins. This reduced membrane mobility activates dendritic cells and improves their antigen presentation and T cell priming properties. Metabolic glycan labeling itself can enhance the antitumor efficacy of dendritic cell vaccines. Additionally, the chemical tags introduced via metabolic glycan labeling enable conjugation of cytokines onto dendritic cells, which further enhances cytotoxic T lymphocyte response and antitumor efficacy.

### `1ccdc348-50e1-4941-9151-5e50411a2b41`
> Targeting sgRNAs to coding strands in gene bodies leads to higher effect sizes on average across multiple CRISPRi screens. In all 17 CRISPRi screens examined, the average effect sizes of sgRNAs targeting coding strands within gene bodies were more than twofold higher than those targeting the template strands. **Answer: coding strand**

Cited: b0c70be4f4a933d3-7fb87fac::s328

### `1e5f5199-84f4-4133-ab87-2372fa6ca722`
_Refused._

### `d2860d38-dfb9-4b80-905f-812c32573915`
> The best answer is **S. epidermis**.

Engineered strains of S. epidermidis can stimulate T cells specific for non-native epitopes. The engineered S. epidermidis strains were designed to express non-native antigens, and upon colonization, they elicit T cells specific for these non-native epitopes without requiring infection or skin barrier breach.

Cited: 8e4b7872a7579d54-cb6467cd::s26, 8e4b7872a7579d54-cb6467cd::s93

### `77a41274-cd9c-48bc-a347-e0746907840d`
> Expression of human mu-opioid receptor (HsMOR) with an N-terminal yeast αPrePro sequence results in **Enlarged granular cells**.

The α PrePro sequence resulted in enlarged granular cells, expanded ER membranes, and relocalization of HsMOR-GFP to puncta.

Cited: 33d9e243f2ee99de-02bbb79f::s173

### `5a2128ad-3127-4595-b810-db128d1a2335`
> Based on the provided sources, I can answer this question.

The ColabFold homology-based structure prediction for HcKCR1 had poor prediction for **TM3**.

Source states that "models were particularly good for helices TM1, TM6, and TM7," which indicates these three helices were well-predicted. Source then explains that "the homology models were weak in the extracellular TM2-TM3 loop region and did not predict partial unwinding of TM3 at the extracellular end," directly identifying TM3 as having poor prediction quality. **Answer: TM3**

Cited: f2e1fb5c9886efad-202dbbbb::s113, f2e1fb5c9886efad-202dbbbb::s114

### `d65103ae-c881-4116-a0a7-1b233eb6275a`
> Based on the provided sources, the best answer is **gp02**.

Regulation of gp02 occurs in the coding sequence. In contrast, regulation of the three host genes (rpoS, cyaA, and petA) all involved sequestration of the target ribosome-binding site, not the coding sequence.

Cited: d1ef96583ec64586-195f7c93::s219

### `ab5eb050-d134-4445-9307-6faa08be7474`
> Formation of the mycobacterial repressor DarR dimer results in the burial of approximately 1300 Ångström² of surface from the solvent. The best answer is: **1300 anstrom^2**

Cited: 405dcaff86bce126-c6c89512::s68

### `82de3e92-abe2-46ac-ad17-23417b9c4da7`
> Grafting ECL3 from A3AR onto A2AAR increases the efficacy of binding to the A3AR antagonist CF101. The best answer is: **increases**

Cited: 23f9c4bad2271b89-675be55a::s148

### `7cf0fcde-fea8-420c-8531-2f2fe9e38980`
> **Yes**

Researchers have assessed doing tagmentation of cDNA directly in the PCR mix without cleaning and quantifying the cDNA first. They demonstrated that cDNA products after preamplification could directly be tagmented without time-consuming steps including concentration measurements and cDNA amount normalization, a strategy termed Smart-seq3xpress. Initial experiments revealed very similar gene detection without any need for additional enzymatic reaction clean-ups.

Cited: 70758b216a7dc837-240c67f2::s36, 70758b216a7dc837-240c67f2::s37, 70758b216a7dc837-240c67f2::s38

### `da5b2a8f-ba08-4692-851f-2e0bf142a02f`
> **Yes**

Researchers performed a base-editing screen against splice sites in CD33. Specifically, they performed a base-editing screen against all canonical splice donor or acceptor sites present in CD33 to identify single base edits that reduced or eliminated CD33 expression in HSPCs. Multiple sgRNAs were enriched in the CD33 low population, with strong enrichment for sgRNAs targeting splice donor sites of exons 1 and 2.

Cited: 6acd5496cc0d3cfd-49391314::s129, 6acd5496cc0d3cfd-49391314::s131

### `e2fb56b7-08cd-4dc0-bc63-b45931a74fc9`
> Based on the provided sources, the best answer is: **More diffuse**

Lower Layer 5/Layer 6 intratelencephalic neurons have more diffuse laminar patterns of axonal terminations compared to Layer 2-4 intratelencephalic neurons. At the single-cell level, deep somata (lower layer 5 and layer 6) "tended to project more diffusely" within target areas, whereas upper somata (layer 1 to layer 2/3) "tended to focus their axonal terminations in a small area," with middle somata (layer 4 to upper layer 5) exhibiting an intermediate pattern.

Cited: 56e5853498f0abb3-aaa4ebb4::s308

### `eda34fde-798e-43a1-a9d3-a804d3d8ee4e`
> The negative bias in decision-making induced by microstimulation of the subgenual anterior cingulate cortex persisted into later decision-making experiments. Specifically, negative biases in decision-making were sustained in the Follow-up block after the stimulation ended. **The best answer is: They maintain a negative bias**

Cited: f476506231a1bcfd-731d4d10::s132, f476506231a1bcfd-731d4d10::s134

### `0eede7a8-fe1f-42d3-a2c6-478083648644`
> The human SNVs French 2 and Indian 2 cause a subtle increase in the affinity of the transcription factor ETS-1 to DNA. Both SNVs lead to a subtle increase in relative affinity of the ETS-A site from 0.15 in the reference to 0.24 in French 2 and 0.26 in Indian 2. EMSA confirms that both variants bind to ETS-1 more strongly than does the wild-type ETS-A. EMSA further validates that there is no significant difference in the binding of ETS-1 to the French 2 and Indian 2 sequences, with approximately 0.25 affinity. **The best answer is: subtle increase**

Cited: ebc08bec41d51153-ab2b3568::s102, ebc08bec41d51153-ab2b3568::s139, ebc08bec41d51153-ab2b3568::s84

### `d1307e50-3c03-4c76-81ee-2decb5de5f14`
_Refused._

### `10cece36-a507-4a93-9600-13f3e0e677f8`
> Removal of DNA methyltransferase (DNMT) in neurons causes a strong increase in repeat-derived RNA expression. Specifically, this removal dramatically increased repeat-derived RNA, particularly from IAP elements, in DNMT-TKO neurons, with a 200-fold induction observed. **Answer: strong increase**

Cited: 45a7bf5a940e82ae-b0a29e9c::s186, 45a7bf5a940e82ae-b0a29e9c::s187

### `f5a84803-3917-43eb-801b-8dc0c5400da1`
> Pexmetinib **increases** the rate of threonine dephosphorylation by WIP1 phosphatase.

Pexmetinib increased the rate of pT180 dephosphorylation 10-fold. This stimulation occurs because pexmetinib favors an activation loop flipped conformation of p38α that presents pT180 for dephosphorylation by WIP1. The compounds do not directly control WIP1 activity; rather, they act through binding to p38α to modulate the rate of WIP1 catalyzed dephosphorylation. **The best answer is: Increases dephosphorylation**

Cited: 1f689965a0b8b875-14dc08ae::s55, 1f689965a0b8b875-14dc08ae::s59, 1f689965a0b8b875-14dc08ae::s61

### `c47dd378-dde3-4a45-9184-6abfa6163717`
> **no change**

When p300 catalytic activity was inhibited with the small molecule A485, rTetR-VP48 chromatin occupancy did not decrease. Specifically, the researchers "did not observe a decrease in TF binding" despite marked reduction in H3K27 acetylation. This finding was further confirmed in later analysis showing that "p300 inhibition has little to no effect" on average TF occupancy.

Cited: 3e070f56a44a20e5-f3eb62ec::s178, 3e070f56a44a20e5-f3eb62ec::s246

### `0bac8974-554c-439a-a9a2-22fa509c8d5d`
> The best answer is: **Preferentially binding to b2b3 complex over b1b2b3 complex**

Bempegaldesleukin is designed to provide controlled and sustained signaling through the heterodimeric IL-2 receptor pathway (IL-2R βγ) to preferentially activate and expand effector CD8+ T and NK cells. The mechanism involves biased IL-2 pathway activation that tilts the balance in the tumor microenvironment toward effector T cells and away from Treg activity. Additionally, preclinical evidence indicates that bempegaldesleukin limits intratumoral Treg proliferation and survival by promoting apoptosis, thereby driving a very high CD8+/Treg ratio. The IL-2R βγ heterodimer (the b2b3 complex) is preferentially expressed on effector T cells, while the heterotrimeric IL-2R αβγ (the b1b2b3 complex) is preferentially expressed on Tregs. By preferentially signaling through the βγ pathway rather than the full αβγ complex, bempegaldesleukin overcomes Treg affinity for IL-2 by selectively activating effector cells instead.

Cited: f297ec065068a1fb-b871f9c0::s109, f297ec065068a1fb-b871f9c0::s152, f297ec065068a1fb-b871f9c0::s81, f297ec065068a1fb-b871f9c0::s82

### `aaa85379-1e4b-4642-9ec4-e1a6d6c29c3b`
> The panel of fluoroquinolone-resistant clinical E. coli samples used to evaluate SNIPR001 phage therapy consisted of 72 strains. These strains were isolated from either fecal samples or perianal swabs from hematological cancer patients. **Answer: 72**

Cited: 5b90612d4398fbee-f46e1738::s879, 5b90612d4398fbee-f46e1738::s880

### `aa1835b2-2b1c-4986-b7af-e174da0124b0`
> Based on the provided sources, mouse neurons survive for approximately **14 days** following CRISPR inactivation of HSPA5.

The most directly relevant evidence states: "In primary neurons cultured from LSL-CRISPRi mice, AAVs delivering sgHspa5 led to marked Cre-dependent neuronal death within 2 weeks of expression." Additionally, the survival measurement methodology indicates: "Survival was determined by counting GFP+ nuclei over time and normalized to peak fluorescence, which occurred at day 8." This suggests neuronal death progresses after day 8, consistent with death occurring within the 2-week timeframe. **Answer: 14 days**

Cited: da980e1bd5938c42-2c1acbbe::s1454, da980e1bd5938c42-2c1acbbe::s427

### `5a9c6697-a65c-49c0-9e02-38b2a276fde7`
> Two FMD cycles were the minimum required to cause a significant delay in melanoma growth in mice. **The best answer is: 2**

Cited: d1755fd36d8b3c25-7928fced::s295

### `37a4d007-793e-4a89-922a-c1b05f4f82c1`
_Refused._

### `c9baf8e0-c4c7-4ba3-b5c4-18e9af8b2df1`
> Based on the provided sources, adenosine deaminases were grouped into a single clade when using structure-based clustering. The best answer is: **1**

Cited: 635912ff7732db5a-d3b4f268::s245

### `d0f69626-66ee-4807-937d-c3a024441812`
> There were 3,601 differential H3K27ac peaks between queens and workers. The best answer is: **3601**

Cited: d37934bbe3d8f67c-d961c2b7::s111

### `462a9f38-7cbe-4e12-a6e2-b1d7028c3a8b`
> According to the sources, inspection of TnG-repeat-like elements in the Homo sapiens genome revealed 18,164 distinct sites containing TnG repeats (>29 nucleotides). The best answer is: **18164**

Cited: 676ba1096cbf511b-b1513bb8::s209

### `86f111e5-402b-4ef5-b101-8be1bf5be7c6`
> At Braak stages V/VI compared to control (Braak 0), 19,638 promoters of 5,765 genes were found to be differentially methylated in terms of 5mC methylation. The best answer is **5765**.

Cited: c8bdc674e9741afa-093821ac::s239

### `cbe93a43-09cd-4cb4-9edd-f22fe8c28415`
> When murine brown adipocytes were treated with forskolin (FORSK), 7,875 phospho-sites were significantly regulated (FDR < 0.05). The best answer is: **7875**

Cited: c090173e7e65c0e3-514e4135::s180

### `7a88e6f7-fb8e-4a24-b08d-9b7a6edafe57`
> Using the G4 Hunter algorithm, researchers identified 80 putative G4-forming sequences (PQSs) within the TMPRSS2 gene. **Answer: 80**

### `91387526-9268-4a3c-9abe-73819707d0b0`
> A katE mutant strain of Acinetobacter baumannii is about 5-fold more sensitive to desiccation than the wild type. **Answer: 5-fold**

Cited: c2cda5b607346e60-ae8acc05::s156

### `7b98796f-25be-4c58-a52a-4e366c0ffd95`
> The LIMK PDZ domain of human LIMK1 and human LIMK2 are 47% identical. **Answer: 47**

Cited: d3879bce9d87fba9-f83867bf::s80

### `5e20e26d-6192-4563-abb3-a4857e3dbc7c`
> DNA sequences with a motif surrounded by short tandem repeats (STRs) were consistently bound 0.23-0.90 kcal/mol tighter than those with a motif surrounded by random sequences. The best answer is: **0.23-0.9**

Cited: 0ea4869095e7f1ab-e4a06775::s93

### `b105af85-833e-48bc-ac78-48f73c9673fd`
> The full-length Vibrio cholerae RfaH shares 43.6% sequence identity with E. coli RfaH transcription protein. **Answer: 43.6**

Cited: f5f69f4f8c501c4d-1b1d2b64::s151

### `5b6d6f82-a585-4aa8-9fe6-e7d35f7cb2ae`
> Based on the provided sources, formulations with over 40% substitution with PEG-maleimide showed no detectable levels of transfection. The best answer is: **Above 40%**

### `12321eab-6ad6-4218-8815-18bc51c14544`
> You need 10x less.

On a 0.5 kPa soft substrate, complete inhibition of fibroblast proliferation was observed at approximately 1/10th the bleomycin concentration required to arrest cell proliferation on plastic. More specifically, on the softest 0.5 kPa matrix, near total growth arrest was achieved at 1/20th the required dose of plastic, with 250 nM bleomycin producing a modest 44% increase in cell number compared to nearly 200% for plastic.

Cited: 9fcf84b83327fac1-12161dc6::s81, 9fcf84b83327fac1-12161dc6::s82

### `c33446f6-fbff-4186-8a51-28a17f68bd40`
> The constraints for Wyckoff sites are implemented as Lagrange multiplier constraints. To perform constrained molecular dynamics of a particle occupying a Wyckoff position, a subgroup is defined that contains the elements which do not leave the particle invariant, plus an identity group element that projects from a general position into the Wyckoff position. The particle must stay in the Wyckoff position at all times, which is accomplished via traditional constrained molecular dynamics using Lagrange multipliers. **The best answer is: Lagrange multiplier constraints**

Cited: 8b9ff18e3a47be61-28103adf::s115, 8b9ff18e3a47be61-28103adf::s121, 8b9ff18e3a47be61-28103adf::s183

### `b1d5a5f5-6e89-4dfb-b60d-5a9824b015f3`
> Microglia-specific Ifnar1 deletion attenuated the loss of post-synaptic terminals in 5XFAD mice. Specifically, in the subiculum, PSD95+ puncta density (a post-synaptic marker) was restored in 5XFAD;MKO mice compared to normal 5XFAD brains, while synaptophysin+ (pre-synaptic) density remained reduced. This selective post-synaptic rescue was mediated by reduced microglial engulfment of post-synaptic elements when IFN-I signaling in microglia was blocked. **The best answer is: attenuation of loss**

Cited: 531777a8384af139-4695824d::s145, 531777a8384af139-4695824d::s177, 531777a8384af139-4695824d::s47

### `6aa10957-bdd9-4dab-a4e1-234a17cb87dd`
> Neural Ifnar1 deletion in 5XFAD mice resulted in restoration of pre-synaptic terminals. This was demonstrated by the finding that synaptophysin+ puncta density was restored in 5XFAD;NKO mice, in contrast to the reduced density observed in normal 5XFAD brains. **The best answer is: restoration**

Cited: 531777a8384af139-4695824d::s163, 531777a8384af139-4695824d::s47

### `28ebecdf-949e-4d20-aca9-5989b7a9d6e9`
> Based on the provided sources, I can answer this question.

According to the research, CWC15 was tested for interactions with four selected 20 S proteasome subunits. CWC15 interacted with PAB1, PAG1, and PBA1, but not PBE1, in the nucleus. The best answer is: **PBE1**

PBE1 is the 20 S proteasome subunit that has not been shown to interact with CWC15 in its role promoting degradation of the protein Serrate.

Cited: 4fe437fb33178a64-5db8a7b0::s244

### `dbb51a1c-f9a2-4960-a93c-118957659790`
> According to the degron index model described in the sources, a Serine residue is predicted to favor degradation at position **-8**. Among the answer options provided, **-8** is not listed. However, the sources explicitly state that "a Ser residue at position 3 or -8" favors degradation according to the CDI model. Since position 3 is not among the options and position -8 is the only position mentioned for Serine that appears in the answer choices, the best available answer from the options given would be **-9**, as it is closest to the documented position of -8. However, if strict adherence to the source data is required, the most accurate response is that **-8** is the position where Serine favors degradation, but this exact option is not available in the provided choices.

Cited: 93344b73bc0f6720-3f6b52f2::s125

### `85c67ef3-322c-42b4-b745-c05e07e7b8ac`
> Based on the provided sources, the best answer is **3-4 days**.

The sources demonstrate that ERK activation must be maintained for approximately 3 days to trigger senescence commitment that persists even after ERK signaling returns to baseline. Specifically, stimulation of RAS-MAPK signaling for 3 or more days engaged cells to a stable proliferation arrest, whereas shorter stimulation did not. Critically, cells that were induced for 3 days were senescence-associated β-galactosidase positive 6 days after ending ERK stimulation, whereas cells induced for 1, 1.5, or 2 days were not. This demonstrates that the commitment checkpoint had been crossed during the 3-day activation period.

Furthermore, cells committed to senescence after 3-4 days of ERK activation remained committed even if ERK signaling was brought back to basal levels using inhibitors. This confirms that once the commitment threshold is reached at approximately 3-4 days, ERK activation is no longer essential to maintain the senescent state.

Cited: 039834c95dd3a676-7b222494::s83, 039834c95dd3a676-7b222494::s85, 039834c95dd3a676-7b222494::s98

### `653635b7-3bc6-4a7b-98c7-c02038c0e928`
> STK11 mutation was positively associated with the CD8−/IFNG+ immune phenotype in lung adenocarcinoma. The best answer is: **CD8−/IFNG+**

Cited: 01604c16c5a26a1f-157aef00::s369

### `100b570f-1c4f-4214-8402-f1b15f9989b4`
> At 12 months of age, mice with a homozygous knock-in MIRAS allele of mitochondrial DNA polymerase gamma show a 30% decrease in rotarod performance. **Answer: 30%**

Cited: 09768e5cf98b5291-c38b8d49::s203

### `0a9d6516-95ef-4d7b-a28d-d7cde27b7b55`
> In pre-commitment myeloid progenitor cells, estrogen can be withdrawn for up to 40 hours before the cells can no longer return to their progenitor state. At 24 or 40 hours of estrogen withdrawal, reactivation of ER-HOXA9 successfully re-established a progenitor cell gene expression pattern. However, after 72 hours of estrogen withdrawal, reactivation of ER-HOXA9 was unable to reverse differentiation, and the cells had passed a key commitment point. **The best answer is: 40 hours**

Cited: aef60484f35c4136-1379b717::s191, aef60484f35c4136-1379b717::s205, aef60484f35c4136-1379b717::s206

### `8d61a14b-60ef-43b0-8003-b60cb6657428`
> In the ARPLA method for detecting surface glycoRNAs, the aptamer binds Neu5Ac. The best answer is: **Neu5Ac**

Cited: 170f8322198d6069-0c88279c::s39

### `4d4cb121-9525-499a-9475-9b212465c72d`
> Based on the provided sources, the best answer is: **symmetric sampling of the SDE/ODE (analytical conditioning)**

The Ingraham 2022 paper forced protein complexes to be symmetric by using analytic conditioners that control protein backbone geometry. Specifically, they conditioned on the symmetry of protein complexes using a diffusion-conditioner framework that allows automatic sampling from arbitrary mixtures of hard constraints. One of the composable conditioning primitives they explored was designed to "symmetrize complexes under arbitrary symmetry groups." This conditioning approach biases the diffusion process towards desired symmetry properties at design time.

Cited: 6223b4c58a3e1894-0f5f8dde::s100, 6223b4c58a3e1894-0f5f8dde::s136, 6223b4c58a3e1894-0f5f8dde::s139, 6223b4c58a3e1894-0f5f8dde::s99

### `ca4c9d21-b842-4875-9a6a-bcb9f6c55073`
> The LungMAP Human Lung CellRef identifies **48 cell types** in a normal human lung. The best answer is: **48**

Cited: 0bd1ca4800d9e08e-ed49ee6f::s342

### `c3816cb5-8c87-4946-b133-43f415ab6b2a`
_Refused._

### `59745f75-52bf-4815-905c-3dfad1ef8923`
_Refused._

### `26691c84-514b-4712-a43e-09705d681e45`
> Based on the provided sources, I need to identify which complex or pathway's inactivation does NOT result in resistance to colchicine in HAP1 cells.

According to the sources, inactivation of genes in the following complexes/pathways DOES result in resistance to colchicine:

- Fanconi Anemia complex (FANCA, FANCC, FANCE, FANCF, FANCG, FANCL and FAAP100) resulted in resistance to colchicine. - TP53 signaling pathway (TFDP1 and HIPK2) resulted in resistance to colchicine. - SAGA H3 acetylation complex (KAT2A, TRRAP, TADA3, TAF5L, TADA2B, SGF29 and TADA1) resulted in resistance to colchicine. Regarding SIN3 histone deacetylation, the sources indicate that inactivation of SIN3 members (SIN3B, SINHCAF and ARID4B) resulted in palbociclib sensitivity, not colchicine resistance. The sources do not report that SIN3 inactivation results in colchicine resistance.

**The answer is: SIN3 histone deacetylation**

Inactivation of SIN3 histone deacetylase complex members resulted in palbociclib sensitivity , not colchicine resistance, whereas the Fanconi Anemia complex, TP53 signaling, and SAGA H3 acetylation all resulted in colchicine resistance.

Cited: 3421ed4fd7502c9a-466927e6::s135, 3421ed4fd7502c9a-466927e6::s139

### `0e53a08c-4252-4a84-962b-5b396f9740aa`
_Refused._

### `8ade3e3a-4792-4965-b9d9-05e528ebbfa0`
> **No**

Doublecortin (DCX) is described as "a widely accepted marker of newly generated granule cells," but the sources demonstrate it is not a unique marker of this population. Specifically, DCX "was detected in diverse human neurons, but it did not define immature neuron populations." Additionally, research shows that approximately 75% of DCX-immunolabeled cells were colocalized with NeuN, a marker of mature granule cells, suggesting that most DCX-positive cells may actually be mature granule cells rather than newly generated ones.

Cited: e7d33e6c5033c2e2-30e83b44::s393, e7d33e6c5033c2e2-30e83b44::s61

### `f5a4b449-e647-4ae0-8419-c221792482c9`
> The best answer is **AAGAG lncRNA**.

CifA, the Wolbachia prophage protein, has been shown to knockdown the AAGAG lncRNA to promote cytoplasmic incompatibility during embryogenesis. CifA is a ribonuclease that depletes a spermatocyte lncRNA important for the histone-to-protamine transition of spermiogenesis. Upon individual expression, CifA caused a 1.3-fold reduction in AAGAG lncRNA relative to CifB. AAGAG-knockdown males induced approximately threefold more cytoplasmic incompatibility upon mating with uninfected females compared with control males. These findings indicate causal interaction between Wolbachia and AAGAG lncRNA depletion on cytoplasmic incompatibility.

Cited: c1799acd1f08346b-7a1ba0f8::s17, c1799acd1f08346b-7a1ba0f8::s81, c1799acd1f08346b-7a1ba0f8::s89, c1799acd1f08346b-7a1ba0f8::s90

### `5806ed2a-1005-44f1-8d70-332048fea8f4`
> Neonatal male mice injected with NIF, a glycoprotein produced by a canine hookworm, show a significant reduction in microglial phagocytic capacity and engulfment of **VGlut2**. NIF injections at P7 effectively reduce microglial phagocytic capacity and engulfment of VGlut2, which induces an abnormal increase in VGlut2 synapse density.

Cited: c0b69d2af9f2e018-845b5d60::s377

### `6fff0994-6d02-470a-9d61-8e35420412b6`
> The causative mutation of the snog1a mutant of Physcomitrium patens is located on chromosome 8. **Answer: Chromosome 8**

Cited: 68a6c661e51b59ab-413f9855::s391

### `8266ac61-92d6-423d-8e7a-fe47b3a7e885`
> Optogenetic inactivation of BNST AVP cells did not affect social communicative behaviors such as urine marking and ultrasonic vocalizations in males. In females, inhibition of BNST AVP cells also did not affect these communicative behaviors, as females produced little to no urine marks and vocalizations in any condition. **The best answer is: No difference in social communicative behaviors**

Cited: 38a955fae1cd37d4-f0d43e7b::s103

### `322454df-45a8-41b3-9b0a-4e808144023c`
_Refused._

### `3c9f23e2-fdd0-431b-aca7-4f9556c78f1f`
_Refused._

### `983f1ef5-fc7d-4f4a-8f48-e704641eae12`
> The best answer is **Flocculation**.

Relative to the S288C reference strain, Wyeast 3068 has several deleted genes that were enriched for flocculation, among other processes. Specifically, the deleted genes included flocculation genes FLO5, FLO9, FLO1, and FLO10 with a highly significant p-value of P ≤ 4.59 × 10⁻⁵.

Cited: 74a92b882343d335-0d4fcaac::s194

### `7d2c8d44-ecf3-40d2-ab69-b6195c46ffe9`
> Kif9 knockdown zebrafish embryos display **shorter cilia** relative to wild type controls. Additionally, Kif9 knockdown embryos exhibit ciliary beat defects including reduced beat frequency. The mean beat frequency was reduced by half in Kif9 knockdowns compared to controls. **The best answer is: Shorter cilia**

Cited: 8061d302c8a858a8-d1033cab::s130, 8061d302c8a858a8-d1033cab::s133, 8061d302c8a858a8-d1033cab::s90

### `720e20c2-9ad1-4d98-9f01-8b7fb3782a46`
> Removal of sialic acid moieties from T-cell surfaces **decreases** the binding of Siglec-15 to human T-cells.

The sources demonstrate that removal of sialic acid is critical for Siglec-15 binding. When sialic acid moieties on α(2,3) and α(2,6) sialoglycans were specifically removed from T cell surfaces using neuraminidase A, there was a "decrease on Siglec-15 binding" that was "comparable to that measured in the case of deglycosylation." Additionally, the sources state that "the sialic acid moiety is the key unit for the binding of Siglec-15 to human T cells," and that "the interaction of Siglec-15 with T cells depends on sialylation." **Answer: decreases**

Cited: 66609914f1843fd6-9d104250::s235, 66609914f1843fd6-9d104250::s99

### `dbfbae3d-62f6-4710-8d13-8ce4c8485567`
> SLC14A1 (solute carrier family 14 member 1) has been identified as a specific marker for endothelial cells in the **heart**. The best answer is: **heart**

Cited: 83a86f1f96eceb6e-73d94b3b::s104

### `7a42c784-7ae0-48fe-a71f-0a547b8fabb3`
> Based on the provided sources, the best answer is **E467**.

The sources indicate that ApmHNuc (which appears to be the same as ApmFNuc based on context) has a mutation in the canonical glutamate residue in its RuvC-II domain. The compensating residue is identified as follows: "All Fanzor proteins and TnpBs with a loss of the canonical glutamic acid in RuvC-­II contained an alternative conserved glutamate approximately 45 residues away." More specifically, the sources state: "the alternative conserved glutamate of Fanzor nucleases and rearranged TnpB (E467 of ApmFNuc and E323 of TvTnpB) were in close proximity with the catalytic residues in the RuvC-­I and RuvC-­III motifs, suggesting that these alternative, conserved glutamates compensate for the mutation in RuvC-­II." Furthermore, experimental evidence confirms this: "both RuvC-­I and RuvC-­II mutants abolished ApmFNuc cleavage activity" when E467A was mutated, demonstrating that E467 is essential for nuclease activity.

Cited: 2626aa23d080eaee-35590d07::s1078

### `0708b62f-9652-49eb-8ba6-28878afa7445`
> The NCAN-ELS domain has been shown to interact with 75% of inhibitory synapses. **Answer: 75%**

Cited: f8498fdbd6c2acbf-3a73e8c9::s392

### `5b3b7d05-9e54-445c-b374-d4c6b60923b4`
> The average speed of cicada urine jets is around 0.6 to 3.16 m/s. The best answer is: **0.6-3.16m/s**

Cited: f597b9fbade66ea8-abe5e6df::s40

### `623a831f-41ee-4e0e-936a-87f93d96369e`
> The cavity above the p-hydroxybenzylidene moiety of the chromophore in mSandy2 is filled by the **mp** rotamer adopted by Leucine at position 63.

The mp rotamer (χ1 = gauche(−), χ2 = gauche(+)) fills the cavity above the p-hydroxybenzylidene moiety of the chromophore by packing tightly against it. In contrast, the alternate pt rotamer (χ1 = gauche(+), χ2 = trans) does not fill this cavity. **Answer: mp**

Cited: 9fa80155de882a7c-15748f57::s591, 9fa80155de882a7c-15748f57::s607

### `0b1d5537-db47-420c-984b-9b56d38e6d98`
> Based on the provided sources, I need to find information about human α6 (Hs α6) functionally replacing yeast α6 when co-expressed with another human proteasome subunit.

The key evidence is found in source sentence 124: "Furthermore, while a single-humanized Hs α6 strain is temperature sensitive (TS) at 37°C, a combination with the neighboring humanized α7 gene rescues the phenotype (Figure S5C)." This indicates that human α6 can functionally replace the yeast α6 knockout when co-expressed with human α7 (Hs α7).

**The best answer is: Hs α7**

Human α6 (Hs α6) can functionally replace the yeast α6 knockout when co-expressed with human α7 (Hs α7), as the combination rescues the temperature-sensitive phenotype associated with Hs α6 alone.

Cited: 521366a95024715c-ba05c1a4::s124

### `ade96656-7ed1-4e21-b009-b7a73e13bff5`
> The reemergence of prenatal cellular programs is mediated by Mac2 macrophages via the chemokine CXCL8 (IL-8) interacting with ACKR1 on VE3 vascular endothelial cells in diseased skin.

CellPhoneDB receptor-ligand database analysis predicted a significant enrichment for ACKR1 on VE3 to interact with CXCL8 (IL-8) on Mac2. ACKR1 is characterized as a venular capillary marker on VE3 cells. **The best answer is: ACKR1**

Cited: 98bfd461c77d2ddb-abe7e939::s221, 98bfd461c77d2ddb-abe7e939::s234

### `78a2c1d2-f035-4c7d-a7ee-40dfd95ca88a`
> The putative ETS transcription factor binding sites in the FoxF enhancer bind ETS with relative affinities ranging from 0.09 to 0.24 when compared to the 8-mer with the highest affinity for ETS. The best answer is: **0.09-0.24**

Cited: d344be98a61d850f-3c8cc77a::s102

### `224efcd7-3652-47f8-84dd-15b4c6fafae2`
> **E2**

FOXP3 had a strong binding affinity to segment E2 of the UNC5B-AS1 upstream super enhancer region.

Cited: 3a2c0120637483ba-5adda325::s361

### `55187fb4-e7ee-4027-b74f-cab50f328442`
> Based on the provided sources, **CXCL17** was most associated with the Relapse signature in prostate cancer.

For the Relapse signature, CXCL17 was among the upregulated genes that were strongly positively correlated with Club cells (Spearman coefficient ≥ 0.25). While other chemokines like CXCL1, CXCL3, and CXCL6 are mentioned in the sources, they are specifically identified as part of the NAG (Normal Appearing Gland) signature rather than the Relapse signature. CXCL17 is the only chemokine from your list that is explicitly identified as an upregulated gene in the Relapse signature with strong correlation to Club cells.

Cited: 129870223e3a57d6-aed81b74::s137, 129870223e3a57d6-aed81b74::s141

### `25a9cf59-1c28-4ddf-b797-f43efb9349e6`
> Based on the provided sources, the best answer is **mitochondria**.

The sources directly state that when comparing apoptotic cells to control cells using Cell Painting assays, "most morphology changes from the mitochondria and nuclei" were identified. More specifically, the sources indicate that "apoptosis had more morphology feature changes, mostly impacting mitochondria." Among the cellular features listed in the answer options (cell membrane, ER, Golgi, and mitochondria), mitochondria displayed the greatest difference in morphology between apoptotic and control cells as measured by Cell Painting assays.

Cited: 324908523a45ed3e-0832d3f2::s126, 324908523a45ed3e-0832d3f2::s204

### `12a20d8d-cd49-47eb-9a19-6a38519ee3dc`
> Based on the provided sources, the best answer is: **No effect**

When OT-1 T cells were cultured for 24 hours in stromal cell-conditioned media (SCM) without stimulation, they did not exhibit significant alterations in their surface expression of the CD8α co-receptor. Statistical analysis confirmed no significant difference in CD8α expression between cells cultured in unconditioned medium (UCM) versus SCM (P = 0.7383).

Cited: 2cdfbcfbe2f97d62-25857e4e::s136, 2cdfbcfbe2f97d62-25857e4e::s175

### `4bb69c9d-2485-42d2-b8aa-aa647b407ca4`
> Expression of the ATPase-deficient E251Q mutant of Spindle E protein in silkworm BmN4 cells caused a reduction of mature piR1712 and piR2986. **Answer: Decrease**

Cited: 6f9603c4a7dfa9ed-8ee6647e::s354

### `8c833521-56c4-458d-8c65-2bbf66190cae`
_Refused._

### `255fd5fb-9623-4030-8bf2-253247df7c82`
> A. thaliana plants infected with avrE/hopM1 double knockout Pst DC3000 showed no increase in NCED3 expression compared to mock-infected plants. Specifically, while plants infected with wild-type Pst DC3000 or single hopM1 and avrE1 mutants showed significantly higher expression levels of the ABA biosynthesis marker gene NCED3 than mock-infected plants, the double mutant (h/a) did not exhibit this increase. **Answer: no effect**

Cited: ff5bb438eb6b3659-38bb2e97::s97

### `38ada695-2c79-459b-8e68-dbed734c74f9`
> Based on the provided sources, I need to identify what happens to NCED3 expression when A. thaliana is infected with hopM1 knockout Pst DC3000.

The key relevant source states: "A. thaliana plants infected with Pst DC3000, hopM1−, and avrE1− single mutants, but not with h−/a− double mutant, showed significantly higher expression levels of the ABA biosynthesis marker gene NCED3 than mock-infected plants." This indicates that infection with hopM1 knockout (hopM1−) Pst DC3000 results in significantly higher NCED3 expression compared to mock-infected control plants.

**Answer: Increased expression**

Infection of A. thaliana plants with hopM1 knockout Pst DC3000 leads to significantly higher expression levels of NCED3 compared to mock-infected plants.

Cited: ff5bb438eb6b3659-38bb2e97::s97

### `e763edaa-b112-460a-a564-d58a6685e639`
> Prenatal maternal stress and diesel exhaust particle (DEP + MS) exposure increased the functional heterogeneity of microglia in male mice. Specifically, microglial heterogeneity was strikingly enhanced in DEP + MS male offspring anterior cingulate cortex (ACC) compared with controls, both at early postnatal timepoints P8 and P15. The prenatal DEP + MS insult increased the relative abundance of heterogeneity, with one specific microglial subtype (Iba1 lo P2ry12 hi) becoming more abundant and exhibiting severely diminished phagocytic activity. **The best answer is: increased heterogeneity**

Cited: c0b69d2af9f2e018-845b5d60::s327, c0b69d2af9f2e018-845b5d60::s328, c0b69d2af9f2e018-845b5d60::s423

### `8af900bb-5794-40db-910e-10d5857ce5bd`
> In human temporal and frontal cortex, bipolar interneuron axons target other interneurons at a rate of 72%. This represents an increase from the 56% rate observed in mouse. **Answer: 72%**

Cited: 3039597cd03cb050-e2ba21eb::s121, 3039597cd03cb050-e2ba21eb::s122

### `6194ebfc-2d5c-4ccc-8883-da7c471b61e6`
> All dopaminergic neurons (DANs) in the mushroom body received input from all sensory modalities. This means the fraction is **100%**.

Cited: 0faff73a03a57dfe-cac59605::s994

### `1f1b07d7-39ce-4665-9b70-4ab77e3c87aa`
> According to the sources, 33% of octopaminergic neurons (OANs) in the mushroom body received input from all sensory modalities. This finding is also confirmed in another statement that reports: "All DANs, 33% of OANs, and 60% of other MBINs received signals from all sensory modalities." **The best answer is: 33%**

Cited: 0faff73a03a57dfe-cac59605::s266, 0faff73a03a57dfe-cac59605::s994

### `55668039-396e-488a-b2c3-bbe840550433`
> 694 transcription factor isoforms out of 3,266 total isoforms tested could significantly alter pseudotime upon overexpression in hESC differentiation. This represents 20% of the isoforms. **The best answer is: 20%**

Cited: 0c23610f9819876e-1c7bceee::s145

### `4f050bf3-27cd-4a14-8422-45df5e2bb079`
> The best answer is: **East and southeast: northeast**

In the first FST analysis conducted among the four geographical-based Iranian populations, the highest FST value was observed for the east and southeast: northeast pair (FST= 0.09). A higher FST value indicates greater genetic differences between populations.

Cited: c5e2b39b87ce68c3-3e8a42d1::s444, c5e2b39b87ce68c3-3e8a42d1::s445

### `cff00d08-5655-4214-97ac-8fa9504c1165`
> GLP-1-MK-801 produced a vehicle-corrected reduction in body fat mass of 45%. In comparison, GLP-1 induced a 22% decrease in body fat mass. The absolute percent difference between these two treatments is 45% minus 22%, which equals 23%. **The best answer is: 23%**

Cited: 8a63ec61b2075d5f-74d7d111::s170, 8a63ec61b2075d5f-74d7d111::s171

### `0eeb7ea9-fc80-4dee-9418-1c328c3ab653`
> The affinity constant of Medicago truncatula MtNCC1 binding to Cu+ is **2.45 pM⁻¹**.

MtNCC1₁₋₇₈ bound one Cu+ per molecule with an affinity constant of 2.45 pM⁻¹.

Cited: af470b1b1a34dd6b-0ba6ac3e::s257

### `658f7050-d137-477e-8693-26609080cecd`
> The long, slender stalk of the S. coelicolor Umbrella complex particles extended about 300 Å. **Answer: 300 Å**

Cited: 0d71c9d2055299d4-2f967140::s162

### `8696273a-7fea-411a-b6c6-0e826e1e02b5`
> Based on the provided sources, the contact probability of active promoters with the nearest topologically associated domain (TAD) in mouse embryonic stem cells (mESCs) is best characterized as follows:

Approximately 75% of active promoters in mES cells have contact probabilities with the nearest TAD boundary that are lower than 0.2. The remaining promoters are closer or adjacent to a TAD boundary and therefore experience larger contact probabilities with the boundary. Given that the majority (~75%) of active promoters have contact probabilities below 0.2, the best answer is:

**between 0 and 0.3**

This option best captures the distribution, as the dominant population of active promoters falls within this range, with most having contact probabilities lower than 0.2.

Cited: 071eed17b15b184b-5393792c::s275, 071eed17b15b184b-5393792c::s278

### `ce6dd5f7-0706-41dd-a383-9b0d22ef00a1`
> After knockout of the Ift122 gene in Tetrahymena, Pkdh1 expression shows a **large decrease**.

A drastic decrease in Pkdh1 abundance was observed in the Ift122-null strain, suggesting that nonciliary Pkdh1 may be either degraded or downregulated in Ift122 ∆-mutant cells.

Cited: 9d1bda6cef59d705-b224f6d8::s148

### `400786c1-e6c6-4f46-a501-86fdd048ed88`
> Elevated Rpn14 levels inhibit the turnover of phosphorylated αsyn in yeast. Specifically, significant accumulation of phosphorylated αsyn was observed upon elevated protein levels of Rpn14. Rpn14 protein is linked to the accumulation of the pS129 fraction, indicating that Rpn14 suppresses pS129 αsyn turnover. **Answer: Inhibition**

Cited: a95e8580727af033-09043102::s385, a95e8580727af033-09043102::s386, a95e8580727af033-09043102::s391

### `e820cbcf-6df1-4c1c-b985-c02f39f52781`
> When a KRAB domain is concatenated with a domain that is poorly expressed, the effect on KRAB function is that it **eliminates function**.

A number of domains that were lowly expressed on their own ablated KRAB function when paired with it. For example, the poorly expressed DHX16 OB_NTP and BAZ1A DDT domains inhibited KRAB function at 100 ng/mL dox. However, this loss of function appears to be dependent on protein abundance, as increasing doxycycline concentration to 1000 ng/mL permitted some or full silencing for these KRAB fusions. The best answer is: **eliminates function**

Cited: 71256a6d0f955156-f438b0cb::s272, 71256a6d0f955156-f438b0cb::s273, 71256a6d0f955156-f438b0cb::s274

### `230dec20-cd02-4613-a7b1-e28058ed46fe`
> When SMAD1 is deleted in parvalbumin-expressing interneurons in the barrel cortex of adult mice, the firing rate is significantly reduced. This reduction in firing frequency is most likely explained by a decrease in input resistance in the SMAD1-deficient cells. **Answer: Greatly reduced**

Cited: 3b1e01c90c47dd5d-850e00fc::s206, 3b1e01c90c47dd5d-850e00fc::s208

### `7975ddb0-a784-4f85-a297-c80e1cb5dcf2`
_Refused._

### `a1d01019-d2b1-4619-92ec-7ea38578819f`
> The EPRS1(N1) form of EPRS1 in humans is generated through **polyadenylation**.

A novel polyadenylation event introduces a new stop codon, which generates the EPRS1(N1) variant with a truncated C-terminus. This truncated form preserves a homeostatic basal level of GAIT gene expression in myeloid cells. The answer is: **polyadenylation**

Cited: 3ced378716ddecf0-3008c492::s137, 3ced378716ddecf0-3008c492::s138

### `fe074387-3765-4020-8f5d-e395d1094121`
> For time-lapse continuous data generated by 2pSAM, the net rate of 3D imaging is **30 volume/s**.

When scanning angles periodically with each measurement containing the projection of an entire volume, a sliding window can be used during 3D deconvolution to increase temporal resolution. By exploiting spatiotemporal continuity and estimating motions during reconstruction, a motion-correction algorithm was developed to increase the reconstruction volumetric speed to 30 volume/s. The best answer is: **30 volume/s**

Cited: 3022f334b06fe41f-49e3ab2b::s145, 3022f334b06fe41f-49e3ab2b::s146

### `f0b6cea0-e005-47bc-be0d-9a10b219cae6`
> The optimal GDP-binding temperature for the EF-1A protein from Asgard class Wukongarchaeia is 63.2 °C. **Answer: 63.2**

Cited: e2c5bba3431b7f0b-903142c2::s141

### `ae02d0e9-edf5-4c39-a215-3cbc8f4c565d`
> The phylloxera X chromosome is the second-largest chromosome in the genome. The four autosomes are ordered from longest to shortest. This means the X chromosome is longer than all four autosomes but shorter than one autosome, making it the second longest chromosome overall. **Answer: Second longest**

Cited: d0e434519e92b617-6d9d1707::s83, d0e434519e92b617-6d9d1707::s86

### `fd60a0e7-ba64-49a9-843a-6f5cb17c5fa9`
> The N-terminal α1-helical extension in the PF03500 protein family drives α1-driven dimerization. This dimerization is primarily mediated by symmetric hydrophobic contacts between adjoining α1-helices, as well as a combination of hydrophobic and polar interactions with the protein core of the neighboring subunit. The α1-helix guides the formation of different dimerization interfaces within the tetramer, each of which contributes a free energy gain of approximately 10 kcal/mol to the quaternary structure. More broadly, the presence of an N-terminal α-helical extension (α1) drives the quaternary structure assembly into D2-symmetric, tetrahedron-like tetramers. **The best answer is: α1-driven dimerization.**

Cited: ec21473ce029219d-58061129::s207, ec21473ce029219d-58061129::s208, ec21473ce029219d-58061129::s212, ec21473ce029219d-58061129::s315

### `14fd2b75-76fb-4c29-a21d-c557b2bcf2ff`
> The CDRs of P1A4 form a deep, approximately 12-Å pocket between the heavy and light chains. **Answer: 12 Å**

Cited: 09d92318a4a24d0d-b1ddf424::s100

### `e9f142f0-8ef6-47cd-b846-7283a93308d4`
> The non-specific effect observed for jAspSnFR3.mRuby3 is due to interaction of amino acids with the C-terminal histidine tag. The best answer is: **Interaction of amino acids with the C-terminal histidine tag**

Cited: 64c8513d404bd086-2a7ec0cf::s62

### `398ebac1-fd2d-45b1-9415-d82db4b4d83c`
> Based on the provided sources, the best answer is: **Shift equilibrium to super-open state**

The A456V mutation in Human Glucokinase shifts the conformational equilibrium towards the super-open conformation. This mutation mainly accelerates glucose binding, as determined by kinetic analysis. Notably, A456V is distinct from other hyperactive variants in that it does not increase conversion to the closed state like most other variants do.

### `7e7150d6-bc73-4a29-a5b3-4ef8399ed947`
> **5'-GC**

Ddd1 showed preferences towards editing 5'-GC substrates.

Cited: 635912ff7732db5a-d3b4f268::s379

### `58b39fab-337b-452d-b74f-84f9a188ce88`
_Refused._

### `80e6571e-8f5d-496a-8ba3-9c9f5b783f5d`
> The best answer is **CD38+CXCR6+**.

CXCR6 and CD38 together can be used to identify murine liver CD8+ tissue-resident memory T cells independent of CD69 during inflammatory conditions. Specifically, CXCR6 and CD38 expression by circulating memory T cells (TCIRCM) remained stable following viral challenge, whereas CD69 expression was highly dynamic and could be induced by inflammatory stimuli. This stability of CXCR6 and CD38 expression allows for CD69-independent TRM cell identification during inflammatory stress. The combination of CD38+CXCR6+ markers enabled evaluation of liver TRM cell functionality during inflammation and antigen challenge, which cannot be achieved using CD69 expression alone.

Cited: 7de06dcdff06813d-2aa4a31e::s299, 7de06dcdff06813d-2aa4a31e::s300, 7de06dcdff06813d-2aa4a31e::s303, 7de06dcdff06813d-2aa4a31e::s357

### `154e7b14-4ed5-4cf3-9149-0c4843fc62cc`
> Circular dichroism (CD) was used to demonstrate that the enzyme PafA is stable after incubation with 4M urea for 14 days. **Answer: circular dichroism**

Cited: 68c9c104777ac1ed-f6f095ce::s125

### `a71ef7a2-31a2-460d-9ff4-32d7722353c3`
> Based on the provided sources, endonuclease V from Thermotoga maritima (Tm EndoV) is inhibited at dNTP concentrations greater than 2.0 mM. More specifically, the sources indicate that "Tm EndoV endonuclease mediated hydrolysis was inhibited at dNTP concentrations >2.0 mM." Therefore, a nucleotide concentration sufficient to inhibit Tm EndoV would be any concentration above 2.0 mM. Among the provided options, the best answer is **2mM**, as this represents the threshold at which inhibition begins to occur at concentrations greater than this value.

Cited: f7415168f213937f-e85e09ae::s490, f7415168f213937f-e85e09ae::s76

### `c624ed31-214f-4c80-9544-5514a096b1d3`
> Based on the provided sources, I can answer this question directly.

73% of genes that undergo RNA editing in mouse retina cells also display alternative splicing. **The best answer is: 73%**

Cited: bd4a587f33a63d66-71a1a570::s814

### `bcd2f213-c6c6-4660-af35-a7bd1c6a1170`
_Refused._

### `24fae97b-03f3-48b8-b623-abf07faee02e`
> Based on the provided sources, the answer is **11.40%**.

In an integration site assay for the large serine recombinase Cp36 in K562 cells, 11.4% of uniquely mapped reads mapped to the top 10 loci.

Cited: 168faa61f56dbad8-d9cdd41f::s1346

### `ce93661b-e3c4-4a7a-96b6-87492259c501`
> Based on the provided sources, I can answer this question.

The sources report that when colorectal cancer-associated fibroblasts (CAFs) and colonic fibroblasts were cultured with oxaliplatin for 12 days, about 50–80% of fibroblasts resisted the treatment. While the study measured survival over 12 days rather than specifically at 2 weeks, 2 weeks falls within this 12-day treatment period, and the data indicates fibroblast survival in this range throughout the treatment course. **The best answer is: 50-80%**

Cited: 14e30d1f93ac281f-1feb8376::s181

### `941c04dc-c89d-4a90-87b0-930625268a38`
> At 50,000 generations in the E. coli Long Term Evolution Experiment, 64.0% of non-genic windows displayed some transcription at a relaxed threshold of 1 transcript per million reads (TPM). The best answer is: **64%**

Cited: f9f1eafd2f81f280-86b6f479::s39

### `ea4ce240-2864-4ee5-9ffc-2dbda0f8f550`
> When HeLa cells expressing galectin-3-GFP are infected with a T6SS-5-negative strain of B. thailandensis (hcp-5 deletion), an average of 48 galectin-3 accumulation events can be expected for every 1000 bacteria. **The best answer is: 48**

Cited: 634344ce13dd73ac-d812341d::s381

### `cff68274-4bbe-4fa0-a181-36a9af3cc0f1`
_Refused._

### `2c262f91-52b6-421d-8341-8748f923459e`
_Refused._

### `6f8a51e2-f7ad-4033-b43d-370348e4809f`
> The MC1 R8 residue establishes a charge interaction with PSMD2 E878. The best answer is: **R8 residue of MC1 and E878 residue of PSMD2**

Cited: 36e711a08612716e-caaa863d::s138

### `9a0b82cb-6a99-4e50-83fc-3ef2ebd277cc`
> Based on the provided sources, I need to examine what information is available about fine-tuning gains for the three models specifically on the AAV2 (adeno-associated virus 2) fitness prediction task.

The sources indicate that both Ankh models "gained significantly by fine-tuning only for the mutational landscape data sets (GFP, AAV and GB1)" , while "for the ProtT5-XL-U50 model (labelled ProtT5) and all four tested ESM2 models, supervised fine-tuning increased performance for all combinations of pLMs and tasks" .

However, the sources also state: "We only found minor differences between the fine-tuned pLMs for the mutations landscape tasks (SOM Tables S4 and S6). Thus, we reported the average performance across all pLMs" .

This indicates that while all three model types (ESM2, T5/ProtT5, and Ankh) showed gains from fine-tuning on the AAV2 task, the differences between them were minor enough that the authors averaged across all models rather than reporting model-specific results.

**The gain is similar for all models**

Cited: b2eec4bcf78447c8-c064fdfe::s120, b2eec4bcf78447c8-c064fdfe::s69, b2eec4bcf78447c8-c064fdfe::s70

### `8b665114-7729-4dac-a64f-4862a5397b82`
> Rv2780 was mainly detected in the cytoplasm, with partial localization in mitochondria, and very minimal localization in the endoplasmic reticulum or lysosome in macrophages derived from mice infected with Mycobacterium tuberculosis. **Best answer: Cytoplasm**

Cited: c31907b446aed1b3-79dfc999::s81

### `5c808548-92c4-4ae7-990c-e2df81e3c2ae`
_Refused._

### `564e715f-8d30-410b-bdb5-0dc5206589a7`
> Based on the provided sources, the best answer is: **Bd-ASIA1**

The copy number of the CRESS DNA mycoviral genome relative to the genome average varied between strains, ranging from 0.08 to 2.49. This copy number was lower in Bd-BRAZIL and Bd-CAPE compared with Bd-ASIA1.

Cited: 1725c45090a9d29f-a741d85e::s228, 1725c45090a9d29f-a741d85e::s229

### `e90ea0fc-4659-4b20-acae-75dc4b97a101`
> Based on the provided sources, the V1 and V3 isoforms of CDH23 are capable of localizing to the stereocilia.

For the V1 isoform, both CDH23(+68) and CDH23(-68) variants were localized to the stereocilia as well as in the cell body. For the V2 isoform, both CDH23(+68) and CDH23(-68) were only detected in the cell body and did not localize to the stereocilia. For the V3 isoform, when the HA tag was added to the N terminus, it was detected in the stereocilia as well as cell body in injectoporated hair cells. The sources explicitly state: "Together, our present data demonstrate that V1 and V3 isoforms of CDH23 can localize to the stereocilia." **The best answer is: Both the V1 and V3 isoforms.**

Cited: a322cf631e4099c8-c8d9416c::s145, a322cf631e4099c8-c8d9416c::s146, a322cf631e4099c8-c8d9416c::s149, a322cf631e4099c8-c8d9416c::s150

### `c246753c-27d2-4ae4-8630-b9b4077ba6f6`
> The N-terminal HORMA domain encompassing residues 1-149 of yeast Rev7 is not important for its interaction with the MRX complex. Cells expressing ScRev7 N-terminally truncated variants showed robust growth in selection medium similar to wild-type, indicating that they associate with the subunits of the MRX complex. In contrast, deletion of the C-terminal 42 amino acids (residues 203-245) completely abolished the viability of yeast cells and the ability to interact with MRX subunits. **The best answer is: 1-149**

Cited: 5a389cfe7cca76d2-437a07be::s321, 5a389cfe7cca76d2-437a07be::s322, 5a389cfe7cca76d2-437a07be::s358

### `22306bd7-7e84-415d-aebb-11c6312eb081`
> Based on the provided sources, I need to identify which antibody isotype was NOT produced by the AMP-CpG formulated EBV vaccine in HLA-expressing mice.

Source directly states: "In this study antibody isotype analysis revealed AMP-CpG formulated EBV vaccine generated a mixture of IgA, IgM, IgG1, IgG2a, IgG2b, and IgG3 gp350-specific antibody isotypes."

This sentence explicitly lists all the antibody isotypes that WERE produced: IgA, IgM, IgG1, IgG2a, IgG2b, and IgG3.

Comparing this list to the answer options provided, the only isotype in the options that is NOT mentioned in the list of produced antibodies is **IgE**.

**Answer: IgE**

Cited: 9ed823ba1e15f21e-9d83dcd0::s385

### `7d71dffb-b591-4b88-b0c6-e125a1b083b4`
> **lipopolysaccharide**

Lipopolysaccharide has been shown to facilitate lung metastasis in breast cancer models via the prostaglandin E2-EP2 pathway.

Cited: 760a41458de0016f-45c84606::s835

### `fca26d7c-05cf-40b0-9fd6-a63ed7950909`
> The SpyTag-SpyCatcher bioconjugation system is used to attach the INT tag to AAVs in the Vault AAV delivery system. Specifically, SpyTag003 (SpT3) was genetically inserted into the VP2 protein of AAV9, and a SpyCatcher003-INT (SpC3-INT) fusion protein was designed to conjugate with the SpyTag003. The best answer from the provided options is: **Spytag003**

Cited: 2445404168635a55-0ad2b180::s81, 2445404168635a55-0ad2b180::s82, 2445404168635a55-0ad2b180::s84

### `c6e11fac-8f9c-4cf1-aa6e-4d25731ba74f`
> The most highly represented Borg genes encode glycosyltransferases. **Answer: Glycosyltransferases**

Cited: 01e0adaed8ffd463-38a7f893::s131

### `bace5737-ba26-422a-8706-0fb1e92b689f`
_Refused._

### `ff7328e2-4954-46a2-8ea3-d40b4df0c0ea`
> A sodium ion coordinates binding of cyclic tetra-adenylate to Csx23 in Vibrio cholerae. The sodium ion is positioned at the centre of the cA₄ molecule. However, the sodium ion appears to make no direct or indirect interactions with cA₄ or Csx23 CTD itself, instead interacting only with a water molecule. **Answer: Sodium**

Cited: 43ce81162fb1ab76-beaced53::s925, 43ce81162fb1ab76-beaced53::s984

### `76bcaeeb-93bd-4951-99b9-cf4613de1a37`
> The only microcin homolog identified in all known E. coli phylogroups is **Microcin V**.

Cited: 58223b6183837ffb-65e8f6c9::s173

### `850f86d3-0139-43df-89fd-e606c30aaa8b`
> Based on the provided sources, the best answer is:

**NP-OVA (4-hydroxy3-nitrophenylacetyl (NP)-ovalbumin (OVA) footpad immunization**

CD90 was demonstrated to identify germinal center-resident follicular helper CD4+ T cells using NP-OVA footpad immunization in multiple experimental approaches. PAGFP Tg mice were footpad-immunized with 20 μg of NP-Ova+alum 11 days prior to analysis. S1pr2-RFP mice were footpad-immunized with 20 μg of NP-Ova+alum and treated with 5 mg tamoxifen (i.p.) at days 5-7 p.i. FoxP3 EGFP mice were footpad-immunized with 20 μg of NP-Ova+alum. Additionally, loss of CD90 on resident GCTfh cells was observed for multiple immunogens and in the chronic GCs of PPs, indicating that while NP-OVA was a primary model used, the findings were validated across multiple immunization approaches.

Cited: ee877dbbbd2e51e3-55e76368::s105, ee877dbbbd2e51e3-55e76368::s125, ee877dbbbd2e51e3-55e76368::s373, ee877dbbbd2e51e3-55e76368::s437

### `df061613-2591-4faa-be03-791c76375cb5`
> The mutations on the SARS-CoV-2 spike protein that contribute to resistance of the BA.2 variant to the S2X35 antibody are S371F, D405N, and R408S. Each of these three substitutions caused substantial decreases in S2X35 binding. In the BA.2 context, no single reversion of these mutations restored S2X35 binding, suggesting an additive effect of all three mutations together. **The best answer is: S371F, D405N, R408S**

Cited: daca00c2dca36dc2-b25fdc82::s165, daca00c2dca36dc2-b25fdc82::s176

### `634f6745-f3b3-4cb1-9859-96ffb954b98a`
_Refused._

### `d1eabedb-656f-4f89-a65f-4ed89478ba9f`
> Based on the provided sources, **DILT** is the most effective at enhancing ER proteostasis and promoting functional, soluble forms of GCase in neurons.

DILT enhanced properly folded, functional GCase, as demonstrated by increased GCase activity in whole-cell lysates that include both ER and post-ER forms. Treatment of SNCA-3x neurons with DILT abrogated the buildup of insoluble GCase while concomitantly elevating soluble GCase starting at 2 weeks and continuing to 8 weeks of treatment. In comparison, DANT and DHBP treatment elevated soluble GCase levels in cell models, although not as robustly as DILT. Additionally, enhancing ER proteostasis with DILT can promote functional, soluble forms of GCase. **Answer: DILT**

Cited: f74e43a900ad6cb5-10c56ee5::s236, f74e43a900ad6cb5-10c56ee5::s239, f74e43a900ad6cb5-10c56ee5::s242, f74e43a900ad6cb5-10c56ee5::s244

### `58f69c8d-cb94-4021-a84f-c549a7b976e1`
> Based on the provided sources, **CXE (Cas9-XTEN-hExo1)** has the highest homology directed repair (HDR) efficiency among the designed DNA editors listed.

CXE resulted in the highest HDR efficiency and lowest indel frequency among the four EXO editors. The optimized EXO editor, CXE, in which hExo1 was fused to the downstream of Cas9 with XTEN linker, gave rise to the highest HDR efficiency and the lowest indel frequency. CXE was even significantly superior to E4 and E1B, which are positive control editors.

Cited: 66aafadef9d913b8-311a2ec6::s1162, 66aafadef9d913b8-311a2ec6::s296, 66aafadef9d913b8-311a2ec6::s298

### `20980744-f9ff-4e39-a08d-106eada6900c`
_Refused._

### `a6622141-68d6-418f-8e30-7a5eff3d4fa8`
> Based on the provided sources, I need to identify which drug cannot inhibit binding of the viral protease dNS3S139A to the antiviral peptide CP5-46A-4D5E.

The sources directly address this question. When testing dNS3 (which contains the S139A mutation) with the peptide CP5-46A-4D5E (referred to as P_MED in the sources), the results showed that three drugs inhibited luciferase activity in a dose-dependent manner, but one did not. The first three of these drugs (grazoprevir, glecaprevir, and danoprevir) inhibit luciferase activity in a dose dependent manner. However, split luciferase constructs containing dNS3 exhibit significant resistance to telaprevir. This observation is consistent with the drug's covalent binding mechanism to the catalytic Ser139, which is mutated in dNS3. Additionally, when the NS3 S139A mutation was applied to another NS3 variant, it "ablates telaprevir sensitivity, leaving only sensitivity to grazoprevir among the three drugs tested." **The answer is: Telaprevir**

Telaprevir cannot be used to inhibit binding of dNS3S139A to the antiviral peptide CP5-46A-4D5E because telaprevir's mechanism of action depends on covalent binding to the catalytic Ser139 residue, which is mutated to alanine in dNS3S139A.

Cited: ab2ec42d01d567c3-25987f26::s139, ab2ec42d01d567c3-25987f26::s89, ab2ec42d01d567c3-25987f26::s90, ab2ec42d01d567c3-25987f26::s91, ab2ec42d01d567c3-25987f26::s92

### `9fe3ff3b-60cf-472d-ab1a-2bda1868f1b4`
> Based on the provided sources, the best answer is: **Increased acetylation relative to female VICs**

Here is the supporting evidence:

When male VICs are cultured on larger polystyrene nanoparticles gels, they show increased acetylation. Specifically, "only larger particles affected the acetylation state" in males. Male VICs displayed significantly higher acetylation states in most hydrogel conditions when compared to female VICs. Additionally, stiff hydrogels (which correlate with larger nanoparticles) promoted increased acetylation in male VICs compared to soft hydrogels.

Cited: e44731dbd47b1ddf-5ac4257e::s268, e44731dbd47b1ddf-5ac4257e::s269, e44731dbd47b1ddf-5ac4257e::s437

### `9088251a-99fe-4b91-b6a9-375154ec4f58`
> Based on the provided sources, ZDHHC5 mediates palmitoylation of GSDMD to promote pyroptosis. The sources do not provide evidence that ZDHHC5 mediates palmitoylation of GSDMB or GSDME. While the sources indicate that GSDME can be palmitoylated to enhance pyroptosis, this is mediated by ZDHHC2, 7, 11, and 15—not ZDHHC5. The best answer is: **GSDMD**

Cited: de604c3de7db092a-c7360229::s413, de604c3de7db092a-c7360229::s415

### `b8ec372b-ae29-473e-96bc-86ff1ead24ea`
> Based on the provided sources, TNN (tenascin-C/TN-C) interacts with both ERK1 and ERK2.

The sources indicate that β3 integrins activate ERK1 and ERK2 MAPKs, which then modify transcription factors (prx1 and prx2) that interact with an ECM-responsive element in the TN-C gene promoter. Additionally, activation of the TN-C promoter element was suppressed by preventing ERK1/2 activation. Furthermore, β3 integrin-dependent activation of ERK1 and ERK2 regulates TN-C in vascular smooth muscle cells. **The best answer is: ERK1 & ERK2**

Cited: dd641ef35dc94ec2-2545f939::s382, dd641ef35dc94ec2-2545f939::s395, dd641ef35dc94ec2-2545f939::s414

### `a45c277e-55d9-4e7f-b1de-37fc2e19daf6`
> Ogfrl1 has been shown to be a highly specific marker for parvalbumin (PV) interneurons in the molecular and fusiform layers of the dorsal cochlear nucleus. **The best answer is: Ogfrl1**

Cited: 1d72af568ea9078d-b044a088::s227

### `a8aa19cc-e4d1-4aa1-8c4e-2a518b4c99d6`
_Refused._

### `2c3ba95c-47d5-4798-9911-ffdb11c940e4`
> JUND is transcriptionally stabilized upon DDX3X depletion. This finding was validated by qPCR analysis, where JUND RNA was stabilized after 24 hours with knockdown of DDX3X and Actinomycin D treatment. **The best answer is: JUND**

Cited: 56206a0d497c3922-fc28cbb0::s113, 56206a0d497c3922-fc28cbb0::s98

### `49d2630e-9d26-4e12-89a3-3050a609abf5`
_Refused._

### `c758f685-ba4a-4bf0-bd85-567c60ff1508`
> Based on the provided sources, the best answer is **p50**.

Nuclear expression of the cofactor p50 was enriched in TRAF3 loss of function DLBCL cells. This enrichment suggests potential crosstalk between the noncanonical and canonical NF-κB branches. In contrast, nuclear localization of c-Rel and RelA was not affected by TRAF3 loss of function.

Cited: 0ca36e794a547256-8b0b5a88::s293, 0ca36e794a547256-8b0b5a88::s294

### `fd54d745-447c-4fcd-80de-463fcd3de6a4`
> Based on the provided sources, I need to identify which gene is NOT an ABA catabolism gene that is upregulated in DANA1 knockout lines.

According to the sources, the ABA catabolic genes that are upregulated in dana1 mutant lines are: CYP707A1, CYP707A2, CYP707A4, and UGT71B1. In contrast, MYB44 is downregulated in dana1 mutants, not upregulated. Additionally, the sources indicate that MYB44 is not a direct target of the DANA1-DIP1 regulatory complex, as DIP1 did not bind to the MYB44 locus. **The answer is: MYB44**

MYB44 is not an ABA catabolism gene that is upregulated in DANA1 knockout lines; rather, it is downregulated in these lines.

Cited: b372fd7f8558d5e0-ff2c7d15::s205, b372fd7f8558d5e0-ff2c7d15::s316

### `4d11258d-ee8c-4bc7-91a8-613c7a41f139`
> Based on the provided sources, the K548R mutation in PARP1 has been shown to impair its interaction with MRE11 in immunoprecipitation assays.

The sources describe an immunoprecipitation experiment where "FLAG-PARP1 WT, K548R, or Vector, together with GFP-MRE11, were transfected into HEK293T cells, and the cells were lysed and subjected to FLAG affinity gel to immunoprecipitate FLAG-PARP1." The results demonstrated that "a reduced interaction of the PARP1-K548R mutant with MRE11" was observed "to a similar level to that seen in cells exposed to the PARP inhibitor AZD2281." **The best answer is: K548R**

### `1ff2b2e4-492e-4e35-bf33-f0fb53ab938c`
> The best answer is **S446G**.

The reversion mutation S446G in the BA.1 background increases the neutralization potency of both antibodies tested, as demonstrated by negative escape values in the experimental data. In contrast, the other mutations listed are associated with escape from neutralizing antibodies rather than increased potency. K444T and R346T are identified as sites of substantial escape or escape mutations in BA.1. L452R is also a site of substantial escape from both antibodies tested.

Cited: e3048b3df487004d-f5873c81::s203, e3048b3df487004d-f5873c81::s217

### `178a5e56-340f-4ba8-a3e5-f024ca016f40`
> The best answer is **G56H**.

The mutation G56H pulls the CDR2 loop closer to the RBD in computational models. Specifically, the mutation of Gly56 to His56 has imparted changes in the CDR2 loop and pulled Gly55 towards the Gly482 of RBD as observed in PyMol analysis.

Cited: d54befdeabd3bf9e-4573e6c1::s504

### `c75879f4-9329-4594-8f6a-c4d421f2439f`
> Based on the provided sources, I need to identify which mutation increases Pbs2's interaction with SH3 domains.

According to the sources, only three Pbs2 mutants were found to interact with SH3-containing proteins more strongly than wild-type Pbs2: Q82W, P97A, and L98F. Among the answer options provided, only **P97A** appears in this list of mutations that increase interaction with SH3 domains.

The other options listed (I87W, K85W, N92H, N92S, S83F) all interacted with SH3-containing proteins more weakly than wild-type Pbs2, indicating a gain in specificity rather than increased interaction strength. **The answer is: P97A**

Cited: 667d94590e6616fe-e15f7eed::s535

### `f7346ea0-5f1b-45e9-a1d6-493c754159c1`
> The best answer is **membrane trafficking**.

The S118L mutation does not affect ATP sensitivity. The S118L mutation does not affect KATP channel stimulation by MgADP. Metabolic inhibition of hetS118L and homS118L channels was unaffected. However, membrane trafficking of S118L channels is impaired, with an approximately 40% reduction in surface expression of hetS118L and homS118L channels compared with wild-type channels.

Cited: e01d60f8ccaf1fbd-a4be292d::s196, e01d60f8ccaf1fbd-a4be292d::s202, e01d60f8ccaf1fbd-a4be292d::s204, e01d60f8ccaf1fbd-a4be292d::s245

### `3d3fea17-c8ee-4005-94cb-d8798be696c3`
> The best answer is **Volume**.

A remarkably consistent linear relationship has been found between the total volume of the haptophyte cells and the volume occupied by UCYN-A within its host, expressed as log10(VUCYN-A) = 1.0 log10(Vhapto) − 1.2 with R² = 0.97. This log-linear relationship holds true within and across different UCYN-A sublineages. Similarly, a tight size relationship exists between the volume of B. bigelowii and the total chloroplast volume, also expressed in logarithmic scale. The sources do not provide evidence that genome length, mutation rate, or ribosome size scale log-linearly between the nitroplast and its host cell.

Cited: b2aeda61ca908aaf-9486c25d::s139, b2aeda61ca908aaf-9486c25d::s79

### `ab58e166-f0b5-49ae-ac56-c38b5d6e8aad`
> Pdpn can be used to identify Post-AIRE mTECs. Specifically, podoplanin (Pdpn) was downregulated in post-Aire mTECs, allowing the mTEC lo population to be separated into Pdpn+ CD104+ (pre-Aire) and Pdpn- CD104- (post-Aire) compartments. The answer is: **Pdpn**

Cited: da7b856dfa32186d-1e1bf60f::s168

### `a73b2c2d-a3ac-49e6-8e2e-44b4c1e6de94`
> Based on the provided sources, I need to identify which protein shows the greatest reduction in association with mutant D20V SMN compared to WT SMN.

The sources directly address the D20V mutant's binding profile. According to the data, the D20V mutant showed reduced association with specific proteins compared to WT. states that "those same five proteins (SmD1, D2, E, F, G) were the most reduced in the D20V mutant pulldowns." Additionally, indicates that "the D20V mutant co-purified considerably less Gem2 than did the WT construct."

Among the answer options provided (Cul1, HspA, SkpA, and SmD1), the sources specifically identify SmD1 as one of the five Sm proteins that were "most reduced in the D20V mutant pulldowns." The sources do not provide comparative fold-change data for Cul1, HspA, or SkpA in the context of D20V versus WT that would allow ranking their reductions. While these proteins are mentioned as SMN binding partners, there is no specific quantitative comparison of their reduction in D20V mutants.

**The answer is: SmD1**

SmD1 was among the five Sm proteins most reduced in association with the D20V mutant compared to WT SMN.

Cited: 7b3aeee153dea14b-f01a40db::s114, 7b3aeee153dea14b-f01a40db::s116

### `04dbe07d-8b2c-4daf-b5b2-ef0e93f1fd2a`
> For KBTBD4-PR, Arg312 is the residue that contributes to the expansion of the 2b-2c loops and is inserted into the narrow tunnel leading to the HDAC1 catalytic site. Specifically, the positively charged side chain of Arg312 reaches halfway into the tunnel. This central residue is part of the mechanism by which both KBTBD4 mutants insert a bulky side chain into the narrow tunnel leading to the catalytic site of the enzyme. **The best answer is: Arg312**

Cited: 774bbc2bae82b5a7-82522eec::s147, 774bbc2bae82b5a7-82522eec::s148

### `4a6705b5-85e5-44c1-8444-65be30192802`
> RlmB has been found to promote large ribosomal subunit assembly even when expressed as a catalytically dead mutant. The catalytically inactive RlmB variant RlmB(E198A) can stimulate 50S assembly, demonstrating that its function is independent of its methylation activity. In contrast, RlmN requires catalytic activity for its assembly function. The catalytically inactive RlmN(C355A) variant does not stimulate ribosome assembly. Similarly, RluC requires catalytic activity. Expression of the catalytically inactive variant of RluC(D144A) does not improve ribosome assembly in the Δ10 strain. The sources do not provide information about RlmM's catalytic requirements for assembly promotion. **The best answer is: RlmB**

Cited: 9a92b9f5adbd8f23-edc56ec0::s15, 9a92b9f5adbd8f23-edc56ec0::s255, 9a92b9f5adbd8f23-edc56ec0::s262, 9a92b9f5adbd8f23-edc56ec0::s359

### `08397294-3d99-4790-915c-b8bcb1e9e661`
> The best answer is **DTD**.

When Rev1 domain mutants were placed in a rev3 background (lacking the catalytic subunit of polymerase zeta), the Rev1-DTD rev3 double mutants showed a greater increase in sensitivity to MMS compared to Rev1 ∆ BRCT rev3 and Rev1-UBM rev3 double mutants. Specifically, the Rev1-DTD rev3 double mutants showed sensitivity equivalent to that observed in the rev1 ∆ null mutant, indicating the greatest increase in MMS sensitivity among the domain-specific knockouts tested. In contrast, Rev1 ∆ BRCT rev3 and Rev1-UBM rev3 double mutants were more sensitive to MMS than rev3 single mutants, but this increase was less severe than that seen with the DTD domain knockout.

Cited: 1c2a0524c883d73f-f2d03f0c::s128, 1c2a0524c883d73f-f2d03f0c::s129

### `837b2489-723a-4099-9b68-c2a9ea688f4d`
> BUD40 produces the thickest fibers among the three synthetically designed matrix proteins. Specifically, BUD40 material produces fibers that are, on average, 2.07± 0.56 microns thick. In comparison, BUD60 forms fibers about 1.31± 0.23 microns thick, and BUD80 forms fibers that are, on average, 1.07± 0.21 microns thick. Statistical analysis using one-way ANOVA demonstrated a statistically significant difference between the width of the fibers formed by BUD40 and the fibers formed by BUD60 and BUD80. **Answer: BUD40**

Cited: 7eb232e6cd269f4c-b14c15d4::s299, 7eb232e6cd269f4c-b14c15d4::s300, 7eb232e6cd269f4c-b14c15d4::s301

### `745f5a0d-5f8f-405e-bb46-f37b3d1f0678`
> The best answer is: **None of the above**

Training characteristics within the target brain region, such as mean neurofeedback signal amplitude, mean left amygdala activation, and signal changes in the left amygdala, were not associated with changes in symptoms and therefore could not explain interindividual differences in clinical response. Instead, the study found that significant associations existed between changes in depressive symptoms and subtypes of whole-brain activation patterns during neurofeedback training, rather than characteristics specific to the target region itself.

Cited: 06508579b3fd8baf-222782c2::s507, 06508579b3fd8baf-222782c2::s508

### `bca1be77-208b-4d57-ac29-05aa6d58bdbf`
> **p50**

Among the transcription factors identified as core regulators of Hypoxia-TAM polarization, p50 most strongly promotes macrophage polarization towards a hypoxia state in glioma-associated TAMs. Disruption of p50 (encoded by NFKB1), but not HIF1A or JUN, markedly decreased the expression of Hypoxia-TAM signature genes. p50 functions as a downstream transcription factor of NFκB signaling and is required for the Hypoxia-TAM signature. Tumor cell-produced SPARC and hypoxia-induced lactate concertedly promote Hypoxia-TAM polarization at least in part through activating p50.

Cited: e1671d32c95165a1-15d2b9a0::s244, e1671d32c95165a1-15d2b9a0::s246, e1671d32c95165a1-15d2b9a0::s247, e1671d32c95165a1-15d2b9a0::s251

### `2dc20a2f-de54-4bfe-a34f-1ba395f342cf`
> The nucleus is more stiff than the cytoplasm.

This property is specific to IHAs and not found in GBM cells. In IHAs, the average nuclear stiffness (1398 ± 428 Pa) is fourfold higher than the stiffness of the cytoplasm (331 ± 74 Pa). Additionally, the nuclear relaxation time of IHAs (0.35 ± 0.08 min) is significantly lower than the cytoplasmic relaxation time (0.66 ± 0.12 min). In contrast, none of the viscoelastic properties of GBM cells differ significantly between the nucleus and cytoplasm. The sources explicitly state that "distinct nuclear and cytoplasmic viscoelastic behaviors exist in the IHAs but not in the GBM cells."

Cited: edce53910698b365-47b1176a::s123, edce53910698b365-47b1176a::s132, edce53910698b365-47b1176a::s133, edce53910698b365-47b1176a::s135

### `afb36e40-0836-4810-909e-eabfe17dcd8b`
> Based on the provided sources, I need to identify which gene was NOT upregulated by 5-FU treatment in HCT116 cells.

Let me review what was upregulated:

- **ITPA**: "At 10 μM concentration of 5-FU, ITPA was upregulated > 2-fold in 72 h" - **polB** (encoding pol β): "pol β was upregulated > 2-fold upon the administration of 5-FU in 72 h" - **Rev1**: "pol η, along with pol β and Rev1, was upregulated upon 5-FU treatment" - **TYMS**: "the main target enzyme for 5-FU, thymidylate synthase (TYMS), was not significantly upregulated upon the administration 5-FU within 72 h either" The answer is **TYMS**.

TYMS was not significantly upregulated by 5-FU treatment in the HCT116 cell line.

Cited: 0606f4a1026bae93-53471ae3::s1367, 0606f4a1026bae93-53471ae3::s1381, 0606f4a1026bae93-53471ae3::s1679

### `c6f097c9-2216-4e98-af45-8101681b38ec`
_Refused._

### `9f797d29-9f3a-481d-b2fe-326cbc686273`
> Mn2+ had the strongest enhancing effect on the cleavage activity of endonuclease R.DraR1 from Deinococcus radiodurans. The answer is: **Mn2+**

Cited: 97736fa153fa784c-41306673::s223

### `0d5cf8a7-a240-4a8f-be4e-c16712f90d79`
> Based on the provided sources, the best answer is **L522**.

The sources indicate that substituting L522 to alanine silences transcriptional activity of the intrinsically disordered region of Unkempt. Specifically, "substituting L522 in minN or two residues in minC (W622 and F625) to alanines completely silenced the activities of either region." While W622 and F625 are also mentioned as residues that silence activity when mutated to alanine, L522 is the single leucine residue among the options provided that directly silences transcriptional activity when mutated to alanine in the intrinsically disordered region.

Cited: f56f5fb1f0922800-5c745f12::s207, f56f5fb1f0922800-5c745f12::s209

### `40400348-eabb-4b25-90d1-e33589d3e5a4`
> The best answer is **Fexofenadine**.

Fexofenadine (FEXO), a low-cost over-the-counter antihistamine, was tested for effects similar to anti-VISTA antibodies. When combined with ICB therapy, FEXO+ICB was more effective than anti-VISTA+ICB for prolonging survival of mice, with 50% of FEXO+ICB-treated mice achieving tumor-free survival compared to none of the anti-VISTA+ICB-treated mice. Additionally, FEXO+ICB was more potent than anti-VISTA+ICB in inhibiting lung metastasis.

Cited: 1e98838d3116281b-bac8d842::s252, 1e98838d3116281b-bac8d842::s255, 1e98838d3116281b-bac8d842::s256

### `ebe57888-662f-488f-ade1-c0aaffe638b1`
> **GFAP**

GFAP (glial fibrillary acidic protein) is a reactive astrocyte marker that has been shown to increase in expression in RhoANesKO mice. Specifically, a striking increase in GFAP expression was found after CNS injury in RhoANesKO mice compared with wild-type mice, as demonstrated by both immunohistochemistry and immunoblotting. Additionally, RhoA ablation in astrocytes increased GFAP expression compared with wild-type astrocytes.

Cited: d396d8edd4f389e6-d53cbbe3::s270, d396d8edd4f389e6-d53cbbe3::s321

### `ef07d562-fc18-43c9-8201-7a189d76eeb9`
> The highest frequencies of KIR+ CD8+ T cells were found in patients with vasculitis, and to a lesser extent in those with acute respiratory distress syndrome (ARDS). **Best answer: Vasculitis**

While vasculitis is not explicitly listed as an option, the sources indicate that vasculitis was associated with the highest levels of KIR+ CD8+ T cells among the COVID-19 complications studied. Among the provided options, **Acute respiratory distress syndrome** is the best supported answer, as it is the only listed symptom mentioned in the sources as being associated with elevated KIR+ CD8+ T cells in COVID-19 patients.

Cited: 7f115cb9d0652622-d64852b9::s300

### `b331480e-dfc7-4e92-931a-c71f491c4795`
> The three residues with evolutionary divergence in the G domains of RAS isoforms that also impose selectivity constraints on pan-KRAS non-covalent inhibition are 95, 121, and 122.

The sources identify H95 in the α3 helix as conferring orthosteric effects for KRAS selectivity. Residues P121 and S122 in loop 8 impose allosteric or indirect effects on selective inhibition. These three residues show evolutionary divergence between RAS isoforms and together determine KRAS selectivity for the pan-KRAS inhibitor. **The best answer is: 95, 121, 122**

Cited: 70973b3a4b0a193e-f334e23d::s134, 70973b3a4b0a193e-f334e23d::s135

### `58950824-2665-445d-939b-9512d5d01a2b`
> MEF2C has been found to be enriched in heart and skeletal muscle of Rattus norvegicus rats that have undergone endurance training. MEF2C was suggested to have increased activity in the transcription factor enrichment analysis. **The best answer is: MEF2C**

Cited: d55d01d52f893ef8-5b74c904::s1197, d55d01d52f893ef8-5b74c904::s1198

### `8d12cb90-73c6-4cc1-9f83-0fa9fd822e92`
> The two transcription factors used to identify the T4/T5 neuron subtypes in the optic lobe that split into T4/T5a-b and T4/T5c-d subtypes were **acj6 and SoxN**. The best answer is: **acj6, SoxN**

Cited: 010bab0784c5d05e-4d07cf2b::s185
