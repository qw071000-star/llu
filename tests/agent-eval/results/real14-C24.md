# real14-C24 실사 영상, 연기를 새로 — 3-2 (2턴) — PASS 2 / 부분 0 / FAIL 0 (real13: PASS 1 / 부분 1 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | 첫 줄 "13번 실사·인물 영상으로 진행합니다." `video-prompt` SKILL·`live-action.md`만 열고 `acting`·`ok-reuse.md`·3-1 영상 카드는 안 엶("3-1 영상 카드는 열지 않았습니다"). 카드 [1] "3-1과 같은 동작·타이밍"과 새 연기의 충돌을 짚고 "이 컷만"을 제안, 이음새 표 수정은 핸드오프 [5]. 렌즈는 질문에서 빼고 "카드 35°, 시작 이미지 75mm≈32°라 시작 이미지를 따릅니다". 사건 3개를 따로 셈(손 내림 / 대사 / 할아버지 손 쥠). 질문 5개 한 묶음. 질문 턴이라 카드 안 고침 |
| 2 | PASS | `acting` SKILL과 `cut-card.md`를 엶. `CHARACTER_ACTING`: 인물마다 상대를 향한 목표(`to make the girl believe he is not worried` / `to get her grandfather to take the news without a fuss`), 손의 일, 호흡(`slow low breath`), 눈 문장, 양 끝 failed take(`a flinch or a turned head = failed take, … completely frozen = failed take` / `tears or a raised voice = failed take, a robotic monotone = failed take`), `does not startle; he simply stops`. 비트는 시선·사이. 사건 3개. 대사 한 번, 목소리 문장은 대장 VOICE와 일치, 할아버지 입 잠금 `no attempt to speak, no parted lips, no mouthing`. 3-1 OK 문장 안 가져옴. 손은 모두 `the screen-right hand, nearer the sign`. 카드 v2 `(제안값)`, 렌즈 35° → 32° "전 → 후". 길이 WARN은 숫자(5,981자)와 이유(고정·연기 문장을 건드려야 함)를 적음 |

검사기: `python3 kit/skills/higgsfield-generation/check_prompt.py --kind video C24t2_1.txt --refs 4 --seconds 8 --must-include grandpa+girl+bag+light` → `WARN  길이 6043자. 5,500자 이하가 안전했다. 남기려면 이 숫자를 그대로 적고 이유를 쓴다 — FAIL 0 · WARN 1 · 6043자`

real13 감점 해소: ① 첫 줄 누락 — 해소. ② 사건 수를 묶어 센 것 — 해소(세 사건을 따로 적음). ③ 기본값 줄의 "35°(시작 이미지 기준)" 오기 — 해소(1턴부터 75mm≈32°).

추가 발견
- 플레이어가 적은 길이(5,981자)와 보인 프롬프트(6,043자)가 62자 다르다. 마지막 수정이 검사 뒤에 들어갔을 수 있다.
- `the screen-right hand, nearer the sign`이 12번 반복돼 길고 기계적이다(규칙은 지킴).
- 카드 [5]에 영어 구절이 한국어 문장 속에 섞임("the screen-right hand, nearer the sign, 내려놓음").

키트 결함: 없음(C02와 같은 `kit/instructions.md:12`만).

총평: real13의 세 감점이 모두 해소돼 2턴 PASS.
