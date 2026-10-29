# real9-C33 반대편 카메라 퍼스트 프레임 — "뒤에서 보는 걸로" 3-4 (2턴) — PASS 2 / 부분 0 / FAIL 0 (real8: PASS 2 / 부분 0 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `image-prompt/SKILL.md`+`first-frame.md` Read. 카메라가 `LC-001-V1`과 다르므로 틀 2(`DERIVED VIEW`), LOCKED EDIT와 섞지 않음. "할아버지는 벽에 등을 대고 앉아 있어서 정말 '뒤'는 벽 밖입니다" → 카메라를 정류장 안쪽 벤치 시간표 쪽 절반, 어깨 너머 길 쪽(1.1m)으로 제안. `이 시점은 … 화면 좌우와 빛 쪽이 뒤집힙니다. 감나무는 화면 오른쪽, 빛도 화면 오른쪽`, 새 LIGHT LOCK `Low dusk sun from screen right, the persimmon-tree side …`. 이 컷만인지 장소 뷰로 먼저 확정할지(3-5 재사용) 질문. 4개 항목, 생성 없음 |
| 2 | PASS | `This is a newly observed direction of the same physical room, not a horizontal mirror of the reference.`, `Do not inherit its camera angle, framing or composition.`, `In this view the persimmon tree is at screen right and the timetable sign pole is at the screen-left edge.`, LIGHT LOCK 화면 오른쪽(물리적으로 V1의 반대 → 일관), WARDROBE·PROP·팔레트·시대 글자 그대로, `the screen-right hand, nearer the persimmon tree`, `Exactly one person is visible.` 전 → 후 3줄(카메라·LIGHT LOCK·랜드마크), 위험 5개, 시선이 안 보여 "추정" 표기. 카드 3-4 신규 `(제안값)` |

## 검사기
내 실행 `--kind image --refs 3 --must-include grandpa+bag+light(화면 오른쪽으로 바꾼 사본)`: `OK — image 프롬프트 2477자, 걸린 항목 없음`

## 추가 발견
- G1 위반 없음. `tmp/` 삭제 확인. 3-1 시작 이미지 OK 카드를 열었으나 `kit/skills/image-prompt/first-frame.md:32`의 "연속성 표에 인물 자리가 없으면 직전 승인 시작 이미지 OK 카드 한 장" 예외에 해당(허용).
- 원래 고정 LIGHT LOCK 문장(`from screen left`)을 의도적으로 `screen right`로 바꿨음. 화면 기준 규칙(규칙 5의 글자 그대로 vs 규칙 6)이 충돌하는 지점이지만 새 뷰의 LIGHT LOCK 재작성이 `first-frame.md`/`location-view.md` 규칙이라 정상.

## 키트 결함
없음.

## 총평
벽 때문에 불가능한 "뒤"를 카메라 위치로 바꾸고 좌우·빛을 일관되게 뒤집음.
