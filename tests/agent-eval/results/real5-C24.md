# real5 C24

**PASS 2 / 부분 0 / FAIL 0** (real4 PASS 2 유지)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `video-prompt`+`live-action.md` 열림, `acting`·`ok-reuse.md` 안 열림. 카드 [1]과 지시 충돌 짚음('3-1 OK를 열지 않으니 …'), 카드 렌즈 35°↔시작 이미지 75mm 정정, 6개 질문에 연기(목표·양 끝)·타이밍·끝 상태 제안 |
| 2 | PASS | `acting` bash로 열림. `CHARACTER_ACTING` 인물마다 목표·손·몸(호흡)·눈·양 끝 `failed take`, 비트 3개(시선·사이), 대사 정확히 1회+할아버지 입 잠금(`no parted lips, no mouthing`), 레지스터 이내. 5,683자 WARN은 숫자·이유 명시('고정 문장이나 연기의 양 끝을 빼야 해서 그대로') |

## 검사기
내 실행(`--kind video --refs 4 --seconds 8 --must-include grandpa+girl+bag+light`): `WARN  길이 5683자. 5,500자 이하가 안전했다 … — FAIL 0 · WARN 1 · 5683자` (허용: 이유와 숫자 적음)

## 추가 발견
질문 턴에 카드 [1]·[4]~[6]을 `(제안값)`으로 미리 고침(사용자 지시와 충돌하는 칸이라 허용).

## 키트 결함
없음.
