---
name: midjourney-prompt
description: Use when the user wants an image made in Midjourney instead of Higgsfield (assets, character sheets, first frames) or says "미드저니", "Midjourney", "MJ". Writes short Midjourney prompts with parameters and reference settings, tells the user what to run, and records the result in the canon. Midjourney has no connector here: the user runs the prompt and brings the result back.
---

# Midjourney prompts (manual route)

Midjourney is not connected to this project: **you write, the user runs and brings the result back** (image or link). Everything in the canon works as usual (asset IDs, cut cards, OK ledger, handoffs). The Higgsfield-only parts do not apply: `check_prompt.py`, `folder_id`, quotes, element UUIDs, "send" and result lookup. Parameters change between Midjourney versions and the sources used for this skill were third-party: **ask the version first** and tell the user to confirm any parameter in the current Midjourney docs when a result ignores it.

## 1. Required information

| Information | From |
|---|---|
| Midjourney version (V7, V8.x …) and whether the user has Omni Reference | ask once; remember it for the work |
| What is made: asset (character view / location / prop) or first frame | the request |
| Subject facts and the fixed description sentences | registry (character IDENTITY + WARDROBE, location, prop), copied verbatim |
| Reference image links already approved (face, style) | registry `확정 job`, OK ledger |
| Aspect ratio | `decisions.md` |

Ask only what is missing, in one batch with proposals (instructions rule 4). Do not ask about the model, save folder or credits: they are the user's own Midjourney settings.

## 2. Prompt shape

- **Short, plain, descriptive:** 25-60 words, one subject. Order: subject → wardrobe → place and light → camera or lens → medium. Natural phrases, not the long English blocks used for Higgsfield. No `REFERENCE AUTHORITY` blocks and no stacked "no X" sentences.
- **Parameters go last**, on one line: `--ar 16:9 --v [version] --stylize [value]`. Add `--no [few words]` only for a thing that actually appeared. Keep the user's version and aspect from the canon.
- **Fixed sentences are copied letter for letter** from the registry; if the registry sentence is long, shorten only in the registry first (a new `_v2`), never in the prompt.
- **Directions:** keep them as screen directions and put at most one short clause in the prompt (`seen from the front`, `facing screen right`). Midjourney can mirror sides (a face mark came out on the opposite side in our Higgsfield test): after the result, write the side actually seen into the registry.
- **No text, logos or captions** in the image unless the canon allows them.
- **A person who feels real:** no appeal words (`cute`, `likable`, `quirky`); describe structure (full cheeks, large round eyes) and add one or two ordinary details (a small mole, a few flyaway curls). Personality belongs in the `ACTING PROFILE`, not the image prompt (`image-prompt` → `character.md`).
- **Not a sheet in one image.** Midjourney does not reliably keep a headless three-panel layout. Make a character as separate images: front full body, rear full body, close-up portrait, each with the approved face image as the character reference.

## 3. References and consistency

- The first approved face image becomes the character reference for every later view (Omni Reference on V7 and later: `--oref [image link]`, strength `--ow`; older versions used `--cref`). Style reference: `--sref [link]`. Reference links must be reachable by Midjourney: the user pastes the link of the approved image.
- A high `--stylize` can overpower a reference: when the face drifts, lower `--stylize` or raise the reference weight, one change per run (instructions rule 3).
- One run, one change. Same failure twice → stop and propose a new reference image or a different framing (instructions rule 8).

## 4. Hand to the user

Show the prompt in one code block, then outside it one plain line each: version, references (ID and role, with the link the user must paste), aspect, number of images to pick from. Tell the user: run it, pick one image, then paste the image or its link and say `됐어`. Do not claim the image was made.

**Risk list (rule 7)** before the prompt, one blocking sentence per risk: face drift between views, mirrored side, wardrobe change, extra people, text in the image.

## 5. Judging and recording

- When the user pastes the image, judge item by item (met / missed); what you cannot see is "추정". The user decides approve or reject (instructions rule 10).
- On approval, write the OK card as usual (`higgsfield-generation` §4 "OK record" format): `job` = the Midjourney image link, `모델 · 설정` = version + parameters, prompt verbatim including the parameter line. In the registry, the element name `char_<인물>_<상태>_v1` is the file name the user saves the image under (their own `00 에셋/인물` folder), because there is no folder tool.
- A first frame for video: the approved image is the start frame; the video itself is made in the video tool the canon names. A model that cannot hold a start frame is a risk (`higgsfield-generation` §1 item 6).
