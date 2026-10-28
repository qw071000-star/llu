카메라를 LC-001-V1과 같게 하면 장소 뷰가 확정된 뷰와 같으니 새 시점이 아니라 그 뷰를 잠그고 할아버지와 가방만 더하는 방식(LOCKED EDIT)으로 바뀝니다. 나머지 4개는 제안대로 반영했고, 카드(`project/cuts/3-4.md`)에 적었습니다.

3-1 시작 이미지(같은 카메라)의 줄을 가져와 바꾼 곳만 보입니다.

- 인물: `ADD THE TWO PEOPLE AND THE BAG` → `ADD THE OLD MAN AND THE BAG`. 손녀 줄, 손녀 참조, 손녀 의상 줄은 뺐습니다.
- 시선: `his eyes on the empty road on the tree side` → `his eyes lowered to the bag`
- 걸쇠: (없음) → `the brass clasp faces the road and stays uncovered between his hands`
- 인원: `Exactly 2 people` → `Exactly 1 person`
- 의상: `The old man: ...` → 접두어 없이 할아버지 문장만 (한 명이라서)

실패 위험과 막는 문장:

1. 시선이 카메라를 봄 (3-2 폐기 job의 실패) → `his eyes lowered to the bag`
2. 걸쇠가 손에 가려지거나 열린 채 나옴 → `clasp closed` + `stays uncovered between his hands`
3. 가방이 손잡이에 매달리거나 커짐 (고정 문장에 "hanging heavy from its handles"가 있음) → `lies across the man's thighs ... about the width of his lap`
4. 카메라가 틀어지거나 가운데로 쏠림 → `WITHOUT reframing ... LOCKED`와 `PRESERVE EXACTLY`
5. 손녀 등 다른 사람이 생김 → `Exactly 1 person is visible`
6. 빛 방향이 뒤집힘 → LIGHT LOCK과 `the west is screen LEFT`를 PRESERVE에 그대로 넣음
7. 35mm 와이드라 인물, 걸쇠, 시선이 작게 나옵니다. 카메라를 고정했기 때문에 막는 문장이 없습니다. 걸쇠 디테일은 3-5 클로즈업이 맡습니다. 시선 방향이 화면에서 읽히는지는 결과를 봐야 알 수 있습니다(추정).

```text
Edit <<<loc_busstop_road_v1>>> WITHOUT reframing: camera position, camera height, angle, lens, framing, horizon line and perspective are LOCKED — zero reframing, zero recentering, zero zoom — this is the same photograph with one change only.
FIRST FRAME of a film shot — the exact state at 0:00 of the video. LEFT and RIGHT are SCREEN directions.
CHANGE — ADD THE OLD MAN AND THE BAG at existing anchors:
- The old man sits on the persimmon-tree half of the bench, his back against the shelter wall, both hands resting on the bag on his lap, his eyes lowered to the bag.
- The bag lies across the man's thighs, clasp closed, about the width of his lap; the brass clasp faces the road and stays uncovered between his hands.
REFERENCE AUTHORITY:
- <<<loc_busstop_road_v1>>> is the exact same photograph. It controls the place, the camera, the light and every object already in it.
- <<<char_grandpa_autumn_v1>>> controls only the old man's face, hair and wardrobe. Same face, same bone structure, same hair, same wardrobe.
- <<<prop_doctor_bag_v1>>> controls only the bag's shape, material and state; its size is as described above.
DO NOT TRANSFER: the character sheet's backdrop, studio lighting, pose or framing.
WARDROBE: A faded olive work jacket over a cream knit vest and a white collared shirt, dark grey wool trousers, scuffed brown leather shoes.
PROP: A worn brown leather doctor's bag with a brass clasp, about 40 cm wide, hanging heavy from its handles.
PRESERVE EXACTLY:
- Camera position, height, angle, lens, framing, horizon line, vanishing point and perspective
- The shelter, bench, timetable sign, persimmon tree, road and paddies
- Low dusk sun from the west, the persimmon-tree side, is the only key; the shelter's single fluorescent tube is off. In this view the west is screen LEFT.
- Shadows, exposure, colour grade, contrast and grain
ONLY CHANGE: the old man and the bag are added exactly as described. Everything else remains 100% identical. Exactly 1 person is visible.
```

- 모드: 퍼스트 프레임 틀 1, LOCKED EDIT (신규 생성)
- 참조(붙이는 순서): 1 `loc_busstop_road_v1` (같은 사진, `job-lc001v1`) · 2 `char_grandpa_autumn_v1` (얼굴·머리·옷만) · 3 `prop_doctor_bag_v1` (모양·재질·상태만)
- 모델: GPT Image 2.5, 1장
- 해상도·비율: 1k (확인용), 16:9
- 길이: 해당 없음 (영상 0:00 상태의 정지 이미지)
- 저장 폴더: `fld-3-4` (3-4 [대기])
- 자동 검사: 통과 (1997자, 참조 3개와 태그 3개 일치, 고정 문장 4줄 글자 일치, 걸린 항목 없음)

아직 생성하지 않았습니다. 이 프롬프트로 만들까요? 만들라고 하시면 폴더를 `3-4 [진행]`으로 바꾸고 1장만 보냅니다.

=== 메타 ===
연 파일(순서대로): .claude/skills/higgsfield-generation/SKILL.md, project/ok-cuts.md (LC-001-V1 절, 3-1 시작 이미지 절), .claude/skills/production-session/ok-reuse.md, .claude/skills/higgsfield-generation/check_prompt.py (사용법만 읽고 실행), project/cuts/3-4.md (수정 전후)
부른 [TOOL]: 없음
고친 정본 파일: project/cuts/3-4.md (v0 → v1: [4] 카메라 LC-001-V1과 같게, [5] 제안 확정, [7] 가져온 OK 3-1 시작 이미지, [10] 위험 → 막는 문장, [11] 줄임. (제안값)은 소리 칸에만 남김). 임시 파일: tmp/ff-3-4.txt, tmp/fixed-3-4.txt
