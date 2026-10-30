---
name: video-prompt
description: Use when writing or fixing an AI video-generation prompt - Seedance, Kling, image-to-video, start/end-frame video. Live-action and character cuts use the 15 blocks; backgrounds, landscapes and painterly styles use 4 paragraphs. When the result comes out wrong, read the symptom-fix file.
---

# Video prompt - common

## 0. Information check before writing

**If the turn writes a full 15-block prompt and newly writes `CHARACTER_ACTING`, open `acting` first** (even if the previous turn was a question turn).

**Stage files:** a new prompt uses `live-action.md` / `background.md`. Open `fixes.md` only when the result came out wrong.

For a live-action cut (15 blocks), fill the table below. Each row goes into one block of the 15.

| Category | Information needed | Block it goes into |
|---|---|---|
| Scene | What happens in this clip (2-4 sentences), era, place, time of day | `SCENE_CONTEXT` |
| Format | Length, aspect ratio, model, sound (dialogue / effects / music or not; dialogue comes from the `shot-list.md` line (a quoted line = dialogue); ask only if it is unclear), save folder | `FORMAT_MODE`, `AUDIO` |
| Look | Medium, texture, colour tone (the look standard in `decisions.md`) | `STYLE` |
| Character assets | Per character: element ID, wardrobe/hair state version, fixed description sentence, voice sentence if there is dialogue | `ACTIVE_REFERENCES`, `AUDIO` |
| Location | Location-view element ID, landmarks at screen left / centre / right / foreground, time of day, hinge side of doors and hinged furniture (screen side + object) and opening direction | `ACTIVE_REFERENCES`, `LOCATION_MAP` |
| Props | Element ID, start state -> end state, who holds it in which hand (screen side + object), size | `ACTIVE_REFERENCES`, `PHYSICS` |
| Start image | First-frame job (if none, make a first frame dedicated to this cut first (`image-prompt` -> `first-frame.md`); never use another cut's), whether to use an end frame | `ACTIVE_REFERENCES` |
| Camera | Position (by objects on screen), height, direction, locked or one move (type, speed, amount) | `CAMERA` |
| Lens | Diagonal field of view (degrees), 3 observable results, depth of field / focus shift — not asked: fill from the start image's mm | `OPTICS` |
| Character position | Per character: start position (0:00, screen side + object), pose, action in progress; end position (last frame) | `FIRST_FRAME_AND_SPATIAL_BLOCKING`, `ACTION_TIMING` |
| Movement path | Route, zones not passed through, walking speed | `LOCATION_MAP`, `ACTION_TIMING` |
| Gaze | Per character: what they look at, when the gaze changes, who must not react | `ACTION_TIMING`, `CHARACTER_ACTING` |
| Timing | Intervals of the main actions (`0:00–0:03`), dialogue text / count / position, moments when prop state changes | `ACTION_TIMING`, `AUDIO` |
| Acting | Per character: objective, both ends of the emotional range | `CHARACTER_ACTING` |
| Light | Dominant light source and direction | `LIGHTING` |
| Seam | State inherited from the previous cut, what must match the next cut's first frame | `PRE_SHOT_CONTINUITY` |
| Forbidden | This cut's rejection reasons and [10], risks of an imported OK (`production-session` -> `ok-reuse.md` §3), the character's "알려진 실패" in the asset registry | `REQUIRED_AND_FORBIDDEN_CONSTRAINTS` |

For a background/landscape video (4 paragraphs), fill only the next table.

| Information needed | Paragraph it goes into |
|---|---|
| Start-image job, model, length, aspect ratio, save folder | Settings |
| Camera move: type, direction, amount (% of frame), speed | `Camera` |
| What moves: for each thing already in the image, direction and speed | `Motion` |
| Medium, shapes to keep, light direction | `Keep` |
| Sound (whether it can be turned off) | `Silent` |

**Vague phrases -> values/sentences** (applies even when the user is not criticising a result. If only "before -> after" is shown, save the fixed full prompt and run the check on it)

| User phrase | Value / sentence |
|---|---|
| Speed ("구름 더 느리게/빠르게", clouds slower/faster) | Only that subject's `Motion` line. Halve/double the travel (% of frame), leave other motion unchanged. Show that line as "전 → 후" |
| Add motion ("풀도 흔들리게", make the grass sway too) | Only things already in the image; add one `Motion` line (direction, strength). In that reply, say "one more event was added" |
| Small repeating elements such as stars or flocks of birds ("별이 더 반짝이게", make the stars twinkle more) | Before generating, say the model does not hold these well. Try once; after 2 failures add it as a post-production overlay. If it is not in the start image, do not try; use a post overlay or a new start image |
| Speed of a person's action ("천천히", slowly) | First count the seconds of the existing interval. The new interval must be longer. Keep the event count and write `[기존보다 긴 구간] — [action], taking the full [N] seconds. [Action] finished in under [N − 1] seconds = failed take.` In "전 → 후" give the seconds of both intervals. If the existing interval is already 4+ seconds or the whole action, ask, as a proposal (제안값), whether to start earlier or lengthen the video |
| Age of the walk ("걸음이 젊어", the walk is young) | Write it as stride, arms, feet, centre of weight, and close the opposite walk: `"[name] walk" — [step size], [arm swing], [feet lifted or dragged], [centre of weight]. A [opposite] walk = failed take.` |
| Look ("영화같이", more cinematic) | Offer one at a time: lens/FOV (§2 table), depth of field, light contrast, one camera move. Do not invent a new STYLE sentence; change STYLE only after the user OKs it |
| Several actions ("…하고 …하고 나가", does X, does Y, leaves) | Apply §2 "Event count" (count, per-shot list, exit as end-frame state) |

How to ask is instructions rule 4. If there are more than 10 questions, group them under subheadings (camera / characters / timing) within one message. Do not split them across several turns.

**Keep the answers in cut card [4]-[6].** The first frame and retries use the same values; if a value changes, fix the card first.

**Consistency check (after writing)**
- Is this cut's start state the same as the previous cut's end state (position, prop state, light)? Take the previous cut's end state from the continuity table
- Do that view's LIGHT LOCK (asset registry), screen left/right and light side match?

## 1. Six principles

1. **Event count decides success,** more than character count (how to count and split: §2 "Event count").
2. **Write states, not transitions.** Fix the start state and end state. If the gap is long, split the generation.
3. **The first frame is 0:00 of the video.** The first-frame paragraph must equal the start image.
4. **One camera move per generation.**
5. **For every reference, state its scope of control.** A location reference does not control composition; a character reference controls only face and wardrobe.
6. **One blocking line per risk.** Put in Forbidden, with a scope tag, only failures that actually occurred (the Forbidden row of the §0 table). Block anticipated risks with Required or a sentence in the relevant block. If a sentence blocking the same symptom already exists, change that sentence instead of adding another.

## 2. Shot design

| To decide | Standard |
|---|---|
| Length | **The canon's cut length first** (`decisions.md`). Only if canon has none: dialogue/action live action 5-10 s, background 10-15 s. Split anything over 15 s |
| Lens conversion | Diagonal field of view (full-frame): 24mm=84° · 28mm=75° · 35mm=63° · 50mm=47° · 65mm=37° · 75mm=32° · 85mm=29° · 100mm=24° · 135mm=18°. For a mm not in the table, interpolate between the two nearest (105mm ≈ 23°). If the cut card and the start image disagree, the start image wins (tell the user and proceed) |
| Chaining | The later generation takes the designated frame of the earlier generation as `start_image`. The later generation's 0:00 is the storyboard time as is, with no lead-in margin (editing handles go only at the end). `PRE_SHOT_CONTINUITY` carries only the inherited state; do not carry over the previous video's framing or lens |
| Location | One location per generation. Confirm a new location as an image first |
| Event count | 1-3 per generation. Count from the final `ACTION_TIMING`/`CHARACTER_ACTING`, every character together: every verb that is a separate visible action (turning the head, lowering a hand, saying a line each count; breathing and blinking do not). Exiting counts (stands up, picks up, turns, leaves = 4; turns, walks over, takes her hand = 3; turns, says the line, steps over, takes his hand = 4 → split; with two people add both: she turns and takes his hand, he lowers his gaze and tightens his fingers = 4). Do not count them in groups. If over, do not merge; first show, as a proposal (제안값), a per-shot event list (shot A: stands up and picks up the bag / shot B: turns and leaves). Propose writing the exit as an end-frame state and an entrance as a first-frame state (exit = at the last frame half the body is outside the frame, already walking, the door closing behind). One task per character. One line of dialogue takes 2-4 s |
| End frame | Use only when there is a composition that must be reached |

## 3. Model notes

| Model | Note |
|---|---|
| Seedance 2.5 | Call references with `<<<요소ID>>>` (element ID), matching the attached elements exactly. Sound is on by default, so an AUDIO block is needed. Voice references were called audio_1, audio_2 in the order attached (observed; not confirmed by official docs). Extend may change the aspect ratio |
| Kling 4.0 | Do not re-describe what is in the image; write only the motion and what to keep. Write the camera as a separate paragraph and do not write an end state |

## 4. Pre-send check (what the check script cannot catch)

- [ ] Did you run the check script (instructions "Check")? `--must-include` gets the asset registry's fixed sentences and imported OK lines
