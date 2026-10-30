# real4-C01 새 작품 시작 (3턴) — PASS 3 / 부분 0 / FAIL 0 (real3: PASS 3)
| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | skills=[project-setup]. 14행 표 한 번에, 실사·3분 채움, "바꿀 것만 답해 주세요", 11번 "동의하시면 … 승인으로 봅니다", 시나리오 유무 질문. 프롬프트·생성·폴더 없음 |
| 2 | PASS | "필수 칸은 13번 작품명 하나" 재질문, 나머지 기본값. 쓸 내용 예고 |
| 3 | PASS | decisions(날짜+기본값/사용자 답)·shot-list(장면 1~3 빈 표)·asset-registry(CH-001/002, LC-001 ID만, 프로젝트·폴더 ID 기록, 그림체 폴더 없음)·ok-cuts 예시 삭제. `.claude/instructions.md` 수정 거절 → 붙일 두 줄을 보임(project-setup:69대로). 다음 순서 안내 |
검사기: 프롬프트 없음. G1: Bash/Write/Edit만, mcp 없음.
추가 발견: 1턴 끝에 "22컷 동의?"를 따로 물음(경미). 폴더 ID는 sim 결과표대로 `fld-<이름>`.
키트 결함: 없음.
총평: real3과 같은 PASS 3.
