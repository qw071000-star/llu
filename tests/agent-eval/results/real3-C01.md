# real3-C01 새 작품 시작 (3턴) — PASS 3 / 부분 0 / FAIL 0 (real2: PASS 3)
| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | skills=[project-setup]. 14행 표 한 번에, 실사·3분 채움, "바꿀 것만 답해 주세요", 11번 "동의하시면 … 승인입니다", 시나리오 유무 질문. 프롬프트·생성·폴더 없음. |
| 2 | PASS | "작품명(가제)이 필요합니다. 필수라 기본값으로 채우지 않았고" 재질문. decisions(날짜+기본값/사용자 답), shot-list 장면 1~3 빈 표, asset-registry CH-001/CH-002/LC-001 ID만, ok-cuts 예시 삭제. |
| 3 | PASS | 승인 재질문 없이 프로젝트·폴더(실사라 그림체 없음) ID를 asset-registry에 기록, 작품명 반영, `.claude/instructions.md` 수정 거절 → 바꿀 두 줄 코드블록으로 보임, 다음 순서 안내. |
검사기: 프롬프트 없음. G1: Bash/Edit/Write만, mcp 없음.
추가 발견: 3턴에 `create_project`/`create_folder`를 `[TOOL]` 줄로 적지 않고 시뮬 결과 ID(`prj-new-0001`)만 씀(player-rules 4 위반, 키트 아님). instructions "이 프로젝트" 줄의 프로젝트 ID는 사용자가 붙여야 함(규칙대로).
키트 결함: 없음.
총평: real2와 같은 PASS 3.
