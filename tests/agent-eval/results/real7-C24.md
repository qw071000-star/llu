# real7 C24

**PASS 2 / 부분 0 / FAIL 0** (real6 PASS 2 유지)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `video-prompt` SKILL+`live-action.md`만(`acting`·`ok-reuse.md`·3-1 카드 안 열림); 카드 [1]과 지시 충돌 짚음, 카드 35° ↔ 시작 이미지 75mm(32°) 정정; 9개 항목에 사건 3개·타이밍·연기 목표와 양 끝 제안; `[TOOL] list_folders` |
| 2 | PASS | `acting/SKILL.md` 열림(프롬프트 턴); `CHARACTER_ACTING` 인물마다 상대를 향한 목표·손·호흡·눈·양 끝 `failed take`; 비트 3개; 손녀 목소리 문장 글자 그대로; `He does not say a single word: no attempt to speak, no parted lips, no mouthing`; 레지스터 내(울음 failed take); 6,279자 WARN에 숫자·이유 명시 |

## 검사기
내 실행 `--kind video --refs 4 --seconds 8 --must-include grandpa+girl+bag+light`: `WARN 길이 6279자. 5,500자 이하가 안전했다 … — FAIL 0 · WARN 1 · 6279자` (플레이어가 숫자 6,278과 이유(인물 2·참조 4·고정 문장)를 적음 → 허용).

## 추가 발견
G1(mcp 호출·생성) 위반 없음, RUN 밖 읽기 없음. 없음.

## 키트 결함
없음.

## 총평
연기 새로 잡기·OK 미반입 모두 충족.
