# real16-C37 고해상도 ("1080p로") (1턴) — PASS 6 / 부분 0 / FAIL 0

> 채점: tests/agent-eval/grader-rules.md. 출력 `runs-real16/C37/out/turn*.md`, 메타 `turn*.meta.json`, 정본 diff, 기대 `scenarios.md`. G1: 모든 턴에서 `mcp__` 도구 호출 없음, RUN 밖 파일 읽기 없음, 시킨 적 없는 생성 없음(확인함).

## 턴별 판정

| 턴 | 항목 | 판정 | 근거 |
|---|---|---|---|
| 1 | 첫 줄·작업 번호 | PASS | `17번 고해상도로 진행합니다.` |
| 1 | rerender.md 경로: draft_job_id로 같은 테이크 1080p, 프롬프트 새로 안 씀 | PASS | `새로 생성하지 않습니다 … draft_job_id로 같은 테이크를 1080p로 올립니다. 프롬프트는 쓰지 않고` |
| 1 | OK 대장의 draft 예·만료일 읽고 기한 알림, draft였는지 사용자에게 안 물음 | PASS | `만료일이 2026-10-31이라 내일까지입니다`; 질문에 draft 여부 없음 |
| 1 | 견적 조회·근거와 함께 알림(없으면 알 수 없음) | PASS | `[TOOL] get_cost(generate_video, draft_job_id=job-v-2-1, 1080p, Seedance 2.5, 8초)` → `견적: 알 수 없음. sim/higgsfield.md에 1080p 견적이 없고` |
| 1 | 보내기 전 확인 받기("뽑아줘"는 생성 지시지만 비용 확인), 생성 안 함 | PASS | `질문 1개: 견적 없이 1080p 업스케일을 지금 보낼까요?`; generate [TOOL] 없음 |
| 1 | 읽기 | PASS | rerender.md + shot-list/ok-cuts/decisions. higgsfield-generation은 grep으로 draft·get_cost 줄만 확인. video-prompt SKILL.md는 안 염(rerender.md가 자급자족) |

## 검사기 결과

- 프롬프트 코드블록 없음(검사할 것 없음).

## 추가 발견

- 480p 8초 약 40 크레딧(sim의 get_cost 줄)을 1080p 값이 아니라는 단서와 함께 인용 — 정직한 처리.

## 키트 결함

- 결함 없음. rerender.md 첫 줄들(`Before sending: get the 1080p quote with [TOOL] get_cost`)이 명확했다.

## 총평

draft 경로·견적 불명 처리·보내기 전 확인 모두 정확.
