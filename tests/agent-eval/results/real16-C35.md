# real16-C35 승인 영상 속도 ("너무 빨라") (2턴) — PASS 9 / 부분 0 / FAIL 0

> 채점: tests/agent-eval/grader-rules.md. 출력 `runs-real16/C35/out/turn*.md`, 메타 `turn*.meta.json`, 정본 diff, 기대 `scenarios.md`. G1: 모든 턴에서 `mcp__` 도구 호출 없음, RUN 밖 파일 읽기 없음, 시킨 적 없는 생성 없음(확인함).

## 턴별 판정

| 턴 | 항목 | 판정 | 근거 |
|---|---|---|---|
| 1 | 첫 줄·작업 번호 | PASS | `15번 영상 결과 고치기로 진행합니다.` |
| 1 | 모호한 말 → §0 표의 사람 동작 속도 줄 사용, fixes.md 안 염 | PASS | reads: video-prompt/SKILL.md만. `엄지 구간이 이미 4초라 더 늘릴 방법: 제안 — 시작을 앞당겨 0:02–0:08(6초)로 하고 길이 8초는 유지` |
| 1 | 기존 구간 초 세기·4초 이상이면 제안으로 묻기 | PASS | `엄지 구간이 이미 4초` → 시작 앞당김 vs 영상 길이 늘리기 두 선택 |
| 1 | 승인 컷 → 새 take로 대체할지 질문 | PASS | `2. 승인된 컷이라 새 take로 교체할지: 제안 — 새 take로 만들고, 기존 OK는 새 결과가 승인될 때까지 유지` |
| 1 | 질문 한 묶음·생성 없음 | PASS | 질문 3개, `아직 아무것도 만들거나 고치지 않았습니다` |
| 2 | 해당 줄만 `전 → 후`, 사건 수 그대로, 초 표시 | PASS | `0:00–0:04 … 0:04–0:08 …(4초)` → `0:02–0:08 — his thumbs move once … taking the full 6 seconds.` |
| 2 | 실패 문장 `finished in under N−1 seconds = failed take` | PASS | `The thumb movement finished in under 5 seconds = failed take.` |
| 2 | 전체 프롬프트에 대해 G7 검사 | PASS | check_prompt 실행(--refs 3 --seconds 8). 재구성한 전체 프롬프트를 내가 다시 검사: OK |
| 2 | G1 생성 통제 | PASS | `"보내"라고 해 주시면 보내겠습니다.` |

## 검사기 결과

- `python3 kit/skills/higgsfield-generation/check_prompt.py --kind video --refs 3 --seconds 8 --must-include grandpa+bag+light C35_full.txt` (OK 카드 프롬프트에 ACTION_TIMING 변경을 적용해 재구성)
  - 결과: `OK — video 프롬프트 4201자, 걸린 항목 없음`

## 추가 발견

- 1턴 도입 문장 `캔버스 파일부터 읽겠습니다.`의 "캔버스"는 키트에 없는 말. 의미 없는 서술.
- 깜빡임을 0:00–0:02로 줄이면서 `one slow blink`이 같은 구간에 남음 — 허용.

## 키트 결함

- 결함 없음. §0 표의 속도 줄이 정확해서 한 번에 맞게 썼다(`kit/skills/video-prompt/SKILL.md:~40`).

## 총평

속도 표 적용·4초 이상일 때 제안 질문·승인 컷 새 take 질문 모두 규칙대로.
