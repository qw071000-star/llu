# real9-C47 두 인물 접촉 ("손 잡게") (2턴) — PASS 2 / 부분 0 / FAIL 0 (real8: PASS 2)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `production-session`·`video-prompt/SKILL.md`·`live-action.md`·`ok-reuse.md`·`cut-card.md`(acting은 2턴에서 엶). `[TOOL] list_folders`·`list_project_assets` 줄. "컷 카드 [1]은 '3-1과 같은 동작'인데, 손잡기는 3-1에 없는 동작"을 먼저 짚음, 사건 4개 → 대사 뺌/3개로(2·5), 어느 손: "손녀의 화면 왼쪽 손(벤치에 가까운 쪽)이 할아버지의 화면 오른쪽 손(시간표에 가까운 쪽)을 가방 위에서 포개어", 가방 닫힘 유지(§6), 절제(§5), 3-3 이음새(1). 렌즈 카드 35°↔시작 이미지 75mm 정정. 경미: 연속성 표 "두 손을 가방 위"와의 충돌을 그 말로 명시하지 않고(가방 위에서 포갠다로 처리), 카드의 대사 켬을 효과음만으로 바꾸는 제안(제안값) |
| 2 (그대로) | PASS | `acting/SKILL.md` 엶. 코드블록 1(15블록), 블록 밖 모드·참조 4·모델·해상도·길이·소리·폴더, `3-1에서 바꾼 줄 (전 → 후)`, 위험 5. git diff `cuts/3-2.md` [1]·[3]~[7]·[10] `(제안값)`. 길이 WARN을 숫자(6,301자, 줄여 본 −100/−240자)로 남김. "보내"를 요청, 생성 없음 |

**검사기**(내 실행, `--kind video --refs 4 --seconds 8`, must-include grandpa+girl+bag+light+motion 0:00–0:03 줄+motion_owner CAMERA·ENVIRONMENT): `WARN 길이 6301자 … — FAIL 0 · WARN 1 · 6301자`. 플레이어가 이 WARN의 숫자와 이유를 적어 허용(`live-action.md:31`).

**추가 발견:** 손 표기 전부 `screen-` + 물건, 방향어 모두 화면 기준(G9 OK).

**키트 결함:** 없음.

**총평:** PASS 2 / 부분 0 / FAIL 0.
