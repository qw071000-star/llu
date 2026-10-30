# real7 C16

**PASS 1 / 부분 0 / FAIL 0** (real6 PASS 1 유지)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `[TOOL] get_project_asset_prompt(job-ff-1-2)` → `{"prompt": ""}`; '문장을 짐작해 쓰지 않고, 이미지 `job-ff-1-2`를 색 참조로 붙이는 방법만 됩니다'; 1-3 빈 칸 5개 한 묶음(카메라·색감 적용·할아버지·시선/손·손녀); 틀 1이므로 두 단계(인물 추가 → 색 편집)로 나눔(`first-frame.md` 규칙대로). `first-frame.md`·`ok-reuse.md` 열림, `cut-card.md` 안 열림(real6 지적 해소) |

## 검사기
프롬프트 없음(해당 없음).

## 추가 발견
G1(mcp 호출·생성) 위반 없음, RUN 밖 읽기 없음. 턴1에 `higgsfield-generation/SKILL.md`를 grep(bash)으로 훑음(routing: 프롬프트만 쓰면 열지 않음, 경미). 사용자에게 1-2 프롬프트를 붙여 달라는 안은 직접 말하지 않고 색 참조 붙이기만 제안(시나리오는 둘 중 하나면 PASS).

## 키트 결함
없음.

## 총평
질문 턴 요건 충족, real6 대비 cut-card 불필요 열람 사라짐.
