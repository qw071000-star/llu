# real3-C05 장소 반대 방향 뷰 (2턴) — PASS 2 / 부분 0 / FAIL 0 (real2: 부분 2 → 개선)
| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `image-prompt/SKILL.md`+`location.md`+`location-view.md`. 카메라 방식 "먼 끝으로 이동, 정류장 뒷벽 쪽에서 원래 카메라 자리를 되돌아봄"(real2 오제안 해소). 3항목(높이·샷 크기·렌즈 / 랜드마크 3개 — 시간표 화면 왼쪽·감나무 화면 오른쪽 / 길 건너 종점) 제안값+이유. "먼저 짚을 것"에 뒤집힌 LIGHT LOCK `Low dusk sun from screen right, the persimmon-tree side …`. |
| 2 | PASS | `Do not inherit its camera angle, framing or composition.` 있음, `WITHOUT reframing` 없음, CAMERA를 원본 카메라와의 관계("looking back … toward the original camera position")로 씀, `not a horizontal mirror`, MASTER GEOMETRY `(as seen from across the road …)` + `Except:`, `In this view … sign pole at screen LEFT … tree at screen RIGHT`, 화면 오른쪽 LIGHT LOCK, 동서남북 없음. `<<<loc_busstop_road_v1>>>` 태그 1개=참조 1. 모드·참조 등은 블록 밖 일반 줄. 검사 실행. |
검사기(`--kind image --refs 1`): `OK — image 프롬프트 2744자, 걸린 항목 없음`. (`--must-include light.lines`는 V1의 screen-left 문장이라 V2에서 FAIL이 나는 것이 맞음 — 채점 대상 아님.)
추가 발견: 2턴 끝에 "높이를 0.45m로 하려면 알려 주세요"로 이미 정한 항목을 다시 물음(지침 4번 "같은 항목을 두 번 묻지 않는다"에 걸릴 수 있으나 "벤치 높이" 모호 해석 확인이라 경미).
키트 결함: 없음(real2 결함 두 건 `image-prompt/SKILL.md:21` 꺾쇠, `location-view.md` 카메라 방식 기준 모두 이번엔 증상 없음).
총평: real2의 태그 WARN·카메라 오제안이 사라짐.
