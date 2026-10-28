제안값 6개를 모두 쓰고 컷 카드 [4]~[6]에 `(제안값)`으로 적었습니다. 3-2 영상 프롬프트입니다. 아직 보내지 않았습니다.

**위험 → 막는 문장**
1. 할아버지가 카메라를 봄(3-2 시작 이미지 거절 이유) → `Nobody looks at the camera.`
2. 더 가까운 샷이라 할아버지의 입술 움직임이 눈에 띔(3-1에서 가져온 동작) → Forbidden `GRANDPA moving his lips or speaking (ENTIRE_SHOT)`, AUDIO에 `no lip movement`
3. 대사가 두 번 나오거나 다른 사람이 말함 → Required `The line is spoken exactly once, by the girl (INTERVAL 0:03–0:05)`
4. 가방이 들리거나 열림 → Required `The bag stays closed on his lap (ENTIRE_SHOT)`, PHYSICS `never lifted, never opened`
5. 손녀의 한 걸음이 크게 보이거나 카메라가 따라감 → `one small step toward the bench and stops`, CAMERA `No pan, no tilt, no zoom, no push-in`. 결과 이미지를 볼 수 없어 추정한 위험입니다.

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
LEFT AND CENTRE: the wooden bench along the concrete shelter's back wall. RIGHT: the timetable sign on its pole. FOREGROUND: the empty road edge. BACKGROUND: the harvested paddies, compressed and soft.
In this view the west, the persimmon-tree side, is screen LEFT. GRANDPA stays on the bench. GIRL stays between the sign and the bench and never steps into the road.

[FIRST_FRAME_AND_SPATIAL_BLOCKING]
(Scope: FIRST_FRAME only.)
- GRANDPA: seated on the tree-side half of the bench, back against the wall, both hands on the bag on his lap, eyes on the empty road on the tree side.
- GIRL: standing at the sign, facing it, mid-reading, the hand nearer the sign tracing the printed times.
- BAG: across GRANDPA's thighs, clasp closed, his hands on top.
Exactly 2 people are visible.

[FORMAT_MODE]
Live action. A single continuous take from 0:00 to 0:08. No cuts. 8 seconds.
All movement is slow and even; nothing accelerates suddenly.

[OPTICS]
Diagonal field of view about 32°. The bench and the timetable sign fill the frame side by side / the paddies behind are compressed and soft / only the two people and the sign are sharp. Shallow depth of field.

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
- Subtitles, text, watermarks, logos. (ENTIRE_SHOT)
```

- 모드: 이미지→영상(시작 이미지), 실사 15블록
- 참조(붙일 순서, 4개): 1 `ff_3-2_v1` 시작 이미지(`job-ff-3-2`) · 2 `char_grandpa_autumn_v1` · 3 `char_girl_raincoat_v1` · 4 `prop_doctor_bag_v1`
- 모델: Seedance 2.5 · 480p(확인용) · 8초 · 16:9 · 소리 켬(대사)
- 저장: `fld-3-2`
- 예상 비용: 약 40 크레딧(OK 대장에 같은 설정이 있어 새 견적은 따로 보지 않음)
- 검사 스크립트: 통과, 5,087자, 걸린 항목 없음

**3-1 OK 프롬프트에서 바뀐 줄 (전 → 후)**
- 시작 이미지 태그: `<<<ff_3-1_v2>>>` → `<<<ff_3-2_v1>>>`
- 시작 이미지 문장: `the shelter, bench, sign, tree` → `the shelter, bench, sign` (3-2는 가까운 샷이라 감나무를 구도에 넣지 않음. 보이는지는 추정)
- `LOCATION_MAP`의 좌표 줄: `LEFT EDGE: the bare persimmon tree. CENTRE: the concrete shelter with the bench along its back wall. RIGHT: the timetable sign on its pole. FOREGROUND: the empty road edge.` → `LEFT AND CENTRE: the wooden bench along the concrete shelter's back wall. RIGHT: the timetable sign on its pole. FOREGROUND: the empty road edge. BACKGROUND: the harvested paddies, compressed and soft.`
- `OPTICS`: `about 63°. The tree, the whole shelter and the sign are fully visible in one frame / straight lines stay straight / no telephoto compression. Deep focus.` → `about 32°. The bench and the timetable sign fill the frame side by side / the paddies behind are compressed and soft / only the two people and the sign are sharp. Shallow depth of field.`
- `CAMERA`: `standing eye level ... same position as in the start image` → `seated eye level ... opposite the middle of the bench, facing north, at the same position as in the start image`
- `CHARACTER_ACTING` 끝 줄: `Neither of them looks at the camera.` → `Nobody looks at the camera.`
- 나머지(`ACTION_TIMING`, `PHYSICS`, `AUDIO`, 연기, Required/Forbidden)는 3-1 그대로입니다.

보낼까요? 보내라고 하시면 `fld-3-2`에 480p로 한 번만 보내고 멈추겠습니다. 3-3 이음새 기준은 3-3을 쓸 때 정합니다.

=== 메타 ===
연 파일(순서대로):
- .claude/skills/higgsfield-generation/SKILL.md (앞부분)
- .claude/skills/higgsfield-generation/check_prompt.py (앞부분)
- project/cuts/3-2.md (고친 뒤 확인)
(그 밖의 파일은 turn1에서 이미 읽음)
부른 [TOOL]: 없음 (검사 스크립트 `check_prompt.py`만 실행. 프롬프트·고정 문장 파일은 `tmp/p32.txt`, `tmp/fixed.txt`)
고친 정본 파일:
- project/cuts/3-2.md ([4] 렌즈 32°·관찰 결과·심도·화면 좌표, [5] 끝·동선·시선, [6] 타이밍·이음새를 `(제안값)`으로 기록)
