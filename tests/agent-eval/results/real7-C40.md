# real7-C40 — 한 번에 여러 수정 ("이것저것 다")

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `image-prompt/SKILL.md`·`first-frame.md` 엶, 3-3 카드·OK 카드 열람. "세 가지를 한 번에 바꿀 수 없습니다(한 생성에 한 가지)", 순서 머리 → 장화 → 하늘(사용자 순서), 장화는 대장 `red rain boots`·3-1·3-2 이음새와 부딪침 + 이 컷만/작품 전체(2), 하늘은 PALETTE 80%·LIGHT LOCK·이웃 컷 색 영향(6), 승인본 새 테이크 질문(1). 생성 없음 |
| 2 (이 컷만. 제안대로 머리부터) | PASS | "머리부터 해"를 생성 지시로 안 받음("보낼까요?"). 코드블록 1(LOCKED EDIT 머리 하나, `Except:` 한 줄, `WARDROBE` 글자 그대로, `Exactly 1 person`), 블록 밖 모드·참조·모델·해상도·길이·폴더, `전 → 후` 한 줄, 위험 4. 카드 `cuts/3-3.md` [11]에 6답을 `(제안값)`으로 기록(git diff 확인) — 6회차 누락 해소. 임시 파일은 scratchpad로 옮김 |

검사기(내 실행, `--kind image --refs 1`, must-include girl+light): `OK — image 프롬프트 1808자, 걸린 항목 없음`.
6회차 대비: PASS 1 / 부분 1 → PASS 2.
키트 결함: 없음.
총평: PASS 2 / 부분 0 / FAIL 0.
