질문 4개 모두 제안값으로 정했고, 컷 카드에 `제안값`으로 적어 두었습니다(`project/cuts/3-5.md` [4][5][7]).

**실패 위험과 막는 문장**
1. 가방이 닫힌 채 나옵니다(소품 참조가 닫힌 가방이라서). → `The bag is OPEN: the brass clasp is undone...` 문장을 넣고, 소품 참조 권한을 모양·재질로 좁히고, `DO NOT TRANSFER`에 닫힌 잠금장치를 적었습니다.
2. 3-1의 와이드 구도, 손녀, 정류장 전경이 따라 들어옵니다. → `<<<image_4>>> controls only colour, grade, contrast and texture. Never take its subjects, composition, people or light direction.` 문장과 `Exactly 1 person is visible` 문장을 넣었습니다.
3. 장소 참조 때문에 와이드 시점으로 돌아갑니다. → `Do not inherit its camera angle, framing or composition.` 문장과 `PRIORITY: the CAMERA block overrides every reference.` 문장을 넣었습니다.
4. 얼굴이 프레임에 들어옵니다. → `His face is above the top edge of the frame, out of shot.`
5. 손가락 수나 모양이 이상하게 나옵니다. → `Two hands, each with four fingers and one thumb.`
6. 질감이 3D 렌더처럼 나옵니다(GPT Image 2.5에 요소를 많이 지정하면 생기는 문제). → 질감 줄을 맨 앞에 두었고(`A real photograph, not a 3D render...`), 요소는 인물 1명과 소품 1개로 줄였습니다.
7. 가방 안에 없던 물건이 생깁니다. → `Inside shows only the dark lining; no objects are visible inside the bag.`
8. 빛 방향이 반대로 나옵니다. → LIGHT LOCK을 글자 그대로 넣고 `In this view the west is screen LEFT.`를 더했습니다.
9. 글자나 현대 물건이 나옵니다. → `Nothing else: no legible text, no modern objects.`

- 모드: 퍼스트 프레임, 새 시점(DERIVED VIEW)
- 참조(붙이는 순서):
  1. `loc_busstop_road_v1`(`job-lc001v1`): 같은 장소. 지리·재질·빛 방향만 가져옵니다.
  2. `char_grandpa_autumn_v1`(`job-ch001`): 손 피부와 의상만 가져옵니다.
  3. `prop_doctor_bag_v1`: 모양과 재질만 가져옵니다. 상태는 프롬프트 문장으로 '열림'을 지정합니다.
  4. `job-ff-3-1`: 색·그레이드·대비·질감만 가져옵니다.
- 모델: GPT Image 2.5
- 해상도: 1k(확인용), 16:9, 1장
- 길이: 없음(이미지)
- 저장 폴더: `fld-3-5`

```text
FIRST FRAME of a film shot — the exact state at 0:00 of the video. LEFT and RIGHT are SCREEN directions.
A real photograph, not a 3D render and not an illustration. Colour, grade, contrast and texture come only from <<<image_4>>>.
Using <<<image_1>>> as the exact same location, generate a new view. Do not inherit its camera angle, framing or composition.
CAMERA: A fixed tripod on the road side of the bench, directly in front of the seated old man, looking north at him. Camera at his seated eye height, tilted down at the bag on his lap, about 60 cm from his hands. Close-up: the open mouth of the bag and his two hands fill about two-thirds of the frame width. His face is above the top edge of the frame, out of shot. 85mm lens, shallow depth of field, focus on the backs of his hands; the bench and the shelter's back wall behind his lap are soft and out of focus.
REFERENCE AUTHORITY:
- <<<image_1>>>: geography, materials, landmarks and light direction only.
- <<<image_2>>>: the old man's skin and wardrobe only — same skin, same wardrobe. Change only the pose, framing, location and lighting.
- <<<image_3>>>: the bag's shape and material only; its state is open and its size is as described below.
- <<<image_4>>> controls only colour, grade, contrast and texture. Never take its subjects, composition, people or light direction.
DO NOT TRANSFER: the character sheet's backdrop, studio lighting, pose or framing; the bag reference's closed clasp, background or camera angle.
PRIORITY: the CAMERA block overrides every reference.
BLOCKING: The old man sits on the wooden bench, the bag lying across his thighs. Mid-pause just after opening it, both hands hold the two sides of the bag's open mouth, one hand on each side, fingers curled over the leather edge, thumbs on the outside. Two hands, each with four fingers and one thumb. Only his hands, jacket cuffs and lap are in frame.
WARDROBE: The old man: A faded olive work jacket over a cream knit vest and a white collared shirt, dark grey wool trousers, scuffed brown leather shoes.
PROP: A worn brown leather doctor's bag with a brass clasp, about 40 cm wide, hanging heavy from its handles. It lies across the old man's thighs, about the width of his lap. The bag is OPEN: the brass clasp is undone and the mouth is spread wide between his hands. Inside shows only the dark lining; no objects are visible inside the bag.
Nothing else: no legible text, no modern objects.
Low dusk sun from the west, the persimmon-tree side, is the only key; the shelter's single fluorescent tube is off. In this view the west is screen LEFT.
Exactly 1 person is visible: the old man, seen only from his hands, cuffs and lap.
```

- 붙이는 참조 4개와 프롬프트 속 태그 4개(`image_1`~`image_4`)를 붙이는 순서대로 맞췄습니다.
- 의상, 가방, LIGHT LOCK 문장은 에셋 대장과 글자까지 같습니다.
- 3-4 끝 프레임의 손 위치를 이 첫 프레임에 맞추는 일은 세션을 끝낼 때 핸드오프에 "총괄에 올릴 것"으로 적겠습니다.

생성은 아직 하지 않았습니다. 이대로 1k 1장을 보낼까요, 아니면 고칠 줄이 있나요?

=== 메타 ===
- 연 파일(순서대로, 이번 턴):
  1. out/ 폴더 목록(turn1.md만 있음, 다시 읽지 않음)
  2. project/cuts/3-5.md (고칠 줄 찾기)
  - 지침·스킬·정본은 turn1에서 읽은 것을 그대로 씀: image-prompt/SKILL.md, image-prompt/first-frame.md, production-session/ok-reuse.md, ok-cuts.md의 `### 3-1 시작 이미지` 절, asset-registry.md
- 부른 [TOOL]: 없음(프롬프트만 요청받아 생성하지 않음)
- 고친 정본 파일:
  - project/cuts/3-5.md: 2줄(카드 버전에 "그대로 → 제안값" 기록), 7·8줄([4] 카메라·렌즈), 10·13·14·15줄([5] 손·시선·가방 안쪽·인원), 18줄([7] 참조 순서 = 태그 image_1~4), 20줄(CH-001 참조 권한을 "손 피부·의상만"으로 맞춤)
