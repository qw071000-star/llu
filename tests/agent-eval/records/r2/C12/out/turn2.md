제안값 4개를 그대로 썼고, 컷 카드 [4]~[6]에 `(제안값)`으로 기록했습니다. 3-2 영상 프롬프트 전문입니다. 생성은 아직 하지 않았습니다.

- 모드: image-to-video (시작 이미지 + 요소 참조), 15블록 실사
- 참조(붙이는 순서): 1 ff_3-2_v1 — 시작 이미지(`job-ff-3-2`) · 2 char_grandpa_autumn_v1 — 할아버지 얼굴·의상 · 3 char_girl_raincoat_v1 — 손녀 얼굴·의상 · 4 prop_doctor_bag_v1 — 가방 재질·모양·상태
- 모델: Seedance 2.5
- 해상도: 480p (확인용)
- 길이: 8초 · 16:9 · 소리 켬(대사)
- 저장 폴더: 「빈 정류장」/3-2 [진행] `fld-3-2`

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
LEFT: the bench along the shelter's back wall, its persimmon-tree half nearer the left. RIGHT: the timetable sign on its pole.
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
Diagonal field of view about 32°. The bench and the timetable sign fill the frame side by side / the paddies behind are compressed and soft / the camera is physically far away. Both people are sharp; only the background is soft; no focus pull.

[CAMERA]
Fixed on a tripod at seated eye level on the far side of the road, opposite the middle of the bench, facing north, at the same position as in the start image, completely locked from 0:00 to 0:08. No pan, no tilt, no zoom, no push-in, no reframing.

[ACTION_TIMING]
0:00–0:03 — GIRL keeps reading, the hand nearer the sign sliding down the times; GRANDPA sits still, eyes on the road.
0:03–0:05 — GIRL turns toward the bench, eyes first, then head, then shoulders, about 1.5 s, and says the line in AUDIO once.
0:05–0:08 — GRANDPA lowers his eyes to the bag and his thumb rests on the brass clasp; GIRL takes one small step toward the bench and stops. The shot ends with GIRL facing the bench and GRANDPA looking down at the bag.

[CHARACTER_ACTING]
GIRL: wants him to decide what they do now. Between worry and impatience; tears = failed take, a playful tone = failed take.
GRANDPA: hides that he expected this. Between stillness and quiet resignation; a sigh or a frown = failed take, no reaction at all = failed take. He never looks at the girl.
Nobody looks at the camera.

[PHYSICS]
motion_owner = CHARACTER: the girl's turn and one step; the grandpa's eyes and thumb.
motion_owner = PROP: the bag stays on his lap, closed and heavy; never lifted, never opened.
motion_owner = CAMERA: none.
motion_owner = ENVIRONMENT: none.

[LIGHTING]
Low dusk sun from the west, the persimmon-tree side, is the only key; the shelter's single fluorescent tube is off.

[AUDIO]
Dialogue in Korean, exactly once. GIRL: "할아버지, 막차 갔대." — a ten-year-old girl's clear, slightly hoarse voice, quiet and careful. GRANDPA does not say a single word: no attempt to speak, no parted lips, no mouthing. Distant wind over the paddies. No music.

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
- Subtitles, text, watermarks, logos. (ENTIRE_SHOT)
```

**3-1 영상에서 가져온 줄:** ACTION_TIMING, PHYSICS, 속도 문장(FORMAT_MODE 둘째 줄)은 글자 그대로 옮겼고, 바꾼 단어는 없습니다. 연기는 3-1과 같고 한 줄만 바꿨습니다: `Neither of them looks at the camera.` → `Nobody looks at the camera.`

**실패 위험 → 막는 문장 (프롬프트에 넣은 곳)**
1. 누군가 카메라를 봄(`job-ff-3-2-old`) → `Nobody looks at the camera.` (CHARACTER_ACTING)
2. 할아버지 입이 움직임 → `GRANDPA does not say a single word: no attempt to speak, no parted lips, no mouthing.` (AUDIO) + Forbidden 줄
3. 대사가 두 번 나옴 → Required `exactly once, by the girl (INTERVAL 0:03–0:05)`
4. 가방이 열리거나 들림 → Required `The bag stays closed on his lap` + PHYSICS
5. 카메라가 밀거나 다시 잡음 → CAMERA의 `completely locked … no reframing`

**검사 스크립트:** `--kind video --refs 4 --seconds 8` + 고정 문장 검사 → FAIL 0 · WARN 1. 경고는 길이 5,089자(5,000자 안팎 권장)입니다. 같은 블록 구성으로 OK를 받은 3-1 영상 프롬프트가 5,027자라서 그대로 두었습니다. 겹치던 배경 문장은 이미 뺐습니다.

**참고:** 3-2는 3-1의 다음 순간이 아니고 같은 순간이라서, 이어받는 상태를 쓰는 PRE_SHOT_CONTINUITY 블록은 넣지 않았습니다. 0:00 상태는 시작 이미지가 정합니다.

이 프롬프트로 480p 확인 생성을 보낼까요? 견적은 약 40크레딧입니다(`get_cost`로 확인 후 전송).

=== 메타 ===
연 파일(순서대로):
1. .claude/skills/higgsfield-generation/check_prompt.py (--help로 사용법만 확인)
2. project/ok-cuts.md — "### 3-1 영상" 절의 프롬프트 글자 수만 셈(길이 비교용)
3. project/cuts/3-2.md (기록 확인)
(1턴에서 읽은 파일은 다시 열지 않음. 임시 파일: tmp/v3-2_prompt.txt, tmp/v3-2_must.txt)

부른 [TOOL]: 없음

고친 정본 파일:
- project/cuts/3-2.md — [4] 렌즈 관찰 결과·심도 (제안값), [5] 지나가지 않는 구역 (제안값)·연기 줄 추가 (제안값), [6] 다음 컷과 맞출 것 (제안값)

검사 스크립트: python3 .claude/skills/higgsfield-generation/check_prompt.py --kind video tmp/v3-2_prompt.txt --refs 4 --seconds 8 --must-include tmp/v3-2_must.txt → FAIL 0 · WARN 1 (길이 5,089자)
