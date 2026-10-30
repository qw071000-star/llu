# real8-C14 "표정은 2-1처럼, 2-2 영상" (2턴) — PASS 2 / 부분 0 / FAIL 0 (real7: PASS 2)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | video-prompt SKILL + live-action.md + ok-reuse.md, 2-1 영상 카드·2-2 시작 이미지 카드. "표정"을 2-1 `CHARACTER_ACTING` 할아버지 줄로 읽고 카메라·낙엽은 안 가져옴. 사건 수 / 손·시선 / 타이밍 / 끝 상태·이음새 / 대사·소리 5항목 제안값+이유. 렌즈 85mm는 기본값 줄 |
| 2 | PASS | `GRANDPA: waits without hoping. …`가 acting_2-1.lines와 글자 그대로. 입 잠금은 ok-reuse §3 예외대로 올림(알림). 손은 `the screen-left hand, nearer the persimmon tree`. 위험 6개. 카드 2-2 작성(제안값 표시). 생성 안 함 |

검사기: `--kind video --refs 3 --seconds 8 --must-include grandpa+bag+light+acting_2-1` → `OK — video 프롬프트 5149자, 걸린 항목 없음`
추가 발견: 2턴에 `acting/SKILL.md`를 엶 — 2-1 연기 줄을 그대로 쓰면 불필요하나, 쓰다듬는 손 연기 한 문장을 새로 더했으므로 허용 범위로 봄. `ff_2-2_v1` 요소명은 추정이라고 알림.
키트 결함: 없음.
총평: PASS 2 유지. G1: tools에 mcp__ 없음, generate_* 없음.
