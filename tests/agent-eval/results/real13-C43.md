# real13-C43 연기 지적 — "1-2에서 할아버지 걸음이 너무 젊어 보여" (1턴) — PASS 0 / 부분 1 / FAIL 0 (real11: PASS 1 / 부분 0 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | 부분 | 첫 줄 "15번 영상 결과 고치기로 진행합니다." `video-prompt` SKILL(§0)만 열고 `fixes.md`는 안 열었다(걸음 나이는 §0 표로 충분). 1-2가 팀원 지수 작업이고 프롬프트가 빈 값이라 원문을 못 봤다고 밝히고, 결과 지적은 재생성 지시가 아니라고 함(추정 표기). 걸음 값을 제안: `"… walk" — 짧고 좁은 보폭, 작은 팔 흔들림, 발을 끌듯, 무게중심 낮게. 성큼성큼 걷는 젊은 걸음 = 실패 테이크.`(§0 걸음 나이 줄: 보폭·팔·발·무게중심 + 반대 걸음 failed take). 승인 컷이라 새 테이크 확인. 흠: "job-v-1-2의 프롬프트는 팀원 계정 작업이라 빈 값으로 조회되어"라고 sim 결과를 인용하면서 `[TOOL] get_project_asset_prompt(job-v-1-2)` 줄이 답에 없다(meta tools는 Bash뿐, `sim/higgsfield.md`를 grep). 플레이어 규칙 4와 `instructions.md:39`(팀원 작업은 `get_project_asset_prompt`)에 어긋남 |

검사기: 프롬프트 없음.

추가 발견
- 걸음 이름을 `"할아버지 walk"`처럼 한국어 섞어 제안했다(프롬프트는 영어여야 함). 제안 단계라 경미.
- "1-2 승인 설정을 따릅니다"라고 썼으나 팀원 컷의 설정은 본 적이 없다(추정 표시 없음).

키트 결함
- `kit/instructions.md:39`: "teammate's work: `get_project_asset_prompt`"가 있어도 "조회했으면 `[TOOL]` 줄로 적는다"는 형식 규칙이 키트에는 없다(시험 환경 규칙에만 있음). 시험 하네스 쪽 문제일 수 있으나, 고침: 규칙 10 "Report item by item"에 "state which lookup (`[TOOL] …`) a quoted result came from" 한 구절.

총평: 걸음 나이 처리와 팀원 컷 처리는 맞았고, sim 조회를 `[TOOL]` 줄 없이 인용했다.
