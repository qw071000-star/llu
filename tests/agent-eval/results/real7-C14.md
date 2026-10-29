# real7-C14 "표정은 2-1처럼, 2-2 영상" (2턴) — PASS 2 / 부분 0 / FAIL 0 (real6: PASS 2)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `[TOOL] list_project_assets(fld-2-2)`. video-prompt SKILL + production-session SKILL → ok-reuse.md + live-action.md, 2-1 영상 카드·2-2 시작 이미지 카드. "표정 그대로"를 2-1 `CHARACTER_ACTING` 할아버지 줄로 읽고 카메라·낙엽은 안 가져옴. 사건 수·타이밍(쓰다듬기 2번)·끝 상태·시선/소리 4항목 제안값+이유. 렌즈 85mm는 기본값 줄 |
| 2 | PASS | `GRANDPA: waits without hoping. Between stillness and quiet resignation; a sigh or a frown = failed take, a smile = failed take. His eyes stay on the empty road …`가 acting_2-1.lines와 글자 그대로. 입 잠금은 ok-reuse §3 예외대로 올림(알림). 손은 `the screen-left hand, nearer the persimmon tree`. 위험 6개. 카드 2-2 작성(제안값 표시). acting 안 엶(OK 줄 그대로). 생성 안 함 |

검사기: `--kind video --refs 3 --seconds 8 --must-include grandpa+bag+light+acting_2-1` (답 코드블록, 플레이어 `out/2-2_video_prompt.txt`와 diff 없음) → `OK — video 프롬프트 4714자, 걸린 항목 없음`
추가 발견: 1턴에 cut-card.md를 엶(카드 쓰기 전 질문 턴, real6과 동일, 경미). real6의 2턴 acting 열기는 해소.
키트 결함: 없음.
총평: PASS 2 유지. G1: tools에 mcp__ 없음, generate_* 없음.
