# real16-C06 새 소품 (할머니 사진 액자) (2턴) — PASS 7 / 부분 2 / FAIL 0

## 턴별 판정

| 턴 | 기대 | 판정 | 근거 |
|---|---|---|---|
| 1 | 첫 줄 | 부분 | "9번 소품 만들기·고치기로 진행합니다."가 맞지만 같은 문장이 1·3번째 줄에 두 번 나옴 |
| 1 | prop.md 열기, PR-002 후보, 시트 필요 여부 | PASS | reads image-prompt/SKILL.md·prop.md; "독립 에셋(`PR-002` 후보)"; "1. 시트 필요 여부: 제안 — 시트를 만든다" |
| 1 | 크기(cm+신체)·재질·사용 흔적·무게·나오면 안 되는 재질·상태·누가 드는지를 제안값·이유와 함께(7개) | PASS | "3. 크기: 약 13×18cm, 할아버지 손바닥 한 뼘", "4. 무게감", "5. 나오면 안 되는 것", "6. 상태 변화와 손" |
| 1 | shot-list 3-4 행은 고치지 않고 제안만 | PASS | "3-4 행은 이번에 고치지 않았습니다." (diff에 shot-list 없음) |
| 2 | 소품 틀: 회색 무배경, 손·사람 없음, `Avoid` 줄 | PASS | "isolated on a plain seamless light grey studio background… no hands…"; "Avoid: acrylic or thin metal frames, glossy new finish, any text…" |
| 2 | 에셋 대장 PR-002 기록(`(제안값)`), 틀 정리 | PASS | diff: `### PR-002 할머니 사진 액자` 표 + `초안(제안값)` (제목·표 행까지 추가 — prop.md의 "초안 줄만"보다 넓음) |
| 2 | 검사 후 표시 (G7), 생성 안 함 | PASS | Bash check_prompt --kind image tmp/pr002.txt --refs 0 --must-include tmp/must.txt; "이 프롬프트를 이미지로 보낼까요?" |
| 2 | G2 한국어 | 부분 | "Now the registry `초안(제안값)` line, then remove the tmp files." (영어); T1 "번쩅이는" 오타 |
| 전체 | G1·G9 | PASS | mcp 없음; 손은 "화면 오른쪽 손(시간표 쪽)" |

## 검사기 결과

- C06 t2 코드블록 1: `--kind image --refs 0`: OK — image 프롬프트 1071자, 걸린 항목 없음

## 추가 발견

- 소품 프롬프트에 사람이 없는데 `LEFT and RIGHT are SCREEN directions, never the character's own…`가 들어감(해가 없지만 불필요, instructions.md:27은 사람이 있는 프롬프트용).

## 키트 결함

- kit/context/tasks.md:8 — 도구 사이 영어 서술(C04 결함 2와 동일): 고침은 instructions.md:12 독립 문장.

## 총평

소품 질문·틀·대장 기록은 정확. 영어 한 줄·오타·첫 줄 중복으로 부분 2건.
