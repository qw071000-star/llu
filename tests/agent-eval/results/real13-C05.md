# real13-C05 장소 반대 방향 뷰 (2턴) — PASS 2 / 부분 0 / FAIL 0 (real11: PASS 2 / 부분 0 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | "7번 장소 새 시점으로 진행합니다." `location.md`+`location-view.md`, 부모 `LC-001-V1`(`job-lc001v1`). "안에서"라 카메라 방식을 "반대편 끝으로 이동"으로 정함. 질문 4개(카메라 위치 / 건너편 풍경 / 길 방향 / 이 뷰의 LIGHT LOCK 좌우 뒤집힘 "감나무 화면 오른쪽, 시간표 화면 왼쪽"). 높이 1.6m는 기본값으로 제시 |
| 2 | PASS | 틀 A: `Do not inherit its camera angle, framing or composition.`, `WITHOUT reframing` 없음, 카메라를 원본 관계로("looking back along the same central axis toward the original camera position"), `reverse` 한 단어 아님, `not a horizontal mirror of the reference`, MASTER GEOMETRY에 `(as seen from across the road, looking at the shelter's open front)` + `Except:` 줄, `In this view the persimmon tree is at screen RIGHT… sign at screen LEFT`, LIGHT LOCK `Low dusk sun from screen right, the persimmon-tree side, is the only key; …` 글자 그대로. 동서남북 없음. "벤치 높이" 두 해석을 밝히고 0.45m 제안(`location-view.md` Common 규칙). registry 초안 기록 |

검사기: `--kind image --refs 1 --must-include`(좌우 뒤집은 light 문장) → `WARN 인물이 있는 프롬프트에서 좌우를 썼는데 좌표 문장이 없다` · `FAIL 0 · WARN 1 · 2668자`. 검사기 오탐: 프롬프트에 사람이 없음("no building, car, person…"의 `person`에 반응). 플레이어가 이유를 밝히고 유지. (표준 `light.lines`를 넣으면 반대 뷰라 FAIL이 나는 것은 정상)
추가 발견: Template A의 `the vanishing point [position]` 칸이 "horizon low in the frame"로만 채워짐(경미).
키트 결함: `kit/skills/higgsfield-generation/check_prompt.py` 좌표 문장 WARN이 `no people/person` 부정문에도 걸림 → 'no person' 앞 부정 문맥이면 사람 없음으로 처리. (통합과 무관)
총평: 좌우 뒤집기·LIGHT LOCK 재작성 모두 정확, PASS 2.
