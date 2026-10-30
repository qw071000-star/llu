# real4-C47 — 두 인물 접촉 (손 잡게)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `production-session`·`video-prompt` SKILL·`live-action.md`·`ok-reuse.md`(카드 [1] "3-1과 같은 동작"이라 정당)·OK 대장 3-1. [TOOL] list_folders/list_project_assets(sim). "손잡기는 3-1에 없는 동작이라 섞으면 편집에서 튑니다", 사건 4개 → 대사 빼 3개, 손 `the screen-left hand, nearer the persimmon tree` ↔ 할아버지 `screen-right hand, nearer the sign`(가방 위 손 유지), 시선, 연기 양 끝(절제). 생성 없음. `acting`은 질문 턴에 안 엶(좋음) |
| 2 (그대로, 프롬프트 턴) | PASS | `acting/SKILL.md`·`live-action.md` 열고 15블록. 위험 7, 블록 밖 모드·참조 4·모델·해상도·길이·폴더, 카드 v2 기록 `(제안값)`, 검사기 여러 번 실행, "480p로 보낼까요?" 생성 없음 |

검사기(내 실행, `--kind video --refs 4 --seconds 8`, must-include grandpa+girl+bag+light): `WARN  길이 7203자. 5,500자 이하가 안전했다…` / `— FAIL 0 · WARN 1 · 7203자`. 플레이어가 7,203자와 이유(−110자, 고정 문장·양 끝은 못 뺌) 적음 → 허용.

3회차 대비: PASS 2 유지(6443→7203자로 길어짐, WARN 이유 있음).
추가 발견(경미): 길이가 인물 2·손 화면 쪽 표기 누적으로 증가. 샷 나누기 제안은 없었음.
키트 결함: 없음.
총평: PASS 2 / 부분 0 / FAIL 0.
