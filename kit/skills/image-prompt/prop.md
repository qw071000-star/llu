# Prop

## Required information

| Required information | Template slot |
|---|---|
| Is a sheet needed? Does it appear large on screen, or only as a distant light/outline? | whether to make one |
| Object, material, signs of use | `[prop]`, `[Use marks]` |
| Size (cm + body reference) | size cue, asset registry |
| Physical properties in terms of weight | asset registry (the video's `PHYSICS`) |
| Materials/shapes that must not appear | `Avoid` |
| State changes in the story, who holds it in which hand (screen side + object) | asset registry `상태 머신` |
| For editing: which result is meant (that cut's job / the asset itself) | the target to edit |

## Rules

- **A prop whose state, hand or size changes is made as an independent asset.** Give it a worn look.
- **If no sheet is needed** (only a distant light), do not make one; propose writing it as a sentence in the cut prompt. Even so, show the proposed size (numerically: cm; for vehicle class, m + person reference), era and state in one line (for vehicles and signs, so that lettering and destinations are not legible). In this case do not use the asset registry `초안` line (instructions rule 4). If accepted, write that sentence only on the `[5] 소품` line of the cut card, and quote only that card line in the reply. Do not output a code block. **For vehicle/building class,** do not use the studio template below; crop it from a scene frame (location view) and make it an element.
- **Size is set in the scene.** Using a studio prop as a reference throws the size off. Make video elements by cropping from a scene frame.
- **A fixed description sentence has only material, shape, size and signs of use.** Do not include state (open/closed), posture (sagging/raised) or hands. Those go in the `상태 머신` and the cut prompt.
- **Write physical properties as weight.** Write it as sagging, not puffed up, no sharp angles.
- **Manage state with the `상태 머신`.** State between cuts is kept in the `shot-list.md` `연속성 표`.
- **When registering, write only the asset registry `초안` line.** Do not edit the shot list or `연속성 표`; only propose the lines to change.
- **Editing a confirmed prop:** edit the asset image with LOCKED EDIT (`SKILL.md` §3) and put size and shape in PRESERVE. If the original job is not in the registry, do not ask; write the element ID (`<<<prop_…_v1>>>`) as the edit source into the prompt, and tell the user in one line that the job is unrecorded. If the original image was not seen, write the PRESERVE background as `the existing background`, and mark any unseen state as "추정" (assumed). If the fixed description sentence changes, confirm it as a new element ID (`prop_<object>_v2`) and move the old one to the asset registry `폐기 목록`.
  - Cuts approved with the old element stay as they are. Whether to regenerate is asked per cut.

## Template

```text
Photorealistic product-reference photograph of [prop: material, wear, size cue], isolated on a plain
seamless light grey studio background, nothing else in frame — no scene, no room, no other objects,
no hands, no people. [Use marks.] Soft even studio lighting from the front-top, minimal shadow.
Sharp focus throughout. Avoid: [wrong materials], brand logos, text, watermarks.
```
