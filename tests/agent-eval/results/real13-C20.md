# real13-C20 장소 상태판: 형광등 켜기 (2턴) — PASS 1 / 부분 1 / FAIL 0 (real11: PASS 2 / 부분 0 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | "8번 장소 고치기로 진행합니다." `location.md`+`location-edit.md`. 형광등 켜기와 해 진 직후는 두 변경이므로 2단계로 나누자고 제안(형광등 먼저, 1단계 결과는 아직 "해 진 직후"가 아님을 한 줄 알림), 빛이 바뀌므로 LIGHT LOCK 새로 쓴다고 알림, 형광등 위치·번짐 범위 질문. 프롬프트·생성 없음 |
| 2 | 부분 | 표준 LOCKED EDIT 여는 문장, CHANGE/PRESERVE EXACTLY/ONLY CHANGE 항목 일치, `lit but does NOT glow: no halo, no bloom, no light spilling onto the roof, the road or the ground`, 장소 재묘사 없음, 부모 LIGHT LOCK의 형광등 꺼짐을 PRESERVE에서 빼고 해만 남김, 블록 밖 LIGHT LOCK "전 → 후", registry 초안 기록. 감점: `location-edit.md` Template 1 STATE 공식("This is the same object in the same position with one state change only: [old] becomes [new]. Preserve its shape, dimensions, material, orientation and surroundings.")이 없고 `SKILL.md` §3의 일반 CHANGE 형식("Change the tube from off to on. Keep its position… locked")만 씀 |

검사기: `--kind image --refs 1` → `OK — image 프롬프트 1492자, 걸린 항목 없음`
추가 발견: 없음.
키트 결함: `kit/skills/image-prompt/SKILL.md` §3 CHANGE 줄(`Change [현재 상태] to [새 상태]. Keep its … locked.`)과 `location-edit.md` Template 1의 STATE/ROTATE/ADD/REMOVE 공식이 같은 칸에 대한 두 가지 문형이라 플레이어가 앞의 것을 고름. `location-edit.md:Rules/Template 1` 위에 "In a location edit, replace the §3 CHANGE sentence with the formula below" 추가, 또는 `SKILL.md` §3 CHANGE 줄에서 "location edits: see location-edit.md Template 1" 안내. (공식이 두 파일로 나뉜 통합의 부작용)
총평: 나누기·LIGHT LOCK 처리는 정확, STATE 공식 누락으로 t2 부분.
