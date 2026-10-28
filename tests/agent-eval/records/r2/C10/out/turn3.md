제안값으로 채웠고, 렌즈는 시작 이미지 그대로(대각 약 47°) 썼습니다. 돌아서는 시간은 3-1 영상 OK대로 약 1.5초입니다(제안값). 모두 컷 카드에 기록했습니다.

**설정**
- 모드: image-to-video (시작 이미지로 시작), 실사 15블록
- 참조(붙이는 순서):
  1. `ff_3-3_v1`: 시작 이미지(`job-ff-3-3`)
  2. `char_girl_raincoat_v1`: 손녀의 얼굴·머리·의상만
- 모델: Seedance 2.5
- 해상도: 480p (확인용)
- 길이·비율: 8초 · 16:9
- 소리: 대사 없음, 효과음만(바람, 장화 한 걸음)
- 끝 프레임 이미지: 안 씀
- 저장 폴더: `fld-3-3` (3-3 [진행])

**위험 → 막는 문장** (아직 실제 실패는 없고, 모두 예상 위험입니다)

| 위험 | 막는 문장 |
|---|---|
| 몸이 휙 돈다 | 0:03–0:05에 눈→머리→어깨 순서로 약 1.5초 (3-1 OK 줄) |
| 대사가 없는데 입이 움직인다 (Seedance는 소리가 기본으로 켜짐) | `does not say a single word: no attempt to speak, no parted lips, no mouthing` |
| 카메라를 본다 | `She never looks at the camera.` |
| 시간표 글씨가 읽힌다 (§7) | Required `printed times … stay unreadable` |
| 벤치 쪽을 보니 할아버지가 화면에 들어온다 | Required `Exactly one person` |
| 걸음이 커져 화면 밖으로 나간다 | Required `still fully in frame` (FINAL_FRAME) |
| 줌이나 화면 재구성이 생긴다 | CAMERA `completely locked … no reframing` |

**3-1 영상 OK에서 가져온 줄** (글자 그대로 두고, 할아버지·대사 부분만 뺐습니다)
- ACTION_TIMING 0:03–0:05: `…about 1.5 s, and says the line in AUDIO once.` → `…about 1.5 s.`
- ACTION_TIMING 0:05–0:08: `GRANDPA lowers his eyes … ; GIRL takes one small step toward the bench and stops.` → `GIRL takes one small step toward the bench and stops.`
- PHYSICS: `the girl's turn and one step; the grandpa's eyes and thumb.` → `the girl's hand, her turn and one step.`
- 그 카드의 금지 줄(할아버지 입)은 이 컷에 할아버지가 나오지 않아 옮기지 않았습니다.

검사 스크립트 결과: `check_prompt.py --kind video --refs 2 --must-include 고정 문장 3개` → OK, 걸린 항목 없음 (4371자).

