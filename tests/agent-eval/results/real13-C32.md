# real13-C32 사용자가 말한 손 — "손녀 오른손에 우산" (2턴) — PASS 1 / 부분 1 / FAIL 0 (real11: PASS 2 / 부분 0 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | 첫 줄 "11번 퍼스트·끝 프레임으로 진행합니다." 자기 컷(3-1 카드·핸드오프·OK)과 `first-frame.md`만 열었다. "오른손은 화면 기준으로 이해했습니다", 그 손(시간표 쪽)은 이미 시간을 짚는다는 충돌과 화면 왼손 대안 제시. 새 소품 우산 사양(남색, J자 손잡이, 80cm)을 제안값으로, 승인 컷이라 새 테이크로 만들지 확인. 생성 없음 |
| 2 | 부분 | 본인 기준으로 바꿔 `the screen-left hand, farther from the sign`으로 쓰고 "손녀 본인 오른손을 화면 왼손으로 바꾼 것은 추정"이라 밝혔다(`her right hand` 없음). 사람 줄·`Exactly 2 people are visible.` 있음. 그러나 두 사람이 보이는데 `WARDROBE:`에 손녀 문장만 있고 할아버지 문장이 없다. must-include에 grandpa를 넣으면 검사기 FAIL. 카드 3-1 [5]에 `(제안값)`·`(추정)` 기록(diff), 위험 4개, "전 → 후" 있음 |

검사기: `--kind image C32t2_1.txt --refs 1 --must-include grandpa+girl+light` → `FAIL  고정 문장이 글자 그대로 들어 있지 않다: A faded olive work jacket over a cream knit vest and a white… — FAIL 1 · WARN 0 · 1867자` (girl+light만 넣으면 `OK`)

추가 발견
- 손녀가 시간표를 향해 선 방향(등/옆)에 따른 "본인 오른손" 변환은 키트에 표가 없어 플레이어 판단(추정 표기로 허용; real11과 동일 판정).
- 3-1 승인 영상 `job-v-3-1`이 새 시작 이미지로 다시 필요하다고 알림(좋음).

키트 결함
- `kit/skills/image-prompt/first-frame.md` Template 1/2의 WARDROBE 줄 위: 통합 커밋 096550e가 "If a person is visible, include a `WARDROBE:` line. Also put that sentence in the check's `--must-include` file." 줄을 지웠다(통합 때문). 템플릿에는 `WARDROBE: [asset registry sentence, verbatim]` 한 줄뿐이라 "보이는 사람 모두" 의미가 약하다. 고침: 템플릿 줄을 `WARDROBE: [one registry sentence per visible person, verbatim]`로 바꾼다.
- `kit/instructions.md:27`: 옆모습·등지고 선 인물의 "본인 오른손" 변환표 없음(real11 지적 유지). 고침: "back to camera: own right = screen right; profile facing screen-right: own right = the hand nearer the camera, give screen side + object, mark 추정".

총평: 화면 방향 처리는 맞았으나 LOCKED EDIT에서 두 번째 인물의 WARDROBE 문장을 빠뜨렸다(통합으로 삭제된 규칙).
