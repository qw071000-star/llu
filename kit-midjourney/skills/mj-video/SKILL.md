---
name: mj-video
description: Use when the user wants a short clip from an approved Midjourney image (image-to-video, "영상으로", "움직이게", "애니메이트"). Writes the motion prompt and the settings to try, and tells the user what to run. Midjourney is not connected: the user runs it and brings the clip back.
---

# Short clips from a still (manual route)

Midjourney's video feature animates an image: the image is the **start frame** and the prompt describes only the motion. This skill was written from the vendor's announcement and third-party guides, **not verified by generation**: say so, and ask the user to confirm the current options (motion strength, clip length, extend) in Midjourney.

## 1. Required information

| Information | From |
|---|---|
| The approved start image (a `3-1 스틸` card) | OK ledger. None → make it first (task 10) |
| The one action: who or what moves, from where to where | cut card [6] |
| Motion strength (low / high) and length, as the user's Midjourney offers them | ask; propose low for a face, high for scenery |
| Camera: still, or one move | cut card [4]; default still |
| Sound | not made here: sound is added in editing |

## 2. Motion prompt

- **Only the motion**, 10–30 words: do not re-describe what is already in the image.
- **One action per clip**, one subject, one camera behaviour (or still). Write speed as a physical referent (`one slow head turn over three seconds`), not an adjective.
- No dialogue and no mouth movement: Midjourney clips are silent, a spoken line is added in editing. If a person must not speak, say `mouth stays closed`.
- No text, no cuts, no new objects entering.

```text
[the subject] [one motion with a number or referent], [what stays still], camera [still / one slow move]
```

## 3. Hand to the user, judge and revise

A complaint in words ("너무 많이 움직여", "얼굴이 변해") is enough: change one thing in the motion prompt or the settings and give the new prompt as "전 → 후". Show the prompt, the start-image link to attach, and the settings; the user runs it and pastes the clip or a few frames. **Viewing table:** from the prompt's seconds, one row per interval `구간 | 프롬프트가 지시한 것 | 확인`, last column empty for the user; the first row is whether 0:00 equals the start image (position, scale, gaze, hands). A ✘ row is the symptom to fix by one change (instructions rule 2). Anything not visible in the frames is "추정".

## 4. Common symptoms

| Symptom | Fix |
|---|---|
| 0:00 is not the start image (subject smaller, objects moved) | confirm the image was set as the start frame; try low motion; a model that cannot hold the start frame is a limit: propose editing instead |
| Too much movement or a morph | low motion; shorter motion phrase; one action |
| Face changes during the clip | low motion; keep the head turn small; reduce to a still |
| Camera drifts | `camera completely still` |

## 5. Record

On approval write the clip card `3-1 영상`: link, the motion prompt verbatim, settings, `시작 이미지: [link · card 3-1 스틸]` (`mj-production` §4).
