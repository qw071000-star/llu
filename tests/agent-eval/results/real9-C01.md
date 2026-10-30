# real9-C01 새 작품 시작 (3턴) — PASS 3 / 부분 0 / FAIL 0 (real8: PASS 3 / 부분 0 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `project-setup` 스킬 + 정본 4개만 읽음. 14행 표 한 번에, 사용자 답(실사·3분·시골 정류장·인물 둘) 채움, "바꿀 것만 답해 주세요", 11번 "동의하시면 만들어도 된다는 승인으로 봅니다", 작품명(필수)·시나리오 유무 질문. 프롬프트·생성·폴더 없음 |
| 2 | PASS | "작품명은 필수 칸이라 기본값으로 채우지 않았습니다 … 이것만 다시 묻습니다." decisions(날짜+사용자 답/기본값), shot-list 장면 1~3 빈 표(줄거리 지어 쓰지 않음), asset-registry CH-001/CH-002/LC-001 ID만, ok-cuts 예시 줄·카드 삭제(diff 확인). 폴더는 아직 안 만듦 |
| 3 | PASS | 프로젝트·폴더 ID(`prj-new-0001`, `fld-인물` 등)를 대장 폴더 표에 기록, 그림체 폴더 없음(실사), 작품명을 5개 파일 제목에 반영. `.claude/instructions.md` 수정이 거절돼 바꿀 두 줄을 그대로 보임. 다음 순서(컷 나누기 → 인물 시트 → 장소) 안내 |

검사기: 프롬프트 없음.
추가 발견:
- 3턴 답에 `[TOOL] create_project/create_folder` 줄이 하나도 없다(`grep TOOL out/turn3.md` = 0). "Higgsfield 호출은 시험 환경이라 실제로 하지 않았습니다"라고만 쓰고 `sim/higgsfield.md` 결과표 ID를 인용했다. PLAYER-RULES 4번 위반(시뮬레이션 규칙 이지 키트 규칙은 아님). G1(실제 mcp 호출 없음)은 PASS.
- shot-list를 `1-1 대기` 대신 `장면 1/2/3` 빈 줄로 둠. 시나리오가 없으면 빈 표여도 된다는 기대 안.
- `PLAYER-RULES.md`, `SKILLS-INDEX.md`가 git status에서 삭제로 보임(하네스 쪽 일, 플레이어 오류 아님으로 판단).
키트 결함: 없음. (`.claude/instructions.md` "이 프로젝트" 줄은 보호 경로라 사용자가 직접 고쳐야 하는 시험 환경 제약, real8과 같음.)
총평: real8과 같은 PASS 3. G1: tools에 mcp__ 없음, generate_* 없음. 읽기도 정본 4개와 스킬 1개로 최소.
