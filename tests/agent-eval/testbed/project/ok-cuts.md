# OK 대장 — 「빈 정류장」

> 사용자가 OK(승인)한 결과물만 둔다. 승인한 그 자리에서 쓴다.
> 프롬프트는 생성에 보낸 글자 그대로 둔다(`higgsfield-generation` §4).
> 목록은 기준이 필요할 때 읽는다. 카드는 그 번호를 가져다 쓸 때 그 카드 하나만 연다.
> 같은 번호·종류의 새 OK가 생기면 옛 카드는 로그로 옮기고 목록 줄을 바꾼다.

## 목록

| 번호 | 종류 | job | 모델 · 설정 | 승인일 | OK 이유 (가져다 쓸 만한 것) | 한계 |
|---|---|---|---|---|---|---|
| CH-001 | 인물 | `job-ch001` | GPT Image 2.5 · 2k | 2026-10-21 | 얼굴 | 없음 |
| CH-002 | 인물 | `job-ch002` | GPT Image 2.5 · 2k | 2026-10-21 | 전체 | 주근깨 약함 |
| LC-001-V1 | 장소 | `job-lc001v1` | GPT Image 2.5 · 2k | 2026-10-22 | 정류장 분위기 | 감 열매 조금 많음 |
| 1-1 | 시작 이미지 | `job-ff-1-1` | GPT Image 2.5 · 1k | 2026-10-23 | 하늘 색 | 없음 |
| 2-1 | 영상 | `job-v-2-1` | Seedance 2.5 · 480p · 8초 | 2026-10-24 | 할아버지 표정(기대 안 하는 얼굴) | 낙엽 속도 |
| 2-2 | 시작 이미지 | `job-ff-2-2` | GPT Image 2.5 · 1k | 2026-10-25 | 전체 | 없음 |
| 3-1 | 시작 이미지 | `job-ff-3-1` | GPT Image 2.5 · 1k | 2026-10-25 | 색감, 질감 | 없음 |
| 3-1 | 영상 | `job-v-3-1` | Seedance 2.5 · 480p · 8초 | 2026-10-26 | 손녀 돌아서는 속도 | 없음 |
| 3-2 | 시작 이미지 | `job-ff-3-2` | GPT Image 2.5 · 1k | 2026-10-27 | 전체 | 없음 |
| 3-3 | 시작 이미지 | `job-ff-3-3` | GPT Image 2.5 · 1k | 2026-10-27 | 전체 | 없음 |

- **번호:** 컷은 장면-컷(`3-1`), 에셋은 에셋 ID(`CH-001`, `LC-001-V2`).
- **종류:** 시작 이미지 · 끝 이미지 · 영상 · 인물 · 장소 · 소품 · 그림체.

## 카드

### CH-001 인물

- job: `job-ch001` · 승인: 2026-10-21 · 저장: 00 에셋 / 승인
- 모델 · 설정: GPT Image 2.5 · 2k · 16:9 · 장 수 1
- 시작 이미지: —
- 참조(붙인 순서): 없음
- 가져온 OK: 없음
- OK 이유: "얼굴 좋다, 이걸로"
- 한계: 없음
- 프롬프트(보낸 그대로):

