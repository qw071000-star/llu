# real9-C48 화면 밖으로 나가기 (2턴) — PASS 2 / 부분 0 / FAIL 0 (real8: PASS 1 / 부분 1)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | 3-3 카드·정본·`production-session`·`video-prompt/SKILL.md`·`live-action.md`. `[TOOL] list_folders`/`list_project_assets` 줄(real8 경미 해소). 사건 3개("나가기도 한 사건으로 셉니다"), 나가는 방향 "화면 왼쪽, 정류장 지붕 끝 쪽" 제안(3-4 이음새), 끝 상태 "이미 걷는 중이고 몸 절반이 프레임 밖", 타이밍 3·2·3초, 3-4 연속성 표 인물 자리를 핸드오프 [5]로. 생성 없음 |
| 2 (그대로) | PASS | `live-action.md`·`acting`·`cut-card.md`. 코드블록 1(15블록), `FINAL_FRAME: half of her body outside the left edge`, `GIRL exits toward the screen-left end`, 손 `the screen-right hand, nearer the sign`, 블록 밖 모드·참조 2·모델·해상도·길이·폴더, 위험 7. **real8의 `shot-list.md` 내용 칸 수정은 없음**(git diff는 `cuts/3-3.md`만). 프레임 밖 인물(할아버지) 언급도 SCENE_CONTEXT에서 제거됨. 경미: 이웃 3-1 OK 카드를 열었다고 스스로 정정(문장은 쓰지 않음) |

**검사기**(내 실행, `--kind video --refs 2 --seconds 8`, must-include girl+light): `OK — video 프롬프트 5099자, 걸린 항목 없음`.

**추가 발견:** 기준 OK가 아닌 3-1 카드 열람은 G4 경미 위반(`instructions.md` 읽기 지도) — 본인이 첫 줄에서 고백하고 가져다 쓰지 않았으므로 감점하지 않음.

**키트 결함:** 없음.

**총평:** PASS 2 / 부분 0 / FAIL 0 (real8의 `production-session` §1 위반 해소).
