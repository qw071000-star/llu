# real11-C48 화면 밖으로 나가기 — "3-3 영상 끝에 손녀가 화면 밖으로" (2턴) — PASS 2 / 부분 0 / FAIL 0 (real9: PASS 2 / 부분 0 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `production-session/SKILL.md`, `video-prompt/SKILL.md`, `live-action.md`, 자기 컷 3-3 카드·OK 대장. `acting`은 아직 안 엶(프롬프트 쓰는 턴에 열라는 `tasks.md` 13번 행 준수). 첫 줄 "프롬프트를 쓰기 전에 확인할 것이 7개 있습니다". 나가는 쪽 "화면 왼쪽, 지붕 끝과 벤치 쪽(이유: 3-1에서 손녀가 벤치 쪽으로 걸었으므로 방향이 이어짐, 길로는 나가지 않음)". 마지막 프레임 "몸 절반이 프레임 밖이고 이미 걷는 중". 사건 수 확인: 시간표 확인·돌아섬·걸어 나감 = 3개, 타이밍 3 / 1.5 / 3.5초. 컷 내용 변경("돌아선다" → "돌아서서 나간다")을 이 컷만인지 전체인지 묻는 항목 포함. 카드 [1]을 `(제안값)`으로 갱신(`production-session` §1: 사용자가 [1]과 다른 방향을 줄 때 허용). 생성 없음 |
| 2 | PASS | 15블록 코드블록 1개. `LEFT and RIGHT are SCREEN directions …`, `GIRL walks toward the screen-left edge along the shelter side and never steps into the road`, 끝 상태 `The shot ends with her already walking, half of her body outside the frame at the screen-left edge`, `FINAL_FRAME` 필수 항목, 손은 `the screen-right hand, nearer the sign`, 걸음은 `Walk — small even steps …` + `running = failed take`, `Exactly 1 person`. 블록 밖 모드·참조 2·모델·480p·8초·`fld-3-3`, 위험 5개(추정 표기), 보낼지 질문. 카드 [1]·[3]~[6]을 `(제안값)`으로 기록(diff 확인). 검사: 첫 실행 WARN(PHYSICS의 손에 화면 쪽 없음)을 고치고 재실행해 0이 되었다고 보고, `tmp/` 삭제 |

## 검사기
내 실행 `--kind video --refs 2 --seconds 8 --must-include girl+light`: `OK — video 프롬프트 4433자, 걸린 항목 없음`

## 추가 발견
- G1 위반 없음(`sim/higgsfield.md`를 읽었으나 결과를 답에 쓰지 않음). 2턴에서 `acting/SKILL.md`를 열음 — 새 CHARACTER_ACTING을 쓰는 턴이라 필요.
- 1턴 질문이 7개로 많으나 정본 빈칸(끝 자세·동선·시선·타이밍·소리)이 실제로 비어 있어 모두 필요.

## 키트 결함
없음.

## 총평
나가기를 "이미 걷는 중, 몸 절반 프레임 밖"의 끝 상태로 쓰고 사건 3개를 세어 규칙대로 처리했다.
