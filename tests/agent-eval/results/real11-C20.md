# real11-C20 장소 상태판: 형광등 켜기 (2턴) — PASS 2 / 부분 0 / FAIL 0 (real9: PASS 2 / 부분 0 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `image-prompt` SKILL + `location.md` + `location-edit.md`. 계보 STATE, 참조 `loc_busstop_road_v1`. "형광등 켜기"와 "해 지고 난 직후"는 따로 뗄 수 있는 두 변경이라 2단계로 나누자고 하고 말씀하신 순서(형광등 먼저)를 제안. 새 LIGHT LOCK이 필요하다고 짚음. 형광등 위치·빛 모양·"직후" 구체값·이름/계보를 제안값으로 5개. 프롬프트·생성 없음 |
| 2 | PASS | LOCKED EDIT 표준 여는 문장(`… lens, framing … zero reframing …`), CHANGE / PRESERVE EXACTLY / ONLY CHANGE, STATE 공식 `one state change only: off becomes lit`, `lit but does NOT glow: no halo, no bloom, no light spilling onto the road, the timetable sign or the persimmon tree`. 장소를 다시 묘사하지 않음(PRESERVE에 이름만). 시간대 변경은 2단계로 남김. 대장 `초안(제안값)` 기록 |

검사기: `--kind image C20_t2 --refs 1` → `OK — image 프롬프트 1632자, 걸린 항목 없음`
추가 발견: 프롬프트가 원 LIGHT LOCK 문장 대신 PRESERVE 줄에 "Low dusk sun from screen left … stay exactly as they are"로 씀(새 LIGHT LOCK 초안은 대장에만 기록). 형광등 켜진 판의 최종 LIGHT LOCK은 생성 확정 후 대장에 확정해야 함.
키트 결함: 없음.
총평: real9와 같은 PASS 2.
