# real14-C06 새 소품 (2턴) — PASS 2 / 부분 0 / FAIL 0 (real13: PASS 1 / 부분 1 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | 첫 줄 "9번 소품 만들기·고치기로 진행합니다." `image-prompt` SKILL + `prop.md`만 읽음. 7개 질문을 제안·이유와 함께 한 묶음으로: 시트 여부 / 재질·낡음 / 사진 속 모습 / 크기 "약 13×18cm, 할아버지 손바닥보다 약간 큼, 가방 폭 40cm의 절반 미만" / 무게 / 나오면 안 되는 것 / 상태·손 "화면 오른쪽 손(벤치 중앙 쪽)이 꺼냄". PR-002 매김. "기본값으로 씀: GPT Image 2.5 · 1k · 16:9 · 저장 `fld-props`". 도구 0 — 질문 턴에 registry·컷 카드 안 씀 |
| 2 | PASS | 소품 틀: 회색 무배경, `no hands, no living people`, `Avoid: plastic or metal modern frames, brand logos, text, legible writing, watermarks`, 크기 cm. 모드·참조 없음·모델·해상도·비율·폴더를 블록 밖에 한 줄씩. 위험 4줄, "이미지로 만들까요?" 대장 `PR-002` `초안(제안값)`+고정 설명문(제안값) 기록(diff). shot-list·연속성 표는 안 건드리고 3-4 변경은 핸드오프 [5]로 제안(prop.md Rules). 검사 후 `tmp/` 삭제 |

검사기: `python3 kit/skills/higgsfield-generation/check_prompt.py --kind image C06t2_1.txt --refs 0` → `OK — image 프롬프트 824자, 걸린 항목 없음`

real13 감점 해소: ① 첫 줄 누락 — 해소. ② 질문 턴(1턴)에 registry 임시 행 기록 — 해소(1턴 도구 0, 대장 변경은 2턴 diff 한 곳뿐).

추가 발견
- 프롬프트에 소품 틀에 없는 `LEFT and RIGHT are SCREEN directions…` 문장이 들어감. 사람이 없는 프롬프트라 불필요하지만 해는 없다. `holding… face not sharply legible`와 `Sharp focus throughout`이 살짝 부딪침.
- 도구 사이에 영어 한 줄("Check passed. I'll record the answers…") 노출.

키트 결함: C02와 같은 `kit/instructions.md:12`(도구 사이 글 한국어).

총평: real13의 두 감점이 모두 해소돼 2턴 PASS.
