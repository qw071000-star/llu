# real11-C51 "프롬프트 한국어로 줘" 3-3 퍼스트 프레임 (1턴) — PASS 0 / 부분 1 / FAIL 0 (real9: PASS 1 / 부분 0 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | 부분 | 맞은 것: `ok-cuts.md`의 3-3 시작 이미지 OK 카드로 번역("3-3 퍼스트 프레임은 이미 OK(`job-ff-3-3`, GPT Image 2.5 · 1k · 16:9, 2026-10-27)입니다. 아래 번역은 읽기용이고, 생성에는 영어 원문을 그대로 씁니다"), 카드·검사·생성 없음, 번역이 카드와 충실(50mm, 참조 권한, `시간표에 더 가까운 화면 오른쪽 손`, 광원 화면 왼쪽, 의상, `정확히 1명`). **감점:** `tasks.md` 23번 행("a translation is for reading, outside the code block")과 달리 한국어 번역 전체를 ` ```text ` 코드블록 안에 넣음 — 사용자가 번역을 생성용으로 붙여 넣을 수 있고, 코드블록은 영어 생성용이라는 약속(G6)이 깨짐. 번역에 쓰인 근거 카드 외에 컷 카드 3-3도 열어 [8]과 대조함(23번 행은 "that one OK card"만) |

## 검사기
코드블록이 번역(비프롬프트)이라 검사 대상이 아님. 형식상 돌려 본 결과(`--kind image --refs 2`): `OK — image 프롬프트 820자, 걸린 항목 없음` (참조 1로 돌리면 태그 수 불일치 FAIL — 번역을 프롬프트로 취급한 것의 부작용).

## 추가 발견
- G1 위반 없음. 영어 원문은 다시 보이지 않음(번역만) — 요청이 번역이므로 허용.
- 끝의 "다음에 쓸 수 있는 작업" 두 가지는 요청 밖 제안이지만 질문 한 묶음 안이라 경미.

## 키트 결함
- `kit/context/tasks.md:39`(23번 행) "a translation is for reading, outside the code block"가 표의 마지막 칸 끝에 묻혀 있다. 제안: 같은 문장을 `kit/instructions.md` Output의 "New prompt" 불릿에 한 줄 더 쓰거나 `kit/skills/production-session/ok-reuse.md` 맨 위에 "Translation: plain text, never a code block"을 넣는다.

## 총평
번역 자체는 충실했으나 코드블록에 넣어 "번역은 블록 밖" 규칙을 어겼다.
