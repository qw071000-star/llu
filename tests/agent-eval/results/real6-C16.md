# real6 C16

**PASS 1 / 부분 0 / FAIL 0** (real5 PASS 1 유지)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `[TOOL] get_project_asset_prompt(job-ff-1-2)` → 빈 문자열; '색감 문장을 지어내지 않고 … 그 이미지를 색 참조로 붙이는 쪽'; 1-3 빈 칸 4개 한 묶음; 프롬프트·생성 없음. `first-frame.md`·`ok-reuse.md` 열림 |

## 검사기
프롬프트 없음(해당 없음).

## 추가 발견
G1(mcp 호출·생성) 위반 없음, RUN 밖 읽기 없음. 턴1에 `higgsfield-generation/SKILL.md` 제목만 grep(bash), `cut-card.md` 열람(질문 턴, 카드 쓰기 전). 답에는 영향 없음.

## 키트 결함
있음(경미): `production-session/SKILL.md:18`이 '카드가 없으면 … `cut-card.md` 틀로 초안'이라 질문 턴에도 cut-card를 열게 유도, `context/routing.md:48`은 '답을 적을 때'만 → 18줄 끝에 '(질문 턴에는 열지 않고 답을 적을 때 연다)' 추가.
