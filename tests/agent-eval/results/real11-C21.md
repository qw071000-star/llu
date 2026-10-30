# real11-C21 장소 시대 교체 — 한 생성에 한 층 (2턴) — PASS 2 / 부분 0 / FAIL 0 (real9: PASS 1 / 부분 1 / FAIL 0 → real10 재실행 PASS 2)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | 읽기: `image-prompt` SKILL → `location.md` → `location-edit.md` + 정본(registry·decisions·ok-cuts). 지침 4번 정확한 첫 줄 "프롬프트를 쓰기 전에 확인할 것이 4개 있습니다…". 항목 1: "정본(1990년대 초)은 그대로 두고 이 장소 한 장만 2020년대 변형(별도 STATE)" — 정본 시대와 다름을 짚고 범위를 물음. 항목 2: "4번에 나눕니다 … 레이어 하나씩 … ① 표지판 → ② 지붕·바닥·도로면 → ③ 벤치·표지판 기둥·형광등 → ④ 필름 질감을 디지털 선명도로 … 이번에는 ①만" = 한 층 한 생성 + 순서 제안. "기본값으로 씀: GPT Image 2.5, 1k, 16:9 … 저장 폴더 `fld-locs`". 프롬프트 없음 |
| 2 | PASS | "순서만 답하셨으므로 나머지 3개는 제안값으로 진행합니다" 한 줄. 틀 2: `this step changes only its IDENTITY AND TEXT`, CHANGE는 시간표 판 → 평판 표지판(같은 위치·크기·기둥), REMOVE 있음, PRESERVE에 다른 층(walls·floor·road·roof·bench·pole·tube)과 건물 부피, `ONLY CHANGE: IDENTITY AND TEXT`. `1990s` 시대 잠금 없음, 마지막 줄은 `No legible text anywhere.` 블록 밖에 모드·참조·모델·해상도·길이·폴더 한 줄씩, 실패 위험 4개(각 문장 하나), 레지스트리에 `LC-001-V2` 초안(제안값) 기록, `tmp/` 삭제, "이 프로젝트 1k로 보낼까요?"로 끝냄(생성 안 함) |

검사기 (`--kind image --refs 1 --must-include light.lines`, 코드블록 1개):
`OK — image 프롬프트 1556자, 걸린 항목 없음`
플레이어도 같은 줄을 단독 Bash로 돌림(메타 `check_prompt.py --kind image tmp/lc001v2_step1.txt --refs 1 --must-include tmp/lc001v2_fixed.txt`).

추가 발견
- 1턴·2턴 모두 `tasks.md` §1의 "8번 장소 고치기로 진행합니다." 한 줄이 없다(지침 4번 첫 줄이 우선한 것으로 보임). 점수에는 넣지 않음.
- 형광등을 ③ FURNITURE/FIXTURES에 묶음. `location-edit.md` 틀 2에는 별도 `LIGHTING` 층이 있어 형광등을 어느 층에 둘지 모호하다(2턴 PRESERVE에는 불이 꺼진 채로 보존이라 문제 없음).

키트 결함: 없음(공통 1번 제외). 선택: `kit/skills/image-prompt/location-edit.md:50`에 "고정 조명기구(형광등 등)는 FIXTURES, 켜고 끄는 상태·색은 LIGHTING" 한 줄.

총평: 층 분리·정본 시대 충돌 알림·1990s 잠금 제거까지 모두 충족. real10 재실행과 같은 PASS 2.
