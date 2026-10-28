제안값으로 썼습니다. 검사 스크립트(`check_prompt.py`, 영상, 참조 4, 고정 문장 포함)를 돌렸고 FAIL 0, WARN 1입니다. WARN은 길이(5,258자)인데, 승인된 3-1 프롬프트와 같은 구조라 그대로 둡니다(줄이면 가져온 문장이 달라집니다). 생성은 하지 않았습니다.

**실패 위험 → 막는 문장**
| 위험 | 막는 문장 |
|---|---|
| 할아버지 입이 움직임(3-1 거절 사유) | `GRANDPA does not say a single word; no attempt to speak, no lip movement` (AUDIO, Forbidden) |
| 대사가 두 번 나옴(3-1 거절 사유) | `Dialogue in Korean, exactly once` + Required `spoken exactly once` (0:03–0:05) |
| 할아버지가 손녀를 봄(3-1 거절 사유) | `He never looks at the girl` (CHARACTER_ACTING) |
| 누군가 카메라를 봄(3-2 시작 이미지 거절 사유) | `Nobody looks at the camera` + Forbidden `Anyone looking at the camera` |
| 가까운 샷이라 손녀가 휙 돌거나 프레임 밖으로 나감 | 돌아서는 순서와 1.5초, `one small step ... and stops`, `never steps into the road` (3-1에서 가져옴) |

**3-1에서 바꾼 줄 (전 → 후)**
- START IMAGE 태그: `ff_3-1_v2` → `ff_3-2_v1`
- OPTICS: `about 63°. The tree, the whole shelter and the sign are fully visible ... Deep focus.` → `about 32°. The bench and the sign are fully visible side by side ... paddies behind are compressed and soft. Shallow depth of field, no focus pulls.`
- CAMERA: `standing eye level` → `seated eye level ... opposite the middle of the bench`
- LOCATION_MAP, FIRST_FRAME: 투샷 구도(벤치 화면 왼쪽, 시간표 오른쪽)로 바꿈. 3-2 시작 이미지 프롬프트의 문장 사용
- CHARACTER_ACTING: `The shot is close, so everything stays small and lives in the eyes and hands.` 한 줄 추가
- Forbidden: `Anyone looking at the camera` 한 줄 추가
- ACTION_TIMING, PHYSICS, 속도 문장, AUDIO, 대사: 그대로

