# real9-C05 장소 반대 방향 뷰 (2턴) — PASS 2 / 부분 0 / FAIL 0 (real8: PASS 1 / 부분 1 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `image-prompt` SKILL + `location.md` + `location-view.md` + OK 대장 `LC-001-V1` 카드. 부모 `LC-001-V1`(`job-lc001v1`). 카메라 위치 / 높이·샷 크기 / 남길 랜드마크 / 길 건너 종점 4항목을 제안값+이유로. "부모에서 감나무는 화면 왼쪽, 표지판은 오른쪽이라 좌우가 뒤집힘"을 알리고 새 LIGHT LOCK 초안 `Low dusk sun from screen right, the persimmon-tree side …`을 미리 보임. 프롬프트·생성 없음 |
| 2 | PASS | `Do not inherit its camera angle, framing or composition.` 있음, `WITHOUT reframing` 없음. 카메라를 원본과의 관계로: `looking back along the same central axis toward the original camera position across the road`(`reverse` 한 단어로 때우지 않음). `This is a newly observed opposite direction … not a horizontal mirror of the reference.` MASTER GEOMETRY에 `as seen from across the road, looking at the shelter's open front` + `Except:` 줄로 이 뷰 설명. `In this view the persimmon tree is at screen right and the timetable sign is at screen left. Low dusk sun from screen right, the persimmon-tree side, is the only key`. 동서남북 없음. "벤치 높이"를 앉은 눈높이 1.1m로 풀고 사용자에게 알림. 대장에 `LC-001-V2` 초안(제안값) 기록, 위험 5개, 생성 안 함 |

검사기: `check_prompt.py --kind image --refs 1` → `OK — image 프롬프트 2406자, 걸린 항목 없음`
추가 발견: 2턴에 `higgsfield-generation` SKILL을 열지 않음(real8의 부분 사유 해소). 대장 PALETTE·ERA LOCK·FINISH와 OK 카드 문장이 다름을 알리고 대장 문장 사용(지침 5번)을 밝힘 — 좋은 처리. "벤치 높이" 해석(1.1m)은 한 줄 알림이 있어 허용.
키트 결함: 없음.
총평: real8 부분이 해소돼 PASS 2. G1: mcp__ 없음, 생성 없음.
