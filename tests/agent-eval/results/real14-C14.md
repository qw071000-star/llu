# real14-C14 "표정은 2-1처럼, 2-2 영상" (2턴) — PASS 2 / 부분 0 / FAIL 0 (real13: PASS 1 / 부분 1 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | 첫 줄 "13번 실사·인물 영상으로 진행합니다." `ok-reuse.md`·`live-action.md` 엶, `acting` 안 엶(질문 턴), 카드 파일 없음("이번 턴은 질문만 하므로"). 2-1 영상 카드의 할아버지 `CHARACTER_ACTING`+입 금지만 가져온다고 밝힘. `[TOOL] list_folders`·`list_project_assets`. 질문 4개(쓰다듬기 동작·시간 / 끝 상태 / 배경 움직임 / 시작 이미지 요소 이름) 제안·이유. 렌즈 85mm는 "기본값으로 씀". 마지막 질문(요소 이름)은 불필요에 가깝다 |
| 2 | PASS | `acting` SKILL과 `cut-card.md`를 엶(meta reads). 15블록 전문. `CHARACTER_ACTING`의 2-1 할아버지 줄 글자 그대로, 쓰다듬는 손은 뒤에 새 문장으로 붙임. 손은 모두 `screen-left hand, nearer the tree`. 입 잠금 `no parted lips, no mouthing`(2-1보다 강화, 보고함). 카드 `cuts/2-2.md` v0를 `(제안값)`으로 기록, [7] "가져온 OK: 2-1 영상 — 표정". 위험 6줄, "추정" 2줄, 생성 안 함 |

검사기: `python3 kit/skills/higgsfield-generation/check_prompt.py --kind video C14t2_1.txt --refs 3 --seconds 8 --must-include grandpa+bag+light+acting_2-1` → `OK — video 프롬프트 4998자, 걸린 항목 없음` (플레이어도 WARN 1건을 고쳐 재검사)

real13 감점 해소: 2턴에서 새 연기 문장을 쓰면서 `acting`을 안 열었던 문제 — 해소(이번엔 열었다; `live-action.md:3`의 "새 문장 하나라도 더하면 acting을 연다"가 효과).

추가 발견: 도구 사이 영어 한 줄("Fix the WARN by giving that hand a screen side.") 노출. 첫 줄이 두 번 출력됨.

키트 결함: C02와 같은 `kit/instructions.md:12`만.

총평: real13의 G8 감점이 해소돼 2턴 모두 PASS.
