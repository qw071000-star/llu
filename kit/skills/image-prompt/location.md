# Location

For the first empty-space master use Template 1; for a previously unseen space of the same building use Template 1-B.

## Required information

| Required information | Template slot |
|---|---|
| Location identity (era, region, use) | first line `[SPACE]` |
| For a new space in the same building: reference jobs, shared material/window/lighting rules, the space's function and circulation | Template 1-B first line, `FUNCTION`, `CONTINUITY` |
| Camera position, height, direction, shot size | `CAMERA` |
| The element seen first | `THE DOMINANT ELEMENT` |
| Walls, openings, floor, ceiling per direction; vanishing point (long-axis space) | `SPATIAL GEOGRAPHY` |
| What must be absent | `Nothing else` |
| Palette ratio, materials, signs of use and where | palette, `Real material truth`, `Real aged surfaces` |
| Light source, the screen side the light comes from in this view and the object on that side, time of day | light sentence (LIGHT LOCK) |
| Image finish (camera, lens, film) | `Image finish` |
| Era lock (season, year, place) | `Era lock` |
| Does it contain lettering, like signs or price tags? | no-text line |
| For a new viewpoint or edit: that file's table | `location-view.md` / `location-edit.md` |

## Rules

**A location is an asset of the work.** If a new axis is needed, do not turn the camera with a cut prompt; confirm one more view. Exception: if that axis is used in only one cut, first-frame Template 2 (`first-frame.md`).
- What opens a new view: 180° opposite, eye level → high angle, beyond a threshold.
- What is not a new view: closer or wider from the same direction, only the person's position differs.

**Lineage:** branches from `MASTER` as follows.
- `CLEAN`: a version with only structure/layout tidied, LOCKED
- `VIEW`: camera change, DERIVED
- `PROP`: prop enlargement, DERIVED
- `STATE`: light/occupancy/prop state, LOCKED. If a camera change gets mixed in, it is a VIEW, not a STATE
- `FIX`: error removal, LOCKED

Only an approved child becomes the next parent. Do not derive from a discarded variant. Do not attach children to each other. For a sibling view, change only CAMERA·FRAMING (foreground/midground/background) from the parent prompt and keep the rest identical to the letter.

**Writing directions (instructions rule 6: all in screen terms)**
- In MASTER GEOMETRY, write the reference viewpoint first in parentheses: `(directions as seen from [camera position], looking at [what])`.
- Write LIGHT LOCK as the screen side of that view + the object on that side: `Low dusk sun from screen left, the [object] side, is the only key.` Because the object has a name, the light stays the same even if the view changes.
- There is one LIGHT LOCK per view. For the opposite-direction view, flip left and right and write that view's LIGHT LOCK anew (`from screen right, the [object] side`), and record it on that view's line in the asset registry.

**How to write**
- **Write the era by objects, materials, lettering and finish. Not by colour.** Separate past and present by the presence of film grain.
- **Verify era and period accuracy against sources.** If an anachronism is intended, record it as such.
- **Use equipment names (camera, lens, film stock) only for still images.** For video, use the field of view (degrees).
- **For a long-axis space (corridor, platform, passage), write the vanishing-point position directly and drop `Rule of thirds`.** One-point perspective and the rule of thirds collide.
- **Only for an empty-space reference plate** use the diagonal (`the room read at an angle, not square-on`) and `Rule of thirds composition.` Real cuts and first frames follow the cut's angle.
- **`Empty deserted [space], still air.` is stronger than `no people`.** To convey scale without a person: `A person standing here would be small in all this space.` (if narrow, `would fill most of the room`).
- **If there are two or more objects of the same kind, distinguish them by name and position.**
- **Write the hinge of a door or hinged furniture relative to an object** (`hinged on the edge nearer the wardrobe`). Do not write it relative to the camera, like `nearer the camera`.
- **When moving a sentence to another location, check the light source, material and furniture nouns line by line.** The sibling-plate rule holds only within the same location.
- **For an object whose shape keeps coming out wrong, write the shape as it appears on screen:** `reads as a TALL NARROW RECTANGLE`
- **Write a nameless crowd without faces:** `seen from behind … no faces visible anywhere, dissolving into darkness toward the edges`. Do not use it for a character named in the script.
- **If a lit light source bleeds:** `lit but does NOT glow: no halo, no bloom, no light spilling onto [surfaces]`
- **Lettering:** `[Hand-lettered signage], text not legible. No legible text anywhere.` Do not put actual wording in quotes. The model will try to write it.

