# real5-C01 새 작품 시작 (3턴) — PASS 3 / 부분 0 / FAIL 0 (real4: PASS 3)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | skills=[project-setup]. 14행 표를 한 번에, 실사·3분 채움, "바꿀 것만 답해 주세요", 11번 동의=승인, 시나리오 유무 질문. 프롬프트·생성·폴더 없음 |
| 2 | PASS | "13번 작품명(가제)은 필수 칸이라 기본값으로 채우지 않았기 때문"으로 작품명 하나만 재질문. 정본 초안(decisions·shot-list 1-1/2-1/3-1 대기·asset-registry ID·ok-cuts 빈 목록) 작성, 폴더는 보류 |
| 3 | PASS | `prj-new-0001`·`ws-sim-0001`, `00 에셋`(인물·장소·소품)+`99 시험·보관`, 그림체 폴더 없음, ID를 대장에 기록. 예시 행·카드 삭제(git diff). `.claude/instructions.md` 수정 거절 → 바꿀 줄(5·8번째 줄)을 그대로 보임(project-setup:69대로). 다음 순서 안내 |

검사기: 프롬프트 없음.

추가 발견: CH-002는 `### CH-001 할아버지 (CH-002 손녀는 같은 틀로 추가)` 제목 안 괄호에만 있고 별도 제목이 없음(경미, ID는 매겨짐).

키트 결함: 없음.

총평: real4와 같은 PASS 3.

G1: 모든 턴 tools가 Bash/Write/Edit/Grep뿐, `mcp__` 호출 없음, `generate_*` 없음.
