# real16-C01 새 작품 시작 (3턴) — PASS 10 / 부분 2 / FAIL 0

## 턴별 판정

| 턴 | 기대 | 판정 | 근거 |
|---|---|---|---|
| 1 | 첫 줄 "N번 작업명으로 진행합니다." | PASS | "1번 새 작품 시작으로 진행합니다." |
| 1 | 정본이 비었음을 알아채고 project-setup만 연다 (G4/G8) | PASS | meta skills [project-setup], reads decisions.md·shot-list.md만 |
| 1 | 14개 질문을 표 한 번에, 준 정보(실사·3분) 채움, 고정 문장, 대본 질문 1회 | PASS | 표 14행 "실사(사용자 답)" "전체 3분(사용자 답)"; "바꿀 것만 답해 주세요. 나머지는 기본값으로 합니다."; "대본이나 스토리보드가 있나요?" |
| 1 | 프롬프트·생성·폴더 생성·정본 쓰기 없음 (G1) | PASS | "이번 턴은 질문만 하고 정본은 쓰지 않습니다." tools=[Bash(ls)] |
| 2 | (2차) 작품명 필수를 다시 묻고, 받은 것(3개 장면·기본값)은 다시 묻지 않음 (G3) | PASS | "작품명(가제)은 필수라 기본값으로 채울 수 없고, 아직 받지 못했습니다." |
| 3 | 정본 초안 4개: decisions 날짜·근거, shot-list 장면 1~3 `대기`(시나리오 없음→빈 표), registry ID만(CH-001·CH-002·LC-001·PR-001), ok-cuts 비움 | PASS | diff: decisions "(2026-10-30, 기본값)"·"(사용자 답)" 줄마다; shot-list 장면 1/2/3 대기; ok-cuts 예시 줄·카드 삭제 |
| 3 | 틀 흔적 제거(예시 줄, [ ], [예:], 제목의 [작품명], CLAUDE.md 제목) | PASS | grep "[ ]/[예:/[작품명]" 남은 것 없음; CLAUDE.md `「빈 정류장」` |
| 3 | Higgsfield 프로젝트·폴더 생성(1턴 11번 기본값 동의가 승인) 후 ID 기록 | 부분 | registry `prj-new-0001`·`fld-00 에셋`·`fld-99 시험·보관` 기록, 그러나 답에 `[TOOL] create_project/create_folder` 줄이 0개(플레이어 규칙 4: 쓰면 [TOOL]로 적는다). 키트가 `create_project`를 어디에도 이름 짓지 않음(결함 1) |
| 3 | "이 프로젝트" 세 줄(작품명·프로젝트 ID·정본 위치) — 보호 경로 거절 시 줄을 그대로 보여 붙여 넣게 함 | PASS | "- Title: 「빈 정류장」 · Higgsfield project: 빈 정류장 (`prj-new-0001`)\n- Canon location: repo `project/`" (.claude/instructions.md 5·8번째 줄) |
| 3 | 다음 순서 안내(인물 시트→장소→소품→컷 카드), 그림체 단계는 실사라 건너뜀 | PASS | "1. 인물 시트(할아버지, 손녀) 2. 장소 마스터 3. 소품 4. 컷 나누기와 컷 카드 발행" |
| 전체 | G2 한국어·짧게 | 부분 | T1 "캔온(정본)이 비어 있는지 확인하고" — canon 음차(키트 결함 2) |
| 전체 | G1 mcp 호출·시킨 적 없는 생성 없음 | PASS | tools에 mcp 없음, [TOOL] generate 없음 |

## 검사기 결과

- (프롬프트 없음): 코드블록 없음 — 검사 대상 아님

## 추가 발견

- T3 `shot-list.md`가 장면 1~3 줄만 있어 컷 번호(1-1…)는 아직 없음. 시나리오 없음이므로 키트 §2 "scene numbers in an empty table"대로(문제 없음).
- T3 `.claude/instructions.md`는 실제로 고쳐지지 않았다(git status에 없음). 플레이어가 거절됐다고 보고하고 줄을 제시 — 키트 §4 절차와 일치.

## 키트 결함

- kit/skills/project-setup/SKILL.md:52 — 프로젝트 생성 도구(`create_project`)가 키트 어디에도 없음(grep 0건), 폴더 도구 `create_folder`만 higgsfield-generation/SKILL.md:37에 있음 → 플레이어가 호출 없이 "만들었습니다"만 보고. 고침: :52에 "프로젝트는 `[TOOL] create_project`, 폴더는 `create_folder`로 만들고 받은 ID를 대장에 적는다" 추가.
- kit/instructions.md:12 (:20·:24의 'canon') — 영어 'Canon'이 한국어 답에 '캔온'으로 샘. 고침: :12에 "한국어 문장에서는 항상 '정본'이라고 쓰고 canon/캔온은 쓰지 않는다" 추가.

## 총평

질문표·정본 초안·다음 순서는 정확. Higgsfield 생성은 [TOOL] 흔적 없이 보고만 해서 부분 1건.
