# real13-C35 승인 영상 속도 — "너무 빨라, 천천히" 2-1 (2턴) — PASS 1 / 부분 1 / FAIL 0 (real11: PASS 2 / 부분 0 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | 부분 | 내용은 맞다. 2-1이 `승인`임을 `[TOOL] list_folders`·`list_project_assets`로 확인, "새 테이크로 만들까요"(질문 2), 엄지 구간이 이미 4초라 "앞당길까 영상을 늘릴까"를 제안값으로 묻는 것(질문 3, `video-prompt/SKILL.md:53`), 사건 수 그대로 2개. 카드 파일을 만들지 않음("이번 턴은 질문만 하므로"). 흠: ① 답이 `[TOOL]` 줄과 "2-1은 승인 상태입니다"로 시작해 "15번 …으로 진행합니다."가 없다("판단 … (15번)"만). ② 15번 행은 `video-prompt` §0만 열라는데 `production-session/SKILL.md`도 열었고 존재하지 않는 `cuts/2-1.md`를 시도 |
| 2 | PASS | 확정 프롬프트(OK 카드)에서 `[ACTION_TIMING]` 두 줄만 고쳐 "전 → 후"로 보임: `0:00–0:04 → 0:00–0:02`, `0:04–0:08 → 0:02–0:08 — a longer interval than before: … taking the full 6 seconds … A thumb movement finished in under 5 seconds = failed take.` 두 구간의 초 모두 표기, 사건 수 그대로, 나머지 블록 글자 그대로. 전체를 저장해 검사 실행. 카드 `2-1.md` v0 신설(값을 쓰는 턴). 생성 없음 |

검사기: 플레이어가 지운 임시 파일을 재구성(OK 카드 + 위 두 줄 수정)해 실행: `--kind video C35_new.txt --refs 3 --seconds 8 --must-include grandpa+bag+light` → `OK — video 프롬프트 4229자, 걸린 항목 없음`

추가 발견: 없음. 승인 컷 덮어쓰기 없음(`job-v-2-1` 유지).

키트 결함
- `kit/instructions.md:41`: 영상 결과 지적(15번) 턴 첫 줄 "[N]번 …" 누락(통합 전부터 있던 문제; 사용자 요청에 `[TOOL]` 조회가 먼저 올 때 특히).
- `kit/context/tasks.md:35` 15번 행: "`video-prompt` §0 only for speed·stars·gait"인데 컷 번호가 있으면 `production-session`을 열라는 `instructions.md:39`와 충돌해 플레이어가 둘 다 열었다. 고침: 15번 행에 "(cut number given: do not open production-session; use the OK card)".

총평: 속도 수정 값은 정확했고 첫 줄과 불필요한 스킬 열기가 흠이다.
