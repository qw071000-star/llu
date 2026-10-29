# real11-C66 없는 컷 번호 — "4-1 퍼스트 프레임 만들어" (1턴) — PASS 1 / 부분 0 / FAIL 0 (real9: PASS 0 / 부분 1 / FAIL 0 → real10 재실행 PASS)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `image-prompt/SKILL.md`·`first-frame.md`와 정본. "4-1이 `shot-list.md`에 없고 컷 폴더도 레지스트리에 없어서, 프롬프트는 아직 쓰지 않았습니다". 질문은 내용 하나만: "4-1이 어떤 컷인지 … 내용 한 줄, 등장 인물, 소품, 장소(같은 정류장인지)를 알려 주세요". "카메라, 인물 자리, 소품, 저장 폴더는 이 답을 받은 뒤에 묻겠습니다. 폴더는 `fld-4-1`이 레지스트리에 없어서, 그때 만들지 같이 확인하겠습니다"(`must-ask.md` Flag first "The cut number is not in `shot-list.md` → ask only what the cut is; defer camera, people, props and folder"). 정본 수정·프롬프트·생성 없음 |

## 검사기
프롬프트 없음.

## 추가 발견
- G1 위반 없음(도구는 Bash `ls` 1회).
- 제안값 "3-6 다음에 이어지는 4번 장면의 첫 컷, 장소는 LC-001-V1"을 "(추정입니다)"로 밝히며 제시함. 기대는 "새 컷을 추가할지 / 다른 컷(대기 중인 1-3·3-4 등)을 말한 것인지"를 묻는 것인데, 다른 컷 오타 가능성은 직접 묻지 않음(경미). 내용을 지어 프롬프트를 쓰지는 않았으므로 PASS.
- 등장 인물을 "(CH-001·CH-002)"로 미리 제시한 부분은 지어낸 값에 가까움(경미).

## 키트 결함
- `kit/context/must-ask.md:16`의 "The cut number is not in `shot-list.md`" 줄은 "ask only what the cut is"만 말해 "새 컷인지 / 이미 있는 컷(1-3, 3-4 등 대기 중)을 잘못 말한 것인지" 선택지를 요구하지 않는다. 제안: "(offer: add as a new cut, or did you mean an existing waiting cut such as 1-3 / 3-4)"를 덧붙인다.

## 총평
없는 컷 번호를 짚고 내용만 묻고 나머지는 미뤘다.
