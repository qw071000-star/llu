# real6-C40 — 한 번에 여러 수정 ("이것저것 다")

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `image-prompt/SKILL.md`·`first-frame.md` 엶. "변경 하나당 프롬프트 하나", 순서 머리 → 장화 → 하늘, 승인본 새 테이크 질문(1), 적용 범위 이 컷만(2: CH-002 `red rain boots`와 부딪쳐 `Except` 한 줄), 하늘은 PALETTE 80/15/5·LIGHT LOCK·이웃 컷 영향 짚음(6), 생성 없음 |
| 2 (이 컷만. 제안대로 머리부터) | 부분 | "머리부터 해"를 생성 지시로 안 받음(보기 전 프롬프트). 코드블록 1(LOCKED EDIT 머리 한 가지, `WARDROBE` 글자 그대로, `Exactly 1 person`), 블록 밖 모드·참조·모델·해상도·길이·폴더, `전 → 후` 한 줄, 위험 5, 보낼까요. 미달: 답 받은 컷 질문(승인본 대체·적용 범위·순서·머리/장화/하늘 값)을 컷 카드에 `(제안값)`으로 기록하지 않음 — `git status`에 `cuts/3-3.md` 변경 없음, `cut-card.md`도 안 엶(`instructions.md:26`, `routing.md:45`). 경미: 임시 파일을 `RUN/tmp`가 아닌 RUN 루트에 만들었다 지움, 답에 `git status` 잡음 노출 |

검사기(내 실행, `--kind image --refs 1`, must-include girl+light): `OK — image 프롬프트 1845자, 걸린 항목 없음`(플레이어가 첫 실행의 WARN "raised hand 화면 쪽 없음"을 고침).
5회차 대비: PASS 2 → PASS 1 / 부분 1 (카드 기록 누락 회귀).
키트 결함: `instructions.md:26` 카드 기록 규칙이 규칙 4의 맨 끝 줄이라 편집 프롬프트 턴에서 빠짐. 고칠 것: 같은 줄을 `instructions.md` "출력"의 끝에 "프롬프트를 보인 턴이 끝나기 전에 받은 답을 컷 카드/대장에 적었는지 확인" 한 줄로 반복.
총평: PASS 1 / 부분 1 / FAIL 0.
