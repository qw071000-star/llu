# real9-C34 소품 지적 — "왕진 가방이 너무 새 거 같아" (2턴) — PASS 2 / 부분 0 / FAIL 0 (real8: PASS 1 / 부분 1 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `image-prompt/SKILL.md`+`prop.md` Read. `"너무 새 것"은 다시 만들라는 말이 아니라서 아직 아무것도 만들지 않았습니다.` 어느 결과인지(컷 job / 에셋 자체) 질문, 제안값은 에셋 자체. 사용 흔적 4개(손잡이 바램·모서리/바닥 쓸림·옆면 잔금·걸쇠 광 죽음)와 금지 재질 제안. 절차 보임: `고정 설명문이 바뀌므로 prop_doctor_bag_v2가 됩니다. 옛 v1은 폐기 목록으로 옮깁니다. 승인된 컷(2-1, 3-1)은 v1 그대로` |
| 2 | PASS | "그대로"=에셋 자체 고치기(real8의 "job을 알려 주세요" 재질문 없음 — `kit/skills/image-prompt/prop.md:24`대로 요소 ID를 원본으로 프롬프트까지). LOCKED EDIT 전문: `Edit <<<prop_doctor_bag_v1>>> WITHOUT reframing …`, `CHANGE — the whole bag surface`, PRESERVE에 모양·처짐·폭 약 40cm, `Avoid: glossy synthetic leather, shiny coating, bright new brass, brand logos, text, watermarks.` 블록 밖 모드·참조·모델·1k·`fld-props`, "job 미기재" 알림, 위험 5개, 확정 뒤 처리(v2, 승인 컷 v1 유지). 인물 없는 소품이라 화면 좌우 문장 생략을 밝힘(규칙 6의 "인물이 나오는 프롬프트마다"에 해당 없음). 대장 PR-001에 `초안(제안값)` |

## 검사기
내 실행 `--kind image --refs 1`: `OK — image 프롬프트 1329자, 걸린 항목 없음`

## 추가 발견
- G1 위반 없음. `tmp/` 삭제 확인.
- 프롬프트의 `plain seamless light grey studio background`, `nearly new-looking leather and bright brass`는 원본 이미지를 보지 못하고 `prop.md` 틀과 사용자 지적에서 짐작한 값인데 "추정" 표기가 없다(대장 출처는 "3-1 장면 프레임에서 잘라 만듦"이라 스튜디오 배경이 아닐 수 있음). 규칙 10 경미 위반.
- 유일한 입력(승인 컷 2-1·3-1이 쓴 v1)을 건드리지 않는다는 점을 명시 — 좋음.

## 키트 결함
- `kit/skills/image-prompt/prop.md:24`는 편집 원본을 요소 ID로 쓰라고 하나, 대장 PR-001의 출처가 "장면 프레임에서 잘라 만듦"인 경우 배경이 스튜디오가 아님(PRESERVE에 `plain seamless light grey studio background`를 쓰면 틀릴 수 있음). 제안: prop.md:24에 "PRESERVE 배경 줄은 원본 이미지를 못 봤으면 `the existing background` 로 쓴다"를 한 구절 추가.

## 총평
real8의 재질문 실패가 prop.md 보강으로 해소됨 — 프롬프트까지 정확히 감.
