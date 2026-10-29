# Location — edit of the same photograph (LOCKED EDIT)

This is work that locks the camera. The opening sentence and the `CHANGE / PRESERVE EXACTLY / ONLY CHANGE` grammar are in `SKILL.md` §1·§3.

## Required information

| Required information | Template slot |
|---|---|
| Approved parent job, lineage type (STATE / FIX / CLEAN) | `<<<image_1>>>`, record |
| The one thing to change and its position (screen terms) | `CHANGE — [TARGET AND LOCATION]` |
| Task: object edit (ROTATE / STATE / ADD / REMOVE) / light-or-occupancy state plate / era-or-material replacement / keep only the layout and transform | Template 1 / 1 / 2 / 3 |
| For removal, the surface to be revealed; for addition, the existing anchor | formula line |
| What to preserve: architecture, attributes of unchanged targets | `PRESERVE EXACTLY` |

## Rules

- **One change.** Only two changes that do not hold if separated (a lit screen and that screen's light) are written as `two changes` and two CHANGE blocks. Time of day (removing the sun, the sky) and turning on a light source can be separated, so split them into two generations. When split, tell the user in one line that the step-1 result is not yet the requested state (e.g. night).
- **When changing direction, lock the position; when changing state, lock the shape and direction.**
- **Identify the target as one thing, tied to its position:** `the nearest [object]`, `the [object] on the RIGHT` (screen terms).
- **Do not re-describe the location.** Do not widen an ambiguous target.
- **Do not do an edit that moves something from A to B in one generation.** Split into two steps REMOVE → ADD, or split the views.
- **A state plate that changes only light or time of day is a STATE.** When changing only the occupancy, add to an existing anchor, without faces.
- **If the edit changes the light,** remove the parent's LIGHT LOCK from PRESERVE and write only the changing light source in CHANGE. Light sources that do not change stay in PRESERVE. When confirmed, record that STATE view's LIGHT LOCK separately in the asset registry. A new LIGHT LOCK proposal uses the light source's screen side + object; if the position is unknown, ask.

## Template 1 (틀 1) — object edit and state plate

Put one of the formulas below into CHANGE of the `SKILL.md` §3 template, and add the attributes of unchanged targets to `PRESERVE EXACTLY`.

```text
ROTATE  Keep [object] in the exact same position, at the same height and on the same mount. Rotate only
        [named part] [degrees / direction] so that it faces [target]. Preserve its design, scale and support.
STATE   This is the same object in the same position with one state change only: [old state] becomes
        [new state]. Preserve its shape, dimensions, material, orientation and surroundings.
ADD     Add [subject / object] only at [existing anchor], matching its existing scale, perspective, contact
        and light. Do not alter the anchor or surrounding structure.
REMOVE  Remove [object] from [location]. Continue [revealed surface] naturally through the vacated area.
        The object is completely gone; no residual shadow, indentation, fragment or duplicate.
```

**Corrections**
- It moves away while rotating → `Rotate it in place around its existing mount; do not translate, raise, lower or resize it.`
- The design changes when the state changes → `The same [object], [its parts], dimensions and orientation remain unchanged; only its [state] changes.`
- The added subject hides structure → `Place the new subject within the existing [anchor], at its established scale, without moving or covering adjacent landmarks.`
- Even the surroundings get redesigned → `Every unnamed object and surface remains in its exact position, scale, orientation, material and colour.`

## Template 2 (틀 2) — era/material/design replacement (one layer per generation)

An era is not a single line like `1960s style` but a bundle of layers. Specify the target-era counterpart for each original element, and do not create new building volumes. Change one layer, confirm it, and use that confirmed version as the parent of the next layer.

Layers: `IDENTITY AND TEXT` (sign boards and their lettering policy) · `STRUCTURAL SURFACES` (walls, floor, roof, road paving) · `DOORS, WINDOWS AND FRAMES` · `FURNITURE / VEHICLES / FIXTURES` (benches, signpost poles, streetlights, cars) · `LIGHTING` · `IMAGE CHARACTER` (grain, sharpness, contrast, exposure). Put an element in only one layer (the sign board in `IDENTITY AND TEXT`, its pole in `FIXTURES`). Write that layer's name in `ONLY CHANGE`. The order of changes is also the order of this list (`IDENTITY AND TEXT` first → `IMAGE CHARACTER` last). One layer per step of the plan.

```text
Edit <<<image_1>>> WITHOUT reframing: camera position, camera height, angle, lens, framing, horizon line and perspective are LOCKED — zero reframing, zero recentering, zero zoom — this is the same photograph with one change only.
The [SOURCE IDENTITY AND ERA] is turning into [TARGET IDENTITY AND ERA]; this step changes only its [LAYER].
CHANGE — [LAYER]:
[Source element] becomes [its target-era counterpart], in the same position and at the same scale.
[One line per element of this layer.]
REMOVE: [source-era elements of this layer that must not remain].
PRESERVE EXACTLY:
- Camera, framing, perspective and composition
- Every building volume and opening position
- [The other layers, as they are now]
- [Untargeted environment — street, planting, distant background — and retained objects]
ONLY CHANGE: [LAYER]. Everything else remains identical.
[Era lock of the target scene]
```

In the intermediate steps of a multi-step era replacement, write only this layer in the target era and leave the other layers as `unchanged from the parent image`. Use the target era lock on the last line only at the last layer, and do not repeat the source era's name in intermediate steps.

**Corrections**
- Building form gets redesigned too → `Preserve every building volume, roofline, wall position, opening, gate and planting location; change only the named design layer.`
- Eras get mixed → `Remove every [source-era] vehicle, fixture, sign, handle and light. Nothing from the source era remains unless explicitly preserved.` (nouns of this layer only)
- New lighting breaks the exposure → `Replace the source fixtures with the named target sources while preserving the overall night/day exposure and composition.`

## Template 3 (틀 3) — keep only the layout and change the location

Choose the mode first and do not mix them.
- **A, camera also locked:** LOCKED EDIT. Lock the layout, perspective and camera distance. If there are several layers, one layer at a time as in Template 2.
- **B, borrow only the layout:** a new image (`only for the LAYOUT`). Do not lock camera or pixel structure. Since it is a new MASTER, include the dominant element, `Nothing else` and era lock from `location.md` Template 1.

For each anchor write wall membership and the front/back, above/below, side relations. Write in screen order left → centre → right, and do not mix material transformation and furniture preservation in one sentence.

```text
[A: LOCKED EDIT opening]
[B: Using <<<image_1>>> only for the LAYOUT — [anchors and relations] — generate a completely different
    image: [new real space]. Do not copy its camera angle, framing, materials, lighting or original context.
    CAMERA: [new camera position, height, direction and distance]]
PRESERVE THE LAYOUT ([A: as framed in the reference / B: directions as seen from [viewpoint]]; LEFT and
RIGHT are SCREEN directions, never the character's own left or right):
- [Anchor] on the LEFT [relation]
- [Anchor] at the CENTRE [relation]
- [Anchor] on the RIGHT [relation]
- [Furniture] below / beside / in front of [anchor]
[A only: same sizes, angles, perspective and camera distance.]
REMOVE THE ORIGINAL CONTEXT: [what must disappear].
REBUILD AS: [new place, era, permanent surfaces, real depth and functional details].
[A: ONLY CHANGE: [the one layer]. The layout, the named furniture, the camera and the framing stay 100% identical.]
[B: LIGHT: [sources and falloff]. Keep the layout above exactly. Finish and era lock as location.md 틀 1.]
```

**Corrections**
- Furniture positions change → `Keep every named anchor at the same place, size and angle, preserving all screen left/centre/right and above/below relationships.`
- Even the furniture to be kept changes → `Change only the permanent room surfaces. The named furniture remains the exact same objects with the same materials and wear.`
