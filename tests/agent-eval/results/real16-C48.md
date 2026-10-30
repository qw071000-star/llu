# real16-C48 화면 밖으로 나가기 (2턴) — PASS 11 / 부분 0 / FAIL 0

> 채점: tests/agent-eval/runs-real16/C48/out/turn*.md·meta.json, git diff. 기준: grader-rules.md, scenarios.md(G1–G9 + C48), kit/.

## 턴별 판정표

| 턴 | 기대 항목 | 판정 | 근거 |
|---|---|---|---|
| 1 | 첫 줄 | PASS | "13번 실사·인물 영상으로 진행합니다." |
| 1 | 퇴장 방향 제안 + 다음 컷 3-4 이음새 | PASS | "1. 퇴장 방향: 제안 — 화면 왼쪽 … 3-4는 손녀 없이 할아버지만" · "3-4의 인물 자리가 연속성 표에 미정" |
| 1 | 나가기는 끝 프레임 상태로 | PASS | "5. … 마지막 프레임에서 몸 절반이 프레임 밖(화면 왼쪽)이고 이미 걷는 중" |
| 1 | 사건 수 확인 | PASS | "타이밍: 제안 — 사건 3개 … 사건이 3개 이내라 컷을 나누지 않아도 됨" |
| 1 | 목표 변경 범위(이 컷만/전체) 먼저 짚기 | PASS | "2. 목표 변경의 범위: 제안 — 이 컷만 … 목록 줄 수정은 핸드오프 [5]로" |
| 1 | 질문 턴에 acting 안 엶·live-action.md는 엶(시작 이미지 있음) | PASS | reads: shot-list, video-prompt/SKILL, 3-3 카드, decisions, registry, live-action.md, ok-cuts |
| 2 | 15블록 프롬프트·acting 열기 | PASS | reads: acting/SKILL.md, cut-card.md; 블록 14개(+PRE_SHOT 생략: 시작 이미지가 0:00) |
| 2 | 퇴장을 끝 프레임 상태로 씀·화면 쪽 손 | PASS | "The shot ends with her body half outside the frame at the screen-left edge, already walking." · "the screen-right hand, nearer the sign" |
| 2 | 검사기(G7) | PASS | 2회 실행 후 "통과(4,500자, 걸린 항목 없음)". 내 재검사: "OK — video 프롬프트 4500자, 걸린 항목 없음" |
| 2 | 카드 v2 갱신·(제안값)·[1] 완료 조건 | PASS | diff: "카드 버전: v2 · 2026-10-30", [1] 목표·완료 조건 갱신, "(제안값)" 표기. shot-list·3-4 연속성은 안 고침("핸드오프 [5]로 넘기겠습니다") |
| 2 | 블록 밖 모드·참조·모델·해상도·길이·저장 + 위험 목록 + 생성 안 함 | PASS | "- 저장 폴더: fld-3-3", "실패 위험 (막는 문장) 1–5", ""그대로"나 "좋아"는 생성 명령으로 받지 않습니다." |

## 검사기 결과

C48 T2 코드블록 1개(영상, 참조 2, 8초), must-include = girl/light 2문장:
`OK — video 프롬프트 4500자, 걸린 항목 없음` (종료 0)

## 추가 발견

- 카드 [8]을 "CH-002 WARDROBE · LC-001-V1 LIGHT LOCK"으로, [10] 라벨을 "난 실패"로 쓴 것은 cut-card.md 템플릿 그대로(키트 쪽 문제).
- PRE_SHOT_CONTINUITY 없음 — 시작 이미지가 0:00을 정하고 3-2와 영상 연결이 없어 타당.

## 키트 결함

- `kit/skills/production-session/cut-card.md:26` "[10] 난 실패" 오기(위 C45와 동일) — 플레이어가 기존 카드의 "알려진 위험" 라벨을 템플릿 라벨로 바꿔 씀.

## 총평

퇴장·이음새·사건 수·검사까지 키트대로 처리했다.
