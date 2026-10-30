# real13-C30 이미지 결과 모호한 지적 — "너무 어려 보여" 3-3 (2턴) — PASS 2 / 부분 0 / FAIL 0 (real12-recheck: PASS 2 / 부분 0 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | 첫 줄 "11번 퍼스트·끝 프레임으로 진행합니다." 승인본 `job-ff-3-3`을 기준으로 한 LOCKED EDIT("새로 그리지 않음"), `first-frame.md`+`character-edit.md`를 열었다. CH-002 "about ten"과 다름을 짚고 "이 컷만 / 인물 전체" 질문(제안: 이 컷만, 이웃 3-1·3-2가 열 살 기준). 승인 컷이므로 새 테이크 제안. 열두 살 표지를 `character-edit.md`의 아이 나이 규칙(키·어깨·팔다리·얼굴 길이·자세, 피부는 그대로)으로 제안. 3-3 카드 [5]에 사용자 값 기록(diff), 생성 안 함 |
| 2 | PASS | "이 컷만"을 수락으로 받고 LOCKED EDIT 프롬프트를 냄. 여는 문장·`CHANGE — AGE`·`PRESERVE EXACTLY`(카메라, 건축, `IDENTITY BONES`)·`ONLY CHANGE`. `WARDROBE:` 대장 문장과 LIGHT LOCK 글자 그대로, 참조는 `job-ff-3-3` 1장. 블록 밖에 모드·참조·모델·해상도·저장 폴더와 "나이: about ten → about twelve" 등 "전 → 후", 위험 5개. 카드에 `(제안값)` 표시(diff). 생성하지 않고 "보낼까요?" |

검사기: `--kind image C30t2_1.txt --refs 1 --must-include girl+light` → `OK — image 프롬프트 1867자, 걸린 항목 없음`

추가 발견
- 마지막 줄이 `no babyface, no beauty filter`로 [젊게] 줄을 썼다. 열 살 → 열두 살은 나이를 올리는 것이므로 `character-edit.md:208`의 [늙게] 줄 쪽이다(어린이라 큰 영향은 없음). 경미.
- `IDENTITY BONES:`에 머리(`straight black hair in a low ponytail`)를 다시 묘사했다. 얼굴이 아니라 머리라 허용 범위.

키트 결함: 없음. (아이 나이 규칙은 `character-edit.md:213`에서 잘 찾았다.)

총평: real12와 같다. 정본과 다른 요청을 짚고 범위를 물은 뒤 LOCKED EDIT로 정확히 썼다.
