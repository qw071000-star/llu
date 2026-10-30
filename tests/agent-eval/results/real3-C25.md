# real3-C25 — 같은 쪽 클로즈업 (거울 문장 조건)
| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | reads: image-prompt SKILL·location.md·location-view.md(+대장·decisions). 같은 쪽 다가가기로 규정("반대 방향이 아닙니다 … 좌우와 빛 쪽은 부모와 같습니다"). 질문 4개(높이·렌즈·랜드마크·표지판 디자인) 한 묶음, 표지판 위치 오른쪽 중앙·절반 점유 반영. 생성 없음 |
| 2 | PASS | `Do not inherit its camera angle…` 있음. `Move in from the same side and along the same line of sight; no reverse angle and no view from behind.` 있음, `newly observed direction … mirror` 없음(0건). `text not legible`. 랜드마크: 지붕 모서리·벽·흐린 감나무 가지. `In this view the shelter wall is at screen left and the timetable sign is at screen right.` 뒤 LIGHT LOCK 글자 그대로. 부모 `<<<loc_busstop_road_v1>>>` |
검사기(채점자, --kind image --refs 1 --must-include light.lines): `OK — image 프롬프트 2835자, 걸린 항목 없음`
지난 회차 대비: PASS 2 유지. real2의 "같은 문장 안 shift toward screen right 충돌"은 사라짐.
추가 발견: 없음.
키트 결함: 없음.
총평: PASS 2 / 부분 0 / FAIL 0
