# real13-C24 실사 영상, 연기를 새로 — 3-2 (2턴) — PASS 1 / 부분 1 / FAIL 0 (real11: PASS 2 / 부분 0 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | 부분 | 내용은 맞다. `video-prompt` SKILL·`live-action.md`만 열고 `acting`·`ok-reuse.md`·3-1 카드는 안 열었다(메타 reads, skills=[]). 카드 [1] "3-1과 같은 동작·타이밍"과 새 연기가 어긋난다고 짚고 "이 컷만"을 제안했다. 렌즈는 질문에서 뺐다. 카드 파일을 만들지 않았다. 그러나 첫 줄이 `**시작 보고**`로 시작해 "[N]번 [작업명]으로 진행합니다."가 없다(13번). 이벤트를 "손녀 고개 돌림·대사·할아버지 시선"으로 3개라 했지만 질문 3번에 이미 "손을 내리고 고개를 돌려 대사"가 들어 있어 손 내리기를 묶어 셌다(`video-prompt/SKILL.md:82` "Do not count them in groups"). 기본값 줄에 "35°(시작 이미지 기준)"라고 썼으나 시작 이미지는 75mm=32°라 t2에서 정정 |
| 2 | PASS | 이 턴에 `acting`을 열었다(meta skills=['acting']). `CHARACTER_ACTING`: 인물마다 상대를 향한 목표(`makes GRANDPA hear…`, `makes GIRL believe…`), 손의 일, 호흡, 눈 문장, 양 끝 failed take(`a trembling voice or tears = failed take, a cheerful or indifferent tone = failed take` / `a turned head, a sigh or closed eyes = failed take, a completely blank stare … = failed take`), `does not startle; simply stops`. 사건 3개(손 내림·고개 돌림·대사), 시선 이동은 비트. 목소리 문장은 대장과 글자 그대로, 할아버지 입 잠금(`no attempt to speak, no parted lips, no mouthing`) 있음. 3-1 OK 문장은 안 가져옴. 화면 방향·손 표기 맞음(`the screen-right hand, nearer the sign`). 카드를 v2로 고치고 `(제안값)` 표시(diff). 렌즈 35° → 32° "전 → 후" 보고. WARN 6,182자는 숫자와 이유(고정 문장, 약 380자 줄임) 적음 |

검사기: `--kind video C24t2_1.txt --refs 4 --seconds 8 --must-include grandpa+girl+bag+light` → `WARN  길이 6182자. 5,500자 이하가 안전했다 … — FAIL 0 · WARN 1 · 6182자` (플레이어가 숫자·시도한 줄임·이유를 적었으므로 허용)

추가 발견
- 플레이어가 `check_prompt.py`를 단독 Bash로 돌렸고(`cd` 없음) 끝에 `tmp/`를 지웠다. G1 위반 없음(mcp 호출 없음, RUN 밖 읽기 없음).
- `PRE_SHOT_CONTINUITY` 없음: 시작 이미지가 이어받는 상태를 담아 `live-action.md:102` "이어받은 상태가 있을 때만"에 부합.
- t2 끝에서 `shot-list.md` 이음새 줄은 핸드오프 [5]로 올린다고 적음(컷 세션 권한 규칙대로).

키트 결함
- `kit/instructions.md:41`: 첫 줄 "[N]번 …으로 진행합니다."가 "Starting a conversation" 4번에 있지만 이번에도 빠졌다. 컷 번호 + "영상 프롬프트" 요청에서 플레이어가 "시작 보고"만 쓴다. 고침: 4번을 §Output 맨 위의 "Line 1 of every answer" 규칙으로 올리고, 시작 보고 예시 첫 줄에 `[N]번 …`을 넣는다.

총평: 실제 연기 내용은 real11과 같게 유지됐고, 질문 턴 첫 줄 형식 하나만 빠졌다.