**프롬프트**
```text
[SCENE_CONTEXT]
Late autumn, early 1990s, a rural bus stop at dusk. A girl reads the timetable sign and tells her grandfather, seated on the bench with a bag on his lap, that the last bus has gone. He says nothing.

[ACTIVE_REFERENCES]
<<<ff_3-2_v1>>> START IMAGE: the exact frame at 0:00. The camera position, lens, framing, composition, the shelter, bench, sign, the light, colour and brightness, and the positions and poses of the two people and the bag at 0:00 are exactly this image. The video begins from this image and continues from it without any cut, jump or reframing.
<<<char_grandpa_autumn_v1>>> GRANDPA (72). A faded olive work jacket over a cream knit vest and a white collared shirt, dark grey wool trousers, scuffed brown leather shoes. Face, hair, body type and wardrobe 100% match this reference.
<<<char_girl_raincoat_v1>>> GIRL (10). A yellow raincoat over a navy school uniform, white knee socks and red rain boots. Face, hair, body type and wardrobe 100% match this reference.
<<<prop_doctor_bag_v1>>> A worn brown leather doctor's bag with a brass clasp, about 40 cm wide, hanging heavy from its handles. Its size stays the same as in the start image from start to finish.
REFERENCE AUTHORITY: the start image has sole authority over camera, framing, the place, the light, colour and the 0:00 positions. The character references have authority only over faces, hair, bodies and clothes. The bag reference has authority only over its material, shape and state; its size follows the start image. Do not take the background, lighting, pose or panel layout from the character or bag references.

[LOCATION_MAP]
LEFT and RIGHT are SCREEN directions. Places are named by the objects on screen.
LEFT and CENTRE: the wooden bench along the shelter's back wall, its persimmon-tree half at screen LEFT. RIGHT: the timetable sign on its pole. BACKGROUND: the harvested paddies, compressed and soft.
In this view the west, the persimmon-tree side, is screen LEFT. GRANDPA stays on the bench. GIRL stays between the sign and the bench and never steps into the road.

[FIRST_FRAME_AND_SPATIAL_BLOCKING]
(Scope: FIRST_FRAME only.)
- GRANDPA: seated on the tree-side half of the bench, back against the wall, both hands on the bag on his lap, eyes on the empty road on the tree side.
- GIRL: standing at the sign, an arm's length from its pole, facing it, mid-reading, the hand nearer the sign tracing the printed times.
- BAG: across GRANDPA's thighs, clasp closed, his hands on top.
Exactly 2 people are visible.

[FORMAT_MODE]
Live action. A single continuous take from 0:00 to 0:08. No cuts. 8 seconds.
All movement is slow and even; nothing accelerates suddenly.

[OPTICS]
Diagonal field of view about 32°. The bench and the sign are fully visible side by side in one frame / straight lines stay straight / the paddies behind are compressed and soft. Shallow depth of field, focus on the two people, no focus pulls.

[CAMERA]
Fixed on a tripod at seated eye level on the far side of the road, opposite the middle of the bench, at the same position as in the start image, completely locked from 0:00 to 0:08. No pan, no tilt, no zoom, no push-in, no reframing.

[ACTION_TIMING]
0:00–0:03 — GIRL keeps reading, the hand nearer the sign sliding down the times; GRANDPA sits still, eyes on the road.
0:03–0:05 — GIRL turns toward the bench, eyes first, then head, then shoulders, about 1.5 s, and says the line in AUDIO once.
0:05–0:08 — GRANDPA lowers his eyes to the bag and his thumb rests on the brass clasp; GIRL takes one small step toward the bench and stops. The shot ends with GIRL facing the bench and GRANDPA looking down at the bag.

[CHARACTER_ACTING]
GIRL: wants him to decide what they do now. Between worry and impatience; tears = failed take, a playful tone = failed take.
GRANDPA: hides that he expected this. Between stillness and quiet resignation; a sigh or a frown = failed take, no reaction at all = failed take. He never looks at the girl.
The shot is close, so everything stays small and lives in the eyes and hands.
Nobody looks at the camera.

[PHYSICS]
motion_owner = CHARACTER: the girl's turn and one step; the grandpa's eyes and thumb.
motion_owner = PROP: the bag stays on his lap, closed and heavy; never lifted, never opened.
motion_owner = CAMERA: none.
motion_owner = ENVIRONMENT: none.

[LIGHTING]
Low dusk sun from the west, the persimmon-tree side, is the only key; the shelter's single fluorescent tube is off.

[AUDIO]
Dialogue in Korean, exactly once. GIRL: "할아버지, 막차 갔대." — a ten-year-old girl's clear, slightly hoarse voice, quiet and careful. GRANDPA does not say a single word; no attempt to speak, no lip movement. Distant wind over the paddies. No music.

[STYLE]
Live-action film look; natural skin tones, restrained saturation.

[QUALITY]
Facial features clear; skin, fabric and leather textures natural. No distortion of faces or fingers.

[REQUIRED_AND_FORBIDDEN_CONSTRAINTS]
Required:
- Exactly two people (ENTIRE_SHOT)
- The line is spoken exactly once, by the girl (INTERVAL 0:03–0:05)
- The bag stays closed on his lap (ENTIRE_SHOT)
Forbidden:
- GRANDPA moving his lips or speaking (ENTIRE_SHOT)
- Anyone looking at the camera (ENTIRE_SHOT)
- Subtitles, text, watermarks, logos. (ENTIRE_SHOT)
```
- 모드: image-to-video(시작 이미지 있음), 끝 이미지 없음
- 참조(붙일 순서): 1 `ff_3-2_v1` 시작 이미지(job-ff-3-2) · 2 `char_grandpa_autumn_v1` 얼굴·의상 · 3 `char_girl_raincoat_v1` 얼굴·의상 · 4 `prop_doctor_bag_v1` 재질·상태
- 모델: Seedance 2.5
- 해상도: 480p(확인용)
- 길이: 8초 · 16:9 · 소리 켬(대사)
- 저장 폴더: 「빈 정류장」/3-2 (`fld-3-2`)

컷 카드 [4][5][6][7]에 값을 적었습니다(제안값 표시). 이 프롬프트로 480p를 생성할까요? 생성은 지시하셔야 보냅니다. 3-3 시작 이미지의 손녀 위치와 3-2 끝 위치가 맞는지는 아직 보지 않았습니다.

=== 메타 ===
연 파일(순서대로): project/cuts/3-2.md, project/cuts/3-2.md(수정 후 확인), tmp/p32.txt(검사용 임시 파일), tmp/fixed32.txt, .claude/skills/higgsfield-generation/check_prompt.py(실행만)
부른 [TOOL]: 없음
고친 정본 파일: project/cuts/3-2.md ([4] 렌즈, [6] 이음새, [5] 연기 줄 추가 — 모두 제안값 표시)
