# real2-C30 — "너무 어려 보여" (3-3 퍼스트 프레임)
| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | reads: 3-3 카드, image-prompt SKILL·first-frame.md·character-edit.md, ok-cuts, 대장. 질문 4개(범위 이 컷만/설정 자체, 승인 `job-ff-3-3` 새 테이크 대체, 나이 표지, 참조). Q1이 CH-002 "about ten"을 명시. 나이 표지는 뒷모습에서 보이는 체형·자세·손·볼선. 생성 없음 |
| 2 | 부분 | `Edit <<<image_1>>> WITHOUT reframing…`, `CHANGE — AGE`, `she must be recognisable as the same girl two years older`, WARDROBE·LIGHT LOCK 글자 그대로, `Exactly 1 person is visible`. 참조 1개(`job-ff-3-3`), 위험 5개, 생성 안 함, 카드 [10]에 `(제안값)`. 그러나 지침 3번·시나리오가 요구하는 바뀐 줄 "전 → 후" 표기가 답에 없음(프롬프트 안 `from about ten … to about twelve`만) |
검사기(채점자, --kind image --refs 1 --must-include girl+light): `OK — image 프롬프트 2055자, 걸린 항목 없음`
지난 회차 대비: 지난번 PASS("전 → 후" 표 있음) -> 2턴이 **후퇴**(전→후 누락).
추가 발견: 카드 3-3 [10] 수정(규칙 4에 따른 기록).
키트 결함: `instructions.md:18`(규칙 3)의 "전 → 후"가 OK 프롬프트 수정에만 걸린 듯 읽힘 -> `instructions.md` "출력" 절에 "LOCKED EDIT/나이 수정은 코드블록 밖에 바뀐 줄 전 → 후 한 줄씩" 추가.
총평: PASS 1 / 부분 1 / FAIL 0
