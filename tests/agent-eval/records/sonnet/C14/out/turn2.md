제안값을 그대로 써서 만들었습니다. 컷 카드(`project/cuts/2-2.md`)에 `제안값`으로 기록했습니다. 검사 스크립트는 통과했습니다(걸린 항목 없음).

**위험 → 막는 문장**
1. 한숨·찡그림·미소 → `a sigh or a frown = failed take, a smile = failed take` (2-1에서 글자 그대로)
2. 입 움직임 → `no attempt to speak, no lip movement` + Forbidden `GRANDPA moving his lips`
3. 카메라 응시 → `He never looks at the camera.`
4. 쓰다듬다 가방이 열림 → `the clasp is never touched; never lifted, never opened` + Required 가방 닫힘
5. 손이 여러 번·빠르게 문지름 → Required `Exactly one stroke` + 모든 동작 느리고 고르게
6. 카메라가 밀고 들어옴 → `No pan, no tilt, no zoom, no push-in, no reframing.`

```text
[SCENE_CONTEXT]
Late autumn, early 1990s, a rural bus stop at dusk. An old man sits alone on the bench with a bag on his lap and watches the empty road. In this medium close shot he strokes the leather of the bag once, slowly, and nothing comes.

[ACTIVE_REFERENCES]
<<<ff_2-2_v1>>> START IMAGE: the exact frame at 0:00. The camera position, lens, framing, composition, the shelter wall, bench, the light, colour and brightness, and the position and pose of the man, his hands and the bag at 0:00 are exactly this image. The video begins from this image and continues from it without any cut, jump or reframing.
<<<char_grandpa_autumn_v1>>> GRANDPA (72). A faded olive work jacket over a cream knit vest and a white collared shirt, dark grey wool trousers, scuffed brown leather shoes. Face, hair, body type and wardrobe 100% match this reference.
<<<prop_doctor_bag_v1>>> A worn brown leather doctor's bag with a brass clasp, about 40 cm wide, hanging heavy from its handles. Its size stays the same as in the start image from start to finish.
REFERENCE AUTHORITY: the start image has sole authority over camera, framing, the place, the light, colour and the 0:00 position. The character reference has authority only over face, hair, body and clothes. The bag reference has authority only over its material, shape and state; its size follows the start image. Do not take the background, lighting, pose or panel layout from the character or bag references.

[LOCATION_MAP]
LEFT and RIGHT are SCREEN directions. Places are named by the objects on screen.
LEFT EDGE: the tree side of the shelter. CENTRE: GRANDPA on the bench, the concrete shelter wall behind him. FOREGROUND: the bag on his lap.
In this view the west, the persimmon-tree side, is screen LEFT. GRANDPA stays on the bench.

[FIRST_FRAME_AND_SPATIAL_BLOCKING]
(Scope: FIRST_FRAME only.)
- GRANDPA: seated on the tree-side half of the bench, back against the wall, both hands on the bag on his lap, mid-stroke with the hand nearer the tree on the leather; eyes on the empty road on the tree side, the face calm and heavy-lidded.
- BAG: across his thighs, clasp closed.
Exactly 1 person is visible.

[FORMAT_MODE]
Live action. A single continuous take from 0:00 to 0:08. No cuts. 8 seconds.
All movement is slow and even; nothing accelerates suddenly.

[OPTICS]
Diagonal field of view about 29°. Only GRANDPA and the bag are sharp / the background is compressed and soft / his face and the bag fill the frame. Shallow depth of field.

[CAMERA]
Fixed on a tripod at seated eye level at the near edge of the road, about 2 m from GRANDPA, facing the tree-side half of the bench, at the same position as in the start image, completely locked from 0:00 to 0:08. No pan, no tilt, no zoom, no push-in, no reframing.

[ACTION_TIMING]
0:00–0:03 — the hand nearer the tree finishes one slow stroke along the leather and stops; his eyes stay on the empty road.
0:03–0:06 — his hand stays still on the leather; his eyes stay on the road; one slow blink.
0:06–0:08 — both hands rest on the bag, still. The shot ends with him still watching the road, both hands resting on the closed bag.

[CHARACTER_ACTING]
GRANDPA: waits without hoping. Between stillness and quiet resignation; a sigh or a frown = failed take, a smile = failed take. His eyes stay on the empty road on the tree side with slow, heavy blinks.
He never looks at the camera.

[PHYSICS]
motion_owner = CHARACTER: the grandpa's eyes and the hand nearer the tree only, one slow stroke.
motion_owner = PROP: the bag stays on his lap, closed and heavy; the clasp is never touched; never lifted, never opened.
motion_owner = CAMERA: none.
motion_owner = ENVIRONMENT: none.

[LIGHTING]
Low dusk sun from the west, the persimmon-tree side, is the only key; the shelter's single fluorescent tube is off.

[AUDIO]
No dialogue. GRANDPA does not say a single word; no attempt to speak, no lip movement. The faint sound of a palm on leather, distant wind over the paddies. No music.

[STYLE]
Live-action film look; natural skin tones, restrained saturation.

[QUALITY]
Facial features clear; skin, fabric and leather textures natural. No distortion of faces or fingers.

[REQUIRED_AND_FORBIDDEN_CONSTRAINTS]
Required:
- Exactly one person (ENTIRE_SHOT)
- The bag stays closed on his lap (ENTIRE_SHOT)
- Exactly one stroke of the hand on the leather (INTERVAL 0:00–0:03)
Forbidden:
- GRANDPA moving his lips (ENTIRE_SHOT)
- Subtitles, text, watermarks, logos. (ENTIRE_SHOT)
```

- 모드: 영상 image-to-video, 실사 15블록
- 참조(붙일 순서): 1 `ff_2-2_v1` 시작 이미지(`job-ff-2-2`) — 전부 · 2 `char_grandpa_autumn_v1` — 얼굴·머리·의상만 · 3 `prop_doctor_bag_v1` — 재질·형태·상태만
- 모델: Seedance 2.5 · 480p(확인) · 8초 · 16:9 · 소리 효과음만
- 저장 폴더: 2-2 `fld-2-2` (프로젝트 `prj-sim-0001`)
- 표정 가져온 OK: 2-1 영상(`job-v-2-1`) — `CHARACTER_ACTING` 할아버지 줄과 입 움직임 금지 줄, 글자 그대로

화면 속 배경(벽, 왼쪽 감나무 쪽)은 제가 이미지를 보고 확인한 것이 아니라 제안값입니다. 시작 이미지와 다르면 알려 주세요. 생성은 하지 않았습니다. 보내라고 하시면 보냅니다.

=== 메타 ===
- 연 파일(순서대로): project/cuts/2-2.md, .claude/skills/video-prompt/live-action.md(턴1 읽은 것 재사용), .claude/skills/higgsfield-generation/check_prompt.py(실행만), tmp/p22.txt(작성)
- 부른 [TOOL]: 없음
- 고친 정본 파일: project/cuts/2-2.md (v0 → v1, 제안값 기록)
