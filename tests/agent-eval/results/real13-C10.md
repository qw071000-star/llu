# real13-C10 영상, 일부만 답함 3-3 (3턴) — PASS 3 / 부분 0 / FAIL 0 (real11: PASS 2 / 부분 1 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | "13번…" 첫 줄. `video-prompt`+`live-action.md`, `acting`은 안 엶(질문 턴). 질문 5개(끝 상태 / 사건 3개 타이밍 / 시선 / 연기 범위 / 소리). 렌즈·길이·소리 기본값은 "기본값으로 씀: … 렌즈는 시작 이미지의 50mm(47°)". 3-1 끝과 시작 이미지가 다르다는 참고 한 줄 |
| 2 | PASS | 렌즈=망원·대사 없음 반영, "몰라"는 제안값으로 카드 3-3 [1][3][5][6] 기록(diff, `(제안값)`). 망원이 시작 이미지 50mm와 충돌한다고 한 번 확인(시나리오상 PASS), 대안(85mm 시작 이미지부터) 제시 |
| 3 | PASS | `acting` SKILL 엶(메타 reads). 15블록 전문: OPTICS `Diagonal field of view about 47°` + 관찰 결과 3 + 심도, mm 없음. WARDROBE·LIGHT LOCK 글자 그대로, AUDIO 대사 없음 + `no attempt to speak, no parted lips, no mouthing`, `LEFT and RIGHT are SCREEN directions…`, 손은 `screen-right hand, nearer the sign`. CHARACTER_ACTING: 목표·손의 일·호흡·눈·범위 양 끝 failed take·3초 돌기. 사건 3개. 카드 [4] 렌즈 기록 |

검사기: `--kind video --refs 2 --seconds 8 --must-include girl+light` → `OK — video 프롬프트 5497자, 걸린 항목 없음`
추가 발견: Forbidden에 `Legible text on the timetable`을 예상 위험으로 넣음(`live-action.md` 15번 행: 실제로 난 실패만). 경미.
키트 결함: 없음. real11의 `acting` 누락이 `live-action.md` 맨 위 문장 + `video-prompt/SKILL.md:10`으로 해결됨.
총평: PASS 3.
