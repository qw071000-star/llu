# real5-C10 영상, 일부만 답함 3-3 (3턴) — PASS 3 / 부분 0 / FAIL 0 (real4: PASS 2 / 부분 1 → 개선)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | production-session + video-prompt SKILL + live-action.md. **acting 안 엶**(real4 감점 해소). 8항목을 소제목 3묶음(사건·끝 / 시선·타이밍·연기 / 소리·이음새)으로 제안값+이유. 렌즈·길이·카메라는 "기본값으로 씀: 50mm=47°" 한 줄. 시작 이미지 `job-ff-3-3` 인지. 카드 3-3 [3]의 소리 빈 칸 → 대사 질문 |
| 2 | PASS | 망원이 시작 이미지 50mm와 부딪친다고 한 번 질문("시작 이미지 그대로 50mm" 제안, 망원이면 퍼스트 프레임 재작성+대체). 나머지는 제안값으로 정해 카드 [1][3]~[6]에 `(제안값)`으로 기록(git diff). 시나리오 2턴 PASS 조건. 이 컷만/전체 룩 질문은 과함(경미) |
| 3 | PASS | acting SKILL을 이 턴에 엶. 15블록 전문: OPTICS `Diagonal field of view about 47°` + 관찰 3개(mm 없음), girl·LIGHT LOCK 글자 그대로, 손 `the screen-right hand, nearer the sign`, `Nobody looks at the camera`, 입 잠금, `Exactly one person`, AUDIO 효과음만(대사 없음). 사건 수를 2개 → 3개로 정정. 위험 7줄. 검사 5회 실행, 생성 안 함 |

검사기: `--kind video --refs 2 --seconds 8 --must-include girl+light`: `OK — video 프롬프트 5447자, 걸린 항목 없음`

추가 발견: 카드 3-3 [1] 완료 조건이 "사건 2개"로 남아 3턴 정정(3개)과 어긋남. 프롬프트 파일을 `out/`에 둠.

키트 결함: 없음.

총평: real4의 acting 조기 열람 감점 해소.

G1: 모든 턴 tools가 Bash/Write/Edit/Grep뿐, `mcp__` 호출 없음, `generate_*` 없음.
