# real5-C05 장소 반대 방향 뷰 (2턴) — PASS 2 / 부분 0 / FAIL 0 (real4: PASS 2)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | image-prompt SKILL + location.md + location-view.md. 부모 `job-lc001v1`, 카메라 방식(먼 끝으로 이동)을 정함. 4항목(높이·샷 크기 / 랜드마크 3개 — 표지판 화면 왼쪽·감나무 화면 오른쪽 / 종점 / 이 뷰 LIGHT LOCK 화면 오른쪽) 제안값+이유. "좌우가 뒤집힙니다" 짚음 |
| 2 | PASS | `Do not inherit its camera angle, framing or composition.`, CAMERA를 원본 카메라와의 관계로("looking back … toward the original camera position"), `not a horizontal mirror`, MASTER GEOMETRY `(as seen from across the road…)` + `Except:` + `In this view the timetable sign is at screen left and the persimmon tree is at screen right`, LIGHT LOCK `from screen right, the persimmon-tree side`. WITHOUT reframing 없음. 동서남북 grep 0. 태그 1 = 참조 1. 높이 "벤치 높이"는 앉은 눈높이 1.1m로 풀어 "전 → 후" 알림 |

검사기: `--kind image --refs 1`: `OK — image 프롬프트 2814자, 걸린 항목 없음`

추가 발견: 없음.

키트 결함: 없음.

총평: real4와 같은 PASS 2.

G1: 모든 턴 tools가 Bash/Write/Edit/Grep뿐, `mcp__` 호출 없음, `generate_*` 없음.
