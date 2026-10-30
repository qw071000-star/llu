# real11-C47 두 인물 접촉 — "손 잡게" 3-2 (2턴) — PASS 0 / 부분 2 / FAIL 0 (real9: PASS 2 / 부분 0 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | 부분 | "13번 실사·인물 영상으로 진행합니다." 3줄 보고. 읽기: 3-2 카드·핸드오프·shot-list·decisions·OK 대장·registry + `video-prompt` SKILL·`live-action.md`(자기 컷만, 이웃 카드 안 엶). 질문 5개 제안값+이유. 충족: 1 "카드와 요청이 다릅니다 … 카드 [1]과 이음새 줄은 총괄 핸드오프 [5]로"; 3 "손녀의 화면 왼쪽 손(벤치에 가까운 손)을 할아버지의 화면 오른쪽 손(시간표 쪽 손, 가방 위) 위에 포개 얹습니다. 쥐거나 깍지 끼지 않고, 가방은 닫힌 채"(누가·어느 손·무엇을, 연속성 표의 가방 위 두 손과 이어지게 처리, §5 절제); 4 할아버지 반응·시선. **감점:** 사건 수. 2번 "1) 돌아서며 말하고 2) 다가가 3) 손 얹음 … 동작은 한 번에 3개까지"라고 했으나 돌아서기·말하기·걸어가기·손 얹기는 동사 4개다. `video-prompt/SKILL.md:81` "Count every verb … Do not count them in groups"인데 '돌아서며 말하고'를 하나로 묶었다(예시 "turns, walks over, takes her hand = 3"에는 말하기가 없다). 4개면 샷 나누기를 제안해야 했다 |
| 2 | 부분 | `acting/SKILL.md`를 이 턴에 엶. 카드 [1][4][5][6]에 `(제안값)` 기록, 렌즈 "32°(75mm, 시작 이미지 기준)". 프롬프트 15블록: 손은 모두 `the screen-left hand, nearer the persimmon tree` / `his screen-right hand, nearer the sign`, `Nobody looks at the camera`, 연기 양 끝(`tears = failed take, hugging or clinging = failed take`, `a sigh or a frown = failed take`), `she does not squeeze`. 블록 밖 모드·참조 4개·설정·폴더, 위험 6개(마지막은 추정 표시), `tmp/` 삭제, "이 프롬프트로 영상을 만들까요?"로 끝냄. **감점:** 검사기 WARN 1개(길이 6509자 > 5,500)를 "인물 2명에 참조 4개 … 3-1 승인본도 비슷한 길이"로 남겼다. 3-1 승인본은 5,060자(<5,500)라 근거가 사실과 다르고 1,400자는 CHARACTER_ACTING 확장이다. 사건도 4개 그대로 썼다 |

검사기 (`--kind video --refs 4 --seconds 8 --must-include grandpa+girl+bag+light.lines`, 코드블록 1개):
`WARN  길이 6509자. 5,500자 이하가 안전했다. 남기려면 이 숫자를 그대로 적고 이유를 쓴다` / `— FAIL 0 · WARN 1 · 6509자`
(플레이어는 숫자를 적었으나 이유가 부정확. 오탐 아님.)

추가 발견
- 1턴 "기본값으로 씀"에 `75mm, 약 32°` — `SKILL.md:79` 표와 맞음.
- 대사("할아버지, 막차 갔대.")를 3-1에서 가져와 2번 제안에 넣은 것은 카드 [1]("3-1과 같은 동작") 근거가 있고 사용자에게 제안으로 보였다.

키트 결함
- `kit/skills/video-prompt/SKILL.md:81` 사건 수 줄: 예시가 "turns, walks over, takes her hand = 3"뿐이라 대사가 있는 컷에서 '말하기'를 세는지 모호하다. 고침: 예시에 "turns, says the line, steps, takes her hand = 4 → split" 한 줄.
- `kit/skills/higgsfield-generation/check_prompt.py` 길이 WARN 문구("남기려면 이 숫자를 그대로 적고 이유를 쓴다")가 이유 검증이 없어 길이 초과를 쉽게 통과시킨다. 고침: WARN 문구에 "승인된 비슷한 컷 프롬프트의 글자 수와 비교해 적는다"를 추가하거나 6,000자 초과를 FAIL로.

총평: 손 접촉의 화면 기준 표기·연기 범위·충돌 알림은 좋았으나 사건 수를 묶어 셌고 길이 WARN을 부정확한 근거로 남겼다.
