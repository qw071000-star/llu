# 실사·인물 컷 — 15블록

인물·소품·대사가 있는 실사 컷에 쓴다. 연기 블록(9번)은 `acting` 스킬을 함께 읽는다.

## 블록 구성

순서와 제목은 고정이다. 쓸 게 없는 블록도 제목은 남긴다. `PRE_SHOT_CONTINUITY`는 앞 숏에서 이어받는 상태가 있을 때만 맨 앞에 둔다.

| # | 블록 | 쓰는 것 | 자주 틀리는 것 |
|---|---|---|---|
| — | `PRE_SHOT_CONTINUITY` | 이어받는 위치·자세·소품 소유·문·빛. 이어받지 않는 것(이전 프레이밍·렌즈)도 적는다 | 확인 없이 계승 |
| 1 | `SCENE_CONTEXT` | 시대·장소·이 클립의 일, 2~4문장 | 카메라·연기를 여기 몰기 |
| 2 | `ACTIVE_REFERENCES` | 실제로 붙인 참조마다 ID·역할·권한 한 줄. 인물 줄은 나이·체형·머리·의상·신발 + `100% matches the reference` | 안 붙인 태그를 쓰거나, 붙여 놓고 안 씀 |
| 3 | `LOCATION_MAP` | 좌표 문장, 카메라 위치, 전·중·후경, 광원. 랜드마크는 대문자 이름으로 | "근처에", "그 문" |
| 4 | `FIRST_FRAME_AND_SPATIAL_BLOCKING` | 0:00에 누가 어디서 무슨 동작 **도중인지**, 소품 위치·소유, 보이는 인원 수. 범위는 첫 프레임만 | 숏 전체로 확대 |
| 5 | `FORMAT_MODE` | 실사, 단일 연속 테이크, 길이 | 단일 테이크라 해 놓고 컷 요구 |
| 6 | `OPTICS` | 대각 화각(도) + 관찰 가능한 결과 3개, 심도 | mm·조리개·렌즈 브랜드 (영상 모델은 듣지 않는다) |
| 7 | `CAMERA` | 위치·높이·방향·고정 여부·움직임과 속도 | 복합 움직임 |
| 8 | `ACTION_TIMING` | `0:00–0:03 —` 구간별 행동·대사, 마지막 프레임 | 빈 구간, 횟수가 바뀜(한 번 → 계속) |
| 9 | `CHARACTER_ACTING` | 목표와 행동, 눈, 감정 범위의 양 끝 = 실패 (`acting` 스킬) | 감정 형용사 |
| 10 | `PHYSICS` | `motion_owner = CHARACTER / PROP / CAMERA / ENVIRONMENT`별 무게·접촉 | 누가 움직이는지 불분명 |
| 11 | `LIGHTING` | 실제 광원 하나를 지배광으로, 방향 | 참조 사진 룩으로 색온도 단정 |
| 12 | `AUDIO` | 대사 원문, 횟수, 목소리, 효과음, "No music". 말하지 않는 인물 명시 | — |
| 13 | `STYLE` | 매체 질감·색조 한두 줄 | 스타일이 얼굴까지 통제한다고 가정 |
| 14 | `QUALITY` | 해상감, 피부·직물 질감, 손가락 왜곡 억제 | — |
| 15 | `REQUIRED_AND_FORBIDDEN_CONSTRAINTS` | Required: 지킬 상태·횟수·범위. Forbidden: **실제로 나온 실패만**, 범위 태그(`ENTIRE_SHOT`, `INTERVAL 0:03–0:06`, `FINAL_FRAME`) | 과거 실패를 끝없이 누적 |

## 덜어내는 법

