# real13-C48 화면 밖으로 나가기 — "3-3 영상 끝에 손녀가 화면 밖으로" (2턴) — PASS 1 / 부분 1 / FAIL 0 (real11: PASS 2 / 부분 0 / FAIL 0)

G1: 메타상 `mcp__` 도구 호출 없음, RUN 밖 읽기 없음(PASS). `git status`의 `PLAYER-RULES.md`·`SKILLS-INDEX.md` 삭제는 실행기 흔적.

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | 부분 | 내용 PASS: 사건 "시간표 한 번 더 보기 → 돌아서기 → 걸어 나가기 3개", 방향 화면 왼쪽 제안, 나가기는 끝 프레임 상태, 소리 칸 질문. 그러나 첫 줄에 `[N]번 [작업명]으로 진행합니다.`가 없음(`kit/instructions.md:41`, `kit/context/tasks.md:58`): "**시작 보고**"로 시작 |
| 2 | PASS | `acting` 열림, 검사 `OK — … 5069자`(WARN 1개를 고쳐 다시 돌림), "몸 절반이 왼쪽 밖, 이미 걷는 중", 카드 [3]~[6] `(제안값)`, 생성 없음, "영상으로 만들까요?" |

## 검사기
turn2 영상 프롬프트: `--kind video --refs 2 --seconds 8 --must-include(girl·light)` → `OK — video 프롬프트 5069자, 걸린 항목 없음`

## 추가 발견
- 카드 `이음새` 칸과 [1] 완료 조건이 `[ ]`로 남음(질문 때 3-4 이음새는 말했음). `kit/skills/production-session/cut-card.md` 기록 규칙.

## 키트 결함
- 첫 줄 규칙 미준수(C46과 같음, `kit/instructions.md:41`).

## 총평
프롬프트는 깨끗하고 t1 첫 줄만 빠졌다.
