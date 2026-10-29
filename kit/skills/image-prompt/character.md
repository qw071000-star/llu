# Character + wardrobe sheet — new

## Required information

| Required information | Template slot |
|---|---|
| Age, origin, skin, face structure (face shape, jaw, cheekbones, nose, mouth; adults get mature adult bone structure), eyes (shape, colour) | `CHARACTER IDENTITY` |
| Build (what life has left on the body), shoulders, posture | `BODY AND PROPORTIONS` |
| Outfit: outerwear → closure → collar/pockets → inner layer/neckline → bottoms → shoes, allowed accessories, what is absent (`no bag`) | `OUTFIT` |
| Hair: length, texture, parting, shape around the face, rear view, colour, finish | `HAIR` |
| Headless-panel variant: A headless human body / B ghost mannequin (shared across the work, decided at the first sheet) | left line of `PANEL LAYOUT` |
| Background colour/texture, light direction and quality (shared across the work; use the line of the first confirmed sheet as is) | `BACKGROUND AND LIGHTING` |
| Is it a period piece? | prohibition line |
| If the character has dialogue: acting profile, voice sentence | asset registry (`acting` §6·§7; open that skill too) |

## Rules

**Spec (do not change within a work):** One 16:9 image divided vertically into 3. The three panels share the same background and the same lighting. The sheet is the original attached as a reference for every cut, so make it at the final resolution (2k) from the start. Checking at 1k and regenerating at 2k gives a different person. Use the work's default model and record the model actually used.
- Left: front full body from the neck down. Keep hands and shoes (to see sleeves and length)
- Centre: rear full body
- Right: front close-up from the chest up. The panel used as the face reference when generating cuts

**For a new sheet, write the whole of Template 1.** Do not copy the prompt of another sheet in the OK ledger as an example (it may be shorter or an old version).

**New-sheet writing order:** deliverable → identity → panels → build → outfit → hair → realism → background/lighting → consistency lock → prohibitions.

**Identity:** Do not make the character resemble a real actor or celebrity. A reference image is not the source of the face. Write objective facial-structure traits first, before subjective words like `beautiful`, `elegant`.

**Headless-panel variant — unify to one within a work**
- A headless human body: for checking fit and silhouette. The risk is an injury image. The `not an injury` sentence must be included (Template 1).
- B ghost mannequin: for confirming garment cut. The risk is a plastic mannequin. Do not use `mannequin` alone. Replace the left line of Template 1 with:
  `LEFT PANEL: a front-facing full-body wardrobe view: the outfit holds its own shape as if worn by an invisible person, hollow ghost-mannequin product photography, no mannequin material visible anywhere, the collar opening is empty and shows the dark hollow inside the garment, cut off cleanly just above the shoulder line with NO head, NO neck and no shoulder stump protruding, no plastic torso, no stand, no pole, no base, real human hands emerge from the ends of both sleeves hanging relaxed slightly away from the sides, the shoes stay on the floor at the bottom of the trousers.`

**Frequent accidents and sentences to add**

| Symptom | Sentence |
|---|---|
| A head appears above the left neck | In the opening sentence: `including the intentionally HEADLESS left panel` + `Do not add, infer, reconstruct or complete a head or face in that panel` |
| Plastic mannequin | `hollow ghost-mannequin, invisible person, empty collar, no dress form, no stand` |
| Occupational props appear on their own | `No profession-signaling props unless explicitly requested: no stethoscope, instruments, clipboard, pen, bag or visible logo.` |
| Garment floats off the floor | `the garment stands on the floor with a natural contact shadow, not floating, not tilted` |
| Looks too young | `mature adult bone structure, defined nasolabial folds, no babyface` |
| Hair keeps the old era | `matte and modern, no pomade shine, no sculpted vintage wave` (when moving to the present) |
| Badge/name-tag text garbled | `a plain blank badge, no writing, no photo, no logo` |
| Tone/grain drifts | instead of "같은 룩" (the same look), the four words `palette, contrast, grain, falloff` |

**Derivatives and elements**
- Derive only from the confirmed version. Never make a derivative of a derivative. Never delete the confirmed version.
- Make video elements separately for each outfit/hair state (`char_<character>_<state>_v1`). If the state changes within one video, attach both elements and split by time range.

