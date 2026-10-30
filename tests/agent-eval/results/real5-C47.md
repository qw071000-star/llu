# real5-C47 — 두 인물 접촉 ("손 잡게")

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `production-session`·`video-prompt` SKILL·`live-action.md`·`ok-reuse.md`·OK 대장 3-1 영상(카드 [1] "3-1과 같은 동작"이라 정당). `acting`은 안 엶. "손잡기는 카드 [1]과 다른 방향", 사건 4 → 대사 빼 3, 손 `the screen-left hand, nearer the persimmon tree` ↔ 그의 `screen-right hand, nearer the timetable sign`(가방 위 손 유지·가방 닫힘), 연기 양 끝(울음·매달림 / 손 빼기·되잡기), 생성 없음 |
| 2 (그대로, 프롬프트 턴) | PASS | `acting/SKILL.md` 엶. 15블록 코드블록 1 + 블록 밖 모드·참조 4·모델·해상도·길이·폴더, 위험 6, 검사기 여러 번 실행, "480p에 보낼까요?" 생성 없음. 1턴에 말한 대사 생략 판단을 "정정"으로 바로잡음 |

검사기(내 실행, `--kind video --refs 4 --seconds 8`, must-include grandpa+girl+bag+light): `WARN  길이 6566자. 5,500자 이하가 안전했다. 남기려면 이 숫자를 그대로 적고 이유를 쓴다` / `— FAIL 0 · WARN 1 · 6566자`. 플레이어는 "6,495자"와 이유(고정 문장·연기 양 끝은 못 뺌)를 적음 → 이유는 허용(`live-action.md:31`), 숫자는 71자 틀림(경미).
4회차 대비: PASS 2 유지(7203 → 6566자).
추가 발견: 샷 나누기 제안 없음(경미). 키트 결함 없음.
총평: PASS 2 / 부분 0 / FAIL 0.
