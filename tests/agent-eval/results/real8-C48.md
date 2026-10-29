# real8-C48 — 화면 밖으로 나가기

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | 3-3 카드·shot-list·decisions·registry·ok-cuts·`video-prompt/SKILL.md`·`live-action.md`. 사건 3개(읽기·돌아서기·나가기, "나가기도 셉니다"), 나가는 쪽 화면 왼쪽(벤치·감나무 쪽, 3-4는 할아버지 컷), 끝 상태 "몸 절반이 화면 왼쪽 가장자리 밖, 이미 걷는 중", 타이밍 3·2·3초. 생성 없음. 문제 예고: "컷 목록 한 줄은 '돌아서 걸어 나간다'로 넓혀 고칩니다"(아래 2턴 참고). `[TOOL]` 폴더 조회 줄 없음(경미) |
| 2 (그대로, 프롬프트 턴) | 부분 | 맞음: `acting/SKILL.md`·`cut-card.md` 엶, 코드블록 1(15블록), `FINAL_FRAME` 몸 절반 프레임 밖 + `GIRL leaves only through the screen-left edge`, 손 `the screen-right hand, nearer the sign`, 블록 밖 모드·참조 2·모델·해상도·길이·폴더, 위험 6, 연기 `tears … failed take, running or a hurried walk = failed take`, `cuts/3-3.md` `(제안값)`. 미달: `project/shot-list.md` 3-3의 "내용(한 줄)"을 고침(`손녀가 시간표를 한 번 더 보고 돌아서 화면 왼쪽으로 걸어 나간다`). `production-session/SKILL.md:15` — 컷 세션은 컷 목록에서 "자기 줄의 상태 칸과 확정 job 칸만". 내용 칸은 총괄 몫(핸드오프 [5]). 경미: SCENE_CONTEXT·CHARACTER_ACTING에 "her grandfather, who is out of frame"·"she goes to him"이 있어 프레임 밖 인물이 렌더될 위험(7회차도 같은 지적) |

검사기(내 실행, `--kind video --refs 2 --seconds 8`, must-include girl+light): `OK — video 프롬프트 5116자, 걸린 항목 없음`.
추가 발견: `tmp/` 삭제, 빈 폴더도 정리.
키트 결함: 컷 세션이 컷 목록 내용 칸을 못 고친다는 규칙이 `production-session/SKILL.md:15`에만 있고, 이 턴에는 그 SKILL을 안 열어도 되는 길(routing 표)이라 항상 읽히는 파일에 없음. 고칠 것: `context/routing.md` §3 "컷 세션의 정본" 항목 끝에 "컷 목록은 자기 줄의 상태·확정 job 칸만 고친다. 내용 칸은 핸드오프 [5]로 총괄에 올린다" 한 줄.
7회차 대비: PASS 2 → PASS 1 / 부분 1.
총평: PASS 1 / 부분 1 / FAIL 0.
