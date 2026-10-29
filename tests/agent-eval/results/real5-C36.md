# real5-C36 — 레지스터와 부딪치는 연기 ("웃게")

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | 질문 턴에 `acting` 안 엶(meta reads에 live-action·cut-card만). "컷 목록 2-2 줄은 '같은 얼굴로 가방을 쓰다듬음'", `decisions.md` §5 절제와 충돌, "입술을 다문 입꼬리와 눈가까지"로 범위 안에 둠, 6개 한 묶음, 생성 없음. 경미: 이웃 2-1 영상 OK 카드를 열어 `a smile = failed take`를 인용(`routing.md:44` 이웃 OK 카드는 기준 OK 아니면 열지 않음) |
| 2 (그대로, 프롬프트 턴) | PASS | `acting/SKILL.md` 엶. 15블록 코드블록 1 + 블록 밖 모드·참조 3·모델·해상도·길이·폴더, 위험 7, `a broad grin, visible teeth or a laugh = failed take` / `no change in the face at all = failed take`, 손 `the screen-left hand, nearer the tree`. 카드 `(제안값)` 기록. "보낼까요?" 생성 없음. 임시 파일 `p22.txt`를 RUN 루트에 만들었다가 지움 |

검사기(내 실행, `--kind video --refs 3 --seconds 8`, must-include grandpa+bag+light): `OK — video 프롬프트 5496자, 걸린 항목 없음`.
(identity_grandpa.lines를 더하면 FAIL이 나지만 승인된 2-1 OK 프롬프트에도 IDENTITY 문장이 없고 `character.md:51`이 "컷 프롬프트에는 WARDROBE만"이라 했으므로 기대 쪽 오류.)

4회차 대비: PASS 2 유지(5689자 WARN → 0).
추가 발견: 2-1 OK 카드 열람(경미).
키트 결함: `live-action.md:14` "인물 줄은 고정 설명문" ↔ `character.md:51` "WARDROBE만" 모호(아래 요약).
총평: PASS 2 / 부분 0 / FAIL 0.
