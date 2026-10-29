# Live-action / character cuts - 15 blocks

Do not open `acting` in a question turn. On the turn that writes the prompt, open `acting` before writing `CHARACTER_ACTING` (skip it only when every acting line comes verbatim from an OK; adding even one new acting sentence means open it).

## Blocks

- Order and titles are fixed. Keep the title even for a block with nothing to write.
- Put `PRE_SHOT_CONTINUITY` first only when there is state inherited from the previous shot.

Fill each block from the `SKILL.md` §0 table and the empty template below; this table lists only common mistakes and the rules the template does not show.

| # | Block | Common mistakes |
|---|---|---|
| — | `PRE_SHOT_CONTINUITY` | Inheriting without checking. Writing "previous shot": state each inherited item (position, pose, prop ownership, light) as its current state (`the bag is closed`) |
| 1 | `SCENE_CONTEXT` | Cramming camera/acting in here |
| 2 | `ACTIVE_REFERENCES` | A character line carries the registry WARDROBE sentence only, never the IDENTITY sentence. Tag not attached, or attached and unused. With a voice file, add `[NAME]'s voice 100% matches audio_[N]`. State change within one generation: attach two elements and split by time (`[A] until 0:04, [B] from 0:04`). A reference seen in only part of the shot: state the scope (`only inside the mirror, only 0:06–0:14`) |
| 3 | `LOCATION_MAP` | "near", "that door". Not re-stating, for this cut, which screen side each fixed object is on |
| 4 | `FIRST_FRAME_AND_SPATIAL_BLOCKING` | Widening to the whole shot |
| 5 | `FORMAT_MODE` | Cuts required in a single take. If a cut is needed: `hard cuts only at 0:0a; the camera never cuts by itself` plus, per cut, length, camera, first-frame character, action. If a character would vanish between cuts, put the cut mid-walk; if that still fails, remove the cut |
| 6 | `OPTICS` | mm, aperture, lens brand (convert mm with the `SKILL.md` §2 table). One lens per shot; the field of view changes only at cuts. Face, whole location and hand detail mixed in one beat (split the cut) |
| 7 | `CAMERA` | Compound moves |
| 8 | `ACTION_TIMING` | Empty intervals, changed counts |
| 9 | `CHARACTER_ACTING` | Emotion adjectives |
| 10 | `PHYSICS` | Unclear who is moving |
| 11 | `LIGHTING` | Asserting the reference photo's look |
| 12 | `AUDIO` | — |
| 13 | `STYLE` | Assuming style controls the face; more than one or two lines |
| 14 | `QUALITY` | — |
| 15 | `REQUIRED_AND_FORBIDDEN_CONSTRAINTS` | Accumulating past failures (Forbidden: item 6 of `SKILL.md` §1). Required: 3-5 states/counts to keep. Wanted state first, failure as outcome |

## How to trim

- **Cut events (`SKILL.md` §2 "Event count") before the length.** If it is still near 5,500 characters, trim in this order: location -> style -> environment (QUALITY, background description) -> acting sentences, starting with removing authority explanations in `ACTIVE_REFERENCES` that overlap `REFERENCE AUTHORITY`. If it shrinks only by removing fixed sentences, imported OK lines, or the ends of the emotional range, do not trim; leave a WARN (in the reason, write what you tried to trim and the characters cut. Example: `5,788자 유지: 인물 2·참조 4, 겹친 권한 설명 −300자`). With 2 characters and 4 references it is easy to go over. With three or more characters, splitting the shot comes before trimming.
- **Location information: the coordinate line + at most four lines.** Camera, fore/mid/background, light, and the path if needed. The longer it is, the more the character references get pushed out.
- **Do not include characters, tags, or scene numbers that do not appear in this shot.**
- **Narrow the scope of forbidden terms:** `no [X] on [Y]`. A forbidden term can summon the thing itself.
- **If the user says "put in everything to forbid"**, group by category (`[Faces and clothing]` `[Camera and editing]` …). Cut the event count further to compensate.

## Empty template

