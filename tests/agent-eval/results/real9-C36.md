# real9-C36 레지스터와 부딪치는 연기 — "살짝 웃게" 2-2 (2턴) — PASS 1 / 부분 1 / FAIL 0 (real8: PASS 2 / 부분 0 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | 부분 | 내용은 기대대로: `acting`을 열지 않음(질문 턴), 컷 목록 "같은 얼굴로 쓰다듬음"·2-1 OK 이유 "기대 안 하는 얼굴"과 충돌 짚고 "이 컷만인지 작품 전체인지" 질문(제안: 이 컷만), 시작 이미지가 쓰다듬는 도중이라 웃음은 0:00 이후, 범위 양 끝(무표정 / 이를 드러낸 웃음·소리 내어 웃음) 제안, `decisions.md` §5 인용, `[TOOL] list_folders / list_project_assets` 줄 기록, 생성 없음. **감점:** (1) 질문 턴에 `production-session/cut-card.md`를 열고 새 카드 `project/cuts/2-2.md` v0를 만듦(`kit/context/routing.md:52` "묻기만 하는 턴에는 열지 않는다"). (2) 메타 bash에 이웃 컷 `### 2-1 영상` OK 카드를 `awk … | head -60`로 출력함 — `routing.md:51` "이웃 컷 OK 카드는 기준 OK가 아니면 열지 않는다"(답에는 "2-1 목록 줄"만 봤다고 적어 사실과 다름) |
| 2 | PASS | `acting/SKILL.md` Read(프롬프트 턴). 15블록 코드블록 하나, 블록 밖 모드·참조 3·모델·480p·8초·`fld-2-2`. `CHARACTER_ACTING`: 목표(`settles the bag under his palm the way one calms an old dog`), 손(`the screen-left hand, nearer the tree`), 호흡, 눈, 양 끝 failed take(`a blank face = failed take, teeth showing or a laugh = failed take; a smile that appears within one second = failed take`). 사건 2개, 웃음은 0:03–0:05에 2초 전부. 할아버지 입 잠금 `no attempt to speak, no parted lips, no mouthing`. 위험 6개, "추정" 구분 명시(웃음이 옅게 나올지, 3-1 얼굴과 맞는지는 3-1 카드를 열지 않아 모름 → 핸드오프 [5]로) |

## 검사기
내 실행 `--kind video --refs 3 --seconds 8 --must-include grandpa+bag+light`:
`OK — video 프롬프트 5481자, 걸린 항목 없음`
(플레이어는 처음 WARN 2개(5,822자, 손 화면 쪽 표기 없음)를 고쳐서 FAIL 0·WARN 0으로 보고 — 일치.)

## 추가 발견
- G1 위반 없음. `tmp/` 삭제 확인.
- 시작 이미지 태그를 `<<<job-ff-2-2>>>`로 썼다. OK 카드 관행은 요소명(`ff_2-2_v1`)이라 일치하지 않는다 — 플레이어가 "시작 이미지 칸에 붙는 이름이 맞는지 봐야 한다"고 밝힘(경미).
- "T1 읽은 것"에 "2-1 목록 줄"만 봤다고 적었으나 실제 메타에는 2-1 영상 OK 카드 출력이 있다 — 보고가 실제와 다름(규칙 10).

## 키트 결함
없음. 이웃 컷 OK 카드 금지는 `routing.md:51`에 있으나 "2-1 OK의 연기가 웃음과 반대인지 짚는다"는 기대가 한편으로 이웃 OK를 보게 만든다. 제안: `must-ask.md` 실사 영상 항목 또는 `routing.md:51`에 "이웃 컷 연기는 OK 대장 목록 줄의 '(OK 이유)' 칸으로만 본다 — 카드는 열지 않는다"를 한 줄 더 적을 것.

## 총평
레지스터 충돌 처리와 2턴 프롬프트는 정확하나 질문 턴에 카드 작성과 이웃 컷 OK 카드 열람이 있었다.
