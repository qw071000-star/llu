# real14-C31 장소 시간대 바꾸기 — "밤으로, 형광등 켜진 걸로" (2턴) — PASS 2 / 부분 0 / FAIL 0 (real13: PASS 1 / 부분 1 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | 첫 줄 "8번 장소 고치기로 진행합니다." `location.md`·`location-edit.md`. "시간대와 조명 켜기는 따로 할 수 있다"며 두 번으로 나눔(밤 먼저), "1단계 결과는 아직 요청하신 상태가 아닙니다(해가 빠지고 형광등은 꺼진 채라 매우 어두울 것, 추정)". 이 뷰의 PALETTE·LIGHT LOCK이 바뀌어 STATE로 따로 기록. 형광등 위치는 대장에 없다고 밝히고 제안값. 질문 4개, 프롬프트·생성 없음. 다만 새 LIGHT LOCK 문장을 화면 쪽으로 미리 적지는 않고 2단계 질문(3번)에 위치만 제안("정류장 중앙, 벤치 바로 위") |
| 2 | PASS | "그대로"를 수락으로 받아 1단계(밤) LOCKED EDIT. 표준 여는 문장. CHANGE에서 해와 하늘만 바꾸고 부모 LIGHT LOCK은 PRESERVE에 안 둠(`location-edit.md` Rules), 켜지 않는 형광등은 `stays OFF`. 해 질 녘 문장 없음. 블록 밖 "전 → 후" 3줄, 위험 4개, 재고지 "2단계(형광등 켜기)는 1단계 승인 뒤". registry `초안(제안값)` 기록(diff). 생성 안 함, "1k로 보낼까요?" |

검사기: `python3 kit/skills/higgsfield-generation/check_prompt.py --kind image C31t2_1.txt --refs 1` → `WARN  인물이 있는 프롬프트에서 좌우를 썼는데 좌표 문장이 없다 … — FAIL 0 · WARN 1 · 1595자` → 검사기 오탐: 프롬프트에 사람이 없다. `lens character`의 `character`를 인물로 센 것(`check_prompt.py:51`). 플레이어도 "사람이 없어 그대로 둠"이라 이유를 적음.

real13 감점 해소: 질문 턴 첫 줄 누락 — 해소.

추가 발견: 프롬프트의 `No moon, no stars, no new light sources of any kind`는 2단계(형광등 켜기)와 충돌하지 않도록 1단계 한정임을 답에서 알림(좋음).

키트 결함: `kit/skills/higgsfield-generation/check_prompt.py:51` — 사람 판별 정규식의 `character`가 `lens character`·`character of the light` 같은 말에도 걸린다 → `\bcharacter\b`를 빼거나 `character sheet|\[PERSON\]`로 좁힌다.

총평: 시간대·조명 분리와 LIGHT LOCK 처리가 맞고 real13의 첫 줄 감점이 해소돼 PASS 2.
