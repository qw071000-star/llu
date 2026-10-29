# real13-C01 새 작품 시작 (3턴) — PASS 1 / 부분 2 / FAIL 0 (real11: PASS 3 / 부분 0 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | 부분 | `project-setup` 열고 14행 표 한 번에, 준 값(실사·3분·시골 정류장) 채움, 13번 작품명 "필수. 기본값이 없습니다", 11번 동의=승인 문구, 생성·폴더 없음. 그러나 첫 줄이 "**판단:** …"로 시작해 "[N]번 새 작품 시작으로 진행합니다."가 없음 (`kit/context/tasks.md:8`) |
| 2 | PASS | "작품명은 필수 항목이라 기본값으로 채울 수 없어서 다시 묻습니다." 장면 3개 반영, 도구·파일 0. 대본 유무를 한 번 더 물음(제안: 없음) — 메모 참조 |
| 3 | 부분 | diff: decisions.md 날짜+사용자 답/기본값, shot-list 장면 1~3 빈 행(줄거리 없음), registry CH-001·CH-002·LC-001 + 폴더 ID, ok-cuts 예시 줄·카드 삭제, CLAUDE.md 제목. `.claude/instructions.md` 수정 거절 → 바꿀 두 줄을 코드블록으로 보임(project-setup §4). 다음 순서 4줄. 감점: 프로젝트·폴더를 만들었다고 쓰고 prj-new-0001을 인용하면서 `[TOOL] create_project/create_folder` 줄이 하나도 없음("위의 [TOOL] 호출"이라는 문장만 있음) |

검사기: 프롬프트 없음.
추가 발견: t2가 1턴에 이미 물은 "대본/콘티 있나요?"를 다시 물음(`kit/instructions.md` 규칙 4 "같은 항목 두 번 금지"). `project-setup/SKILL.md:55`는 "없다고 답했으면" 안 묻는다고만 해서 미답일 때가 비어 있음.
키트 결함: ① `kit/instructions.md:41`+`kit/context/tasks.md:8` 첫 줄 규칙이 "시작 보고" 3줄 설명과 나란히 있어 또 "판단:"으로 시작함 → `instructions.md` "Output" 맨 위에 "Every answer that starts a task: line 1 is `[N]번 …으로 진행합니다.`, before any 판단/시작 보고 heading" 추가. ② `kit/skills/project-setup/SKILL.md:55` → "대본 유무는 1턴 표 밖 추가 질문이면 2턴에 다시 묻지 말고 '없음'으로 둔다" 추가. (통합 때문에 생긴 결함 아님)
총평: 질문·정본·폴더 처리는 정확, 첫 줄 누락과 [TOOL] 흔적 없음으로 부분 2.
