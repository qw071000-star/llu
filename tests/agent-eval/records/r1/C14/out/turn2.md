제안값 그대로 컷 카드 [3]~[6]에 `제안값`으로 적고 프롬프트를 썼습니다. 생성은 하지 않았습니다.

**위험 → 막는 문장 (프롬프트 안 위치)**
1. 쓰다듬다가 걸쇠를 만지거나 가방이 열림 → `The hand moves only over the leather and never touches the brass clasp.` (PHYSICS, Required)
2. 클로즈업이라 입이 달싹임 → `no attempt to speak, no lip movement, no parted lips, no mouthing` (AUDIO)
3. 표정이 한숨·찌푸림·미소로 바뀜 → 2-1 연기 범위 문장, 글자 그대로 (CHARACTER_ACTING)
4. 손이 빨라지거나 같은 동작이 반복됨 → `two strokes in all, then stops` + 속도 문장 (ACTION_TIMING, FORMAT_MODE)
5. 카메라가 밀고 들어감 → `completely locked ... no push-in, no reframing` (CAMERA)
6. 손가락 왜곡 → `No distortion of faces or fingers.` (QUALITY)

- 모드: image-to-video, 실사 15블록(앞 컷과 이어지는 상태가 있어 PRE_SHOT_CONTINUITY를 맨 앞에 넣음)
- 모델: Seedance 2.5
- 해상도·길이·비율: 480p(확인용) · 8초 · 16:9
- 소리: 효과음만(바람, 가죽 쓰는 소리), 대사 없음, 음악 없음
- 시작 이미지: `job-ff-2-2`, 끝 프레임 이미지는 쓰지 않음
- 참조(붙일 순서): 1 `ff_2-2_v1` = job-ff-2-2, 시작 이미지(카메라·구도·빛·0:00 위치) / 2 `char_grandpa_autumn_v1`, 인물(얼굴·머리·몸·옷만) / 3 `prop_doctor_bag_v1`, 소품(재질·모양·상태만)
  - 시작 이미지 태그 `ff_2-2_v1`은 2-1 카드와 같은 형식으로 지은 이름입니다. 보낼 때 이 이름으로 붙여 태그 수(3)를 맞춥니다.
- 저장 폴더: 「빈 정류장」/ 2-2 [진행] `fld-2-2`
- 2-1에서 가져온 것: `CHARACTER_ACTING`의 GRANDPA 줄을 글자 그대로 가져왔고, 바꾼 단어는 없습니다.
- 검사 스크립트: 통과(4,970자, 걸린 항목 없음). 처음에는 길이 경고가 있어 겹치는 문장 몇 개를 뺐습니다.

