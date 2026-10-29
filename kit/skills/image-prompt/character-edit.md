# Character + wardrobe sheet — editing a confirmed sheet

The basis is that character's sheet card (job) in the OK ledger. Do not make a new one. Open only this file for editing (`character.md` is for new sheets). The sentences the template needs are already in it.

## Required information

| Required information | Template slot |
|---|---|
| Base sheet job, what to change (outfit = `Outfit` line / hair), new state (head to foot, down to the shoes) | Template 1 `CHANGE` |
| Old items to remove (by name, down to shoes and small props), new neckline | Template 1 `REMOVE COMPLETELY` |
| Is the edit an era move? | Template 1 `Era move` line |
| Did the user point to an outfit/hair reference image? (if they say "이걸로" (this one) but there is no image, ask) | Template 1 authority lines |
| Changing age ("50대처럼" (like in their 50s))? target age, age markers (wrinkles, skin, hair colour, posture, hands) | Template 2 `CHANGE — AGE`, `IDENTITY BONES` |
| Headless-panel variant A / B (same as the base sheet) | Template 1 LEFT PANEL line (A / B) |

## Rules

- Resolution 2k from the start and the work's default model, as for a new sheet (`character.md`). Outside the block, show each changed value as "전 → 후" (e.g. `나이: about seventy → about fifty-five`).

**When editing**
- Change only one thing at a time, outfit or hair. The exception is two changes that do not hold if separated, such as an era move (hair signals the era more strongly than clothes). If you bundle them as an exception, write the reason in one line.
- Do not re-describe the face; only instruct to preserve it. If a face sentence competes with the reference image, the face is regenerated.
- Outfit scope is `In all three panels`; hair scope is `Only in the center and right panels`. Using three panels for hair produces a head on the left.
- **Fill every neckline and [old 1]~[old 3] slot of the template** with the same items (the neckline is where edits fail most often).
- When moving the era, also erase by name the elements that make that era (hair grease, wide tie, logo, sneakers, etc.).
- Write the four cut details for the new outfit (length, closure, collar, pockets), and add `No profession-signaling props.` so no occupation-revealing props attach.
- When an outfit/hair reference image is attached, include the three authority lines of Template 1. Always include the `Do not transfer the face …` line, no exceptions.
- When changing age, use Template 2. Use the `IDENTITY BONES` line as in the template and do not invent new facial features (nose, eye shape, etc.).
- If the right-panel face becomes a different person in the result: delete the face description and write `Change the hair around the existing face; do not regenerate, reinterpret, beautify, age or reshape the face.`
- When confirmed, add a new state line (WARDROBE fixed sentence, job) to that character in the asset registry. Do not delete the old state.

## Template 1 (틀 1) — one outfit or hair change

