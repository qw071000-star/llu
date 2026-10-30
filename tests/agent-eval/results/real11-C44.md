# real11-C44 "카메라 좀 더 가까이" 3-2 퍼스트 프레임 (2턴) — PASS 2 / 부분 0 / FAIL 0 (real9: PASS 2 / 부분 0 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `image-prompt/SKILL.md`·`first-frame.md`, 자기 컷(3-2 카드·핸드오프·OK 카드)만. "11번 퍼스트 프레임, 3-2 컷 세션", 모호한 "좀 더 가까이"를 구체 값으로: "카메라 위치는 그대로 … 렌즈만 75mm → 100mm … 미디엄 클로즈 투샷, 두 사람과 가방이 모두 프레임에 남습니다". 틀 2(새 시점)로 보이고 LIGHT LOCK 그대로("방향이 뒤집히지 않아"). 승인 `job-ff-3-2`를 새 테이크로 만들고 새 결과 OK 후 교체할지 질문. 질문 2개, 생성·프롬프트 없음 |
| 2 | PASS | 틀 2: `Using <<<loc_busstop_road_v1>>> as the exact same location, generate a new view. Do not inherit its camera angle, framing or composition.`, CAMERA 한 줄만 바뀜(`medium close two-shot … 100mm lens`), `LEFT and RIGHT are SCREEN directions …`, WARDROBE·PROP·LIGHT LOCK 글자 그대로, `the screen-right hand, nearer the sign`, `Exactly 2 people are visible.`. 승인본에 없던 `Nobody looks at the camera.`를 카드 [10]에서 가져왔다고 "전 → 후"에 밝힘(렌즈 75mm → 100mm, 구도, 두 문장 추가). 블록 밖 모드·참조 4·모델·1k·폴더, 위험 4개(추정 표기). 카드 3-2 [4]에 `(제안값)` 기록(diff 확인), 보내지 않고 "보낼까요?" |

## 검사기
내 실행 `--kind image --refs 4 --must-include grandpa+girl+bag+light`: `OK — image 프롬프트 2462자, 걸린 항목 없음`

## 추가 발견
- G1 위반 없음. `tmp/` 삭제 확인. `Alexa Mini` 표기는 승인본(OK 카드)과 같음(대장 FINISH의 Alexa LF와 다르지만 컷 프롬프트 기준이 승인본).
- 승인본에 없던 문장 2개(`Nobody looks at the camera.`, `Do not inherit …`)를 한 생성에 더함 — 카메라 변경에 따른 틀 2의 필수 문장과 카드 [10]의 막는 문장이라 "하나의 변경" 범위로 보고 공개했으므로 허용.

## 키트 결함
없음.

## 총평
"좀 더 가까이"를 렌즈·샷 크기 값으로 풀어 틀 2로 쓰고, 승인본과 달라진 곳을 모두 밝혔다.
