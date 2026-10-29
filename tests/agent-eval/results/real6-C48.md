# real6-C48 — 화면 밖으로 나가기

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `video-prompt/SKILL.md`, 3-3 카드(자기 컷)·컷 목록·OK 대장. 카드 [1] "돌아선다"와 요청이 다름(1), 사건 읽기·돌아서기·걸어 나가기 = 3(2), 나가는 쪽 "화면 왼쪽 지붕 끝, 길 쪽 아님", 끝 프레임 "몸 절반이 프레임 밖, 이미 걷는 중", 3-4는 할아버지만 나옴(이음새), 생성 없음 |
| 2 (그대로, 프롬프트 턴) | PASS | `live-action.md`·`acting/SKILL.md`·`cut-card.md` 엶. 코드블록 1(15블록 전문 — 5회차 결함 해소), 블록 밖 모드·참조 2·모델·해상도·길이·소리·폴더, 위험 7, FINAL_FRAME `about half of GIRL's body is outside the left edge, mid-stride`, 손 `the screen-right hand, nearer the sign`·`the screen-left hand, farther from the sign`. 카드 `cuts/3-3.md` v2(`(제안값)`, [1] 수정은 핸드오프 [5]로 확인 요청), 컷 목록은 총괄 소관이라 안 고침. 생성 없음 |

검사기(내 실행, `--kind video --refs 2 --seconds 8`, must-include girl+light): `OK — video 프롬프트 5052자, 걸린 항목 없음`.
5회차 대비: PASS 1/부분 1 → PASS 2.
추가 발견: SCENE_CONTEXT가 "toward her grandfather, who is out of frame"라 쓰나 나가는 방향은 화면 왼쪽(경미, 사용자가 말하지 않은 목적지 암시).
키트 결함: 없음.
총평: PASS 2 / 부분 0 / FAIL 0.