```text
Create a photorealistic single wide horizontal three-panel character reference sheet of the same man. The image is divided into three clean vertical sections with no borders, captions or text.

CHARACTER IDENTITY:
A Korean man in his early seventies with weathered tan skin, deep-set dark eyes, a short grey crew cut, a lean build and slightly stooped shoulders. Deep lines at the eyes and mouth, sun spots on the cheekbones, thin grey brows, a broad flat nose and a closed, slightly downturned mouth. The same exact identity must be maintained wherever the face is visible.

PANEL LAYOUT:
- LEFT PANEL: a front-facing full-body wardrobe view shown strictly from the neck down. The panel is intentionally HEADLESS and ends cleanly at the base of the neck. This is an editorial clothing crop, not an injury: no head, no face, no wound, no gore, no dark opening. The plain background continues cleanly above the neckline. Both hands visible and empty, feet fully visible.
- CENTER PANEL: a full-body rear view of the same man from head to toe, same neutral pose.
- RIGHT PANEL: a large front-facing close-up portrait from the upper chest upward, calm neutral expression, the gaze with a definite focal distance just behind the lens.

BODY AND PROPORTIONS: a lean seventy-year-old build, slightly stooped shoulders, weight a little forward.
OUTFIT — IDENTICAL IN ALL THREE PANELS: A faded olive work jacket over a cream knit vest and a white collared shirt, dark grey wool trousers, scuffed brown leather shoes. The jacket is buttoned to the second button, two chest pockets with flaps; the shirt collar sits over the vest. One physically identical outfit seen from different views. No logos, no prints, no unintended accessories. No profession-signaling props unless explicitly requested.
HAIR — CENTER AND RIGHT PANELS: a short grey crew cut, thinning at the crown, natural matte finish.
REALISM: visible fine skin texture with natural pores, subtle asymmetries and uneven skin tone, no digital smoothing, no beauty filter, matte natural complexion. Eyes have genuine moisture and a small specular catchlight, one eyelid very slightly lower than the other, real iris texture.
BACKGROUND AND LIGHTING: one continuous plain warm-grey seamless backdrop across all panels, soft frontal key light from slightly above. All panels share the same lighting direction, exposure, palette and finish.
CONSISTENCY RULES: one person only. Do not create three similar men. Preserve the exact left-to-right order: headless front outfit view / full-body rear view / front close-up portrait.
no text, no watermark, no logos, no frame borders, no other people, no duplicate figures, no extra panels, no props, no beauty filter, no plastic skin, no extra fingers
```

### CH-002 인물

- job: `job-ch002` · 승인: 2026-10-21 · 저장: 00 에셋 / 승인
- 모델 · 설정: GPT Image 2.5 · 2k · 16:9 · 장 수 1
- 시작 이미지: —
- 참조(붙인 순서): 없음
- 가져온 OK: 없음
- OK 이유: "픽스"
- 한계: 주근깨가 약하게 나옴
- 프롬프트(보낸 그대로):

```text
Create a photorealistic single wide horizontal three-panel character reference sheet of the same girl. The image is divided into three clean vertical sections with no borders, captions or text.

CHARACTER IDENTITY:
A Korean girl of about ten with a round face, straight black hair in a low ponytail and a slim build. Light warm skin with faint freckles across the nose, dark almond eyes, straight thin brows, a small nose and a neutral closed mouth. The same exact identity must be maintained wherever the face is visible.

PANEL LAYOUT:
- LEFT PANEL: a front-facing full-body wardrobe view shown strictly from the neck down. The panel is intentionally HEADLESS and ends cleanly at the base of the neck. This is an editorial clothing crop, not an injury: no head, no face, no wound, no gore, no dark opening. The plain background continues cleanly above the neckline. Both hands visible and empty, feet fully visible.
- CENTER PANEL: a full-body rear view of the same girl from head to toe, same neutral pose.
- RIGHT PANEL: a large front-facing close-up portrait from the upper chest upward, calm neutral expression, the gaze with a definite focal distance just behind the lens.

BODY AND PROPORTIONS: a slim ten-year-old build, narrow shoulders, slightly knock-kneed stance.
OUTFIT — IDENTICAL IN ALL THREE PANELS: A yellow raincoat over a navy school uniform, white knee socks and red rain boots. The raincoat is unbuttoned, hood down, with two flap pockets; the uniform collar is visible at the neck. One physically identical outfit seen from different views. No logos, no prints, no unintended accessories. No profession-signaling props unless explicitly requested.
HAIR — CENTER AND RIGHT PANELS: shoulder-length straight black hair gathered in a low ponytail with a plain black elastic, a few loose strands at the temples, natural matte finish.
REALISM: visible fine skin texture with natural pores, subtle asymmetries and uneven skin tone, no digital smoothing, no beauty filter, matte natural complexion. Eyes have genuine moisture and a small specular catchlight, one eyelid very slightly lower than the other, real iris texture.
BACKGROUND AND LIGHTING: one continuous plain warm-grey seamless backdrop across all panels, soft frontal key light from slightly above. All panels share the same lighting direction, exposure, palette and finish.
CONSISTENCY RULES: one person only. Do not create three similar girls. Preserve the exact left-to-right order: headless front outfit view / full-body rear view / front close-up portrait.
no text, no watermark, no logos, no frame borders, no other people, no duplicate figures, no extra panels, no props, no beauty filter, no plastic skin, no extra fingers
```

### LC-001-V1 장소

