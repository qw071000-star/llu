# real11-C13 "3-1의 색감과 질감으로 3-5 퍼스트 프레임" (2턴) — PASS 1 / 부분 1 / FAIL 0 (real9: PASS 2 / 부분 0 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | 부분 | `ok-reuse.md`·3-1 시작 이미지 카드를 봄. "3-1 프롬프트에 질감 문장이 없어서 새로 만들지 않고, 색 참조로만 붙이고 권한을 색·대비·질감만으로 좁힘". 카메라(새 시점 틀 2)·손 동작·가방 안·3-4 이어받기·참조 4장을 제안값+이유로 6개. 대장 팔레트 문장 차이도 짚음. **감점:** 질문 턴에 `cut-card.md`를 열어 `project/cuts/3-5.md`를 새로 만듦(`git status ?? project/cuts/3-5.md`). `kit/context/tasks.md` §3 "On question-only turns do not … create card files" 위반 |
| 2 | PASS | 틀 2: `Do not inherit its camera angle, framing or composition.`, 권한 줄 `<<<ff_3-1_v2>>> controls only colour, grade, contrast and texture. Never take its subjects, composition, people or light direction.`, 참조 4 = 태그 4, 가방 열림(`Except: the bag is open in this cut.`), WARDROBE·PROP·LIGHT LOCK 글자 그대로, 손은 화면 쪽+물건, `Exactly 1 person`. 색 문장을 지어내지 않음 |

검사기: `--kind image C13_t2 --refs 4 --must-include bag+light+grandpa` → `OK — image 프롬프트 2558자, 걸린 항목 없음`
추가 발견: 렌즈를 "2-2 클로즈업과 같은 85mm"로 "기본값으로 씀"에 넣음(근거: OK 대장). 시작 이미지가 없는 새 컷이라 렌즈 기본값이 정해져 있지 않으므로 질문에 넣는 쪽이 더 정확했을 수 있으나 위반은 아님.
키트 결함: C11과 같은 모순 — `kit/instructions.md` 끝줄("write answers on the cut card before ending the turn") ↔ `kit/context/tasks.md` §3 마지막 줄. 고침은 C11 참고.
총평: 핵심(색 문장 안 지어냄, 권한 좁힘)은 정확. 질문 턴에 카드 파일 신설로 1턴 부분.