```text
[SCENE_CONTEXT]
Late autumn, early 1990s, a rural bus stop at dusk. The girl reads the timetable sign once more, checking that there really is no bus left. Then she turns back toward the bench where her grandfather waits, out of frame, and takes one small step toward it. Nobody else is here.

[ACTIVE_REFERENCES]
<<<ff_3-3_v1>>> START IMAGE: the exact frame at 0:00. The camera position, lens, framing, composition, the shelter, the timetable sign, the road edge, the light, colour and brightness, and the girl's position and pose at 0:00 are exactly this image. The video begins from this image and continues from it without any cut, jump or reframing.
<<<char_girl_raincoat_v1>>> GIRL (10). A yellow raincoat over a navy school uniform, white knee socks and red rain boots. Face, hair, body type and wardrobe 100% match this reference.
REFERENCE AUTHORITY: the start image has sole authority over camera, framing, the place, the light, colour and the 0:00 position. The character reference has authority only over face, hair, body and clothes. Do not take the background, lighting, pose or panel layout from the character reference.

[LOCATION_MAP]
LEFT and RIGHT are SCREEN directions. Places are named by the objects on screen.
LEFT EDGE: the end of the concrete shelter; the bench inside it is off screen to the LEFT. RIGHT HALF: the timetable sign on its pole with the girl in front of it. BACKGROUND: harvested rice paddies and low hills. FOREGROUND: the empty road edge.
In this view the west is screen LEFT. GIRL stays on the road edge between the sign and the shelter, never crosses in front of the camera and never goes behind the sign.

[FIRST_FRAME_AND_SPATIAL_BLOCKING]
(Scope: FIRST_FRAME only.)
- GIRL: standing at the timetable sign, an arm's length from its pole, facing the sign in three-quarter back view, mid-reading, the hand nearer the sign raised to the printed times.
Exactly 1 person is visible.

[FORMAT_MODE]
Live action. A single continuous take from 0:00 to 0:08. No cuts. 8 seconds.
All movement is slow and even; nothing accelerates suddenly.

[OPTICS]
Diagonal field of view about 47°. The girl and the sign fill the right half of the frame / the end of the shelter stays at the left edge / the paddies behind are slightly soft while the girl is sharp. Moderate depth of field; no focus pull.

[CAMERA]
Fixed on a tripod at standing eye level on the near edge of the road, opposite the timetable sign, looking north, at the same position as in the start image, completely locked from 0:00 to 0:08. No pan, no tilt, no zoom, no push-in, no reframing.

[ACTION_TIMING]
0:00–0:03 — GIRL keeps reading, the hand nearer the sign sliding down the times once, then dropping to grip the cuff of her raincoat sleeve.
0:03–0:05 — GIRL turns toward the bench, eyes first, then head, then shoulders, about 1.5 s.
0:05–0:08 — GIRL takes one small step toward the bench and stops. The shot ends with GIRL in three-quarter profile facing screen LEFT, one step from the sign, still fully in frame.

[CHARACTER_ACTING]
GIRL: makes sure once more that no bus is left, then goes back to him; her hand holds her own sleeve instead of showing the worry. Continuous naturalistic eye life, the eyes reaching the bench side a beat before the head turns. Between quiet checking and quiet resignation; tears or a big sigh = failed take, no reaction at all = failed take. She never looks at the camera.

[PHYSICS]
motion_owner = CHARACTER: the girl's hand, her turn and one step.
motion_owner = PROP: none.
motion_owner = CAMERA: none.
motion_owner = ENVIRONMENT: none.

[LIGHTING]
Low dusk sun from the west, the persimmon-tree side, is the only key; the shelter's single fluorescent tube is off.

[AUDIO]
No dialogue. GIRL does not say a single word: no attempt to speak, no parted lips, no mouthing. Distant wind over the paddies; the soft scuff of one rain-boot step on the road edge. No music.

[STYLE]
Live-action film look; natural skin tones, restrained saturation.

[QUALITY]
Facial features clear; skin and fabric textures natural. No distortion of faces or fingers.

[REQUIRED_AND_FORBIDDEN_CONSTRAINTS]
Required:
- Exactly one person, the girl (ENTIRE_SHOT)
- The printed times on the sign stay unreadable (ENTIRE_SHOT)
- GIRL is still fully in frame, one step from the sign (FINAL_FRAME)
Forbidden:
- Subtitles, text, watermarks, logos. (ENTIRE_SHOT)
```

프롬프트만 만들었고, 생성은 하지 않았습니다.

**질문**
1. 이 프롬프트로 480p 8초 확인본을 한 개 보낼까요? 약 40크레딧이 들고, 저장 위치는 `fld-3-3`입니다.

=== 메타 ===
연 파일(순서대로):
1. .claude/skills/higgsfield-generation/SKILL.md
2. project/cuts/3-3.md (수정 후 확인)

부른 [TOOL]: 없음

검사: tmp/v-3-3.txt, tmp/must.txt로 check_prompt.py를 실행했고 결과는 OK입니다.

고친 정본 파일:
- project/cuts/3-3.md:
  - [4] 렌즈: 시작 이미지 그대로 47° (사용자 답)
  - [6] 타이밍: 1.5초에 돌아섬 (제안값)
  - [10] 위험 → 막는 문장
