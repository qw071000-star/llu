# real6-C08 퍼스트 프레임, 정보 부족 3-4 (2턴) — PASS 2 / 부분 0 / FAIL 0 (real5: PASS 2)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | 3-4 카드 없음을 알리고 정본에서 구성. image-prompt SKILL + first-frame.md. 카메라 / 앉은 자리 / 시선 / 손·0:00 동작 4항목을 제안값+이유. 가방 닫힘·인원 1명·모델·`fld-3-4`는 "기본값으로 씀". 이웃 OK 카드는 first-frame 인물 자리 예외 범위 |
| 2 | PASS | `Edit <<<loc_busstop_road_v1>>> WITHOUT reframing`(틀 1), `LEFT and RIGHT are SCREEN directions …`, WARDROBE·PROP·LIGHT LOCK 글자 그대로, `Exactly one person is visible.`, 자리표시 태그 없음, 손은 `screen-right hand … rests on the bag's brass clasp`. 50mm 제안이 V1 35mm로 바뀐 것을 알림. 3-4 카드 v0 작성([4][5]에 값, 제안값 표시) |

검사기: `check_prompt --kind image --refs 3 --must-include grandpa+bag+light` → `OK — image 프롬프트 2068자, 걸린 항목 없음`
추가 발견: 1턴이 "컷 카메라가 확정 장소 뷰와 같은가"를 첫 질문으로 직접 묻지 않고 틀 2(50mm 미디엄)를 제안으로 내놓음. 질문 4번째 줄 "카메라"가 같은 역할을 해서 PASS로 침. must-ask.md "첫 질문" 문구를 그대로 따르지는 않음.
키트 결함: 없음.
총평: PASS 2 유지.
