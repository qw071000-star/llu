# real16-C05 장소 반대 방향 뷰 (2턴) — PASS 10 / 부분 0 / FAIL 0

## 턴별 판정

| 턴 | 기대 | 판정 | 근거 |
|---|---|---|---|
| 1 | 첫 줄 | PASS | "7번 장소 새 시점으로 진행합니다." |
| 1 | location.md + location-view.md, 부모 job-lc001v1, 카메라를 원본 카메라와의 관계로 (G8) | PASS | reads location.md·location-view.md; "부모는 확정된 `LC-001-V1`(`job-lc001v1`)"; "정류장 지붕 앞 가장자리에서 1m쯤 안쪽, 정중앙에 서서 길을 봅니다" |
| 1 | 빈 칸(높이·샷 크기·남길 랜드마크) 제안 | PASS | 2. 카메라 높이 1.6m, 4. 화면에 남길 것, 3. 끝점 |
| 1 | 반대쪽 카메라 → 좌우·빛 뒤집힘을 질문 턴에 알림 (기능 18) | PASS | "**알림:** …낮은 저녁 해는 이 뷰에서 화면 오른쪽으로 옵니다(`from screen right, the persimmon-tree side`)" |
| 2 | `Do not inherit its camera angle…`, `WITHOUT reframing` 없음 | PASS | 프롬프트 1행 "Do not inherit its camera angle, framing or composition."; WITHOUT 없음 |
| 2 | `not a horizontal mirror`, 감나무=화면 오른쪽, 시간표=화면 왼쪽, 해=화면 오른쪽(감나무 쪽), 동서남북 없음 | PASS | "This is a newly observed opposite direction… not a horizontal mirror"; "In this view the timetable sign is at screen LEFT and the persimmon tree is at screen RIGHT. Low dusk sun from screen right, the persimmon-tree side, is the only key…" |
| 2 | MASTER GEOMETRY에 기준 시점 + `Except:` 줄 | PASS | "MASTER GEOMETRY (as seen from across the road, looking at the shelter's open front)"; "Except: only the underside edge of the tin roof…" |
| 2 | "벤치 높이" 두 가지로 읽힘 → 값 제안·추정 표시 | PASS | "'벤치 높이'는 벤치 앉는 면, 약 0.45m… 앉은 사람의 눈높이(약 1.1m)로 읽을 수도 있는데, 이쪽은 '추정'입니다." |
| 2 | 검사 후 표시 (G7), 생성 안 함 | PASS | Bash check_prompt --kind image tmp/lc001v2.txt --refs 1 --must-include tmp/must.txt; "이미지로 만들어" 요청 대기 |
| 전체 | G1·G2·G9 | PASS | mcp 없음, 한국어, 방향 전부 화면 기준 |

## 검사기 결과

- C05 t2 코드블록 1: `--kind image --refs 1 --must-include 반전된 LIGHT LOCK(screen right)`: OK — image 프롬프트 2913자, 걸린 항목 없음
- 같은 파일, 비반전 light.lines(screen left)로 검사 시: FAIL 고정 문장 불일치 1 — 이 뷰는 반대쪽이라 화면 오른쪽 문장이 맞으므로 정본 light.lines 쪽이 맞지 않는 것(오탐 아님, 기대 반대)

## 추가 발견

- Template A의 `the vanishing point [position]`을 쓰지 않음(경미, 검사기 미검출).

## 키트 결함

- kit/skills/image-prompt/location-view.md:38 — 열린 야외 장면이면 소실점 절을 빼도 되는지 불명확해 C05가 생략. 고침: "(소실점이 정해지지 않는 열린 야외는 이 절을 뺀다)" 한 줄.

## 총평

반대 뷰의 좌우·빛 뒤집기를 질문과 프롬프트 모두에서 정확히 처리.
