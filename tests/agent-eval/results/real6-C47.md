# real6-C47 — 두 인물 접촉 ("손 잡게")

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `production-session`·`video-prompt` SKILL·`live-action.md`·`ok-reuse.md`·OK 대장 3-1 영상(카드 [1] "3-1과 같은 동작"이라 정당). `acting` 안 엶. "카드 [1]·이음새 표는 3-1과 같은 동작 → 손잡기는 새 동작"(1), 사건 4 → 대사 빼 3(2), 손: 손녀가 화면 오른쪽에서 와 `할아버지의 화면 오른쪽 손(시간표에 가까운 손)`을 잡고 다른 손은 닫힌 가방 위(3 = 가방 위 두 손 연속성 충돌 처리), 할아버지 반응 절제(4), 렌즈 카드 35° ↔ 시작 이미지 75mm 불일치 짚음. 생성 없음 |
| 2 (그대로, 프롬프트 턴) | PASS | `acting/SKILL.md`·`cut-card.md` 엶. 코드블록 1(15블록), 블록 밖 모드·참조 4·모델·해상도·길이·소리·폴더, 위험 7, 3-1에서 가져온 줄 + 삭제 줄 공개, 연기 양 끝(`tears`/`playful squeeze` / `sliding the … hand out` / `gripping back` = failed take), 손 `the screen-left hand, nearer the bench` ↔ `his screen-right hand, nearer the sign`. 카드 `cuts/3-2.md` v2 `(제안값)` 기록(git diff 확인). 길이 WARN을 숫자(5,998자)와 이유(고정 문장·연기 양 끝은 못 뺌)로 남김 → 숫자 일치. 보낼까요, 생성 없음 |

검사기(내 실행, `--kind video --refs 4 --seconds 8`, must-include grandpa+girl+bag+light): `WARN  길이 5998자. 5,500자 이하가 안전했다. 남기려면 이 숫자를 그대로 적고 이유를 쓴다` / `— FAIL 0 · WARN 1 · 5998자`. 플레이어가 숫자·이유 적음(허용, `live-action.md:31`).
5회차 대비: PASS 2 유지(6566 → 5998자, 숫자 오차도 해소).
추가 발견: 샷 나누기 제안은 없음(사건 3으로 줄임, 허용). 검사용 임시 파일은 scratchpad.
키트 결함: 없음.
총평: PASS 2 / 부분 0 / FAIL 0.
