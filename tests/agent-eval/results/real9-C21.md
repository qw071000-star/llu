# real9-C21 장소 시대 교체 (한 생성에 한 층) (2턴) — PASS 1 / 부분 1 / FAIL 0 (real8: PASS 0 / 부분 2 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `image-prompt` SKILL + `location.md` + `location-edit.md`(틀 2) + OK 대장 LC-001-V1 카드. 정본 충돌: "`decisions.md`(1990년대 초, 현대 물건 금지)는 그대로 둠 … 이 에셋만인지 작품 전체인지 먼저 정해야" + 변형 `LC-001-V1-2020s`(STATE, 부모 `job-lc001v1`)로 따로 기록 제안. "한 생성에 한 층씩 5단계": ① 표지판 판(IDENTITY AND TEXT) → ② 지붕·바닥·도로 포장(STRUCTURAL SURFACES) → ③ 벤치·기둥·형광등(FIXTURES) → ④ 조명 → ⑤ 이미지 마감(IMAGE CHARACTER). 층 목록 순서와 일치, 한 단계에 한 층(real8의 층 혼합 해소). 층별 2020년대 대응물 제안, "이번에 보낼 프롬프트는 ① 하나". 프롬프트·생성 없음 |
| 2 | 부분 | 층 문법은 맞음: `this step changes only its IDENTITY AND TEXT layer.`, 요소 하나(표지판 판)의 목표 시대 대응물(`2020s bus-stop sign plate of reflective printed sheeting … same position … same scale on the same pole`), `REMOVE:`(옛 판의 붓 자국·벗겨진 페인트), PRESERVE에 다른 층(지붕·벤치·단일 기둥·형광등·도로)과 `Every building volume and opening position`, `ONLY CHANGE: IDENTITY AND TEXT`, 기둥은 ③ 층이라 안 건드림(real8의 판/기둥 혼합 해소). 글자 정책 `text not legible`/`No legible text anywhere`. 감점: 맨 끝 시대 줄이 `at this step only the sign plate is 2020s, everything else stays early 1990s`이고 첫 줄도 `The early-1990s rural bus stop is turning into …` — 기대는 "`1990s` 시대 잠금이 남지 않는다(목표 시대 잠금)". 5단계 중 첫 단계의 중간 상태라 합리적이지만 기대와 어긋나 부분 처리. 키트가 중간 단계의 시대 줄을 안내하지 않음(아래 결함). 답 첫 줄에 "순서만 말씀하셨으므로 나머지 4개는 제안값으로 정했습니다"로 알림, 대장 LC-001에 `LC-001-V1-2020s` `초안(제안값)` 기록(diff 확인), 생성 안 함 |

검사기: `check_prompt.py --kind image --refs 1 --must-include light` → `OK — image 프롬프트 1527자, 걸린 항목 없음` (검사기는 시대 줄을 보지 않음)
추가 발견: PRESERVE에 LIGHT LOCK 문장 `Low dusk sun from screen left … tube is off`를 글자 그대로 둠(맞음, 이 단계는 빛을 안 바꿈). 1턴 대응물 표에서 "형광등 → 꺼진 LED"를 ③ 층에 둔 것은 FIXTURES 정의(벤치·기둥·가로등)와 맞음.
키트 결함: `kit/skills/image-prompt/location-edit.md:54,65` 틀 2는 첫 줄에 `[SOURCE ... ERA]`, 끝에 `[Era lock of the target scene]`만 두고, 여러 단계로 나눈 중간 단계에서 시대 줄을 어떻게 쓸지 안내가 없다. 고치기: 65줄 뒤에 "중간 단계: 이번 층만 목표 시대로 쓰고 나머지는 `unchanged from the parent image`로 쓴다. 원 시대 이름(`1990s`)은 되풀이하지 않는다. 마지막 층에서 목표 시대 잠금을 쓴다" 한 줄을 추가(또는 기대를 "중간 단계는 원 시대 문구 허용"으로 고침).
총평: real8의 층 혼합 두 건이 해소돼 PASS 1/부분 1로 개선. G1: mcp__ 없음, 생성 없음.
