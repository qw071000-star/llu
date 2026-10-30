# real8-C05 장소 반대 방향 뷰 (2턴) — PASS 1 / 부분 1 / FAIL 0 (real7: PASS 2)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | image-prompt SKILL + location.md + location-view.md. 부모 `job-lc001v1`. 높이·샷 크기 / 랜드마크(시간표 화면 왼쪽·감나무 화면 오른쪽, "좌우가 뒤집힙니다") / 길 건너 종점 / 새 LIGHT LOCK(해 화면 오른쪽, 감나무 쪽) 4항목. 프롬프트·생성 없음 |
| 2 | 부분 | 프롬프트 내용은 PASS: `Do not inherit its camera angle, framing or composition.`, `not a horizontal mirror of the reference`, 카메라를 원본과의 관계로, MASTER GEOMETRY에 `as seen from across the road`, 새 LIGHT LOCK `from screen right, the persimmon-tree side`, `WITHOUT reframing` 없음, 동서남북 없음. "벤치 높이"를 0.45m로 해석하고 알림. 감점: 검사 때문에 `check_prompt.py --help`와 `grep … higgsfield-generation/SKILL.md`로 그 SKILL을 엶 — 프롬프트만 쓰는 턴이라 불필요(G7·routing.md §1 "프롬프트만 쓰면 열지 않는다"). 검사 줄은 image-prompt/SKILL.md:108에 이미 있음 |

검사기: `--kind image --refs 1` (답 코드블록) → `OK — image 프롬프트 2765자, 걸린 항목 없음`
추가 발견: MASTER GEOMETRY가 `RIGHT … sign / LEFT … tree`(기준 시점 문구 포함)와 뒤이은 `In this view … screen LEFT/RIGHT` 줄로 한 프롬프트에 두 방향이 공존하나 기준 시점이 명시돼 기대 충족.
키트 결함: 경미 — 플레이어가 검사 줄을 못 찾고 다른 SKILL을 연 것은 image-prompt/SKILL.md:108이 맨 끝 체크리스트라서. 고칠 한 줄: location-view.md 맨 끝에 "검사: `python3 .claude/skills/higgsfield-generation/check_prompt.py --kind image tmp/파일 --refs 1`" 줄을 둔다(각 단계 파일 끝에 검사 줄).
총평: 프롬프트·좌우·빛 PASS, 2턴 불필요한 SKILL 열람으로 부분. G1: tools에 mcp__ 없음, generate_* 없음.
