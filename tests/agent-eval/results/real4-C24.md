# real4 C24

**PASS 2 / 부분 0 / FAIL 0** (real3 PASS 2 유지)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `video-prompt`+`live-action.md`+`acting` 열림, `ok-reuse.md` 안 열림. 카드 [1] '3-1과 같은 동작'과 요청 충돌을 짚음. 6개 질문(사건 3개, 대사·타이밍, 끝 상태·시선, 연기 목표·양 끝, 이음새) |
| 2 | PASS | `CHARACTER_ACTING`: 인물마다 목표·손·호흡·눈·양 끝 failed take. 비트는 시선·사이. 대사 한 번, 할아버지 입 잠금 문장. 레지스터 안. 카드 3-2 고침 `(제안값)` |

## 검사기
검사기(내 실행, `--kind video --refs 4 --seconds 8 --must-include grandpa+girl+bag+light`): `WARN  길이 5798자. 5,500자 이하가 안전했다 … — FAIL 0 · WARN 1 · 5798자`. 플레이어가 숫자와 이유('인물 2·참조 4')를 적음 → 허용.

## 추가 발견
추가: 임시 파일 `p32.txt`·`must32.txt`가 RUN 루트에 남음, 스크래치패드도 RUN 밖 경로 사용(플레이어 규칙 5). 기대 오류 가능: 시나리오는 1턴에 `acting`을 열라 하지만 `routing.md` acting 줄은 '프롬프트를 쓰는 턴에 연다'.

## 키트 결함
없음.