- job: `job-lc001v1` · 승인: 2026-10-22 · 저장: 00 에셋 / 승인
- 모델 · 설정: GPT Image 2.5 · 2k · 16:9
- 시작 이미지: —
- 참조(붙인 순서): 없음
- 가져온 OK: 없음
- OK 이유: "정류장 분위기 딱 좋아"
- 한계: 감 열매가 조금 많음
- 프롬프트(보낸 그대로):

```text
Generate a rural bus stop at dusk.
CAMERA: wide shot, camera at standing eye level on the far side of the two-lane road, looking at the shelter's open front, the shelter read slightly at an angle, not square-on.
THE DOMINANT ELEMENT: the low dusk sun raking in from screen left across the shelter's concrete face.
SPATIAL GEOGRAPHY (as seen from the road; LEFT and RIGHT are SCREEN directions, never the character's own left or right):
At the CENTRE, a concrete bus shelter with a corrugated tin roof, its open front facing the camera. A wooden bench runs along its back wall. At the RIGHT of the shelter, a painted metal timetable sign on a single pole. At the LEFT, a bare persimmon tree with a few orange fruits left on the top branches. Behind the shelter, harvested rice paddies stretch to low hills. In the foreground, the cracked asphalt edge of the road.
Nothing else: no other buildings, no cars, no people, no legible text.
Empty deserted bus stop, still air.
Palette of roughly 80% dry ochre and grey concrete — 15% deep blue dusk sky — 5% persimmon orange.
Real material truth: rough cast concrete with rain streaks, rusted tin ridges, a bench worn pale where people sit.
Low dusk sun from screen left, the persimmon-tree side, is the only key; the shelter's single fluorescent tube is off. The persimmon tree is at screen LEFT.
Image finish: ARRI Alexa Mini, 35mm lens, Kodak Vision3 250D. Era lock: late autumn, early 1990s, rural South Korea. Nothing more recent anywhere in frame. Hand-lettered signage, text not legible. No legible text anywhere.
```

### 1-1 시작 이미지

- job: `job-ff-1-1` · 승인: 2026-10-23 · 저장: 1-1 / 승인
- 모델 · 설정: GPT Image 2.5 · 1k · 16:9
- 시작 이미지: —
- 참조(붙인 순서): 1 loc_busstop_road_v1 — 장소
- 가져온 OK: 없음
- OK 이유: "하늘 색 좋아"
- 한계: 없음
- 프롬프트(보낸 그대로):

```text
FIRST FRAME of a film shot — the exact state at 0:00 of the video. LEFT and RIGHT are SCREEN directions, never the character's own left or right.
Using <<<loc_busstop_road_v1>>> as the exact same location, generate a new view. CAMERA: an extreme wide shot from the harvested paddies behind the reference camera, across the road, at standing eye level, looking toward the shelter; the shelter is small at the right third of the frame. Shot on an ARRI Alexa Mini with a 50mm lens, Kodak Vision3 250D.
REFERENCE AUTHORITY:
- <<<loc_busstop_road_v1>>>: geography, materials, landmarks, light direction
PRIORITY: the CAMERA block overrides every reference.
LANDSCAPE: harvested rice paddies with straw stubble fill the lower half; the two-lane road crosses the frame left to right a third of the way up; the bare persimmon tree stands just left of the shelter; low hills along the horizon; a few thin clouds lit orange from below.
Nothing else: no people, no cars, no animals, no legible text, nothing more recent than the early 1990s.
Low dusk sun from screen left, the persimmon-tree side, is the only key; the shelter's single fluorescent tube is off. The sun sits low near the horizon at the screen-left edge, its light raking across the stubble.
Palette of roughly 80% dry ochre and grey concrete — 15% deep blue dusk sky — 5% persimmon orange.
Exactly 0 people are visible.
```

### 2-1 영상

- job: `job-v-2-1` · 승인: 2026-10-24 · 저장: 2-1 / 승인
- 모델 · 설정: Seedance 2.5 · 480p · 8초 · 16:9 · 소리 켬(효과음만)
- 시작 이미지: job-ff-2-1
- 참조(붙인 순서): 1 ff_2-1_v1 — 시작 이미지 · 2 char_grandpa_autumn_v1 — 인물 · 3 prop_doctor_bag_v1 — 소품
- 가져온 OK: 없음
- OK 이유: "할아버지 표정 너무 좋다. 기대 안 하는 얼굴"
- 한계: 0:06에 낙엽이 조금 빨리 떨어짐
- 프롬프트(보낸 그대로):

