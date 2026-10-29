# real7-C10 영상, 일부만 답함 3-3 (3턴) — PASS 2 / 부분 1 / FAIL 0 (real6: PASS 2 / 부분 1)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | video-prompt SKILL + live-action.md(acting 안 엶, 질문 턴). 사건 2개 / 돌아서는 방향·끝 / 시선·손 / 타이밍 / 대사 / 연기 범위 / 이음새 7항목 제안값+이유. 렌즈는 묻지 않고 "시작 이미지 50mm≈47°" 기본값 줄. 시작 이미지 `job-ff-3-3`을 앎 |
| 2 | PASS | "나머지는 몰라"를 제안값 처리, 카드 [1][3][4][5][6] 기록(제안값/사용자 답 구분). 망원이 시작 이미지 50mm와 부딪친다고 짚고 A 유지 / B 새 퍼스트 프레임(85mm≈29°) 한 번만 물음 — 시나리오가 허용한 경로. 프롬프트 안 씀 |
| 3 | 부분 | 15블록 전문, 렌즈 `about 47°` + 관찰 결과 3개(mm 없음), GIRL 의상·LIGHT LOCK 글자 그대로, AUDIO 대사 없음→효과음만, 손은 전부 `screen-right hand, nearer the sign`(real6의 `farther` 모순 없음), 위험 8개, 생성 안 함. 감점: 새로 쓴 `CHARACTER_ACTING`(GIRL: wants to be sure … lets go of hoping)인데 `acting` SKILL을 3턴 어디서도 열지 않음(meta reads 비어 있음, G8). 목표 문장도 `[상대]에게 + 동사` 형식이 아님 |

검사기: `--kind video --refs 2 --seconds 8 --must-include girl+light` (답 코드블록, 플레이어 `out/prompt_3-3_video.txt`와 diff 없음) → `OK — video 프롬프트 4724자, 걸린 항목 없음`
추가 발견: (1) 2턴 카드 편집에서 "[10] 난 실패 → 막는 문장"은 키트 틀(cut-card.md:26) 라벨 그대로라 정상. (2) 3턴 "요소 이름 `ff_3-3_v1` vs `job-ff-3-3`" 되묻기는 해 볼 만하나 경미.
키트 결함: 없음(플레이어 누락). 다만 routing.md:25·live-action.md:21에 이미 "새로 쓰면 acting을 연다"가 있는데 3턴처럼 앞 턴이 질문 턴이었던 체인에서는 놓침. 보강안: video-prompt/SKILL.md §0 점검표 맨 위에 "15블록 전문을 쓰는 턴: CHARACTER_ACTING을 새로 쓰면 먼저 acting/SKILL.md" 한 줄.
총평: 질문·렌즈 충돌 처리는 PASS, 3턴 acting 미열람으로 부분. G1: tools에 mcp__ 없음, generate_* 없음.
