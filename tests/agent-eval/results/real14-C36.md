# real14-C36 레지스터와 부딪치는 연기 — "살짝 웃게" 2-2 (2턴) — PASS 1 / 부분 1 / FAIL 0 (real13: PASS 1 / 부분 1 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | 부분 | 내용은 맞다: 라벨 "[13]번 실사·인물 영상으로 진행합니다." `acting`·`cut-card.md`를 열지 않고 카드도 안 만듦. 컷 목록 2-2 "같은 얼굴로 가방을 쓰다듬음"과 다름을 플래그하고 "이 컷만 / 작품 전체" 질문, `decisions.md` §5(절제)와 맞는 "입꼬리만, 이는 안 보임", 2-1 OK 이유 "기대 안 하는 얼굴"과 반대로 읽힐 이음새 지적(2-1 영상 카드는 안 열고 OK 목록만 봄). 사건 3개 셈. 감점: 답의 첫 줄이 도구 호출 전의 영어 한 줄 "Reading the 2-2 start-image card and the 2-1 video card (the neighbour's OK, for the seam) now."이고 라벨은 그 다음이다(`kit/instructions.md:12` 첫 줄 규칙, 한국어 규칙). 말과 달리 2-1 영상 카드는 열지 않았다 |
| 2 | PASS | `acting` SKILL을 엶. `CHARACTER_ACTING`: 입꼬리 몇 mm, 입 닫힘, 이 안 보임, 소리 없음, 비트는 시선(길 → 가방), `does not startle; it simply stops`, 눈 문장, 양 끝 `a face that never changes = failed take, teeth showing or the cheeks lifting into a laugh = failed take`. 손은 모두 `screen-left hand, nearer the persimmon tree` 식. 입 잠금(`no attempt to speak, no parted lips, no mouthing`). `ACTIVE_REFERENCES` 할아버지 줄은 WARDROBE 문장만(IDENTITY 문장 없음, grep 0). 카드 `cuts/2-2.md` v0 `(제안값)`, 컷 목록 변경은 핸드오프 [5]로 올림. 길이 WARN은 6,380자라는 숫자와 이유(약 630자 줄였고 더 줄이면 고정 문장·연기 양끝을 지워야 함)를 적음. 위험 6줄, "480p로 영상으로 보낼까요?" |

검사기: `python3 kit/skills/higgsfield-generation/check_prompt.py --kind video C36t2_1.txt --refs 3 --seconds 8 --must-include grandpa+bag+light` → `WARN  길이 6380자. 5,500자 이하가 안전했다. 남기려면 이 숫자를 그대로 적고 이유를 쓴다 — FAIL 0 · WARN 1 · 6380자` (숫자·이유를 적었으므로 허용)

real13 감점 해소: `ACTIVE_REFERENCES`에 IDENTITY 문장을 붙인 문제 — 해소(`live-action.md` 블록 표의 "A character line carries the registry WARDROBE sentence only"). 새 감점: 1턴 첫 줄 앞에 영어 진행 문장.

추가 발견
- `OPTICS`의 "the camera is physically far away"는 85mm 클로즈업(카메라 약 2m)과 어긋나는 템플릿 문구. 해는 작음.
- 시작 이미지 태그를 `<<<job-ff-2-2>>>`(job ID)로 씀 — 대장에 요소 이름이 없어 허용.

키트 결함: `kit/instructions.md:12` — 첫 줄 규칙은 "answer's first line"만 말하고, 도구를 먼저 부르는 턴에서 도구 전 진행 문장이 먼저 보이는 것은 막지 않는다 → "Write the 번호 line before the first tool call; any text shown between tool calls is also short Korean."

총평: 연기 범위·WARDROBE 규칙은 맞았으나 1턴이 영어 진행 문장으로 시작해 부분 1.
