# real11-C05 장소 반대 방향 뷰 (2턴) — PASS 2 / 부분 0 / FAIL 0 (real9: PASS 2 / 부분 0 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `image-prompt` SKILL + `location.md` + `location-view.md` 엶. 부모 LC-001-V1(`job-lc001v1`), 카메라 높이·위치·끝점·남길 것(표지판 화면 왼쪽, 감나무 화면 오른쪽)·렌즈·빛(새 LIGHT LOCK `…from screen right, the persimmon-tree side…`)·이름을 제안값+이유로 7개 한 묶음. 좌우·빛이 뒤집힌다고 먼저 알림. 프롬프트·생성 없음. (라벨 오류: "4번 장소 새 시점" — tasks.md는 7번) |
| 2 | PASS | `Do not inherit its camera angle, framing or composition.` 있음, `WITHOUT reframing` 없음. 카메라를 "원본 카메라 위치로 되돌아 보는" 관계로 씀(`reverse` 한 단어 아님). `This is a newly observed opposite direction … not a horizontal mirror` 있음. MASTER GEOMETRY에 기준 시점 `(as seen from across the road …)` + `Except:` 줄. 화면 기준 문장 `timetable sign … at screen LEFT … persimmon tree … at screen RIGHT`, LIGHT LOCK `from screen right, the persimmon-tree side`. 동서남북 없음. "벤치 높이"의 두 뜻(0.45m/1.1m)을 짚고 한쪽을 골라 알림. 레지스트리 초안 기록(diff) |

검사기: `--kind image C05_t2 --refs 1` → `OK — image 프롬프트 2499자, 걸린 항목 없음`. (참고: `--must-include light`를 붙이면 FAIL — 부모 뷰의 LIGHT LOCK이 아니라 뒤집힌 새 LIGHT LOCK이 맞으므로 검사기 오탐이 아니라 기대 오류. 시나리오도 `--must-include`를 요구하지 않음)
추가 발견: 7개 질문에 렌즈(35mm=63°)를 넣었다. must-ask는 렌즈 never-ask이지만 장소 뷰에는 "시작 이미지 mm"가 없어 위반으로 보지 않음. 샷 크기(미디엄 와이드)는 안 물었는데 사용자가 2턴에 직접 답함.
키트 결함: 없음.
총평: 좌우·빛 뒤집기까지 정확.
