# real4-C13 "3-1의 색감과 질감으로 3-5 퍼스트 프레임" (2턴) — PASS 1 / 부분 1 / FAIL 0 (real3: PASS 2)
| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | image-prompt SKILL+first-frame.md, production-session SKILL+ok-reuse.md+3-1 시작 이미지 카드(+cut-card.md). "3-1 프롬프트에는 색·질감 문장이 없고 … 문장을 지어내지 않고 3-1 시작 이미지를 색 참조로 붙이며 권한은 색·그레이드·대비·질감으로만". `[TOOL] list_project_assets(fld-3-5)`. 6항목(모드 틀 2 / 카메라 / 프레임·인원 / 손 / 가방 열림 / 3-4 이음) |
| 2 | 부분 | 참조 4=태그 4, `<<<ff_3-1_v2>>> controls only colour, grade, contrast and texture…`, DO NOT TRANSFER, 의상·PROP(`Except: the bag is open.`)·LIGHT LOCK 글자 그대로, 손은 screen-left/right+물건, `Exactly 1 person`. 카드 3-5 v0. 감점: `Real material truth: scuffed leather … weathered hands with sun spots …` 새 질감 문장을 추가 — ok-reuse.md:35 "문장을 지어내지 말고 참조로 붙인다"와 어긋남(플레이어가 "제가 새로 쓴 한 줄"이라 밝힘) |
검사기(`--kind image --refs 4 --must-include bag+light`): `OK — image 프롬프트 2895자, 걸린 항목 없음`
추가 발견: 없음.
키트 결함: 경미 — `image-prompt/location.md:15,77`의 `Real material truth` 슬롯이 장소용인데 틀 2를 쓰는 퍼스트 프레임에서 따라 써짐. 고칠 곳: `image-prompt/first-frame.md` 틀 2에 "질감 문장은 색 참조가 담당, `Real material truth`를 새로 쓰지 않는다" 한 줄.
총평: 색 전용 참조 처리는 정확, 질감 문장을 지어낸 것만 감점.
