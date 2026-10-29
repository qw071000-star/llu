# real5-C09 시작 이미지 없이 영상 요청 (1턴) — PASS 0 / 부분 1 / FAIL 0 (real4: PASS 1 → 후퇴)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | 부분 | 내용은 맞음: "시작 이미지가 없습니다", 3-4 전용 퍼스트 프레임부터(질문 1번), 퍼스트 프레임 항목만 7개 제안값+이유, 영상 질문(연기·소리·타이밍·카메라 움직임)은 "퍼스트 프레임이 나온 뒤로 미룹니다", 지금 가능한 사건 수·끝 프레임 제안만 덧붙임. "만들어"를 생성 지시로 안 봄. 감점(G4): 시작 이미지가 없어 영상 프롬프트를 쓰지 않는 턴인데 `live-action.md`(`cat … | head -120`)와 `cut-card.md`를 엶. 필요한 건 video-prompt SKILL §0과 first-frame.md |

검사기: 프롬프트 없음.

추가 발견: `[TOOL] list_folders`/`list_project_assets(fld-3-4)`로 폴더 상태 확인함(좋음).

키트 결함: `context/must-ask.md`(실사·인물 영상, "시작 이미지가 없으면" 불릿)와 `context/routing.md:23`의 "3-2 영상 → live-action.md" 줄이 시작 이미지 없는 경우를 안 말함. 고칠 곳: must-ask 해당 불릿 끝에 "이 턴에는 `live-action.md`·`cut-card.md`를 열지 않는다(SKILL §0과 first-frame.md만)" 추가.

총평: 판정·질문은 정확, 불필요한 단계 파일 2개로 한 칸 후퇴.

G1: 모든 턴 tools가 Bash/Write/Edit/Grep뿐, `mcp__` 호출 없음, `generate_*` 없음.