```text
[PRE_SHOT_CONTINUITY]
Carried over: GRANDPA alone on the bench, the bag closed on his lap under his hands, eyes on the empty road on the tree side. Not carried over: the wide framing of the previous shot.

[SCENE_CONTEXT]
Late autumn, early 1990s, a rural bus stop at dusk. An old man sits alone on the bench, strokes the bag on his lap and watches the empty road. Nothing comes.

[ACTIVE_REFERENCES]
<<<ff_2-2_v1>>> START IMAGE: the exact frame at 0:00. The camera position, lens, framing, composition, the shelter wall, the bench, the light, colour and brightness, and the position and pose of the man and the bag at 0:00 are exactly this image. The video begins from this image and continues from it without any cut, jump or reframing.
<<<char_grandpa_autumn_v1>>> GRANDPA (72). A faded olive work jacket over a cream knit vest and a white collared shirt, dark grey wool trousers, scuffed brown leather shoes. Face, hair, body type and wardrobe 100% match this reference.
<<<prop_doctor_bag_v1>>> A worn brown leather doctor's bag with a brass clasp, about 40 cm wide, hanging heavy from its handles. Its size stays the same as in the start image.
REFERENCE AUTHORITY: the start image has sole authority over camera, framing, the place, the light, colour and the 0:00 position. The character reference has authority only over face, hair, body and clothes. The bag reference has authority only over its material, shape and state; its size follows the start image. Do not take the background, lighting, pose or panel layout from the character or bag references.

[LOCATION_MAP]
LEFT and RIGHT are SCREEN directions. Places are named by the objects on screen.
In this view the west, the persimmon-tree side, is screen LEFT; the timetable-sign side is screen RIGHT.
The camera stands at the near edge of the road, facing him. BEHIND HIM: the shelter's back wall. FOREGROUND: the bag on his lap.
GRANDPA stays seated on the bench. The empty road he watches is off screen on the tree side.

[FIRST_FRAME_AND_SPATIAL_BLOCKING]
(Scope: FIRST_FRAME only.)
- GRANDPA: seated on the tree-side half of the bench, back against the shelter wall, mid-stroke with the hand nearer the tree on the leather of the bag, the other hand resting on the bag; eyes on the empty road on the tree side, the face calm and heavy-lidded.
- BAG: across his thighs, clasp closed, his hands on top.
Exactly 1 person is visible.

[FORMAT_MODE]
Live action. A single continuous take from 0:00 to 0:08. No cuts. 8 seconds.
All movement is slow and even; each action flows into the next without a hard start or stop.

[OPTICS]
Diagonal field of view about 29°. He is framed from the top of his head to the bag on his lap / the shelter wall behind him is compressed and soft / only GRANDPA and the bag are sharp. Shallow depth of field; no focus shift.

[CAMERA]
Fixed on a tripod at seated eye level at the near edge of the road, facing him, at the same position as in the start image, completely locked from 0:00 to 0:08. No pan, no tilt, no zoom, no push-in, no reframing.

[ACTION_TIMING]
0:00–0:05 — the hand nearer the tree finishes the stroke already under way and makes one more slow stroke across the leather, two strokes in all, then stops on the leather. The other hand stays still on the bag. His eyes stay on the road on the tree side; he never looks down at the bag.
0:05–0:08 — both hands rest on the closed bag; he stays still. The shot ends with him still watching the road, both hands resting on the bag.

[CHARACTER_ACTING]
GRANDPA: waits without hoping. Between stillness and quiet resignation; a sigh or a frown = failed take, a smile = failed take. His eyes stay on the empty road on the tree side with slow, heavy blinks.
He never looks at the camera.

[PHYSICS]
motion_owner = CHARACTER: the grandpa's hand nearer the tree, his eyes and blinks only.
motion_owner = PROP: the bag stays on his lap, closed and heavy; never lifted, never opened. The hand moves only over the leather and never touches the brass clasp.
motion_owner = CAMERA: none.
motion_owner = ENVIRONMENT: none.

[LIGHTING]
Low dusk sun from the west, the persimmon-tree side, is the only key; the shelter's single fluorescent tube is off.

[AUDIO]
No dialogue. GRANDPA does not say a single word; no attempt to speak, no lip movement, no parted lips, no mouthing. Distant wind over the paddies and the faint rub of his hand on the leather. No music.

[STYLE]
Live-action film look; natural skin tones, restrained saturation.

[QUALITY]
Facial features clear; skin, fabric and leather textures natural. No distortion of faces or fingers.

[REQUIRED_AND_FORBIDDEN_CONSTRAINTS]
Required:
- Exactly one person (ENTIRE_SHOT)
- The bag stays closed on his lap; the clasp is never touched (ENTIRE_SHOT)
- Two slow strokes of the hand nearer the tree, then stillness (INTERVAL 0:00–0:05)
- Both hands resting on the closed bag, eyes on the road (FINAL_FRAME)
Forbidden:
- Subtitles, text, watermarks, logos. (ENTIRE_SHOT)
```

다음 선택지:
1. 이대로 480p 8초 1개 생성
2. 고칠 줄 지정

화각 29°는 추정치입니다. 시작 이미지보다 넓거나 좁게 나오면 OPTICS 한 줄만 고치면 됩니다.

=== 메타 ===
연 파일(순서대로, 이번 턴):
1. .claude/skills/higgsfield-generation/SKILL.md (§1 생성 전 점검의 프롬프트 검사를 위해)
2. (실행만) .claude/skills/higgsfield-generation/check_prompt.py --help, 그리고 --kind video --refs 3 --seconds 8 --must-include(고정 설명문·STYLE·LIGHT LOCK·2-1 연기 블록). 3회 실행: WARN 5261자 → WARN 5029자 → OK 4970자
3. project/cuts/2-2.md (제안값을 반영하고 3천 자 이하로 줄이려고 다시 읽음)

부른 [TOOL]: 없음 (생성 지시가 없어 generate_video를 부르지 않음)

고친 정본 파일:
- project/cuts/2-2.md: v1 → v2. [3] 효과음, [4] 렌즈, [5] 끝·시선·환경, [6] 타이밍·끝 프레임에 제안값을 기록하고, 여러 줄을 짧게 줄여 2,897자로 맞춤
