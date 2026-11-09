# Asset lock test (잠금 시험)

A sheet that came out well once is a lucky image until it has held across angles, light and co-stars. This file tests a confirmed asset **before the first video uses it**. Test images only (1k, check quality). No video is generated here.

## When

- The user says "잠금 시험", "스트레스 테스트", "이 인물 영상에 써도 돼?".
- Offered **once** before the first video prompt of a cut whose character or prop reads `잠금 상태: 초안` in the registry (`context/must-ask.md`, row 13). If the user skips, write `건너뜀` and do not ask again for that asset. A skipped asset is allowed; the risk goes into cut card [10].

## Status (asset registry line under each character and prop)

`잠금 상태: 초안` → `잠금(YYYY-MM-DD)` or `건너뜀`. Fill the line: test jobs, the date, and 한계 (what still drifts). Locations are tested through their views (`location-view.md`, one LIGHT LOCK per view) and are not tested here.

## Required information

| Information | From |
|---|---|
| The asset and its confirmed sheet job; for a prop, its fixed description sentence | Registry |
| The real light the asset will stand in: LIGHT LOCK of each location view it appears in | Registry view table |
| Co-stars who share frames with this character | `shot-list.md` |

Ask only what is missing, in one batch with proposals (instructions rule 4).

## Test set for a character (one image per test, each its own generation)

1. **New angle:** three-quarter or profile view, neutral pose, plain background.
2. **Close-up:** chest up, neutral light.
3. **Real light:** the asset inside the confirmed location view, that view's LIGHT LOCK sentence verbatim.
4. **Two-shot:** beside each co-star, one image per co-star, using both sheets (`REFERENCE AUTHORITY` block, `image-prompt` §2).

Prompt shape (fill from the registry; run the check script on each, instructions "Check"):

```text
Using <<<char_[name]_[state]_v1>>> only for [NAME]'s face, hair and wardrobe. [Shot size], [camera position by objects on screen], [NAME] [neutral pose]. [WARDROBE sentence, verbatim.] [LIGHT LOCK sentence, verbatim, tests 3 and 4.] Photorealistic, natural skin texture. LEFT and RIGHT are SCREEN directions, never the character's own left or right.
```

A prop: two images. Held in the intended hand at the intended size beside the character, and alone at the intended state (new → worn as the cut needs).

## Judging (the user decides; instructions rule 10)

Show this table with the last column empty:

| Test | Look at | ✔/✘ |
|---|---|---|
| 1 angle | same person as the sheet; hair and build unchanged | |
| 2 close-up | face structure, eyes, skin age | |
| 3 real light | wardrobe colour and collar unchanged under that light | |
| 4 two-shot (per co-star) | the two faces stay distinct, no blending; no extra props | |

- All ✔ → `잠금(date)`; write what drifted at the edges into 한계.
- A ✘ → change one thing (the sentence or the reference) and re-run only that test. The asset stays `초안`.
- The same test fails twice → stop (instructions rule 8). Propose a new sheet version (`v2`) or removing the shot type from the cuts; do not keep adding sentences.

## After the test

Record the test jobs on the asset's registry line and put 한계 into the `[10]` field of every cut card that uses the asset. Credits: quote before sending (instructions rule 10). Do not send the next test before the user has judged the previous one.
