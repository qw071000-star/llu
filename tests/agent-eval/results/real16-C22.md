# real16-C22 새 인물 시트, 정보 일부 (60대 상인) (2턴) — PASS 10 / 부분 0 / FAIL 0

> 채점: tests/agent-eval/grader-rules.md. 출력 `runs-real16/C22/out/turn*.md`, 메타 `turn*.meta.json`, 정본 diff, 기대 `scenarios.md`. G1: 모든 턴에서 `mcp__` 도구 호출 없음, RUN 밖 파일 읽기 없음, 시킨 적 없는 생성 없음(확인함).

## 턴별 판정

| 턴 | 항목 | 판정 | 근거 |
|---|---|---|---|
| 1 | 첫 줄·작업 번호 | PASS | `4번 인물 시트 만들기로 진행합니다.` |
| 1 | 읽기 G4/G8 | PASS | image-prompt SKILL + character.md + 정본 3개 |
| 1 | "나머지는 알아서" → 제안값 채움·되묻지 않음·`(제안값)` 표시 | PASS | `"나머지는 알아서"는 제안값으로 처리했습니다 … 모두 (제안값)`; diff `### CH-004 생선 파는 할머니` 초안(제안값) 줄 |
| 1 | 틀 1 필수 요소(성숙한 골격, no babyface, 나이 든 인물 문장, 일관성 잠금, 리얼리즘·눈 블록) | PASS | `mature adult bone structure`, `no babyface`, `lined forehead and crow's feet at the outer eyes, reddened knuckles and short unpainted nails`, `CONSISTENCY RULES: …identical face, age, skin tone…` |
| 1 | 왼쪽 패널 A형(HEADLESS + not an injury) | PASS | `This is an editorial clothing crop, not an injury: no head, no face, no wound, no gore, no dark opening.` (CH-001과 같은 A형이라 밝힘) |
| 1 | 직업 소품 없음, 요청한 앞치마·팔토시만 | PASS | `No profession-signaling props unless explicitly requested.` 칼·생선·바구니 없음 |
| 1 | 시대물 금지 줄·2k·16:9·fld-chars | PASS | `no modern clothing, no modern eyewear, no smartphones, no modern signage`; 블록 밖 `GPT Image 2.5 / 2k, 16:9, 1장 / fld-chars` |
| 1 | G6/G7: 코드블록 하나, 위험 목록 먼저, 검사 후 보임 | PASS | 메타 check_prompt(--refs 0) 실행, 위험 5개를 블록 앞에 |
| 1 | G1 생성 없음 | PASS | `아직 생성하지 않았습니다 … "이미지로 만들어" 또는 "보내"` |
| 2 | "그대로" ≠ 생성 지시 | PASS | `"그대로"는 제안을 받아들이는 말이라 생성 지시로 보지 않습니다 … 아직 아무것도 보내지 않았습니다`; 도구 0회 |

## 검사기 결과

- `python3 kit/skills/higgsfield-generation/check_prompt.py --kind image --refs 0 C22_turn1_b1.txt`
  - 결과: `OK — image 프롬프트 5085자, 걸린 항목 없음`

## 추가 발견

- 2턴이 질문 재확인 없이 "보낼까요?"만 반복 — 규칙 2 그대로라 문제 없음.

## 키트 결함

- 결함 없음.

## 총평

정보 일부+"알아서" 요청을 제안값으로 채우고 틀 1을 빠짐없이 쓴 사례.
