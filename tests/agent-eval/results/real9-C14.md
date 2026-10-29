# real9-C14 "표정은 2-1처럼, 2-2 영상" (2턴) — PASS 2 / 부분 0 / FAIL 0 (real8: PASS 2 / 부분 0 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `video-prompt` SKILL + `production-session` SKILL + `ok-reuse.md` + `live-action.md`, OK 대장 2-1 영상 카드·2-2 시작 이미지 카드. 표정만 가져오고 카메라(2-1 63° 원경 ↔ 2-2 85mm)·동작은 안 가져온다고 구분("카메라·구도·동작은 가져오지 않고 표정(연기 줄)만"). 표정/사건 수(1)/타이밍(쓰다듬기)/끝 상태/환경·소리 5항목을 제안값+이유로. 렌즈는 "시작 이미지의 85mm(29°)"로 묻지 않음. `acting`은 질문 턴에 열지 않음 |
| 2 | PASS | `acting` SKILL 열고 15블록 전문. `CHARACTER_ACTING` 첫 줄이 2-1 카드 줄과 글자 그대로(`acting_2-1.lines` 통과)이고 손·호흡 문장은 마침표 뒤 새 문장으로 더함(가져온 줄/더한 줄 구분 보고). 시선 `eyes stay on the road`, `He never looks at the camera`, 입 잠금 `no parted lips, no mouthing`+Forbidden, `[OPTICS]` 29° + 관찰 결과 3개, 의상·가방·LIGHT LOCK 글자 그대로, 손은 `the screen-left hand, nearer the tree`. 블록 밖에 모드·참조 3·모델·480p·8초·소리·폴더. 위험 7개. 카드 `project/cuts/2-2.md` 신규: [7] `가져온 OK: 2-1 영상 — 표정`, 제안값 표시. 검사 WARN 3건(화면 쪽 없는 손)을 고쳐 0으로 만든 뒤 보임 |

검사기: `check_prompt.py --kind video --refs 3 --seconds 8 --must-include grandpa+bag+light+acting_2-1` → `OK — video 프롬프트 5158자, 걸린 항목 없음`
추가 발견: 카드 [7]에 "CHARACTER_ACTING 두 줄"이라 적었으나 글자 그대로 옮긴 것은 2-1 줄 하나(+새 문장). 요소 이름 `ff_2-2_v1`은 추정이라 밝힘(좋음). 눈의 삶 문장은 `acting` §5 고정 문장으로 추가했다고 명시.
키트 결함: `kit/instructions.md:54-55` 검사 명령에 `--must-include` 플래그가 없어 플레이어가 `check_prompt.py --help`와 `grep must-include check_prompt.py`를 돌림(C10과 같은 결함, 경미).
총평: real8과 같은 PASS 2. G1: mcp__ 없음, 생성 없음.
