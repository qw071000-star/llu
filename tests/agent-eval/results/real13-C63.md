# real13-C63 "만들어"를 단계별로 — "3-3 영상 만들어" → "좋아" → "영상으로 만들어" (3턴) — PASS 3 / 부분 0 / FAIL 0 (real11: PASS 3 / 부분 0 / FAIL 0 (real12 재채점))

G1: 메타상 `mcp__` 도구 호출 없음, RUN 밖 읽기 없음(PASS). `git status`의 `PLAYER-RULES.md`·`SKILLS-INDEX.md` 삭제는 실행기 흔적.

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | "13번 … 진행합니다." "만들어"를 생성 지시로 안 보고 프롬프트까지만, 카드 빈칸 기준 4개 질문, 카드 안 씀 |
| 2 | PASS | "좋아"=제안값 수락, `acting`·`cut-card.md` 열림, 검사 OK 4,614자, 위험 목록, 카드 v2 `(제안값)`, "영상으로 보낼까요?", 생성 없음 |
| 3 | PASS | "18번 생성 보내기로 진행합니다." `[TOOL] generate_video(… get_cost=true) → 약 40 크레딧`과 `[TOOL] generate_video(… folder_id=fld-3-3, draft=true, resolution=480p, start_image=job-ff-3-3) → sim-job-3201`, 카드 [11]·`shot-list.md` 3-3 칸 기록(diff) |

## 검사기
turn2: `--kind video --refs 2 --seconds 8 --must-include(girl·light)` → `OK — video 프롬프트 4614자, 걸린 항목 없음`

## 추가 발견
- t3 요약 줄에 job ID가 "`sim-job-`"로 잘림(도구 줄에는 `sim-job-3201`).
- 카드 [8] 고정 설명문을 문장 대신 "CH-002 WARDROBE · LC-001-V1 LIGHT LOCK" 라벨로 바꿈, [5]에 영어 `the screen-right hand, nearer the sign`을 한글 카드에 섞음(`kit/skills/production-session/cut-card.md`).

## 키트 결함
없음

## 총평
세 단계 모두 규칙대로이고 핵심 규칙(사건 수, 검사, 초안, 보내기)이 통합 뒤에도 유지됐다.
