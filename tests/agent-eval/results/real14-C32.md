# real14-C32 사용자가 말한 손 — "손녀 오른손에 우산" (2턴) — PASS 2 / 부분 0 / FAIL 0 (real13: PASS 1 / 부분 1 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | 첫 줄 "11번 퍼스트·끝 프레임으로 진행합니다." 3-1 카드·핸드오프·OK와 `image-prompt` SKILL·`first-frame.md`만 열음. "'오른손'은 화면 기준 오른손으로 받았습니다", 그 손은 이미 시간표를 짚는다는 충돌과 화면 왼쪽 손 대안, "손녀 자신의 오른손이라는 뜻이면 말씀해 주세요(추정 표시)". 새 소품 우산(검은 천 장우산 약 70cm, J자 손잡이) 제안값, 승인 컷이라 새 테이크 확인(Q4), 영상 `job-v-3-1` 재제작 필요 고지. 생성 없음 |
| 2 | PASS | 손녀 기준을 손녀가 향한 방향으로 환산해 `the girl's screen-left hand, farther from the sign`으로 쓰고 "추정" 표기. `her right hand` 없음. 첫 답 대비 변경(우산 끝 높이 "무릎 위" → "땅에서 10cm 위")을 "전 → 후"로 알림. LOCKED EDIT 여는 문장, CHANGE/PRESERVE EXACTLY/ONLY CHANGE, `Exactly 2 people are visible.` `WARDROBE:` 줄에 할아버지·손녀 문장 둘 다 글자 그대로. 카드 3-1 [5]에 `(제안값)`·`(추정)` 기록(diff). 위험 5줄, "이대로 이미지로 만들어 보낼까요?" |

검사기: `python3 kit/skills/higgsfield-generation/check_prompt.py --kind image C32t2_1.txt --refs 1 --must-include grandpa+girl+light` → `OK — image 프롬프트 1896자, 걸린 항목 없음` (플레이어가 처음 돌렸을 때 `a hand's width`를 손 위치로 읽은 WARN이 나왔고 검사기 오탐으로 보고 표현을 바꿈)

real13 감점 해소: 두 사람이 보이는데 `WARDROBE:`에 손녀 문장만 있던 문제 — 해소(`first-frame.md:19` "One WARDROBE: line per visible person" 추가가 효과).

추가 발견: 손녀의 "본인 오른손" → 화면 쪽 환산은 손녀가 시간표를 향한 방향에 달려 있어 플레이어 판단(추정 표기, real13과 같은 허용).

키트 결함
- `kit/skills/higgsfield-generation/check_prompt.py:60` — `hand` 단독 단어 검사가 `hand's`(소유격)에도 걸린다 → `(?<![-\w])hand(?![-\w'’])`로 좁힌다.
- `kit/instructions.md:27`(규칙 6) — 옆모습·등지고 선 인물의 "본인 오른손" 변환표가 없다(real13부터 이어짐) → "back to camera: own right = screen right; facing screen-side: give the hand's screen side + object, mark 추정" 한 줄.

총평: real13의 WARDROBE 누락이 해소되고 화면 방향 처리도 맞아 PASS 2.
