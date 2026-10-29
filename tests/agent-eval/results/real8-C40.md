# real8-C40 — 한 번에 여러 수정 ("이것저것 다")

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `image-prompt/SKILL.md`·`first-frame.md`, 3-3 카드·OK 카드. "세 변경을 한 장씩 ① 머리 ② 장화 ③ 하늘(말씀하신 순서)", 장화는 `WARDROBE`의 `red rain boots`·3-1·3-2와 다름 → 이 컷만 `Except:` 한 줄(3), 하늘은 `PALETTE` 80%·`LIGHT LOCK` 영향(6), 승인본 새 테이크 대체(2). 생성 없음 |
| 2 (이 컷만. 제안대로 머리부터) | PASS | "머리부터 해"를 프롬프트로 읽고 "이대로 보낼까요?". 코드블록 1(LOCKED EDIT, 머리 하나, `WARDROBE` 글자 그대로, `Exactly 1 person`), 블록 밖 모드·참조 1·모델·해상도·폴더, `전 → 후` 한 줄, 위험 4. `cuts/3-3.md`에 6답 `(제안값)` 기록(git diff). `tmp/` 삭제 |

검사기(내 실행, `--kind image --refs 1`, must-include girl+light+L/R 문장): `OK — image 프롬프트 1577자, 걸린 항목 없음`.
추가 발견: 없음. 키트 결함: 없음.
7회차 대비: PASS 2 유지.
총평: PASS 2 / 부분 0 / FAIL 0.