In addition to the lines outside the blocks (instructions "Output"), write in Korean: aspect ratio, sound, start/end image jobs, attached elements (start image included, in order; this count is the check script's `--refs`), risk list.

```text
[SCENE_CONTEXT]
[Era]. [Place, time of day]. [What happens in this clip, 2–4 sentences, only this clip.]

[ACTIVE_REFERENCES]
<<<[start image ID]>>> START IMAGE: the exact frame at 0:00. The camera position, lens, framing,
composition, the room, every piece of furniture, the light, colour and brightness, and the positions
and poses of the people and props at 0:00 are exactly this image. The video begins from this image
and continues from it without any cut, jump or reframing.
<<<[character ID]>>> [NAME] ([age]). [Wardrobe sentence from the asset registry, verbatim].
Face, hair, body type and wardrobe 100% match this reference.
<<<[prop ID]>>> [Prop sentence: material, shape, weight]. Its size stays the same as in the start image.
REFERENCE AUTHORITY: the start image has sole authority over camera, framing, the room, furniture,
light, colour and the 0:00 positions. The character references have authority only over faces,
hair, bodies and clothes. The [prop] reference has authority only over its material, shape and
state; its size follows the start image. Do not take the background, lighting, pose or panel layout
from the character or prop references.

[LOCATION_MAP]
LEFT and RIGHT are SCREEN directions, never the character's own left or right. Places are named by the objects on screen.
[LEFT EDGE / CENTRE / RIGHT / FOREGROUND.] [Where each person stays, by objects.]

[FIRST_FRAME_AND_SPATIAL_BLOCKING]
(Scope: FIRST_FRAME only.)
- [PERSON]: [position by objects], mid-[action], [body direction], [gaze], [hands: the screen-left hand, nearer the [object], ...].
- [PROP]: [position], [state], [who holds it].
Exactly [one person is / N people are] visible.

[FORMAT_MODE]
Live action. A single continuous take from 0:00 to 0:[NN]. No cuts. [NN] seconds.
All movement is slow and even; nothing accelerates suddenly.

[OPTICS]
Diagonal field of view about [N]°. [Observable result 1] / [2] / [3]. [Depth of field.]

[CAMERA]
[Position, height, direction.] [Fixed and completely locked from 0:00 to 0:NN. No pan, no tilt, no
zoom, no push-in, no reframing. / One move with its speed.]

[ACTION_TIMING]
0:00–0:0[a] — [state + action, per person].
0:0[a]–0:0[b] — [the line in AUDIO is said once here; what each person's hands do].
0:0[b]–0:[NN] — [continuing state]. The shot ends with [final state].

[CHARACTER_ACTING]
[PERSON]: [objective as observable action]. [Business: what the hands are doing]. [Body: weight, tempo,
breath]. [Beat change shown by gaze / pause / posture]. [Eye life]. [Range: between X and Y; X = failed
take, Y = failed take]. [Who does not react.] Nobody looks at the camera.

[PHYSICS]
motion_owner = CHARACTER: [ ]
motion_owner = PROP: [`상태 머신`, exactly N transitions; weight, contact]
motion_owner = CAMERA: [none / one move]
motion_owner = ENVIRONMENT: [none / what]

[LIGHTING]
[Practical sources as in the start image; the dominant source comes from screen [left/right], the [object] side.]

[AUDIO]
[Dialogue in [language], exactly once.] [PERSON]: "[line]" — [voice sentence, verbatim]. [PERSON 2] does not say a single word:
no attempt to speak, no parted lips, no mouthing. [Sound effects]. [Music or no music.]

[STYLE]
[Medium, look, skin tones, saturation.]

[QUALITY]
[Facial features clear; skin and fabric textures natural. No distortion of faces or fingers.]

[REQUIRED_AND_FORBIDDEN_CONSTRAINTS]
Required:
- [state to keep] ([ENTIRE_SHOT / INTERVAL 0:0a–0:0b / FINAL_FRAME])
Forbidden:
- [only failures that actually appeared before, each with its scope]
- Subtitles, text, watermarks, logos. (ENTIRE_SHOT)
```

## Sentences used as is

```text
[첫 프레임] [Person] is already in place at 0:00, mid-[action]. No empty establishing frame.
[광각] Diagonal field of view about 63°. [A], [B] and [C] are fully visible in one frame / straight
lines stay straight / no telephoto compression.
[망원] Diagonal field of view about 29°. The background is compressed and soft / only [person] is
sharp / the camera is physically far away.
[상태 머신] [OBJECT] state: [STATE_A] -> [STATE_B], exactly one transition, never reversed.
```
