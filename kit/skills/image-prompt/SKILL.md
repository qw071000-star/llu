---
name: image-prompt
description: Use when writing or fixing AI image generation/editing prompts (GPT Image, Nano Banana, Seedream). Targets are assets (location, prop, character + wardrobe sheet, art style) and first frames that start a video.
---

# Image prompts — common

## 0. Pre-writing information check

Fill in the "required information" table of that asset type's file and the common table below.

| Common | Required information |
|---|---|
| Format | model, resolution (for confirmation), aspect ratio, number of images (1) |
| Save | save folder (`folder_id`) |
| References | image jobs to attach, their attach order, the role of each |
| Mode | new / edit, whether the camera is kept (§1) |

What to ask is in `context/must-ask.md`; how to ask is in instructions rule 4.

**Reference tags:** `<<<LOC>>>`, `<<<CHAR>>>`, `<<<PROP>>>`, `<<<OK>>>`, `<<<A>>>` in the templates are placeholders. Keep the angle brackets and replace only the name inside with the real element name or the attach-order name (`<<<loc_…_v1>>>`, `<<<image_1>>>`). The opening line works the same way: `Edit <<<loc_…_v1>>> WITHOUT reframing`. Number of references = number of tags = number of attached images.

**When a fixed description sentence conflicts with this cut** (an empty-location "no cars" line, but a bus appears in the cut), do not edit the sentence. Right after it (the `[Except: …]` slot of the template) add one line: `Except: [what exists only in this cut].`

## 1. Decide before writing

**① New or edit?** Once a result you like exists, do not regenerate it as new. Regenerating as new gives a different person, a different room. Attach that result as the reference and edit it.

**② Is the camera kept?** Never mix the two modes in one prompt; mixing compromises on a middle value. Using `WITHOUT reframing` together with an opposite direction or rotation (`reverse`, `rotate 180`, `turned round`) in one prompt is a contradiction.

| Mode | When | Opening sentence |
|---|---|---|
| `LOCKED EDIT` | a revised version of the same photograph | `Edit <<<image_1>>> WITHOUT reframing: camera position, camera height, angle, lens, framing, horizon line and perspective are LOCKED — zero reframing, zero recentering, zero zoom — this is the same photograph with one change only.` |
| `DERIVED VIEW` | a new viewpoint of the same location | `Using <<<image_1>>> as the exact same location, generate a new view from [position by on-screen objects], looking toward [object]. Do not inherit its camera angle, framing or composition.` |

**③ What does the reference control?**

| Authority | English | Scope of control |
|---|---|---|
| Same photograph | `the exact same photograph` | down to camera, framing, geometry |
| Same location | `the exact same room / location` | location identity (new viewpoint allowed) |
| Material register | `the same building's material register` | materials, windows/doors, lighting attitude |
| Layout only | `only for the LAYOUT` | relative positions of doors, windows, furniture |
| Element only | `only for [element]` | one named element |

## 2. Two or more references — authority block

```text
REFERENCE AUTHORITY:
- <<<A>>> is the exact same location. It controls geography, materials, landmarks and light direction.
- <<<B>>> controls only [person]'s face, hair and wardrobe.
- <<<C>>> controls only [prop]'s shape, material and state.
DO NOT TRANSFER:
- From <<<B>>>: the backdrop, its lighting, its framing or its pose.
- From <<<C>>>: its background, surface or camera angle.
PRIORITY: If the references conflict, <<<A>>> controls the space and the light; the character
reference controls identity and wardrobe only. Camera and shot size are defined below and override every reference.
```

- For a LOCKED EDIT, change the last line to `Preserve <<<A>>>'s camera, geometry and placement.` Only that one photograph holds the camera.
- **"구도만 참조" (reference the composition only) does not carry the composition over.** Use one of these:
  - Read the reference as coordinates per mass and write them out.
  - Write it as "reproduce as is + list of what to change".
- **"Reproduce as is" also carries over other attributes.** Split by attribute per reference: `Reference 1 gives the composition; take the [sky] only from reference 2.`
- **When an element image is replaced, fix the description in the prompt to match the new image.**
- **Never attach a storyboard thumbnail or a photo of a monitor as a reference.** Face, clothes and colour get mixed. If that composition is needed, first make an empty-location image with the same composition and use it as the location reference.
- **Do not attach or suggest any image the user did not point to,** even if the project has reference photos. If the user gave a spec in words, write it in words only.

## 3. Edit grammar — CHANGE / PRESERVE EXACTLY / ONLY CHANGE

**Every edit prompt: outside the block, show each changed value as "전 → 후", one line each.**

```text
[LOCKED EDIT 여는 문장]
CHANGE — [대상과 위치(화면 기준)]: Change [현재 상태] to [새 상태]. Keep its [position / scale /
orientation — only what this edit does not change] locked. [국소 빛·접촉.]
PRESERVE EXACTLY:
- Camera position, height, angle, lens, framing, horizon line, vanishing point and perspective
- The architecture: [walls, doors, windows, ceiling, floor]
- Every unnamed object in its exact position, scale, orientation, material and colour
- Existing light sources, shadows, exposure and reflections; colour grade, contrast, grain, depth of field
[인물이 보이면] WARDROBE: [asset registry sentence, verbatim].
ONLY CHANGE: [CHANGE와 같은 항목]. Everything else remains 100% identical.
```

- **Write the preserve list more specifically than the change.** Otherwise the rest gets redrawn a little too.
- **Make the CHANGE and ONLY CHANGE items identical.**
- **If a person is visible, include a `WARDROBE:` line.** Also put that sentence in the check's `--must-include` file.
- **A trivial, clear change can also be a short English instruction** (observed: Seedream, Nano Banana).

## 4. Crop and occlusion zones

- **First compute the visible band at the final screening ratio.** Keep the key elements inside that band.
- **Do not put the main subject in an occlusion zone (subtitles, presenters).** Put only incidental elements that may be covered.
- **Raising the high-angle pushes the sky and distant objects out of the band.** If they must be visible, lower the angle.
- **% coordinates and numbers are followed only roughly.** Write in screen-zone units (left third, top centre). If precision is needed, use a layout sketch (colour blocks) as a reference and write "follow the layout only".

## 5. Model notes

| Model | Note |
|---|---|
| GPT Image 2.5 | Specifying many elements pushes the texture toward a 3D render. Reduce the elements or put the texture paragraph first |
| Nano Banana Pro | May be processed by a different model than requested. Record the model actually used before confirming |

## 6. Pre-send checklist (what the check script cannot catch)

- [ ] Is the fixed description sentence identical to the asset registry, down to the letter?
- [ ] Did you check the crop band and occlusion zones?
- [ ] Is no placeholder tag (`<<<LOC>>>` etc.) left?
- [ ] Did you run the check script before showing it? (command and procedure: instructions "Check"). Put into `--must-include tmp/fixed-sentence-file`: the wardrobe, prop, LIGHT LOCK and coordinate sentences from the asset registry
