# First frame (the starting image of a video)

## Required information

| Required information | Template slot |
|---|---|
| Is the cut camera the same as the confirmed location view? (location view job). If the location view in the shot list is exactly the confirmed view or is blank, ask it as the first question and propose "같음(틀 1)" (same, Template 1) | mode: Template 1 / Template 2 |
| Location view job, that view's LIGHT LOCK | `<<<LOC>>>`, `PRESERVE EXACTLY` |
| For each character: element ID, wardrobe state, fixed description sentence | `REFERENCE AUTHORITY`, `WARDROBE` |
| Prop: position, state, who holds it, size (cm + body) | `PROP` |
| Camera: position (by objects on screen), height, what it looks at (when looking down, as in a foot/hand insert, give height and down direction together), distance, shot size (Template 2 also equipment names) | `CAMERA` |
| For each character: starting position (anchor, distance, contact), ongoing action, gaze, hands | `CHANGE` / `BLOCKING` |
| Number of visible people | `Exactly [N] people` |
| Final aspect ratio | settings |
| Anything specific to this cut that conflicts with a fixed description sentence (a prop in the open state; a bag written as held, but on the lap, etc.) | one `Except` line |

## Rules

- **Make the 0:00 state of that cut's video.** Not the thumbnail moment.
- **Choose the mode first.**
  - If the cut's camera is the same as the confirmed location view: write that view as a `LOCKED EDIT` and only add the people and props (Template 1).
  - If the camera differs: make a new viewpoint as a `DERIVED VIEW` (Template 2). If only this cut uses that viewpoint, write Template 2 directly; if several cuts use it, propose confirming the location view first (`location.md`).
  - Camera facing the opposite side of the location view: screen sides flip (`location.md` "Writing directions"). Rewrite the `In this view …` line at the end of Template 2 and the LIGHT LOCK as "전 → 후" (before → after).
  - In Template 1, adding people and props counts as one change (placing that cut's people in the empty location).
  - Changing only art style/texture from the same camera is a `LOCKED EDIT` (`SKILL.md` §3), not a `DERIVED VIEW`.
  - If you make a new viewpoint when the camera is the same, the location view and the first frame's composition will drift apart.
  - The unique sentences of Template 2 (`Do not inherit its camera angle, framing or composition.`, and for the opposite side the `not a horizontal mirror` sentence) go in even when rewriting an OK card that lacks them.
  - If it is "뒤에서" (from behind) but the character has their back against a wall/structure, what is behind is outside the wall. Propose putting the camera inside the structure, over the character's shoulder beside them.
- **Place characters at existing anchors.**
  - Write position as distance and contact. "근처에" (nearby) is not followed.
  - Write mid-action states.
- **Compare with neighbouring cuts.** Check the preceding and following lines of the shot list and the `연속성 표` (character position/posture, prop state).
  - If the `연속성 표` has no character position, take the BLOCKING line from one OK card of the most recent approved start image in which the same character appeared, and propose it. Do not invent a new position. Check that viewpoint and composition do not overlap, and that light direction and character position are the same.
- **When a fixed description sentence conflicts with this cut** (an empty-location "no cars" line, but a bus appears in the cut), do not edit the sentence. Right after it (the `[Except: …]` slot) add one line: `Except: [what exists only in this cut].`
- **If you change the sky or colour,** point out whether it conflicts with the asset registry's PALETTE·LIGHT LOCK and ask.
- **A cut edit that changes only age:** edit the approved start image with LOCKED EDIT (`SKILL.md` §3) and pick the age markers from the `CHANGE — AGE` list of `character-edit.md` Template 2. Do not invent markers.
- **When borrowing the colour feel of another OK**
  - In Template 1 (LOCKED) the colour comes from that location view. If the colour-base OK came from the same view, the colour is already the same, so do not attach a colour reference.
  - The colour reference handles texture. Do not write new texture sentences (`Real material truth` etc.).
  - For a different view, write Template 2 and attach a colour reference. If you must use Template 1, split into two steps (add people → colour edit) per the one-change-per-generation principle.

## Template 1 (틀 1) — when the camera is the same as the confirmed location view (LOCKED EDIT + ADD)

```text
Edit <<<LOC>>> WITHOUT reframing: camera position, camera height, angle, lens, framing, horizon line and
perspective are LOCKED — zero reframing, zero recentering, zero zoom — this is the same photograph with
one change only.
FIRST FRAME of a film shot — the exact state at 0:00 of the video. LEFT and RIGHT are SCREEN directions, never the character's own left or right.
CHANGE — ADD THE PEOPLE AND PROPS at existing anchors:
- [PERSON]: [anchor by objects, distance and contact], mid-[action], [gaze], [hands].
- [PROP]: [position, state, who holds it, size in cm and body terms].
REFERENCE AUTHORITY:
- <<<LOC>>> is the exact same photograph. It controls the place, the camera, the light and every object already in it.
- <<<CHAR>>> controls only [person]'s face, hair and wardrobe. Same face, same bone structure, same hair, same wardrobe.
- <<<PROP>>> controls only [prop]'s shape, material and state; its size is as described in CHANGE above.
DO NOT TRANSFER: the character sheets' backdrop, studio lighting, pose or framing.
WARDROBE: [asset registry sentence, verbatim].
PRESERVE EXACTLY: camera and perspective · every object already in the place · [this view's LIGHT LOCK, verbatim] · shadows, exposure, grade, grain
ONLY CHANGE: the people and props are added exactly as described. Everything else remains 100% identical.
Exactly [one person is / N people are] visible.
```

## Template 2 (틀 2) — when the camera differs (DERIVED VIEW)

```text
FIRST FRAME of a film shot — the exact state at 0:00 of the video. LEFT and RIGHT are SCREEN directions, never the character's own left or right.
Using <<<LOC>>> as the exact same location, generate a new view. Do not inherit its camera angle, framing
or composition. [If the camera faces the other way: This is a newly observed direction of the same physical room, not a horizontal mirror of the reference.] [CAMERA: position by objects, height,
direction, distance, shot size + camera body/lens/film stock.]
REFERENCE AUTHORITY:
- <<<LOC>>>: geography, materials, landmarks, light direction
- <<<CHAR>>>: face, hair, wardrobe only — Use the person in this reference. Same face, same bone structure, same hair, same wardrobe.
  Change only the pose, framing, location and lighting.
- <<<PROP>>>: shape, material and state only; size as described below
DO NOT TRANSFER: the character sheet's backdrop, studio lighting, pose or framing.
PRIORITY: the CAMERA block overrides every reference.
BLOCKING: [each person at an existing anchor: distance and contact, mid-[action]].
WARDROBE: [asset registry sentence, verbatim].
PROP: [position, state, who holds it, size in cm and body terms]. [Except: …]
[PALETTE · ERA LOCK from the asset registry, verbatim]
Nothing else except the people and props named above: [the registry's Nothing else list, without its no-people item].
[아래 두 줄: 반대편 카메라면 필수. 이 표시 줄은 지운다]
In this view [landmark] is at screen [side] and [landmark] is at screen [side].
LIGHT LOCK for this view: the light comes from screen [left/right], the [object] side.
Exactly [one person is / N people are] visible.
```
