# real2-C08 퍼스트 프레임, 정보 부족 (2턴) — PASS 2 / 부분 0 / FAIL 0 (지난: PASS 2)
| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | 시작 보고 세 줄. 컷 카드 3-4 없음 → 정본에서 구성. `image-prompt/SKILL.md`+`first-frame.md`+3-1 시작 이미지 OK 카드(자리 맞춤, first-frame 예외). 5항목: 카메라(LC-001-V1과 같은가→틀 1/2), 시작 위치(3-1과 같게), 동작·손(화면 오른쪽 손, 시간표 쪽), 시선, 인원. 모델·해상도·폴더 "기본값으로 씀", 가방 닫힘은 제시만. |
| 2 | PASS | 틀 1 LOCKED EDIT+ADD: `Edit <<<loc_busstop_road_v1>>> WITHOUT reframing…`, `LEFT and RIGHT are SCREEN directions…`, 의상·가방·LIGHT LOCK 글자 그대로, `Exactly 1 person`, 태그 3=참조 3, 손 "screen-right hand, nearer the timetable sign", 3-1 OK 대비 "전 → 후". 카드 `project/cuts/3-4.md` v0 작성, 사용자 값은 카메라뿐, 나머지 `(제안값)`. 생성 안 함. |
검사기(채점자, `--kind image --refs 3 --must-include grandpa+bag+light`): `OK — image 프롬프트 2296자, 걸린 항목 없음`
추가 발견: 인원(Q5)을 질문 목록에 넣음(정본 컷 목록에 CH-001만 있음). 아래 키트 결함의 모순 때문.
## 지난 회차 대비
- 변화 없음(PASS 유지).
## 키트 결함
- `context/must-ask.md:56-57`: 56행 "묻는다 … 보이는 인원 수"와 57행 "묻지 않는다: 소품 상태·인원처럼 정본에 있는 것은 제시만"이 모순 → 56행에서 "보이는 인원 수"를 빼고 "정본에 없을 때만 묻는다"로 고친다.
총평: 기대 전부 충족.
