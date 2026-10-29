# Location — new viewpoint (DERIVED VIEW)

This is work that changes the camera.

## Required information

| Required information | Template slot |
|---|---|
| Approved parent job, lineage type (VIEW / PROP) | `<<<image_1>>>`, record |
| Which task: opposite direction / new viewpoint from the same side / prop enlargement | Template A / B / C |
| New camera: relation to the original camera, height, direction | `CAMERA` |
| One subject, screen share, 1-3 landmarks to keep, what to push out of frame | `FRAMING` |
| For the opposite direction: camera method (move to the far end / rotate 180° in place; if the parent camera is outside the subject and the user says to look "안에서" (from inside), move to the far end), endpoint of the new direction, repeated elements, numbers/signs | Template A |
| Parent's MASTER GEOMETRY · palette · era lock · finish (asset registry, letter for letter) | inheritance line |
| This view's LIGHT LOCK (screen side + object) | last line |

## Common

- **Write the new camera as a relation to the original camera.** Do not let one word like `reverse` or `close-up` stand in for the camera relation.
- **Write height as a value.** Standing eye level about 1.6m, seated eye level about 1.1m, chair/bench seat about 0.45m, near the floor 0.3m or less. If something like "벤치 높이" (bench height) can be read two ways, propose a value.
- **One subject.** Lock its design/state, its position relative to its surroundings, and 1-3 landmarks. Do not lock framing and on-screen size.
- **Change only CAMERA·FRAMING in the inheritance sentence.** Lines the asset registry lacks (palette, era lock, finish) are taken letter for letter from the prompt on the parent OK card. If neither has them, do not invent; ask. Left/right in MASTER GEOMETRY is from the parent viewpoint; this view's screen sides (flipped for an opposite view: `location.md` "Writing directions") go on the `In this view …` line. After the first line add `Use <<<image_1>>> as the sole geometry and design authority; do not inherit from discarded variants.`
- **If the camera enters a structure,** leave the MASTER GEOMETRY line as is and override it right after with one line `Except: [only what is visible in this view].`
- **End the LIGHT LOCK line exactly as written.** Do not append explanation or parentheses after it.

## Template A (틀 A) — opposite direction

For a long-axis space, width, vanishing point and repeat spacing come before materials.

```text
Using <<<image_1>>> as the exact same [SPACE] — same [materials, repeated elements and light logic] —
generate the OPPOSITE-FACING view. Do not inherit its camera angle, framing or composition.
CAMERA (exactly one of):
  The camera now stands at the far end, looking back along the same central axis toward the original
  camera position.
  From the same camera point, rotate the camera 180 degrees in place and look down the continuation
  behind it.
At [height]. [Strict one-point / natural] perspective, the vanishing point [position].
SPATIAL CONTINUITY:
- Same width, height and proportions
- Same rhythm and spacing of [repeated elements]; repeated elements diminish evenly toward one vanishing point
- Same materials, wear and light logic
- The perspective ends at [endpoint]. No extra junction, stair, window or side opening.
- [Numbers, plates, signs]: plain and unmarked, text not legible
This is a newly observed opposite direction of the same physical [space], not a horizontal mirror of
the reference.
[Parent's MASTER GEOMETRY with its viewpoint · palette · era lock · finish — verbatim]
In this view [landmark] is at screen [side] and [landmark] is at screen [side]. [This view's LIGHT LOCK: the light comes from screen [side], the [object] side.]
```

Keep only one of the two CAMERA lines. Do not mix them or compromise on a middle expression.

**Correction** Width/spacing changes → `Preserve the exact [space] width, ceiling height and regular [element] spacing; repeated elements diminish evenly toward one vanishing point.`

## Template B (틀 B) — new viewpoint of the same location (close-up, medium, top view, oblique, low viewpoint)

For top view, oblique and low viewpoint, also write the negative range (`not from straight above, not from the side`). Even if an object outside the frame appears in the inheritance sentence, do not delete it. The `fall outside` line of FRAMING wins.

```text
Using <<<image_1>>> as the exact same [LOCATION] — same [materials, landmarks and light logic] —
generate a NEW [CLOSE-UP / MEDIUM SHOT / TOP VIEW / OBLIQUE VIEW].
Do not inherit its camera angle, framing or composition.
CAMERA: Move from the reference camera [path and distance]. Place the camera at [height and side],
looking [direction] at [subject] with [perspective]. [Negative range.]
FRAMING: [Subject] fills [amount] of the frame. Keep [1–3 landmarks] visible. [Objects] fall outside
the tighter frame. The background [focus treatment].
CONTINUITY: Preserve the exact design, proportions, material, wear, state and placement relationships
of [subject and anchors]. Keep the same lighting direction, palette and era.
Move in from the same side and along the same line of sight; no reverse angle and no view from behind.
(새 방향이면 위 줄 대신: This is a newly observed direction of the same physical room, not a horizontal mirror of the reference.)
[Parent's MASTER GEOMETRY with its viewpoint · palette · era lock · finish — verbatim]
In this view [landmark] is at screen [side] and [landmark] is at screen [side]. [This view's LIGHT LOCK: the light comes from screen [side], the [object] side.]
```

**Corrections**
- Turns into a new location → `This is the exact same [location / object], preserving its design, materials, state and spatial relationships; only the camera view changes.`
- Surrounding furniture remains in the close-up → `Only [subject] and [narrow context margin] remain in frame. [Furniture list] is outside the tighter composition.`
- Top view comes out oblique → `The optical axis is perpendicular to the surface; its rectangle is square to the frame with no oblique side view.`

## Template C (틀 C) — a prop in the location as a separate asset (lineage PROP)

Choose only one shot type: context close-up (1-3 landmarks) / prop-centred (only a narrow border of the contact surface) / straight-on view / oblique close view. Do not mix the context type with a no-background product shot (`prop.md`). Do not describe the design anew; lock the original's attributes.

```text
Using <<<image_1>>> as the exact same [LOCATION] and the exact same [PROP], generate a
[CONTEXT CLOSE-UP / PROP-CENTRED CLOSE-UP / STRAIGHT-ON DETAIL VIEW / OBLIQUE DETAIL VIEW].
Do not inherit its camera angle, framing or composition.
PROP CONTINUITY: Preserve the exact silhouette, proportions, construction, component positions,
material, wear, colour and operating state of [PROP].
CAMERA: The camera [moves / stands] [relative position], at [height], looking [direction] from [angle].
[Perspective constraint and negative range.]
Move in from the same side and along the same line of sight; no reverse angle and no view from behind.
(새 방향이면 위 줄 대신: This is a newly observed direction of the same physical room, not a horizontal mirror of the reference.)
FRAMING: [PROP] fills [almost the entire image / most of the frame]. Keep [narrow contact surface or
landmarks]. Exclude [room / furniture list].
DETAIL: [surface detail that must be visible]. Do not redesign or add components. Any lettering on it:
text not legible.
LIGHT: Use the same source direction and colour logic as the location. [Lit practical: lit but does
NOT glow: no halo, no bloom.]
[Parent's finish and era lock — verbatim]
```

**Corrections**
- Design changes → `This is the exact same prop, not a redesign: preserve every major contour, component, proportion, material and wear mark.`
- Too much of the surrounding room remains → `The prop and its immediate contact surface occupy nearly the whole frame; no chairs, couches, walls or unrelated furniture are visible.`
- Location identity disappears → `Retain [one or two landmarks] at the frame edge, softly out of focus, to confirm the same location.`
- Thickness disappears → `Keep the [physical edge] visible all around, with enough perspective to read the [prop] as a real object.`
