# real11-C43 연기 지적 — "1-2에서 할아버지 걸음이 너무 젊어 보여" (1턴) — PASS 1 / 부분 0 / FAIL 0 (real9: PASS 1 / 부분 0 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | "15번 영상 결과 고치기". `[TOOL] get_project_asset_prompt(job-v-1-2)` 줄을 적고 결과를 인용("프롬프트가 빈 문자열입니다. 지수 님 계정에서 만든 영상이라 원래 프롬프트를 볼 수 없습니다"), 원인 단정 없이 "추정". "바로 고쳐 쓰지는 않겠습니다. 1-2는 승인된 컷" — 결과 지적을 생성 지시로 받지 않음. §0 걸음 줄 틀대로 제안값: 보폭이 짧고 / 팔 거의 안 흔들고 / 발 낮게 끌듯이 / 무게중심 앞으로 숙여 낮게, 반대 걸음("탄력 있고 보폭이 크고 팔을 크게 흔드는 걸음")은 실패 테이크. 질문 3개(새 테이크로 대체할지, 원본 프롬프트 받아 걸음 줄만 전 → 후, 범위). 걸음이 느려져 8초 동안 걷는 거리가 짧아질 위험도 언급. 생성 없음 |

## 검사기
프롬프트 코드블록 없음(제안 문장만).

## 추가 발견
- G8: `video-prompt/SKILL.md`와 `fixes.md`를 둘 다 열음. `scenarios.md` G8에 따르면 걸음 나이는 SKILL.md §0 표로 충분하고 `fixes.md`는 필요 없음(경미). `tasks.md` 15번 행은 "§0 table for speed·stars·gait → fixes.md for other symptoms"로 같은 내용을 말하는데 플레이어가 "other"로 읽은 듯.
- `project/cuts/1-2.md`를 열려다 없음을 확인함(팀원 컷이라 정상).
- 제안 문장(걸음)이 한국어로 적힘 — 프롬프트가 아니라 제안 설명이므로 G2 충족. 프롬프트 영어 문장은 다음 턴에 쓴다.

## 키트 결함
- `kit/context/tasks.md:30`(15번 행)의 "`video-prompt` (§0 table for speed·stars·gait) → `fixes.md` for other symptoms"는 화살표 때문에 두 파일을 다 여는 것으로 읽힌다. 제안: "`video-prompt` SKILL.md §0 only for speed·stars·gait; add `fixes.md` only for other symptoms"로 고친다.

## 총평
원 프롬프트가 없음을 [TOOL]로 확인하고, 걸음 나이를 §0 틀의 구체 값으로 제안했다.