**Record:** When confirmed, write it into the asset registry. Do not put MASTER GEOMETRY in cut prompts before approval.
- MASTER GEOMETRY (3-4 sentences, including the reference viewpoint; metres/heights only when there is a basis)
- LIGHT LOCK per view (one sentence, screen side + object)
- PALETTE, ERA LOCK, FINISH (one sentence each)
- Lens per view (mm = °)
- `Nothing else` list
- View lineage (parent, type)

## Template 1 (틀 1) — master (empty space)

```text
Generate [SPACE].
CAMERA: [shot size], camera at [height and position], looking [direction][, the room read at an angle,
not square-on / for a long axis: strict one-point perspective, the vanishing point at (position)].
THE DOMINANT ELEMENT: [the one thing seen first, ideally the light source].
SPATIAL GEOGRAPHY (directions as seen from [camera position], looking [direction]; LEFT and RIGHT are
SCREEN directions, never the character's own left or right):
At the FAR END, [ ]. The RIGHT wall [ ]. At the LEFT, [ ]. [Floor, ceiling, openings.]
Nothing else: no [ ].
Empty deserted [space], still air.
Palette of roughly 80% [ ] — 15% [ ] — 5% [ ].
Real material truth: [ ]. Real aged surfaces: [wear and where it is].
[Light logic, one sentence: the light comes from screen [left/right], the [object] side.]
[Image finish: camera body, lens, film stock.] [Era lock: season, year, place. Nothing more recent
anywhere in frame.] No legible text anywhere.
[Reference plate only, not for a long axis: Rule of thirds composition.]
```

Write the lines outside the block as in instructions "Output": `모드: 신규`, references (none for Template 1; A·B for 1-B), model, resolution, save folder.

## Template 1-B (틀 1-B) — new space in the same building (new MASTER)

Lock as building rules only what repeats in common across the references: material family, the language of doors/windows/frames, lighting method and colour temperature, era, maintenance condition. Do not assert a floor plan the references do not show as fact. Write permanent structure and circulation first, functional furniture next.

```text
Using [<<<A>>>, <<<B>>>] as the same building's material and architectural register — [floor], [wall],
[window / frame], [door] and [lighting rule] — generate a NEW [SPACE] belonging to the same [BUILDING TYPE].
Do not copy the reference rooms' camera, framing, furniture or layout.
CAMERA: [as 틀 1].
THE DOMINANT ELEMENT: [ ].
SPATIAL GEOGRAPHY (directions as seen from [camera position]; LEFT and RIGHT are SCREEN directions, never the character's own left or right):
At the FAR END, [ ]. The RIGHT wall [ ]. At the LEFT, [ ]. [Floor, ceiling, openings and circulation.]
FUNCTION: [required landmarks, furniture and fixtures], arranged for [real use], with a clear entry,
circulation path and working zone. Nothing else: no [ ].
CONTINUITY: use the same [materials, frame profiles, door language, lighting temperature and
maintenance level] as the references.
LIGHT: [sources, falloff]. [Light logic, one sentence: the light comes from screen [left/right], the [object] side.]
Empty deserted [space], still air.
[Palette · material truth · finish · era lock as 틀 1]
```

**Corrections**
- Reference room's furniture gets copied → `Transfer only the building-wide material and architectural language. Do not copy the reference room's furniture, layout or camera.`
- Does not look like the same building → `Repeat the same [floor material], [glass-frame profile], [door language] and [light rule] as the references.`
- Comes out like a showroom with no function → `Arrange the permanent openings and required fixtures for the real operation of [function], with a clear entry, circulation path and working zone.`
