# real4-C05 장소 반대 방향 뷰 (2턴) — PASS 2 / 부분 0 / FAIL 0 (real3: PASS 2)
| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | image-prompt SKILL+location.md+location-view.md. 부모 `job-lc001v1`. 5항목(카메라 위치·높이 / 샷 크기 / 랜드마크 3개 — 시간표 화면 왼쪽·감나무 화면 오른쪽 / 길 건너 종점 / 이 뷰의 LIGHT LOCK 화면 오른쪽). "부모에서 표지판 오른쪽→반대 뷰에서 좌우 뒤집힘" 짚음 |
| 2 | PASS | `Do not inherit its camera angle, framing or composition.`, `WITHOUT reframing` 없음, CAMERA를 원본 카메라와의 관계("looking back … toward the original camera position")로, `not a horizontal mirror`, MASTER GEOMETRY `(as seen from across the road …)`+`Except:`+`In this view … sign at screen LEFT … tree at screen RIGHT`, LIGHT LOCK `from screen right, the persimmon-tree side`. 동서남북 없음(grep 0). 태그 1=참조 1. 검사 실행 |
검사기(`--kind image --refs 1`): `OK — image 프롬프트 2739자, 걸린 항목 없음`
추가 발견: 2턴 끝에 "좌면 0.45m를 원하셨다면"을 다시 물음(이미 정한 "벤치 높이" 해석 확인, 경미).
키트 결함: 없음.
총평: real3과 같은 PASS 2.
