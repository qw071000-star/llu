# 실사·인물 컷 — 15블록

## 블록

- 순서와 제목은 고정이다. 쓸 게 없는 블록도 제목은 남긴다.
- `PRE_SHOT_CONTINUITY`는 앞 숏에서 이어받는 상태가 있을 때만 맨 앞에 둔다.

| # | 블록 | 쓰는 것 | 자주 틀리는 것 |
|---|---|---|---|
| — | `PRE_SHOT_CONTINUITY` | 이어받는 위치·자세·소품 소유·빛. 이어받지 않는 것은 지금 상태로 적는다(`the bag is closed`). "previous shot" 같은 말은 쓰지 않는다 | 확인 없이 계승 |
| 1 | `SCENE_CONTEXT` | 시대·장소·이 클립의 일, 2~4문장 | 카메라·연기를 여기 몰기 |
| 2 | `ACTIVE_REFERENCES` | 붙인 참조마다(시작 이미지 포함) ID·역할·권한 한 줄. 인물 줄은 고정 설명문 + `100% matches the reference`, 음성 파일을 붙였으면 `[NAME]'s voice 100% matches audio_[N]`. 한 생성에서 상태가 바뀌면 요소 둘을 붙이고 시간으로 나눈다(`[A] until 0:04, [B] from 0:04`). 일부에만 나오는 참조는 범위를 적는다(`only inside the mirror, only 0:06–0:14`) | 안 붙인 태그, 붙이고 안 씀 |
| 3 | `LOCATION_MAP` | 좌표 문장, 카메라 위치, 전·중·후경, 광원. 컷마다 고정 물건이 화면 어느 쪽인지 다시 쓴다. 문은 열리는 쪽을 물건으로(`hinged on the edge nearer the wardrobe`) | "근처에", "그 문" |
| 4 | `FIRST_FRAME_AND_SPATIAL_BLOCKING` | 0:00에 누가 어디서 무슨 동작 **도중인지**, 소품, 보이는 인원 수 | 숏 전체로 확대 |
| 5 | `FORMAT_MODE` | 실사, 단일 연속 테이크, 길이. 컷이 필요하면 `hard cuts only at 0:0a; the camera never cuts by itself`와 컷마다 길이·카메라·첫 프레임 인물·동작. 인물이 컷 사이에서 사라지면 컷을 걷는 도중에 걸고, 그래도 안 되면 컷을 없앤다 | 단일 테이크인데 컷 요구 |
| 6 | `OPTICS` | 대각 화각(도, 시작 이미지의 mm를 SKILL.md §2 표로 환산) + 관찰 결과 3개, 심도. 렌즈는 샷당 하나, 화각은 컷에서만 바뀐다. 얼굴·장소 전체·손 디테일을 한 비트에 섞지 않는다(컷을 나눈다) | mm·조리개·렌즈 브랜드 |
| 7 | `CAMERA` | 위치·높이·방향·고정 여부·움직임과 속도 | 복합 움직임 |
| 8 | `ACTION_TIMING` | `0:00–0:03 —` 구간별 행동·대사, 마지막 프레임 | 빈 구간, 횟수가 바뀜 |
| 9 | `CHARACTER_ACTING` | 목표와 행동, 눈, 감정 범위의 양 끝 = 실패. 새로 쓰면 `acting`을 연다 | 감정 형용사 |
| 10 | `PHYSICS` | `motion_owner`별 무게·접촉 | 누가 움직이는지 불분명 |
| 11 | `LIGHTING` | 실제 광원 하나를 지배광으로, 방향(화면 쪽 + 그쪽 물건) | 참조 사진 룩으로 단정 |
| 12 | `AUDIO` | 대사 원문, 횟수, 목소리, 효과음, 음악 여부, 말하지 않는 인물 | — |
| 13 | `STYLE` | 매체 질감·색조 한두 줄 | 스타일이 얼굴을 통제한다고 가정 |
| 14 | `QUALITY` | 해상감, 피부·직물 질감, 손가락 왜곡 억제 | — |
| 15 | `REQUIRED_AND_FORBIDDEN_CONSTRAINTS` | Required: 지킬 상태·횟수 3~5개. Forbidden: `SKILL.md` §1의 7번. 원하는 상태 먼저, 실패는 결과로 | 과거 실패 누적 |

## 덜어내는 법

- **길이보다 사건 수를 먼저 줄인다.** 그래도 5,500자 근처면 장소 → 스타일 → 환경(QUALITY·배경 묘사) → 연기 문장 순서로 줄인다. 고정 문장·가져온 OK 줄·연기의 양 끝을 빼야만 줄어들면 줄이지 않고 WARN을 남긴다(이유와 글자 수를 적는다). 인물이 셋 이상이면 줄이기보다 샷 나누기가 먼저다.
- **장소 정보는 좌표 줄 + 네 줄까지만 쓴다.** 카메라, 전·중·후경, 빛, 필요하면 경로다. 길수록 인물 참조가 밀린다.
- **이 샷에 나오지 않는 인물, 태그, 씬 번호는 넣지 않는다.**
- **금지어는 범위를 좁힌다:** `no [X] on [Y]`. 금지어가 오히려 그것을 부를 수 있다.
- **사용자가 "금지할 것을 다 넣으라"고 하면** 범주별로 묶는다(`[Faces and clothing]` `[Camera and editing]` …). 그만큼 사건 수는 더 줄인다.

## 빈 틀

블록 밖에 한국어로 적는다: 모델, 해상도, 길이, 화면비, 소리, 시작·끝 이미지 job, 붙인 요소(시작 이미지 포함, 순서대로. 이 수가 검사 스크립트의 `--refs`), 위험 목록, 저장 폴더.

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
motion_owner = PROP: [state machine, exactly N transitions; weight, contact]
motion_owner = CAMERA: [none / one move]
motion_owner = ENVIRONMENT: [none / what]

[LIGHTING]
[Practical sources as in the start image; the dominant source comes from screen [left/right], the [object] side.]

[AUDIO]
[Dialogue in [language], exactly once.] [PERSON]: "[line]" — [voice sentence]. [PERSON 2] does not say a single word:
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

## 그대로 쓰는 문장

```text
[첫 프레임] [Person] is already in place at 0:00, mid-[action]. No empty establishing frame.
[광각] Diagonal field of view about 63°. [A], [B] and [C] are fully visible in one frame / straight
lines stay straight / no telephoto compression.
[망원] Diagonal field of view about 29°. The background is compressed and soft / only [person] is
sharp / the camera is physically far away.
[상태 머신] [OBJECT] state: [STATE_A] -> [STATE_B], exactly one transition, never reversed.
```