```text
[SCENE_CONTEXT]
Late autumn, early 1990s, a rural bus stop at dusk. An old man sits alone on the bench with a bag on his lap and watches the empty road. Nothing comes.

[ACTIVE_REFERENCES]
<<<ff_2-1_v1>>> START IMAGE: the exact frame at 0:00. The camera position, lens, framing, composition, the shelter, bench, sign, tree, the light, colour and brightness, and the position and pose of the man and the bag at 0:00 are exactly this image. The video begins from this image and continues from it without any cut, jump or reframing.
<<<char_grandpa_autumn_v1>>> GRANDPA (72). A faded olive work jacket over a cream knit vest and a white collared shirt, dark grey wool trousers, scuffed brown leather shoes. Face, hair, body type and wardrobe 100% match this reference.
<<<prop_doctor_bag_v1>>> A worn brown leather doctor's bag with a brass clasp, about 40 cm wide, its soft sides scuffed and its corners worn dull. Its size stays the same as in the start image from start to finish.
REFERENCE AUTHORITY: the start image has sole authority over camera, framing, the place, the light, colour and the 0:00 position. The character reference has authority only over face, hair, body and clothes. The bag reference has authority only over its material, shape and state; its size follows the start image. Do not take the background, lighting, pose or panel layout from the character or bag references.

[LOCATION_MAP]
LEFT and RIGHT are SCREEN directions, never the character's own left or right. Places are named by the objects on screen.
LEFT EDGE: the bare persimmon tree. CENTRE: the concrete shelter with the bench along its back wall. RIGHT: the timetable sign on its pole. FOREGROUND: the empty road edge.
The persimmon tree is at screen LEFT. GRANDPA stays on the bench.

[FIRST_FRAME_AND_SPATIAL_BLOCKING]
(Scope: FIRST_FRAME only.)
- GRANDPA: seated on the tree-side half of the bench, back against the wall, both hands on the bag on his lap, eyes on the empty road on the tree side.
- BAG: across his thighs, clasp closed, his hands on top.
Exactly 1 person is visible.

[FORMAT_MODE]
Live action. A single continuous take from 0:00 to 0:08. No cuts. 8 seconds.
All movement is slow and even; nothing accelerates suddenly.

[OPTICS]
Diagonal field of view about 63°. The tree, the whole shelter and the sign are fully visible in one frame / straight lines stay straight / no telephoto compression. Deep focus.

[CAMERA]
Fixed on a tripod at standing eye level on the far side of the road, at the same position as in the start image, completely locked from 0:00 to 0:08. No pan, no tilt, no zoom, no push-in, no reframing.

[ACTION_TIMING]
0:00–0:04 — GRANDPA sits still, eyes on the road on the tree side; one slow blink.
0:04–0:08 — his thumbs move once across the top of the bag and settle; his eyes stay on the road. The shot ends with him still watching the road, hands resting on the bag.

[CHARACTER_ACTING]
GRANDPA: waits without hoping. Between stillness and quiet resignation; a sigh or a frown = failed take, a smile = failed take. His eyes stay on the empty road on the tree side with slow, heavy blinks.
He never looks at the camera.

[PHYSICS]
motion_owner = CHARACTER: the grandpa's eyes and thumbs only.
motion_owner = PROP: the bag stays on his lap, closed and heavy; never lifted, never opened.
motion_owner = CAMERA: none.
motion_owner = ENVIRONMENT: a few dry leaves on the tree tremble in the wind.

[LIGHTING]
Low dusk sun from screen left, the persimmon-tree side, is the only key; the shelter's single fluorescent tube is off.

[AUDIO]
No dialogue. GRANDPA does not say a single word; no attempt to speak, no lip movement. Distant wind over the paddies. No music.

[STYLE]
Live-action film look; natural skin tones, restrained saturation.

[QUALITY]
Facial features clear; skin, fabric and leather textures natural. No distortion of faces or fingers.

[REQUIRED_AND_FORBIDDEN_CONSTRAINTS]
Required:
- Exactly one person (ENTIRE_SHOT)
- The bag stays closed on his lap (ENTIRE_SHOT)
Forbidden:
- GRANDPA moving his lips (ENTIRE_SHOT)
- Subtitles, text, watermarks, logos. (ENTIRE_SHOT)
```

### 2-2 시작 이미지

