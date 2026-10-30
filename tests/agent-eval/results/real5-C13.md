# real5-C13 "3-1의 색감과 질감으로 3-5 퍼스트 프레임" (2턴) — PASS 2 / 부분 0 / FAIL 0 (real4: PASS 1 / 부분 1 → 개선)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | image-prompt SKILL + first-frame.md + production-session SKILL + ok-reuse.md, 3-1 시작 이미지 카드. "3-1 프롬프트에는 색·질감 문장이 없습니다 → 문장을 지어내지 않고 이미지를 색 참조로, 권한은 colour, grade, contrast and texture만". 7항목(틀 2 / 카메라 / 범위·인원 / 손 / 가방 내부 / 경첩·열린 모양 / 3-4 이음새) |
| 2 | PASS | 참조 4 = 태그 4, `<<<ok_3_1_start>>> controls only colour, grade, contrast and texture. Never take its subjects, composition, people or light direction.` + DO NOT TRANSFER. **`Real material truth` 등 새 질감 문장 없음**(real4 감점 해소; first-frame.md:37 반영). PROP 고정문 + `Except: the bag is open`, 의상·LIGHT LOCK 글자 그대로, 손은 screen 쪽 + 가방 손잡이, `Exactly one person`. 카드 3-5 v0. 생성 안 함 |

검사기: `--kind image --refs 4 --must-include bag+light`: `OK — image 프롬프트 2808자, 걸린 항목 없음`

추가 발견: 참조 태그 이름 `ok_3_1_start`는 플레이어가 지음(ok-reuse.md 권한 문장 표는 `<<<OK>>>` 자리표시만 있음). 이름에 컷 번호가 들어가 ok-reuse §3-6과 살짝 어긋나지만 OK 카드의 원래 요소 이름(`ff_3-1_v2`)도 같음.

키트 결함: 없음(경미: ok-reuse.md 권한 문장 표에 "태그는 OK 카드의 요소 이름" 한 구절이 있으면 이름이 흔들리지 않음).

총평: real4의 질감 문장 창작 감점 해소.

G1: 모든 턴 tools가 Bash/Write/Edit/Grep뿐, `mcp__` 호출 없음, `generate_*` 없음.
