# real4-C36 — 레지스터와 부딪치는 연기

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | meta에 `acting/SKILL.md` 포함. "컷 목록 2-2 원문이 '같은 얼굴로…', 2-1의 '기대 안 하는 얼굴'", 입 다문 작은 웃음, 양 끝 failed take(무표정/이 보임·소리 내어 웃음), 6개 한 묶음. 생성 없음. 경미: 질문 턴에 acting을 엶(`routing.md:27`은 프롬프트 턴) |
| 2 (그대로, 프롬프트 턴) | PASS | 15블록 코드블록 1 + 블록 밖 모드·참조 4·모델·해상도·길이·폴더, 위험 7, `teeth showing or laughing = failed take`, 손 `screen-left hand, nearer the tree`. 마지막 줄 "480p로 보낼까요?" 생성 없음. 카드 `(제안값)` 기록 |

검사기(내 실행, `--kind video --refs 4 --seconds 8`, must-include grandpa+bag+light+identity): `WARN  길이 5689자. 5,500자 이하가 안전했다…` / `— FAIL 0 · WARN 1 · 5689자`. 플레이어가 숫자와 이유(−128자, 고정 문장·연기 양 끝은 못 뺌)를 적음 → 허용(`live-action.md:31`). 

3회차(real3) 대비: PASS 2 유지(5481→5689자, WARN 이유를 적어 통과).
추가 발견: 없음. 키트 결함: 없음.
총평: PASS 2 / 부분 0 / FAIL 0.
