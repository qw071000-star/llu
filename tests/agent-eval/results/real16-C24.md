# real16-C24 실사 영상, 연기를 새로 (3-2, OK를 가져오지 않음) (2턴) — PASS 12 / 부분 1 / FAIL 0

> 채점: tests/agent-eval/grader-rules.md. 출력 `runs-real16/C24/out/turn*.md`, 메타 `turn*.meta.json`, 정본 diff, 기대 `scenarios.md`. G1: 모든 턴에서 `mcp__` 도구 호출 없음, RUN 밖 파일 읽기 없음, 시킨 적 없는 생성 없음(확인함).

## 턴별 판정

| 턴 | 항목 | 판정 | 근거 |
|---|---|---|---|
| 1 | 첫 줄·작업 번호 | PASS | `13번 실사·인물 영상으로 진행합니다.` |
| 1 | 읽기: video-prompt+live-action만, acting·ok-reuse 안 염 | PASS | 1턴 reads에 acting 없음; `연기 문서(acting)는 프롬프트를 쓰는 턴에 엽니다` |
| 1 | 다른 컷 접근 | PASS | 3-2 카드·3-2 핸드오프·3-2 시작 이미지 카드만. 3-1 OK 문장 미사용 |
| 1 | 카드 빈칸을 제안값과 한 번에 묻기 | PASS | 6개 항목: 동작 기준 충돌, 사건·끝 상태, 타이밍·대사, 시선, 연기 범위(절제), 다음 컷 이음새 |
| 1 | 카드 [1]과 사용자 말 충돌 먼저 짚기 | PASS | `카드 [1]과 이음새 점검은 "3-1과 같은 동작"인데 말씀은 "연기를 새로"입니다` |
| 1 | 렌즈 안 묻기·카드와 시작 이미지 mm 불일치 처리 | PASS | `카드에는 35°로 적혀 있지만 시작 이미지는 75mm(약 32°)입니다. 시작 이미지가 이기므로 32°로` |
| 2 | acting 열기(프롬프트 쓰는 턴) | PASS | meta skills `['acting']`; `연기 문서와 카드 형식을 엽니다` |
| 2 | 15블록 순서·고정 문장 글자 그대로 | PASS | 블록 15개 순서대로. WARDROBE·가방 문장·LIGHT LOCK must-include 통과, 목소리 `A ten-year-old girl's clear, slightly hoarse voice, quiet and careful.`, 할아버지 입 잠금 `does not say a single word: no attempt to speak, no parted lips, no mouthing.` |
| 2 | CHARACTER_ACTING: 목표·손의 일·몸·눈·양 끝 failed take·레지스터 | PASS | `wants her grandfather to hear …`, `does not startle; it simply stops`, `a trembling voice or tears = failed take, a flat voice … = failed take`; 울음 없음(§5) |
| 2 | 사건 수 1~3 | PASS | 손녀 3개(대사·고개 돌림·한 걸음), 할아버지 사건 없음 |
| 2 | G7 검사: 보인 프롬프트 = 검사한 프롬프트, WARN 사유 | 부분 | 검사는 3회 돌렸으나 `프롬프트는 점검 뒤에 목소리 파일 문장 하나를 지웠습니다 … 이 수정 뒤에는 점검을 다시 돌리지 않았고`. WARN 사유에 쓴 `6,344자`는 보인 본문과 다름(실측 6305자). 길이 WARN 자체는 이유 있음(2인·참조 4, −347자 시도) |
| 2 | 카드 기록 `(제안값)`·3-1 OK 안 가져옴 | PASS | diff [1][4][5][6] 채움, `가져온 OK: 없음` |
| 2 | G1 생성 통제 | PASS | `"영상으로 만들어"라고 해 주세요. "그대로"나 "좋아"는 보내라는 말로 받지 않습니다` |

## 검사기 결과

- `python3 kit/skills/higgsfield-generation/check_prompt.py --kind video --refs 4 --seconds 8 --must-include grandpa+girl+bag+light C24_turn2_b1.txt`
  - 결과: `WARN  길이 6305자. 5,500자 이하가 안전했다 … — FAIL 0 · WARN 1 · 6305자`

## 추가 발견

- `[OPTICS]`의 `the camera is physically far away`(live-action.md 망원 문장)와 카드의 가까운 거리감이 충돌하지는 않으나, `REQUIRED`의 `Exactly 2 people, the old man in his seat and the bag closed on his lap.` 문장이 어색하다(사람 수와 가방을 한 문장에 섞음).
- 할아버지 연기에 `settles once`(손가락 한 번)가 있는데 `[PHYSICS]`는 `The old man's body does not move`라고 써서 약한 모순.

## 키트 결함

- `kit/instructions.md:47` 검사 줄에 "프롬프트를 고치면 검사를 다시 돌린다"가 없다 → 검사 뒤 문장 삭제가 허용되는 것처럼 읽힘. 수정: `After any edit to the prompt text, run the check again; show only the checked text.`
- `kit/skills/video-prompt/live-action.md:31` How to trim: WARN 사유의 숫자는 보이는 본문의 글자 수여야 한다는 문장이 없음. 수정: `Quote the final length of the text you show.`

## 총평

연기 새로 쓰기·OK 미가져오기·acting 시점 모두 규칙대로. 단 검사 뒤 문장을 지우고 재검사하지 않은 점만 흠.
