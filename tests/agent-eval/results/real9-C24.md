# real9-C24 실사 영상, 연기를 새로 — 3-2 (2턴) — PASS 1 / 부분 1 / FAIL 0 (real8: PASS 2 / 부분 0 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | 부분 | `video-prompt/SKILL.md`+`live-action.md` 열음, `ok-reuse.md`·3-1 OK 카드는 열지 않음("3-1 OK 카드는 열지 않았습니다"). 7개 제안값을 한 묶음으로 질문(목표·손·호흡·양 끝 failed take 포함). 카드 [1]의 "3-1과 같은 동작·타이밍"과 사용자 말의 충돌을 짚음, 렌즈 35° vs 시작 이미지 75mm(≈32°) 알림. **그러나 질문 턴에 `.claude/skills/acting/SKILL.md`를 열었다**(메타 reads 마지막) — `context/routing.md:26` "영상이면 질문 턴에는 열지 않는다" 위반, 시나리오 기준 "1턴에 열면 부분" |
| 2 | PASS | `cut-card.md` Read(카드에 적는 턴). `CHARACTER_ACTING` 인물마다 상대를 향한 목표(`makes her grandfather believe it is no big deal`), 손(`pinches the cuff`), 호흡, 눈 블록, 양 끝 failed take(`tears or a crumpling face = failed take, a flat monotone recital = failed take`; `a visible reaction is a failed take, no reaction at all is also a failed take`). 비트 3개(대사·한 걸음·손가락 누름). 손녀 VOICE 문장 대장과 글자 그대로. 할아버지 입 잠금 `does not say a single word: no attempt to speak, no parted lips, no mouthing`. 절제 레지스터 안. 길이 WARN에 숫자(6,029자)와 이유 기재. 카드 [1][4]~[6]에 `(제안값)` 기록 |

## 검사기
내 실행 `--kind video --refs 4 --seconds 8 --must-include (grandpa+girl+bag+light)`:
`WARN  길이 6029자. 5,500자 이하가 안전했다. 남기려면 이 숫자를 그대로 적고 이유를 쓴다 — FAIL 0 · WARN 1 · 6029자`
(플레이어가 "6,029자 … 5,500자 기준 초과" 이유와 함께 보고 → 허용.)

## 추가 발견
- G1 위반 없음. `tmp/` 삭제 확인.
- 렌즈 관찰 결과 3개를 "추정"으로 명시(규칙 10 충족).
- 플레이어가 길이를 줄이려 6,816자 → 6,029자로 다듬음. 카드 [4] 렌즈를 시작 이미지 값으로 고침.
- 카드 [8]에 고정 설명문 원문을 유지(글자 그대로).

## 키트 결함
없음. `acting` 질문 턴 금지는 `kit/context/routing.md:26`, `kit/skills/video-prompt/live-action.md:3`, `video-prompt/SKILL.md:10` 세 곳에 명확히 적혀 있어 플레이어 위반이다. 다만 사용자가 "연기도 새로 잡아"라고 말한 턴에 모든 문서가 "열지 않는다"고 해도 유혹이 크므로, 이 반복되면 SKILL.md 상단에 "사용자가 연기를 언급해도 질문 턴에는 열지 않는다" 한 줄 추가를 고려.

## 총평
연기 새로 잡기·OK 미반입 충족, 질문 턴에 acting을 연 것만 부분.
