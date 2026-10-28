카메라를 LC-001-V1과 똑같이 하므로 모드는 LOCKED EDIT(틀 1)입니다. 그래서 제가 앞에서 제안한 1~3번(새 시점, 미디엄 샷, 50mm)은 쓰지 않습니다. 4~6번은 제안대로 넣었습니다. 할아버지 자리와 가방 줄은 3-1 시작 이미지 OK 카드에서 글자 그대로 가져왔습니다.

**생성 전 실패 위험 → 막는 문장**
1. 카메라를 봄(3-2 옛 시도 폐기 이유) → `he does not look at the camera.`
2. 가방이 이미 열려 있음(0:00은 닫힘) → `clasp closed` · `It is shut`
3. 가방이 각지거나 작아짐 → PR-001 고정 설명문 + `about the width of his lap` + `not boxy`
4. 손녀나 다른 사람이 생김 → `Exactly 1 person is visible; no one stands at the timetable sign.`
5. 손을 보여 주려고 다가가 찍음(재구도) → LOCKED 여는 문장(zero reframing, zero zoom)
6. 시간표 글씨가 읽힘 / 형광등이 켜짐 → `no legible text anywhere.` · LIGHT LOCK 원문
7. 길 건너 전경이라 손과 걸쇠가 작게 나와 "열기 직전"이 잘 안 읽힘 → 프롬프트로는 막지 못합니다. 이 구도의 한계입니다(추정).

**3-1에서 가져와 바꾼 곳 (전 → 후)**
- `ADD THE TWO PEOPLE AND THE BAG` → `ADD THE OLD MAN AND THE BAG`
- `both hands resting on the bag on his lap, his eyes on the empty road on the tree side.` → `slightly stooped, in the still moment before he opens the bag: both hands rest on top of the closed bag, the fingers of the hand nearer the timetable sign just touching the brass clasp. His eyes are lowered to the bag and his hands; he does not look at the camera.`
- 손녀 줄, 손녀 참조, 손녀 의상 → 삭제
- `Exactly 2 people are visible.` → `Exactly 1 person is visible; no one stands at the timetable sign.`

- 모드: LOCKED EDIT(틀 1, 퍼스트 프레임 0:00)
- 참조(붙이는 순서): 1 `loc_busstop_road_v1`(LC-001-V1, `job-lc001v1`) 장소·카메라 · 2 `char_grandpa_autumn_v1`(CH-001) 얼굴·머리·의상만 · 3 `prop_doctor_bag_v1`(PR-001) 모양·재질·상태만
- 모델: GPT Image 2.5
- 해상도: 1k(확인용) · 16:9 · 1장
- 저장 폴더: 「빈 정류장」/3-4 (`fld-3-4`)
- 검사 스크립트: 통과(FAIL 0 · WARN 0, 참조 3, 고정 문장 3개 원문 일치)

```text
Edit <<<loc_busstop_road_v1>>> WITHOUT reframing: camera position, camera height, angle, lens, framing, horizon line and perspective are LOCKED — zero reframing, zero recentering, zero zoom — this is the same photograph with one change only.
FIRST FRAME of a film shot — the exact state at 0:00 of the video. LEFT and RIGHT are SCREEN directions.
CHANGE — ADD THE OLD MAN AND THE BAG at existing anchors:
- The old man sits on the persimmon-tree half of the bench, his back against the shelter wall, slightly stooped, in the still moment before he opens the bag: both hands rest on top of the closed bag, the fingers of the hand nearer the timetable sign just touching the brass clasp. His eyes are lowered to the bag and his hands; he does not look at the camera.
- The bag lies across the man's thighs, clasp closed, about the width of his lap.
REFERENCE AUTHORITY:
- <<<loc_busstop_road_v1>>> is the exact same photograph. It controls the place, the camera, the light and every object already in it.
- <<<char_grandpa_autumn_v1>>> controls only the old man's face, hair and wardrobe. Same face, same bone structure, same hair, same wardrobe.
- <<<prop_doctor_bag_v1>>> controls only the bag's shape, material and state; its size is as described above.
DO NOT TRANSFER: the character sheet's backdrop, studio lighting, pose or framing; the prop image's background, surface or camera angle.
WARDROBE: The old man: A faded olive work jacket over a cream knit vest and a white collared shirt, dark grey wool trousers, scuffed brown leather shoes.
PROP: A worn brown leather doctor's bag with a brass clasp, about 40 cm wide, hanging heavy from its handles. It is shut; its soft leather sags over his knees, not boxy.
PRESERVE EXACTLY:
- Camera position, height, angle, lens, framing, horizon line, vanishing point and perspective
- The shelter, bench, timetable sign, persimmon tree, road and paddies
- Low dusk sun from the west, the persimmon-tree side, is the only key; the shelter's single fluorescent tube is off. In this view the west is screen LEFT.
- The timetable sign stays unreadable; no legible text anywhere.
- Shadows, exposure, colour grade, contrast and grain
ONLY CHANGE: the old man and the bag are added exactly as described. Everything else remains 100% identical. Exactly 1 person is visible; no one stands at the timetable sign.
```

컷 카드 `project/cuts/3-4.md`를 v1로 고쳤습니다([4] 카메라, [5] 자리·손·시선, [7] 참조·가져온 OK, [10] 위험).
아직 생성하지 않았습니다. 이대로 보낼까요?

=== 메타 ===
연 파일(순서대로):
1. .claude/skills/production-session/ok-reuse.md (사용자가 4번 제안 "3-1과 같은 자리"를 승인)
2. project/ok-cuts.md — "### 3-1 시작 이미지" 절만
3. .claude/skills/higgsfield-generation/SKILL.md (§1-5 검사 스크립트)
4. .claude/skills/higgsfield-generation/check_prompt.py
5. project/cuts/3-4.md (고치기)
임시 파일: tmp/ff-3-4.txt(프롬프트), tmp/fixed-3-4.txt(고정 문장) → check_prompt.py --kind image --refs 3 --must-include → OK
부른 [TOOL]: 없음
고친 정본 파일:
- project/cuts/3-4.md (v0 → v1: [4] 카메라 = LC-001-V1 사용자 답, [5] 자리(3-1 OK에서)·손·시선(제안값), [7] 참조 순서·가져온 OK, [10] 위험 → 막는 문장)
