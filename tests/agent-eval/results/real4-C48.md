# real4-C48 — 화면 밖으로 나가기

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `video-prompt/SKILL.md`·`live-action.md`, 3-3 카드·OK 대장. `acting` 안 엶. 나가는 방향 "화면 왼쪽(지붕 끝 쪽)" 제안+근거, 끝 상태 "몸의 왼쪽 절반이 프레임 밖, 이미 걷는 중", 사건 3개, 3-4에 손녀 없어 이음새 충돌 없음. 질문 6. 생성 없음. 경미: 질문 턴에 카드 [1]을 고침 |
| 2 (그대로, 프롬프트 턴) | 부분 | 15블록 코드블록 + 블록 밖 모드·참조 2·모델·해상도·길이·폴더, 위험 7, FINAL_FRAME `screen-left half of her body past the left edge… already walking`, 카드 기록, "get_cost… 보내려면 만들어". 미달: (1) 다른 컷 핸드오프를 엶 — bash `sed -n 1,80p project/log/3-2_handoff_2026-10-27.md \| head -5`(meta reads) — `routing.md:46` "다른 컷 카드·핸드오프는 열지 않는다" 위반, 3회차에 없던 회귀. (2) meta에 `acting/SKILL.md` 열람 기록이 없는데 프롬프트에 acting 원문 문장(`micro-saccades…`)이 있음 — 열람 누락이거나 메타 누락(확인 불가). (3) 작업 파일 `.draft_3-3.txt`를 RUN 루트에 남김 |

검사기(내 실행, `--kind video --refs 2 --seconds 8`, must-include girl+light): `OK — video 프롬프트 5369자, 걸린 항목 없음`

3회차 대비: PASS 2 → PASS 1/부분 1 (핸드오프 열람·acting 기록 누락).
키트 결함: 없음(규칙은 `routing.md:46`에 명시). 재발하면 `routing.md:46`을 "컷 세션은 자기 컷 번호의 핸드오프만"으로 짧게 바꿔 눈에 띄게.
총평: PASS 1 / 부분 1 / FAIL 0.
