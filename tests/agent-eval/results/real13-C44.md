# real13-C44 "카메라 좀 더 가까이" 3-2 퍼스트 프레임 (2턴) — PASS 2 / 부분 0 / FAIL 0 (real11: PASS 2 / 부분 0 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | 첫 줄 "11번 퍼스트·끝 프레임으로 진행합니다." 승인된 `job-ff-3-2`가 있고 카메라만 바꾸면 틀 2(새 시점, `first-frame.md`)라고 판단("`location-view.md` 틀 B"를 쓰지 않음). 거리를 제안값으로 묻고("약 30% 앞으로, 허리 위 미디엄 클로즈 투샷, 렌즈 바꾸면 변경이 둘이 되어 75mm 유지"), 승인본 교체 여부 확인. 인물 위치·시선·가방·빛은 승인본 그대로. 질문 턴에 카드 만들지 않음, 생성 없음 |
| 2 | PASS | 틀 2 전문(`Do not inherit its camera angle, framing or composition.`, `PRIORITY: the CAMERA block overrides every reference.`, 카메라 장비 `ARRI Alexa Mini … 75mm`). WARDROBE·PROP·LIGHT LOCK·BLOCKING 문장은 승인본과 글자 그대로, 카드 [10]의 실제 실패(카메라를 봄)만 `Nobody looks at the camera.`로 추가. 같은 쪽 카메라라 `not a horizontal mirror`·`In this view` 줄은 안 씀. 블록 밖 모드·참조 4개·모델·해상도·폴더, 바뀐 줄 "전 → 후"(CAMERA, 추가 두 줄), 위험 4개(3-1 영상의 한 걸음이 화면 밖으로 나갈 위험 포함). 카드 3-2에 `(제안값)` 기록(diff) |

검사기: `--kind image C44t2_1.txt --refs 4 --must-include grandpa+girl+bag+light` → `OK — image 프롬프트 2496자, 걸린 항목 없음`

추가 발견
- 틀 2의 `[PALETTE · ERA LOCK from the asset registry, verbatim]` 줄이 없고 `Nothing else`도 짧게 줄었다. 단, 승인본 프롬프트가 이미 같은 형태(그 줄들 없음)여서 최소 변경으로 허용.
- 카드 [4]에 `75mm 유지 = 대각 화각 35°`라고 썼다. 환산표(`video-prompt/SKILL.md:79`)는 75mm = 32°다(카드 v1의 35° 오기를 이어받음; C24 t2는 32°로 바로잡음).

키트 결함
- `kit/skills/production-session/cut-card.md` [4] 렌즈 줄에는 환산표 위치(`video-prompt` §2)만 있어 이미지 작업(`image-prompt`)에서는 표를 안 열어 35°를 그대로 옮긴다. 고침: 카드 [4] 렌즈 칸 옆에 "75mm = 32° · 50mm = 47° · 35mm = 63°" 세 값을 직접 적는다.

총평: 카메라만 바꾸는 편집을 틀 2로 올바르게 분류했고 고정 문장도 그대로 유지했다.
