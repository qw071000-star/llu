제안값 그대로 확정해서 3-5 첫 프레임 프롬프트를 썼습니다. 생성은 지시하신 게 아니라서 보내지 않았습니다. 검사 스크립트는 통과했습니다(걸린 항목 없음).

**실패 위험 → 막는 문장**
1. 참조 가방이 닫힌 상태라 닫힌 채 나옴 → `It is OPEN: the brass clasp undone, the lid folded back`, 참조 권한도 "모양·재질만, 상태는 열림"
2. 얼굴이 들어오거나 카메라를 봄 → `no face in frame` / `no face`
3. 가방 안에 물건이 생김 → `only dark worn cloth lining visible inside, no contents visible`
4. 손이 뭔가 꺼내는 동작을 함 → `Nothing is being pulled out and nothing moves`
5. 색 참조에서 구도·사람·빛 방향이 따라옴 → `controls only colour, grade, contrast and texture. Never take its subjects, composition, people or light direction.`
6. 손·손가락 이상 → `only his two hands, wrists and lap`
7. 3-1 이미지에는 색·질감 문장이 없어 색이 어긋날 수 있음 → 색 참조를 붙여 막았습니다. 생성 후 색감이 3-1과 같은지 봐 주세요.

```text
FIRST FRAME of a film shot — the exact state at 0:00 of the video. LEFT and RIGHT are SCREEN directions.
Using <<<image_1>>> as the exact same location, generate a new view. CAMERA: a close-up from the far side of the road, opposite the middle of the bench, at seated eye level, looking north; the old man's hands and the open mouth of the bag on his lap fill the frame, his knees at the bottom edge, no face in frame; shallow depth of field, focus on the hands and the bag's opening, the shelter wall and paddies behind soft. Shot on an ARRI Alexa Mini with an 85mm lens, Kodak Vision3 250D.
REFERENCE AUTHORITY:
- <<<image_1>>>: geography, materials, landmarks, light direction
- <<<image_2>>>: the bag's shape and material only; its state is OPEN as described below, not closed
- <<<image_3>>> controls only colour, grade, contrast and texture. Never take its subjects, composition, people or light direction.
DO NOT TRANSFER: from <<<image_2>>>, its closed clasp, its background and its camera angle; from <<<image_3>>>, its people, its framing and its light direction.
PRIORITY: the CAMERA block overrides every reference.
BLOCKING: The old man sits on the persimmon-tree half of the bench, his back against the shelter wall. The doctor's bag lies open across his thighs. The hand nearer the clasp rests still on the edge of the bag's mouth, fingers curled over the rim, paused. The other hand rests on the bag's handles. Weathered tan skin, knotted knuckles, dry creased skin; the cuffs of the faded olive work jacket show at the wrists. Nothing is being pulled out and nothing moves.
WARDROBE: A faded olive work jacket over a cream knit vest and a white collared shirt, dark grey wool trousers, scuffed brown leather shoes.
PROP: A worn brown leather doctor's bag with a brass clasp, about 40 cm wide, hanging heavy from its handles. It is OPEN: the brass clasp undone, the lid folded back, the mouth about 40 cm wide, only dark worn cloth lining visible inside, no contents visible.
Nothing else: no other people, no face, no legible text, nothing more recent than the early 1990s.
Low dusk sun from the west, the persimmon-tree side, is the only key; the shelter's single fluorescent tube is off. In this view the west is screen LEFT.
Exactly 1 person is partly visible: only his two hands, wrists and lap.
```

- 모드: 신규, 새 시점(카메라가 장소 뷰와 달라 틀 2)
- 참조(붙이는 순서): image_1 `loc_busstop_road_v1` 장소 · image_2 `prop_doctor_bag_v1` 모양·재질만 · image_3 3-1 시작 이미지(`job-ff-3-1`) 색·질감만. 인물 시트는 얼굴이 프레임 밖이라 붙이지 않습니다.
- 모델: GPT Image 2.5
- 해상도: 1k · 16:9 (확인용)
- 저장 폴더: 「빈 정류장」/3-5 (`fld-3-5`)
- 견적: 약 4 크레딧(추정, 이미지 1k 1장)

**바꾼 것**: 3-1 프롬프트의 색·질감 문장은 따로 없어 글자를 옮기지 않았습니다. 고정 설명문(의상, 가방, LIGHT LOCK)은 에셋 대장 문장 그대로입니다. 장소 뷰의 "Nothing else" 목록은 이 프레임에 맞게 줄였습니다.

**총괄에 올릴 것**: 3-4 카드가 없어 3-4 끝 구도(손 위치)와 이 프레임이 맞는지 확인이 필요합니다.

이 프롬프트로 생성할까요? "생성해"라고 하시면 보냅니다.

=== 메타 ===
연 파일(순서대로):
- project/cuts/3-5.md (turn1에서 만든 초안)
- .claude/skills/higgsfield-generation/check_prompt.py (사용법과 image 검사 부분)
부른 [TOOL]:
- 없음 (생성하지 않음. 검사 스크립트만 실행: tmp/ff35.txt, tmp/fixed35.txt)
고친 정본 파일:
- project/cuts/3-5.md ([4][5][6][7][10][12]를 제안값으로 채움. 제안값 표시 유지)
