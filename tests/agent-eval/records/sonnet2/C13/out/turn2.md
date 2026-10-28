5개 모두 제안값으로 정했습니다. 컷 카드 `3-5`를 v1로 고쳤고, 제안으로 받은 값에는 `(제안값)`을 붙였습니다. 검사 스크립트는 통과했습니다(2,598자, 걸린 항목 없음).

**실패 위험 → 막는 문장**
1. 구도가 장소 뷰 전경으로 돌아가 인물이 넓게 나옴 → `His face is out of frame.` + 근접 CAMERA + `PRIORITY: the CAMERA block overrides every reference.`
2. 3-1 색 참조에서 손녀·구도가 따라옴 → `<<<image_4>>> controls only colour, grade, contrast and texture. Never take its subjects, composition, people or light direction.` + DO NOT TRANSFER
3. 가방 참조(`prop_doctor_bag_v1`)가 닫힌 모양이라 닫혀서 나옴 → `Except: the bag is OPEN here…` + `Ignore the closed state in <<<image_3>>>.`
4. 손이 가방 안으로 들어가거나 내용물이 생김 → `not reaching inside` + `nothing inside is identifiable`
5. 빛 방향이 뒤집힘 → LIGHT LOCK + `In this view the west, the persimmon-tree side, is screen LEFT.` (북향이라 3-1 장소 뷰 문장을 그대로 씀)
6. 손가락 수·손 모양 오류(클로즈업이라 눈에 띔) → `A natural hand with five fingers and correct anatomy.`

```text
FIRST FRAME of a film shot — the exact state at 0:00 of the video. LEFT and RIGHT are SCREEN directions.
Using <<<image_1>>> as the exact same location, generate a new view. CAMERA: a tripod-fixed close-up from inside the shelter, in front of the bench, about 50 cm in front of the old man's knees, looking north toward the shelter's back wall (the same direction as <<<image_1>>>). The lens sits slightly above the bag's open mouth and tilts down about 30° onto the opening and his hand. 85mm lens, shallow depth of field, focus on the hand and the bag's rim. The hand and the bag's open mouth fill most of the frame. His face is out of frame.
REFERENCE AUTHORITY:
- <<<image_1>>>: geography, materials, landmarks, light direction
- <<<image_2>>> controls only the old man's hand, sleeve and wardrobe. Same wardrobe. Change only the pose, framing, location and lighting.
- <<<image_3>>>: shape and material only; its state is open as described below and its size is as described below
- <<<image_4>>> controls only colour, grade, contrast and texture. Never take its subjects, composition, people or light direction.
DO NOT TRANSFER: the character sheet's backdrop, studio lighting, pose or framing. From <<<image_4>>>: the girl, the bench, the timetable sign, its framing.
PRIORITY: the CAMERA block overrides every reference.
BLOCKING: The old man sits on the persimmon-tree half of the bench, his back against the shelter wall. The bag lies across his thighs. The hand nearer the persimmon tree rests with its fingertips lightly on the rim of the bag's open mouth, fingers loosely curled, mid-pause, not reaching inside. His other hand, out of frame, holds a handle of the bag. A natural hand with five fingers and correct anatomy.
WARDROBE: A faded olive work jacket over a cream knit vest and a white collared shirt, dark grey wool trousers, scuffed brown leather shoes. Only the jacket sleeve, the white shirt cuff and a part of the vest are in frame.
PROP: A worn brown leather doctor's bag with a brass clasp, about 40 cm wide, hanging heavy from its handles. Except: the bag is OPEN here, its brass clasp undone and its mouth open, about as wide as his lap; the inside is dark and nothing inside is identifiable. Ignore the closed state in <<<image_3>>>.
Nothing else except the old man's hand and the bag: no other buildings, no cars, no legible text.
Low dusk sun from the west, the persimmon-tree side, is the only key; the shelter's single fluorescent tube is off. In this view the west, the persimmon-tree side, is screen LEFT.
Exactly 1 person is visible, only the hand and sleeve.
```

- 모드: 신규 · 틀 2 DERIVED VIEW (장소 뷰와 다른 클로즈업)
- 참조(붙이는 순서): image_1 `loc_busstop_road_v1` (장소·재료·빛 방향) · image_2 `char_grandpa_autumn_v1` (손·소매·의상만) · image_3 `prop_doctor_bag_v1` (모양·재질만) · image_4 3-1 시작 이미지 `job-ff-3-1` (색감·질감만) — 참조 4 = 태그 4
- 모델: GPT Image 2.5 · 해상도: 1k(확인용) · 화면비 16:9 · 1장 · 길이: 해당 없음(이미지)
- 저장 폴더: `fld-3-5` (「빈 정류장」/3-5)

보내지는 않았습니다. 확인 사항 한 묶음:
- 이 프롬프트로 1k 한 장을 만들까요? (보내면 폴더를 `3-5 [진행]`으로 바꿉니다. 처음 쓰는 설정이 아니라 견적 조회는 생략하고 약 4 크레딧으로 예상합니다.)
- 이 컷은 장소 뷰(`LC-001-V1`)와 같은 북향의 새 시점이라 V1 화면 대응 문장을 그대로 썼습니다. 정식 새 뷰로 에셋 대장에 올리는 것은 총괄 일이라 핸드오프 [5]에 적어 두겠습니다.

=== 메타 ===
연 파일(순서대로): project/cuts/3-5.md(자기 컷 카드, 고치기 전 내용 확인), .claude/skills/higgsfield-generation/check_prompt.py(실행), tmp/3-5_ff.txt, tmp/3-5_fixed.txt(내가 쓴 임시 파일)
부른 [TOOL]: 없음
고친 정본 파일: project/cuts/3-5.md (v0 → v1; [4][5][6][10] 채움, 제안값 표시)
