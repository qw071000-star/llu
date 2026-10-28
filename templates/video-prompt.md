# 영상 프롬프트 빈 틀

규칙은 `guide/03_video-prompt.md`. 아래 틀은 실제로 확정된 프롬프트(고등어 C#4·C#6, 나부코 아침 컷)의 구조를 본뜬 것이다. `[ ]`만 채우고, 쓸 게 없는 블록은 제목을 두고 비운다.

블록 밖에 한국어로 적을 것: 모델 · 해상도 · 길이 · 화면비 · 소리 · 시작/끝 이미지 job · 붙인 요소 목록(순서대로) · 위험 목록.

---

## A. 15블록 (인물·소품·대사가 있는 실사 컷)

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
<<<[prop ID]>>> [Prop sentence: material, shape, weight behaviour]. Its size stays the same as in
the start image from start to finish.
REFERENCE AUTHORITY: the start image has sole authority over camera, framing, the room, furniture,
light, colour and the 0:00 positions. The character references have authority only over faces,
hair, bodies and clothes. The [prop] reference has authority only over its material, shape and
state; its size follows the start image. Do not take the background, lighting, pose, hand, sleeve,
trousers, shoes or panel layout from any reference.

[LOCATION_MAP]
LEFT and RIGHT are SCREEN directions. Places are named by the objects on screen.
[LEFT EDGE: … / CENTRE: … / RIGHT: … / FOREGROUND: …]
[Where each person stays, named by objects. Which areas they never cross.]

[FIRST_FRAME_AND_SPATIAL_BLOCKING]
(Scope: FIRST_FRAME only.)
- [PERSON]: [position by objects], mid-[action], [body direction], [gaze], [hands].
- [PROP]: [position], [state], [who holds it].
Exactly [N] people are visible.

[FORMAT_MODE]
Live action. A single continuous take, one unbroken shot from 0:00 to 0:[NN]. No cuts. [NN] seconds.
All movement is slow and even; nothing accelerates suddenly.

[OPTICS]
Diagonal field of view about [63]°. [Observable result 1] / [2] / [3].
Focus: [deep focus, nothing shifts / shifts once to X after 0:0N].

[CAMERA]
[Fixed on a tripod, eye level, at the same position as in the start image, completely locked from
0:00 to 0:NN. No pan, no tilt, no zoom, no push-in, no reframing.]

[ACTION_TIMING]
0:00–0:0[a] — [state + action, per person].
0:0[a]–0:0[b] — [line in AUDIO is said once here; what each person's hands do].
0:0[b]–0:[NN] — [continuing state]. The shot ends with [final state].

[CHARACTER_ACTING]
[PERSON]: ["named walk"]. [Objective as observable action]. [Eye life]. [Range: between X and Y;
X = failed take, Y = failed take]. [Who does not react, never looks at whom.]
Neither of them looks at the camera.

[PHYSICS]
motion_owner = CHARACTER: [ ]
motion_owner = PROP: [state machine, exactly N transitions; weight, contact, never lifted / dropped]
motion_owner = CAMERA: [none / one move]
motion_owner = ENVIRONMENT: [none / what]

[LIGHTING]
[Practical sources as in the start image]. [White surfaces read white.] The whole frame does not lean
orange or amber and does not sink into darkness. The lamps are on, but their light does not bloom.

[AUDIO]
[Dialogue in Korean, exactly once.] [PERSON]: "[line]" — [voice sentence]. [PERSON 2] does not say
a single word. [Sound effects]. No music.

[STYLE]
[A present-day live-action film shot with a real camera. Natural skin tones, restrained saturation.]

[QUALITY]
[Facial features clear; skin, fabric and [prop] textures natural. No distortion of faces or fingers.]

[REQUIRED_AND_FORBIDDEN_CONSTRAINTS]
Required:
- [state to keep] ([ENTIRE_SHOT / INTERVAL 0:0a–0:0b / FINAL_FRAME])
- [count: exactly once / exactly two people]
Forbidden:
- [only failures that actually appeared before, each with its scope]
- Subtitles, text, watermarks, logos. (ENTIRE_SHOT)
```

### 짧은 판 (동작 하나, 인물 하나 또는 없음 — 예: 팬 위 생선 클로즈업, 확정)

```text
Photorealistic cinematic shot, [place/era]. Single continuous take. Static locked-off camera:
no pan, no zoom, no push-in, no handheld. Real-time speed, no slow motion.

START IMAGE: use the start image exactly as the first frame. Camera position, viewing angle,
framing, [objects] and the background are exactly as in the start image and do not change.

SET: [one sentence]. SHOT: [what is in frame at 0:00].

0:00-0:03 - [state]. 0:03-0:07 - [state]. [What does NOT happen.]

Lens: [as in the start image] + observable results. Audio: [ ]. Style: [ ].
Required: [2–3]. Forbidden: [only real risks].
```

---

## B. 4문단 (인물 연기 없는 배경·풍경·그림체 영상, 시작 이미지 사용)

```text
Camera: a slow, steady [forward glide / sideways glide to the left / rise], moving about [N] percent
of the frame [closer / width / height] over the whole clip. The horizon stays level; no rotation,
no tilt, no zoom.

Motion: [only things already in the image that move, with direction and pace — clouds drift slowly
to the right; thin smoke rises straight up; tiny figures keep to their small tasks].

Keep the hand-painted [watercolor] look, every [shape list], and the light direction from the [side]
exactly as in the image; only the things named above move, slowly and without morphing or melting.

Silent: no dialogue, no music, no sound effects.
```

---

## C. 고화질 재렌더 (확정한 저해상도 테이크를 같은 내용으로)

```text
SOURCE VIDEO: the attached video is the take to reproduce. [Shot-by-shot summary]. Every cut,
duration, line and sound stays the same.
RESOLUTION: the source is [480p/720p]; only resolution and detail differ.
ACTIVE REFERENCES: [same elements, same order, same voice files as the source].
STYLE / QUALITY: [same]. No digital sharpening.
Required: same number, order and length of shots as the source; any difference = failed take.
```