- 장소 정보는 좌표 줄 + 네 줄(카메라 / 전·중·후경 / 빛 / 필요하면 경로)까지만 쓴다. 길수록 인물 참조가 밀린다.
- 인물·장소 설명문은 에셋 대장의 고정 문장을 글자 그대로 쓴다. 같은 인물을 29개 프롬프트에서 같은 문장으로 쓴 작품이 일관성이 가장 높았다.
- 이 샷에 나오지 않는 인물, 태그, 씬 번호, "앞과 같음"은 넣지 않는다.
- 원하는 상태는 Required에 먼저 쓴다. Forbidden에는 실제로 나왔던 실패만 둔다.
- 금지어가 오히려 그것을 부를 때가 있다. 예: "no domes"가 돔 화덕까지 지울 위험이 있었다. 범위를 좁혀(`no domes on buildings`) 쓴다.
- 예외: 같은 컷에서 여러 종류의 실패가 반복됐고 사용자가 "금지할 것을 다 넣으라"고 하면 길게 쓴다.
  - 이때는 범주별로 묶는다(`[Faces and clothing]`, `[The bag]`, `[Camera and editing]`). 고등어 C#4는 이렇게 쓴 판이 확정됐다.
  - 길게 쓸수록 사건 수는 더 줄인다.
- 12,000자 프롬프트는 뒤쪽 금지문이 약해졌다. 반복을 지워 5,000자 수준으로 줄여도 결과는 유지됐다.

## 빈 틀

확정된 프롬프트(고등어 C#4·C#6)의 구조를 본뜬 틀이다.
- `[ ]`만 채운다.
- 블록 밖에 한국어로 적는다: 모델, 해상도, 길이, 화면비, 소리, 시작·끝 이미지 job, 붙인 요소(순서대로), 위험 목록, 저장 폴더.

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
0:0[a]–0:0[b] — [the line in AUDIO is said once here; what each person's hands do].
0:0[b]–0:[NN] — [continuing state]. The shot ends with [final state].

[CHARACTER_ACTING]
[PERSON]: ["named walk"]. [Objective as observable action]. [Eye life]. [Range: between X and Y;
X = failed take, Y = failed take]. [Who does not react, never looks at whom.]
Neither of them looks at the camera.

[PHYSICS]
motion_owner = CHARACTER: [ ]
motion_owner = PROP: [state machine, exactly N transitions; weight, contact]
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
[Facial features clear; skin, fabric and prop textures natural. No distortion of faces or fingers.]

[REQUIRED_AND_FORBIDDEN_CONSTRAINTS]
Required:
- [state to keep] ([ENTIRE_SHOT / INTERVAL 0:0a–0:0b / FINAL_FRAME])
- [count: exactly once / exactly two people]
Forbidden:
- [only failures that actually appeared before, each with its scope]
- Subtitles, text, watermarks, logos. (ENTIRE_SHOT)
```

### 짧은 판 (동작 하나, 인물 하나 또는 없음)

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

## 그대로 쓰는 문장 (검증된 것)

```text
[좌표] LEFT and RIGHT are SCREEN directions. Places are named by the objects on screen.

[장소 참조] Controls geometry, materials, light and atmosphere ONLY — not framing.

[첫 프레임] [Person] is already in place at 0:00, mid-[action]. No empty establishing frame.
Exactly [N] people are visible.

[광각 관찰 결과] Diagonal field of view about 63°. The [A], [B] and [C] are fully visible in one
frame / straight lines stay straight / no telephoto compression.

[망원 관찰 결과] Diagonal field of view about 29°. The background is compressed and soft / only
[person] is sharp / the camera is physically far away.

[속도] All movement is slow and even; nothing accelerates suddenly, and each action flows into the
next without a hard start or stop.

[상태 머신] [OBJECT] state: ON_TABLE -> LIFTED -> CARRIED, exactly one transition, never reversed.

[연기 범위] Between [state A] and [state B]. [one extreme] = failed take; [other extreme] = failed take.

[말하지 않음] [Person] does not say a single word; no attempt to speak, no lip movement.

[대사] The dialogue is in [language], exactly once. [PERSON]: "[line]" — [voice description]. No music.
```
