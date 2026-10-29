# real13-C27 나이 바꾸기 — "50대 때 모습도 … 시트로" (2턴) — PASS 2 / 부분 0 / FAIL 0 (real12-recheck: PASS 1 / 부분 1 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | 확인 질문 없이 첫 줄 "5번 인물 시트 고치기로 진행합니다."(real12의 불필요한 확인이 사라짐). `image-prompt` SKILL + `character-edit.md`만 열었다. 기준은 CH-001 시트 `job-ch001`("새로 만들면 다른 사람이 되므로 … 고칩니다"). 새 상태 요소 `char_grandpa_fifties_v1` 제안, 나이 표지(주름·턱선·눈 밑·머리색·어깨·손)를 제안값으로, 얼굴 뼈대는 "묘사하지 않습니다". 옷은 그대로(3번)로 한 생성 한 가지를 설명. 2k를 "기본값으로 씀"에 적음. 질문 3개 한 묶음, 대장 `초안(제안값)` 줄에 기록 |
| 2 | PASS | `Edit reference image 1: age the same person to about fifty-five …` 틀 2 전문, `CHANGE — AGE`, `IDENTITY BONES` 줄, HEADLESS `not an injury`, `OUTFIT: the exact same clothes in every panel`, 젊게 쪽 마지막 줄(`no babyface, no beauty filter`). 얼굴 새 묘사 없음. 사람이 있는 프롬프트라 `LEFT and RIGHT are SCREEN directions …` 줄도 넣음(지침 6번). 블록 밖에 모델·2k·16:9·폴더와 변경값 "전 → 후" 5줄, 위험 4줄(추정 표시). 생성하지 않고 "보낼까요?" |

검사기: `--kind image C27t2_1.txt --refs 1` → `OK — image 프롬프트 1586자, 걸린 항목 없음`

추가 발견
- "전 → 후"의 `나이: about seventy → about fifty-five`는 대장 IDENTITY(`early seventies`)와 글자가 다르다. 경미.
- 머리색 변경을 나이 표지 안에 넣었다(`character-edit.md:184` "나이 표지는 한 변경"과 일치).

키트 결함: 없음.

총평: real12의 불필요한 확인 질문이 해결됐고(`tasks.md:8` 한 행 일치 규칙이 작동), 틀 2와 사람 줄 규칙 모두 맞다.
