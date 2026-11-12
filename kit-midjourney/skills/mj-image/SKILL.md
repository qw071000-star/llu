---
name: mj-image
description: Use when writing Midjourney image prompts for assets (character views, locations, props, art style) and still frames that start a clip. Users say "미드저니 인물 만들어", "장소 만들어", "소품", "그림체", "퍼스트 프레임", "스틸 컷". Midjourney is not connected: you write, the user runs and brings the result back.
---

# Midjourney image prompts

The user runs every prompt in Midjourney and pastes the chosen image or its link. Never claim an image was made.

## 1. Prompt shape

- **Short, plain, descriptive: 25–60 words, one subject.** Order: subject → wardrobe → place and light → camera or lens → medium. Natural phrases, not stacked rules or `REFERENCE AUTHORITY` blocks.
- **Parameters go last**, on one line (§2). Keep the version and aspect from `decisions.md`.
- **Fixed sentences are copied letter for letter** from the registry (`MJ 문장`, ≤ 40 words). To change one, make a new `_v2` in the registry first, never in the prompt.
- **Negatives:** `--no` with a few words, only for a thing that actually appeared. No sentences of "no X".
- **No text, logos or captions** in the image unless the canon allows them.
- **Appeal words** (`cute`, `likable`, `quirky`, `beautiful`) → describe structure instead (full cheeks, large round eyes, soft brows). Personality belongs to the `ACTING PROFILE`, not the image prompt.
- **A person who feels real:** add one or two ordinary details (a small mole, a few flyaway curls, faint redness at the nose), soft even daylight like an ID photo. Name each by screen side and feature, then write the side actually seen into the registry after the result (the side may come out mirrored).

## 2. Parameters (verify in the user's current Midjourney docs)

Sources for this table were third-party guides, not the official docs. Use only these, with the version the user named; for anything else say "확인 필요".

| Purpose | Parameter | Note |
|---|---|---|
| Aspect | `--ar 16:9` | from `decisions.md` |
| Version | `--v 7` (or the user's version) | |
| Aesthetic strength | `--stylize N` | high values can overpower a reference |
| Randomness | `--chaos N`, `--weird N` | leave out unless asked |
| Exclude | `--no a, b` | few words |
| Style reference | `--sref [image link]` | style only |
| Character / object reference | `--oref [image link]` with `--ow N` | V7 and later; older versions used `--cref`. Reachable link required |
| Image prompt | the link placed first in the prompt | composition and content hints |
| Reproducibility | `--seed N` | helps comparison only, not identity |

## 3. References and consistency

- The first approved face image is the character reference for every later view. The user pastes its link; you place it in `--oref` and say so on the "참조" line.
- Drift: change one thing per run (lower `--stylize`, or raise the reference weight, or shorten the prompt). Same failure twice → rule 7: another reference or framing.
- Where an asset exists only as a text sentence, say so; do not invent a reference.

## 4. Art style (task 9)

An illustration or a fixed look is set with a style reference image (`--sref [link]`), kept in `decisions.md` §3 as the style link. Ask the user for one reference image or a few words of the look; propose `--sref` and a `--stylize` value; record the approved link as `ST-001`.

## 5. Which stage file

| Task | Open |
|---|---|
| Character (new, editing) | `character.md` |
| Location (new, new view) | `location.md` |
| Prop | `prop.md` |
| Still or start frame | `first-frame.md` |

## 6. Checklist before showing a prompt

- [ ] 25–60 words; one subject; parameters on the last line; no text request
- [ ] Fixed sentences identical to the registry, down to the letter
- [ ] The version and aspect match `decisions.md`; only listed parameters used
- [ ] Every reference has a link the user will paste, named on the "참조" line
- [ ] Directions are screen directions, at most one clause
- [ ] Risk list shown; no appeal words; one change if it is a re-run

## 7. After the result: the revise loop

1. The user pastes the image or says in words what is wrong. A word complaint is enough: do not ask for the image.
2. Name the cause in one line, pick **one** change (a word of the sentence, one parameter, or the reference weight), and give the full new prompt with the change shown as "전 → 후". Keep the fixed sentences untouched.
3. The user runs it again and brings the next result. Same failure twice → instructions rule 7.
4. A pasted image is judged item by item (instructions rule 8); on approval go to the OK record.

Judge item by item (instructions rule 8). On approval write the OK card (`mj-production` §4). The user saves the image under its asset file name (`char_<인물>_<상태>_v1`, `loc_<장소>_<뷰>_v1`, `prop_<물건>_v1`) in their own `00 에셋` folder; the registry keeps the link.
