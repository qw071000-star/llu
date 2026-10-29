# real9-C20 장소 상태판: 형광등 켜기 (2턴) — PASS 2 / 부분 0 / FAIL 0 (real8: PASS 2 / 부분 0 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `image-prompt` SKILL + `location.md` + `location-edit.md` + OK 대장 LC-001-V1 카드. 계보 STATE, 부모 `job-lc001v1`. "광원 켜기와 시간대는 떼어도 성립해서 한 생성에 한 가지만 바꾸는 규칙에 걸립니다 … 먼저 형광등 켜기, 그다음 해 지우기"로 둘로 나눔, 1단계 결과는 아직 "해 진 직후"가 아니라고 알림. 형광등 위치(대장에 없어 벤치 위 가정) / 번지지 않는 켠 모양 / 2단계 "해 지고 난 직후" 값을 제안값으로, LIGHT LOCK이 `The sun has set; the shelter's single fluorescent tube … is the only key.`로 바뀐다는 점까지 알림. 프롬프트·생성 없음 |
| 2 | PASS | 1턴 기대 적용: 형광등만 먼저. LOCKED EDIT 표준 여는 문장 `Edit <<<loc_busstop_road_v1>>> WITHOUT reframing: … zero reframing …`, STATE 공식 `This is the same object in the same position with one state change only: switched off becomes switched on.`, `It is lit but does NOT glow: no halo, no bloom, no light spilling onto the road, the persimmon tree or the paddies.`, PRESERVE EXACTLY(카메라, 건축, 이름 없는 물체, 기존 해 빛 — 부모 LIGHT LOCK에서 "형광등 꺼짐" 부분만 뺌), `ONLY CHANGE: the fluorescent tube`. 바뀐 값 "꺼짐 → 켜짐"을 블록 밖에 한 줄, 위험 7개(마지막은 "추정": 부모 사진에 형광등이 보이는지 모름 → 안 보이면 ADD 공식으로). 대장 LC-001에 `초안(제안값)` 기록(diff 확인), 생성 안 함 |

검사기: `check_prompt.py --kind image --refs 1` → `OK — image 프롬프트 1649자, 걸린 항목 없음`
추가 발견: PRESERVE 첫 줄에 건축을 길게 열거("The architecture: the concrete shelter … harvested paddies and low hills behind")한 것은 `location-edit.md` "장소를 다시 묘사하지 않는다"와 살짝 긴장하나, `SKILL.md` §3 PRESERVE가 건축 보존을 요구하는 범위로 보여 허용. 화면 방향 표기(`screen RIGHT`/`screen LEFT`)는 맞음.
키트 결함: 없음.
총평: real8과 같은 PASS 2 수준. G1: mcp__ 없음, 생성 없음.