**Record:** When confirmed, write into the asset registry: the IDENTITY and WARDROBE fixed sentences, job ID, the model actually used, variant (A/B), limitations. Put only the WARDROBE sentence into cut prompts, letter for letter. The face is handled by the reference. The prompt and settings live on the asset ID card in the OK ledger.

## Template 1 (틀 1) — new

```text
Create a photorealistic single wide horizontal three-panel character reference sheet of the same
[woman/man]. The image is divided into three clean vertical sections with no borders, captions or text.

CHARACTER IDENTITY:
[age, origin, skin tone and texture, face shape and bone structure (adults: mature adult bone structure,
defined nasolabial folds), eye shape and colour, brows, nose, mouth, neutral expression]. The eyes have
naturally muted catchlights and no oversized specular glare in the iris. The same exact identity must be
maintained wherever the face is visible.

PANEL LAYOUT (LEFT and RIGHT are SCREEN directions, never the character's own left or right):
- LEFT PANEL: a front-facing full-body wardrobe view shown strictly from the neck down. The panel is
  intentionally HEADLESS and ends cleanly at the base of the neck. This is an editorial clothing crop,
  not an injury: no head, no face, no wound, no gore, no dark opening. The plain background continues
  cleanly above the neckline. The figure stands straight, both arms relaxed slightly away from the sides,
  both hands visible and empty, feet fully visible.
- CENTER PANEL: a full-body rear view of the same person from head to toe, standing straight in the same
  neutral pose. The back of the hair, clothing and shoes are clearly visible. Hands empty.
- RIGHT PANEL: a large front-facing close-up portrait of the same person, framed from the upper chest
  upward, with the same calm neutral expression, the gaze with a definite focal distance just behind the
  lens. The face is centered and unobstructed.

BODY AND PROPORTIONS: [build, shoulders, posture]. Keep exactly the same body proportions in the left and
center panels.
OUTFIT — IDENTICAL IN ALL THREE PANELS: [outer → closure → collar/pockets → inner/neckline → bottoms
→ shoes → allowed accessories]. The neckline and every visible clothing layer must match between panels.
The garment is one physically identical outfit seen from different views, with matching fabric, color,
length, fit, construction and layering. No logos, no prints, no visible brands, no unintended accessories.
No profession-signaling props unless explicitly requested.
HAIR — CENTER AND RIGHT PANELS: [length, texture, parting, shape around the face, rear view, colour,
finish]. The haircut and color must match perfectly between the rear view and the portrait.
REALISM: visible fine skin texture with natural pores, age spots, fine lines, subtle asymmetries and
uneven skin tone, no digital smoothing, no beauty filter, no AI-airbrushed look, skin completely free of
artificial glare shine or highlight blooms, matte natural complexion[; older: lined forehead and crow's
feet at the outer eyes, reddened knuckles and short unpainted nails]. Eyes have genuine moisture and a
small specular catchlight, one eyelid sits very slightly lower than the other, faint capillaries at the
inner corner, natural tear-line, the iris shows real fibrous texture and a soft pupil edge.
BACKGROUND AND LIGHTING: one continuous plain [colour/texture] studio backdrop across all panels, [light
direction and quality], gentle realistic shadows. All panels share the same lighting direction, exposure,
palette and photographic finish.
CONSISTENCY RULES: The three panels must depict one and the same person: identical face, age, skin tone,
body proportions, hair color, outfit materials and color. Do not create three similar models. Preserve the
exact left-to-right order: headless front outfit view / full-body rear view / front close-up portrait.
no text, no watermark, no logos, no frame borders, no captions, no labels, no other people, no duplicate
figures, no extra panels, no props, no furniture, no background objects, no collage decorations,
[adults: no babyface, no overly youthful rounded proportions,] no beauty filter, no airbrushing, no plastic
skin, no glossy skin, no distorted anatomy, no extra fingers, centre panel standing full-body head-to-toe
not cropped not sitting, right panel a tight close-up not a full body[, period: no modern clothing, no
modern eyewear, no smartphones, no modern signage]
```
