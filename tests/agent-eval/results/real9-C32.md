# real9-C32 사용자가 말한 손 — "손녀 오른손에 우산" (2턴) — PASS 2 / 부분 0 / FAIL 0 (real8: PASS 2 / 부분 0 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `image-prompt/SKILL.md`+`first-frame.md` Read, 컷 카드·3-1 핸드오프(자기 컷)만. "오른손"을 화면 기준으로 받고 충돌을 짚음: `화면 오른쪽 손은 지금 시간표 쪽(nearer the sign)에서 시간을 짚는 손입니다`; A(화면 왼쪽 손, `farther from the sign`) / B(화면 오른쪽 손으로 옮김, 변경이 둘) 선택지 제시, `her right hand`를 쓰지 않음. 우산이 에셋 대장에 없음 → 사양(검은 천, 나무 갈고리, 80cm, 비닐·현대 물건 금지) 제안값. 승인 컷이라 새 테이크로 대체할지 질문. 생성 없음 |
| 2 | PASS | 인물 기준 오른손으로 받음: `손녀가 시간표를 향해 옆모습으로 서 있어서, 본인 오른손은 카메라 쪽 손으로 읽었습니다. … (추정)`, "화면 오른쪽 손 → the screen-left hand, farther from the sign" 전 → 후로 알림. 프롬프트에 `her right hand` 없음, `the screen-left hand, farther from the sign` + `the screen-right hand, nearer the sign` 유지, `LEFT and RIGHT are SCREEN directions`, WARDROBE·LIGHT LOCK 글자 그대로, `Exactly 2 people are visible.` 위험 5개(원본에서 손이 비었는지 못 봤다는 "추정" 포함). 카드 3-1 [5]에 `(제안값)` 기록 |

## 검사기
내 실행 `--kind image --refs 1 --must-include grandpa+girl+light`: `OK — image 프롬프트 1867자, 걸린 항목 없음`

## 추가 발견
- G1 위반 없음. `tmp/` 삭제 확인. 첫 검사에서 제목 줄 WARN 1개를 고치고 재실행함(보고함).
- 손 대응(인물 오른손 = 카메라 쪽 손 = 화면 왼쪽 손)의 근거는 옆모습이라 불확실하다. "추정"으로 표시했으므로 규칙 6 충족. real8은 같은 상황을 "화면 오른쪽 손"으로 읽었다 — 옆모습의 매핑이 플레이어마다 갈린다.

## 키트 결함
- `kit/instructions.md:28`(규칙 6)은 "인물이 향한 쪽으로 화면 쪽을 정한다"만 말하고 옆모습(인물이 화면 오른쪽을 향함)에서 본인 오른손이 화면 어느 쪽·무슨 물건에 대응하는지의 표가 없다. 제안: 규칙 6 또는 `first-frame.md`에 "카메라를 봄 → 본인 오른손 = 화면 왼쪽 / 등지고 있음 → 화면 오른쪽 / 옆모습(화면 오른쪽을 향함) → 카메라에 가까운 손, 물건(예: 시간표에서 먼 손)으로 쓰고 추정 표기" 한 줄 표를 넣을 것.

## 총평
화면 기준 충돌을 짚고 "추정"으로 정확히 처리.