- job: `job-ff-2-2` · 승인: 2026-10-25 · 저장: 2-2 / 승인
- 모델 · 설정: GPT Image 2.5 · 1k · 16:9
- 시작 이미지: —
- 참조(붙인 순서): 1 loc_busstop_road_v1 — 장소 · 2 char_grandpa_autumn_v1 — 인물 · 3 prop_doctor_bag_v1 — 소품
- 가져온 OK: 없음
- OK 이유: "OK"
- 한계: 없음
- 프롬프트(보낸 그대로):

```text
FIRST FRAME of a film shot — the exact state at 0:00 of the video. LEFT and RIGHT are SCREEN directions, never the character's own left or right.
Using <<<loc_busstop_road_v1>>> as the exact same location, generate a new view. CAMERA: a medium close shot from the near edge of the road at seated eye level, opposite the tree-side half of the bench, about 2 m from the old man, framing him from the top of the head to the bag on his lap. Shot on an ARRI Alexa Mini with an 85mm lens, Kodak Vision3 250D.
REFERENCE AUTHORITY:
- <<<loc_busstop_road_v1>>>: geography, materials, landmarks, light direction
- <<<char_grandpa_autumn_v1>>>: face, hair, wardrobe only — Same face, same bone structure, same hair, same wardrobe. Change only the pose, framing, location and lighting.
- <<<prop_doctor_bag_v1>>>: shape, material and state only; size as described below
DO NOT TRANSFER: the character sheet's backdrop, studio lighting, pose or framing.
PRIORITY: the CAMERA block overrides every reference.
BLOCKING: the old man sits on the persimmon-tree half of the bench, his back against the shelter wall, both hands resting on the bag on his lap, mid-stroke with the hand nearer the tree on the leather; his eyes on the empty road on the tree side, the face calm and heavy-lidded.
WARDROBE: A faded olive work jacket over a cream knit vest and a white collared shirt, dark grey wool trousers, scuffed brown leather shoes.
PROP: A worn brown leather doctor's bag with a brass clasp, about 40 cm wide, its soft sides scuffed and its corners worn dull. It lies across his thighs, clasp closed.
Nothing else: no other people, no legible text, nothing more recent than the early 1990s.
Low dusk sun from screen left, the persimmon-tree side, is the only key; the shelter's single fluorescent tube is off. The persimmon tree is at screen LEFT.
Exactly 1 person is visible.
```

### 3-1 시작 이미지

- job: `job-ff-3-1` · 승인: 2026-10-25 · 저장: 3-1 / 승인
- 모델 · 설정: GPT Image 2.5 · 1k · 16:9
- 시작 이미지: —
- 참조(붙인 순서): 1 loc_busstop_road_v1 (image_1) — 장소 뷰 · 2 char_grandpa_autumn_v1 · 3 char_girl_raincoat_v1 · 4 prop_doctor_bag_v1
- 가져온 OK: 없음
- OK 이유: "색감이랑 질감 좋다"
- 한계: 없음
- 프롬프트(보낸 그대로):

```text
Edit <<<loc_busstop_road_v1>>> WITHOUT reframing: camera position, camera height, angle, lens, framing, horizon line and perspective are LOCKED — zero reframing, zero recentering, zero zoom — this is the same photograph with one change only.
FIRST FRAME of a film shot — the exact state at 0:00 of the video. LEFT and RIGHT are SCREEN directions, never the character's own left or right.
CHANGE — ADD THE TWO PEOPLE AND THE BAG at existing anchors:
- The old man sits on the persimmon-tree half of the bench, his back against the shelter wall, both hands resting on the bag on his lap, his eyes on the empty road on the tree side.
- The girl stands at the timetable sign, an arm's length from its pole, facing the sign, mid-reading, the hand nearer the sign tracing the printed times.
- The bag lies across the man's thighs, clasp closed, about the width of his lap.
REFERENCE AUTHORITY:
- <<<loc_busstop_road_v1>>> is the exact same photograph. It controls the place, the camera, the light and every object already in it.
- <<<char_grandpa_autumn_v1>>> controls only the old man's face, hair and wardrobe. Same face, same bone structure, same hair, same wardrobe.
- <<<char_girl_raincoat_v1>>> controls only the girl's face, hair and wardrobe. Same face, same bone structure, same hair, same wardrobe.
- <<<prop_doctor_bag_v1>>> controls only the bag's shape, material and state; its size is as described above.
DO NOT TRANSFER: the character sheets' backdrop, studio lighting, pose or framing.
WARDROBE: The old man: A faded olive work jacket over a cream knit vest and a white collared shirt, dark grey wool trousers, scuffed brown leather shoes. The girl: A yellow raincoat over a navy school uniform, white knee socks and red rain boots.
PROP: A worn brown leather doctor's bag with a brass clasp, about 40 cm wide, its soft sides scuffed and its corners worn dull.
PRESERVE EXACTLY:
- Camera position, height, angle, lens, framing, horizon line, vanishing point and perspective
- The shelter, bench, timetable sign, persimmon tree, road and paddies
- Low dusk sun from screen left, the persimmon-tree side, is the only key; the shelter's single fluorescent tube is off. The persimmon tree is at screen LEFT.
- Shadows, exposure, colour grade, contrast and grain
ONLY CHANGE: the old man, the girl and the bag are added exactly as described. Everything else remains 100% identical. Exactly 2 people are visible.
```

