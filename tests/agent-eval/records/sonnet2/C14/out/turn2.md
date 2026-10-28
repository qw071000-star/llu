5개 모두 제안값으로 정했습니다. 컷 카드 `cuts/2-2.md`를 v1로 고쳤고 값에는 (제안값) 표시를 남겼습니다. 생성은 하지 않았습니다. 검사 스크립트는 통과했습니다 (4596자, 걸린 항목 없음).

**2-2 영상 프롬프트**

```text
[SCENE_CONTEXT]
Late autumn, early 1990s, a rural bus stop at dusk. An old man sits alone on the bench with a bag on his lap, seen in a medium close shot. His hand strokes the leather of the bag once more and comes to rest. He watches the empty road. Nothing comes.

[ACTIVE_REFERENCES]
<<<ff_2-2_v1>>> START IMAGE: the exact frame at 0:00. The camera position, lens, framing, composition, the shelter wall and bench, the light, colour and brightness, and the position and pose of the man and the bag at 0:00 are exactly this image. The video begins from this image and continues from it without any cut, jump or reframing.
<<<char_grandpa_autumn_v1>>> GRANDPA (72). A faded olive work jacket over a cream knit vest and a white collared shirt, dark grey wool trousers, scuffed brown leather shoes. Face, hair, body type and wardrobe 100% match this reference.
<<<prop_doctor_bag_v1>>> A worn brown leather doctor's bag with a brass clasp, about 40 cm wide, hanging heavy from its handles. Its size stays the same as in the start image from start to finish.
REFERENCE AUTHORITY: the start image has sole authority over camera, framing, the place, the light, colour and the 0:00 position. The character reference has authority only over face, hair, body and clothes. The bag reference has authority only over its material, shape and state; its size follows the start image. Do not take the background, lighting, pose or panel layout from the character or bag references.

[LOCATION_MAP]
LEFT and RIGHT are SCREEN directions. Places are named by the objects on screen.
CENTRE: GRANDPA on the tree-side half of the bench, his back against the shelter's back wall. FOREGROUND: the empty road edge, where the camera stands about 2 m from him.
In this view the west, the persimmon-tree side, is screen LEFT. GRANDPA stays on the bench.

[FIRST_FRAME_AND_SPATIAL_BLOCKING]
(Scope: FIRST_FRAME only.)
- GRANDPA: seated on the tree-side half of the bench, back against the shelter wall, both hands on the bag on his lap, mid-stroke with the hand nearer the tree moving over the leather; his eyes on the empty road on the tree side, the face calm and heavy-lidded.
- BAG: across his thighs, clasp closed.
Exactly 1 person is visible.

[FORMAT_MODE]
Live action. A single continuous take from 0:00 to 0:08. No cuts. 8 seconds.
All movement is slow and even; nothing accelerates suddenly.

[OPTICS]
Diagonal field of view about 29°. The background wall is compressed and soft / only his face and the bag's brass clasp are sharp / the camera is physically far away. Shallow depth of field.

[CAMERA]
Fixed on a tripod at seated eye level at the near edge of the road, about 2 m from GRANDPA, opposite the tree-side half of the bench, at the same position as in the start image, completely locked from 0:00 to 0:08. No pan, no tilt, no zoom, no push-in, no reframing.

[ACTION_TIMING]
0:00–0:03 — GRANDPA's hand nearer the tree, already moving over the leather, strokes slowly once more and stops; his eyes stay on the road.
0:03–0:08 — both of his hands rest on the bag, still; one slow blink; his eyes stay on the road. The shot ends with him still watching the road, both hands resting on the closed bag.

[CHARACTER_ACTING]
GRANDPA: waits without hoping. Between stillness and quiet resignation; a sigh or a frown = failed take, a smile = failed take. His eyes stay on the empty road on the tree side with slow, heavy blinks. His eyes never drop to the bag.
He never looks at the camera.

[PHYSICS]
motion_owner = CHARACTER: the grandpa's hand nearer the tree on the leather (one stroke only) and his eyes.
motion_owner = PROP: the bag stays on his lap, closed and heavy; never lifted, never opened.
motion_owner = CAMERA: none.
motion_owner = ENVIRONMENT: none.

[LIGHTING]
Low dusk sun from the west, the persimmon-tree side, is the only key; the shelter's single fluorescent tube is off.

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
- His eyes stay on the empty road on the tree side (ENTIRE_SHOT)
- The stroke happens once, then both hands rest on the bag (INTERVAL 0:00–0:03, FINAL_FRAME)
Forbidden:
- GRANDPA moving his lips (ENTIRE_SHOT)
- Subtitles, text, watermarks, logos. (ENTIRE_SHOT)
```

- 모드: 영상, 실사 15블록 (image-to-video)
- 참조(붙일 순서): 1 `ff_2-2_v1` 시작 이미지 `job-ff-2-2` · 2 `char_grandpa_autumn_v1` 인물 · 3 `prop_doctor_bag_v1` 소품
- 모델: Seedance 2.5 · 480p · 8초 · 16:9 · 소리: 효과음만
- 저장 폴더: 「빈 정류장」 / 2-2 (`fld-2-2`)

**2-1에서 가져온 줄:** `CHARACTER_ACTING`의 할아버지 줄과 "He never looks at the camera", `AUDIO`의 입술 문장, Forbidden의 입술 줄, `LIGHTING`, `STYLE`, `QUALITY`를 글자 그대로 옮겼습니다.

**전 → 후 (2-1 → 2-2에서 바뀐 줄):**
- `CHARACTER_ACTING`: 줄은 그대로, 한 문장을 더함 → `His eyes never drop to the bag.` (제안 2)
- `PHYSICS` ENVIRONMENT: `a few dry leaves on the tree tremble in the wind` → `none` (제안 5)
- `PHYSICS` CHARACTER: `eyes and thumbs only` → `hand nearer the tree on the leather (one stroke only) and his eyes`
- `ACTION_TIMING`: 엄지 한 번 → 0:00–0:03 쓰다듬기 한 번 더 후 멈춤, 0:03–0:08 두 손 정지
- `OPTICS`: 63° 광각 → 29° 망원 (관찰 결과 3개, 제안 4)
- `CAMERA`, `LOCATION_MAP`, `FIRST_FRAME`: 2-2 시작 이미지의 위치·구도로 바꿈

**확인할 점**
- 시작 이미지의 요소 이름을 대장에서 확인하지 못해, 2-1의 이름 패턴을 따라 `ff_2-2_v1`로 썼습니다. 붙일 때 실제 이름과 다르면 알려 주세요. 이름과 프롬프트 속 태그를 함께 고쳐야 합니다.
- 할아버지 얼굴이 2-1과 같은지는 추정입니다 (시작 이미지는 승인 프롬프트로 짐작).

생성하려면 "생성해"라고 지시해 주세요. 480p 8초 한 번이며 약 40 크레딧입니다 (시뮬레이션 견적 기준).

[TOOL] 없음 (이번 턴은 생성하지 않음)

=== 메타 ===
연 파일(순서대로): out/ 목록, project/cuts/2-2.md, tmp/2-2_video.txt(직접 작성), .claude/skills/higgsfield-generation/check_prompt.py(실행만)
부른 [TOOL]: 없음
고친 정본 파일: project/cuts/2-2.md (v1)
