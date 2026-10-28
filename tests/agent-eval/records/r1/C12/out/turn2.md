제안값 그대로 컷 카드 [3]~[7]에 `제안값`으로 기록했습니다. 3-2 영상 프롬프트입니다. 아직 보내지 않았습니다.

- 모드: image-to-video (시작 이미지 `job-ff-3-2`, 끝 이미지 없음)
- 참조(붙이는 순서): 1 `ff_3-2_v1` 시작 이미지(카메라·구도·장소·빛·0:00 위치) · 2 `char_grandpa_autumn_v1` 할아버지(얼굴·머리·몸·옷만) · 3 `char_girl_raincoat_v1` 손녀(얼굴·머리·몸·옷만) · 4 `prop_doctor_bag_v1` 가방(재질·모양·상태만, 크기는 시작 이미지)
- 모델: Seedance 2.5
- 해상도: 480p (확인용)
- 길이·화면비: 8초 · 16:9
- 소리: 켬 (손녀 대사 한 번, 바람, 음악 없음)
- 저장 폴더: `fld-3-2`

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
LEFT: the wooden bench along the shelter's back wall, GRANDPA on its tree-side half. RIGHT: the timetable sign on its pole; its printed times are never legible. BACKGROUND: the harvested paddies behind, compressed and soft.
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
Diagonal field of view about 35°. The bench and the timetable sign fill the frame side by side / the paddies behind are compressed and soft / no wide-angle distortion on faces or bodies. Focus stays on both people from start to finish; no focus pull.

[CAMERA]
Fixed on a tripod at seated eye level on the far side of the road, opposite the middle of the bench, facing the shelter, at the same position as in the start image, completely locked from 0:00 to 0:08. No pan, no tilt, no zoom, no push-in, no reframing.

[ACTION_TIMING]
0:00–0:03 — GIRL keeps reading, the hand nearer the sign sliding down the times; GRANDPA sits still, eyes on the road.
0:03–0:05 — GIRL turns toward the bench, eyes first, then head, then shoulders, about 1.5 s, and says the line in AUDIO once.
0:05–0:08 — GRANDPA lowers his eyes to the bag and his thumb rests on the brass clasp; GIRL takes one small step toward the bench and stops. The shot ends with GIRL facing the bench and GRANDPA looking down at the bag.

[CHARACTER_ACTING]
GIRL: wants him to decide what they do now. Between worry and impatience; tears = failed take, a playful tone = failed take.
GRANDPA: hides that he expected this. Between stillness and quiet resignation; a sigh or a frown = failed take, no reaction at all = failed take. He never looks at the girl.
Neither of them looks at the camera.

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
- Subtitles, text, watermarks, logos. (ENTIRE_SHOT)
```

**3-1 영상 프롬프트와의 관계**
- 글자 그대로 가져옴: 속도 문장, `ACTION_TIMING`, `PHYSICS`, `CHARACTER_ACTING`, `AUDIO`. 바꾼 단어는 없습니다.
- 3-2 값으로 씀: 참조(시작 이미지 `ff_3-2_v1`), `LOCATION_MAP`, 첫 프레임(시작 이미지대로 "an arm's length from its pole" 추가), `OPTICS` 35°, `CAMERA` 앉은 눈높이.
- Forbidden에서 3-1의 "GRANDPA moving his lips or speaking" 줄은 뺐습니다. 3-2에서 실제로 난 실패가 아니고, 같은 위험은 AUDIO 문장이 막습니다. 3-1과 똑같이 두고 싶으면 말씀해 주세요.
- 눈의 삶 문장은 넣지 않았습니다. "그대로"를 3-1 연기 문장 그대로로 읽었습니다.

**위험 → 막는 문장**
1. 할아버지가 카메라를 봄. `job-ff-3-2-old`에서 실제로 났습니다. → `Neither of them looks at the camera.` (CHARACTER_ACTING. 카드 [10]의 문장과 같은 뜻이고, 3-1 문장 그대로 씁니다)
2. 할아버지 입술이 움직임. 3-2는 얼굴이 커서 더 잘 보입니다. → `GRANDPA does not say a single word; no attempt to speak, no lip movement.` (AUDIO)
3. 손녀가 휙 돌아섬. 3-1의 OK 이유가 깨집니다. → `eyes first, then head, then shoulders, about 1.5 s` (ACTION_TIMING)
4. 카메라가 밀거나 다시 잡음. 화각이 좁아 작은 움직임도 크게 보입니다. → `No pan, no tilt, no zoom, no push-in, no reframing.` (CAMERA)
5. 가방이 열리거나 들림. 3-4 전까지 닫혀 있어야 합니다. → `never lifted, never opened.` (PHYSICS)
6. 시간표 글씨가 읽힘. 3-2는 시간표가 커서 위험이 큽니다. → `its printed times are never legible.` (LOCATION_MAP)

보내기 전 점검을 마쳤습니다. 첫 프레임이 시작 이미지와 같고, 참조 4개와 태그 4개가 맞습니다. 본문에 컷 번호는 없고, 장소 참조에는 구도 권한을 주지 않았습니다. 프롬프트 자동 검사는 생성 단계에서 돌립니다.

이대로 480p 8초 확인본을 `fld-3-2`에 보낼까요? 고칠 줄이 있으면 그 줄만 말씀해 주세요.

=== 메타 ===
- 연 파일(순서대로):
  - 새로 읽은 파일 없음 (turn1에서 읽은 내용 사용)
  - 고치느라 project/cuts/3-2.md를 다시 열었음
- 부른 [TOOL]: 없음
- 고친 정본 파일:
  - project/cuts/3-2.md
    - [3] 효과음·음악 (제안값)
    - [4] 렌즈 관찰 결과·심도·초점 (제안값)
    - [5] 지나가지 않는 구역 (제안값), 연기 줄 추가 (제안값)
    - [6] 대사 원문 (제안값), 다음 컷 이음새 (제안값)
    - [7] 가져온 OK에 연기·소리 추가
