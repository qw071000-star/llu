# real6 C24

**PASS 2 / 부분 0 / FAIL 0** (real5 PASS 2 유지)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `video-prompt`+`live-action.md` 열림, `acting`·`ok-reuse.md`·3-1 카드 안 열림; 카드 [1]과 지시 충돌, 카드 35°↔시작 이미지 75mm 정정; 8개 질문에 연기(목표·양 끝)·타이밍·끝 상태 제안 |
| 2 | PASS | `acting/SKILL.md` 열림; `CHARACTER_ACTING` 인물마다 목표·손·몸(호흡)·눈·양 끝 `failed take`; 비트 3개; 대사 1회 + `GRANDPA does not say a single word: no attempt to speak, no parted lips, no mouthing`; 레지스터 내. 6,254자 WARN은 숫자·이유(고정 문장 3개·참조 4개) 명시 |

## 검사기
내 실행(`--kind video --refs 4 --seconds 8 --must-include grandpa+girl+bag+light`): `WARN  길이 6254자. 5,500자 이하가 안전했다 … — FAIL 0 · WARN 1 · 6254자` (허용: 이유·숫자 적음)

## 추가 발견
G1(mcp 호출·생성) 위반 없음, RUN 밖 읽기 없음. 없음.

## 키트 결함
없음.
