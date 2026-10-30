# real14-C20 장소 상태판: 형광등 켜기 (2턴) — PASS 2 / 부분 0 / FAIL 0 (real13: PASS 1 / 부분 1 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | 첫 줄 "8번 장소 고치기로 진행합니다." `location.md`+`location-edit.md`. 형광등 켜기와 해 진 직후를 두 변경으로 보고 2단계로 나눔(형광등 먼저), "1단계 결과는 아직 '해 진 직후'가 아니라 '석양 속에서 형광등만 켜진' 상태", 빛이 바뀌므로 LIGHT LOCK을 따로 기록. 질문 3개(나누기 / 형광등 위치·새 LIGHT LOCK / 번짐). 프롬프트·생성 없음 |
| 2 | PASS | 표준 LOCKED EDIT 여는 문장. CHANGE에 STATE 공식 그대로: "This is the same object in the same position with one state change only: the tube is off becomes the tube is lit. Preserve its shape, dimensions, material, orientation and surroundings." 형광등 번짐 방지 `lit but does NOT glow: no halo, no bloom, no light spilling onto the road or the persimmon tree`. PRESERVE에 해(석양)는 남기고 켜지는 형광등만 CHANGE. 장소 재묘사 없음. 블록 밖 LIGHT LOCK "전 → 후". registry `초안(제안값)` 기록(diff). 위험 4줄, "이대로 보낼까요?" |

검사기: `python3 kit/skills/higgsfield-generation/check_prompt.py --kind image C20t2_1.txt --refs 1` → `OK — image 프롬프트 1733자, 걸린 항목 없음`

real13 감점 해소: STATE 공식 누락 — 해소(`location-edit.md` Template 1에 "for a location edit, the formula replaces the generic CHANGE sentence" 한 구절이 들어간 효과).

추가 발견: 없음.
키트 결함: 없음.

총평: 나누기·LIGHT LOCK·STATE 공식이 모두 맞아 2턴 PASS.