### 3-1 영상

- job: `job-v-3-1` · 승인: 2026-10-26 · 저장: 3-1 / 승인
- 모델 · 설정: Seedance 2.5 · 480p · 8초 · 16:9 · 소리 켬
- 시작 이미지: job-ff-3-1
- 참조(붙인 순서): 1 ff_3-1_v2 — 시작 이미지 · 2 char_grandpa_autumn_v1 · 3 char_girl_raincoat_v1 · 4 prop_doctor_bag_v1
- 가져온 OK: 없음
- OK 이유: "손녀 돌아서는 속도 딱 좋다. OK"
- 한계: 없음
- 프롬프트(보낸 그대로):

```text
[SCENE_CONTEXT]
Late autumn, early 1990s, a rural bus stop at dusk. A girl reads the timetable sign and tells her grandfather, seated on the bench with a bag on his lap, that the last bus has gone. He says nothing.

[ACTIVE_REFERENCES]
<<<ff_3-1_v2>>> START IMAGE: the exact frame at 0:00. The camera position, lens, framing, composition, the shelter, bench, sign, tree, the light, colour and brightness, and the positions and poses of the two people and the bag at 0:00 are exactly this image. The video begins from this image and continues from it without any cut, jump or reframing.
<<<char_grandpa_autumn_v1>>> GRANDPA (72). A faded olive work jacket over a cream knit vest and a white collared shirt, dark grey wool trousers, scuffed brown leather shoes. Face, hair, body type and wardrobe 100% match this reference.
<<<char_girl_raincoat_v1>>> GIRL (10). A yellow raincoat over a navy school uniform, white knee socks and red rain boots. Face, hair, body type and wardrobe 100% match this reference.
<<<prop_doctor_bag_v1>>> A worn brown leather doctor's bag with a brass clasp, about 40 cm wide, its soft sides scuffed and its corners worn dull. Its size stays the same as in the start image from start to finish.
REFERENCE AUTHORITY: the start image has sole authority over camera, framing, the place, the light, colour and the 0:00 positions. The character references have authority only over faces, hair, bodies and clothes. The bag reference has authority only over its material, shape and state; its size follows the start image. Do not take the background, lighting, pose or panel layout from the character or bag references.

[LOCATION_MAP]
LEFT and RIGHT are SCREEN directions, never the character's own left or right. Places are named by the objects on screen.
LEFT EDGE: the bare persimmon tree. CENTRE: the concrete shelter with the bench along its back wall. RIGHT: the timetable sign on its pole. FOREGROUND: the empty road edge.
The persimmon tree is at screen LEFT. GRANDPA stays on the bench. GIRL stays between the sign and the bench and never steps into the road.

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
Diagonal field of view about 63°. The tree, the whole shelter and the sign are fully visible in one frame / straight lines stay straight / no telephoto compression. Deep focus.

[CAMERA]
Fixed on a tripod at standing eye level on the far side of the road, at the same position as in the start image, completely locked from 0:00 to 0:08. No pan, no tilt, no zoom, no push-in, no reframing.

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
Low dusk sun from screen left, the persimmon-tree side, is the only key; the shelter's single fluorescent tube is off.

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

### 3-2 시작 이미지

- job: `job-ff-3-2` · 승인: 2026-10-27 · 저장: 3-2 / 승인
- 모델 · 설정: GPT Image 2.5 · 1k · 16:9
- 시작 이미지: —
- 참조(붙인 순서): 1 loc_busstop_road_v1 · 2 char_grandpa_autumn_v1 · 3 char_girl_raincoat_v1 · 4 prop_doctor_bag_v1
- 가져온 OK: 없음
- OK 이유: "좋아"
- 한계: 없음
- 프롬프트(보낸 그대로):

```text
FIRST FRAME of a film shot — the exact state at 0:00 of the video. LEFT and RIGHT are SCREEN directions, never the character's own left or right.
Using <<<loc_busstop_road_v1>>> as the exact same location, generate a new view. CAMERA: a medium two-shot from the far side of the road at seated eye level, opposite the middle of the bench; the bench and the timetable sign fill the frame side by side, the paddies behind compressed and soft. Shot on an ARRI Alexa Mini with a 75mm lens, Kodak Vision3 250D.
REFERENCE AUTHORITY:
- <<<loc_busstop_road_v1>>>: geography, materials, landmarks, light direction
- <<<char_grandpa_autumn_v1>>>: face, hair, wardrobe only — Same face, same bone structure, same hair, same wardrobe. Change only the pose, framing, location and lighting.
- <<<char_girl_raincoat_v1>>>: face, hair, wardrobe only — Same face, same bone structure, same hair, same wardrobe. Change only the pose, framing, location and lighting.
- <<<prop_doctor_bag_v1>>>: shape, material and state only; size as described below
DO NOT TRANSFER: the character sheets' backdrop, studio lighting, pose or framing.
PRIORITY: the CAMERA block overrides every reference.
BLOCKING:
- The old man sits on the persimmon-tree half of the bench, his back against the shelter wall, both hands resting on the bag on his lap, his eyes on the empty road on the tree side.
- The girl stands at the timetable sign, an arm's length from its pole, facing the sign, mid-reading, the hand nearer the sign tracing the printed times.
WARDROBE: The old man: A faded olive work jacket over a cream knit vest and a white collared shirt, dark grey wool trousers, scuffed brown leather shoes. The girl: A yellow raincoat over a navy school uniform, white knee socks and red rain boots.
PROP: A worn brown leather doctor's bag with a brass clasp, about 40 cm wide, its soft sides scuffed and its corners worn dull. It lies across the man's thighs, clasp closed.
Nothing else: no other people, no legible text, nothing more recent than the early 1990s.
Low dusk sun from screen left, the persimmon-tree side, is the only key; the shelter's single fluorescent tube is off. The persimmon tree is at screen LEFT.
Exactly 2 people are visible.
```

### 3-3 시작 이미지

- job: `job-ff-3-3` · 승인: 2026-10-27 · 저장: 3-3 / 승인
- 모델 · 설정: GPT Image 2.5 · 1k · 16:9
- 시작 이미지: —
- 참조(붙인 순서): 1 loc_busstop_road_v1 · 2 char_girl_raincoat_v1
- 가져온 OK: 없음
- OK 이유: "OK"
- 한계: 없음
- 프롬프트(보낸 그대로):

```text
FIRST FRAME of a film shot — the exact state at 0:00 of the video. LEFT and RIGHT are SCREEN directions, never the character's own left or right.
Using <<<loc_busstop_road_v1>>> as the exact same location, generate a new view. CAMERA: a medium shot from the near edge of the road at standing eye level, opposite the timetable sign; the girl and the sign fill the right half of the frame, the end of the shelter at the left edge; the bench is out of frame. Shot on an ARRI Alexa Mini with a 50mm lens, Kodak Vision3 250D.
REFERENCE AUTHORITY:
- <<<loc_busstop_road_v1>>>: geography, materials, landmarks, light direction
- <<<char_girl_raincoat_v1>>>: face, hair, wardrobe only — Same face, same bone structure, same hair, same wardrobe. Change only the pose, framing, location and lighting.
DO NOT TRANSFER: the character sheet's backdrop, studio lighting, pose or framing.
PRIORITY: the CAMERA block overrides every reference.
BLOCKING: the girl stands at the timetable sign, an arm's length from its pole, facing the sign in three-quarter back view, mid-reading, the hand nearer the sign raised to the printed times.
WARDROBE: A yellow raincoat over a navy school uniform, white knee socks and red rain boots.
Nothing else: no other people, no legible text, nothing more recent than the early 1990s.
Low dusk sun from screen left, the persimmon-tree side, is the only key; the shelter's single fluorescent tube is off. The persimmon tree is at screen LEFT.
Exactly 1 person is visible.
```