```text
Edit reference image 1: change only the character's [outfit / hair], while keeping the character's
identity exactly and preserving the sheet's existing three-panel structure exactly, including the
intentionally HEADLESS left panel.

CHANGE — [OUTFIT / HAIR]:
[In all three panels, replace the current outfit with / Only in the center and right panels, change the
hair to] [new state, head to foot, including shoes]. [Outfit: The new outfit is one physically identical
outfit seen from different views, with matching fabric, color, length, fit and layering. No [things not
worn], no logos, no prints.] [Era move: nothing that dates the decade.]

REMOVE COMPLETELY:
[old 1], [old 2], [old 3] are GONE in every panel. Do not layer, merge or
hybridize old and new clothing. [Outfit: At the neckline, only [the new collar] is visible at the base of
the neck. No trace of [old 1], [old 2], [old 3] remains, including in the headless LEFT panel.]

[Clothing or hair reference attached:
Reference image 1 controls identity, face, body proportions, poses, panel layout, framing, background,
lighting and photographic finish. Reference image 2 controls only the design, cut, length, material and
details of [the new item]. Do not transfer the face, body, pose, background or lighting from reference image 2.]

PRESERVE EXACTLY:
- LEFT PANEL: keep it intentionally HEADLESS, front-facing and framed from the neck down, an editorial
  clothing crop, not an injury. Do not add, infer, reconstruct or complete a head or face in that panel.
  Keep the clean neck crop and the uninterrupted plain background above it. [Outfit: Its clothes change
  fully: [new outfit summary], no [old 1], no [old 2], no [old 3].]
- [B ghost-mannequin sheet: instead of the LEFT PANEL line above] LEFT PANEL: a front-facing full-body wardrobe view: the outfit holds its own shape as if worn by an invisible person, hollow ghost-mannequin product photography, no mannequin material visible anywhere, the collar opening is empty and shows the dark hollow inside the garment, cut off cleanly just above the shoulder line with NO head, NO neck and no shoulder stump protruding, no plastic torso, no stand, no pole, no base, real human hands emerge from the ends of both sleeves hanging relaxed slightly away from the sides, the shoes stay on the floor at the bottom of the trousers.
  [Outfit: Its clothes change fully: [new outfit summary], no [old 1], no [old 2], no [old 3].]
- IDENTITY: preserve the exact same face — identical facial features, bone structure, skin, age, eye
  shape, nose, lips and expression. Do not regenerate, reinterpret, beautify, age or reshape the face.
- STRUCTURE: preserve all three poses, body proportions, crop boundaries, panel widths, panel order and
  empty hands.
- ENVIRONMENT: preserve the existing background, lighting direction, exposure, shadows, palette, contrast,
  grain and falloff.

ONLY CHANGE: [the outfit in all three panels including the neckline of the headless panel / the hair in
the center and right panels]. The face and identity 100% identical to reference image 1.
no head on the left panel, no mannequin, no other people, no duplicate figures, no props, no text,
no watermark, no logos, no frame borders
```

## Template 2 (틀 2) — change only the age (same person, different age)

A request like "20대인데 50대처럼 보이게" (a person in their 20s, but looking like in their 50s). Do not re-describe the face. Keep the bone structure and change only the age markers. The age markers (wrinkles, skin, hair colour, posture) do not hold if separated, so count them as one change. Leave the outfit as it is. Keep the result separately as a new-state element (`char_<character>_<age>_v1`).

```text
Edit reference image 1: age the same person to [target age], while keeping the character's identity
and preserving the sheet's existing three-panel structure exactly, including the intentionally HEADLESS
left panel.

CHANGE — AGE:
In the center and right panels, the same person is now [target age]: [age markers — forehead lines and
crow's feet, softened jawline, slight sagging under the eyes, thinner lips, greying at the temples,
skin texture of that age]. In the left and center panels, the posture settles slightly with age:
[shoulders, stance]. Hands in every panel show the same age: [knuckles, veins, skin].

PRESERVE EXACTLY:
- IDENTITY BONES: the same face shape, bone structure, eye shape and colour, nose shape, mouth shape and
  ear shape. The person must be recognisable as the same person at a different age. Do not replace
  the face with a different person.
- LEFT PANEL: keep it intentionally HEADLESS, an editorial clothing crop, not an injury. Do not add,
  infer, reconstruct or complete a head or face in that panel.
- OUTFIT: the exact same clothes in every panel.
- STRUCTURE and ENVIRONMENT: panel widths, panel order, crop boundaries, empty hands, backdrop,
  lighting direction, exposure, palette, contrast, grain and falloff.

[늙게]
ONLY CHANGE: the visible age of the same person. no babyface, no exaggerated old-age makeup, no other people, no text, no watermark, no frame borders
[젊게]
ONLY CHANGE: the visible age of the same person. no babyface, no beauty filter, no other people, no text, no watermark, no frame borders
```

**When making younger,** write `[age markers]` in reverse: shallower wrinkles, hair colour (fewer or no grey hairs), straighter shoulders, firmer hands. Use only the `[젊게]` line for the last line (for older, the `[늙게]` line). **For a child's age** (10 → 12), write it by height, shoulders, limb proportions, face length and posture, and leave the skin as is.
