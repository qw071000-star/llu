# real8-C10 영상, 일부만 답함 3-3 (3턴) — PASS 3 / 부분 0 / FAIL 0 (real7: PASS 2 / 부분 1)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | video-prompt SKILL + live-action.md(acting 안 엶, 질문 턴). 소리 / 끝 상태 / 시선 / 손 / 타이밍 / 연기 범위 / 이음새 7항목 제안값+이유. 렌즈는 묻지 않고 "시작 이미지 50mm(47°)" 기본값 줄. 사건 2개. 시작 이미지 `job-ff-3-3` 앎 |
| 2 | PASS | 렌즈·대사만 반영, 나머지 6개는 제안값으로 카드 3-3 v2에 기록. 망원이 시작 이미지 50mm와 부딪친다고 A(85mm 새 시작 이미지) / B(50mm 유지) 한 번만 물음 — 시나리오 허용 경로. 프롬프트 안 씀 |
| 3 | PASS | `acting` 스킬을 열고 15블록 전문. 렌즈 `about 47°` + 관찰 결과 3개(mm 없음), GIRL 의상·LIGHT LOCK 글자 그대로, AUDIO 대사 없음→효과음만, 손은 `the screen-right hand, nearer the sign`, 위험 6개, 보고 항목별, 생성 안 함. 카드 3-3 [1][3][4][5][6][10] 기록(제안값/사용자 답 구분) |

검사기: `--kind video --refs 2 --seconds 8 --must-include girl+light` (3턴 답 코드블록) → `OK — video 프롬프트 5446자, 걸린 항목 없음`
추가 발견: 없음. 2턴의 렌즈 충돌 질문은 시나리오가 허용(키트 모호 아님).
키트 결함: 없음. real7에서 제안한 "새 CHARACTER_ACTING을 쓰면 acting 먼저"는 이번엔 지켜짐.
총평: real7의 부분(3턴 acting 미열람)이 PASS로 올라감. G1: tools에 mcp__ 없음, generate_* 없음.
