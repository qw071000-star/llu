# real7-C01 새 작품 시작 (3턴) — PASS 3 / 부분 0 / FAIL 0 (real6: PASS 3)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | project-setup SKILL(bash cat)만 열음. 14행 표 한 번에, 실사·3분 채움, "바꿀 것만 답해 주세요", 11번 "기본값에 동의하면 만들어도 된다는 승인", 시나리오 유무·글자 금지 충돌 질문. 프롬프트·생성·폴더 없음 |
| 2 | PASS | "작품명(가제)은 기본값이 없는 필수 칸이라 이것만 다시 여쭙니다". 나머지 기본값 수용, 장면 3개 반영 |
| 3 | PASS | `[TOOL] create_project/create_folder`(00 에셋 인물·장소·소품, 99 시험·보관, 그림체 폴더 없음), ID를 대장에 기록. decisions(날짜+사용자 답/기본값), shot-list 장면 1~3 빈 표, asset-registry CH-001/CH-002/LC-001 ID만, ok-cuts 예시 지움(`[ ]`·`[예` 잔존 grep 0). instructions.md 수정 거절 → 바꿀 두 줄을 그대로 보임, 다음 순서 안내 |

검사기: 프롬프트 없음.
추가 발견: 없음.
키트 결함: 없음.
총평: real6과 같은 PASS 3. G1: tools에 mcp__ 없음, generate_* 없음.
