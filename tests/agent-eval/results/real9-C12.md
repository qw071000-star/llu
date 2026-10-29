# real9-C12 "3-1의 모션처럼 3-2 영상" (2턴) — PASS 2 / 부분 0 / FAIL 0 (real8: PASS 2 / 부분 0 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `production-session` SKILL → `ok-reuse.md`, `video-prompt` SKILL + `live-action.md`, 3-2 카드·핸드오프·OK 대장 `3-1 영상`·`3-2 시작 이미지` 카드(3-1 영상 카드 하나만). 시작 보고 3줄, `[TOOL] list_project_assets(folder_id=fld-3-2)`. 가져올 것: `ACTION_TIMING`·`PHYSICS`·속도 문장(+연기·대사). 알림: "카드 [4]의 35°와 시작 이미지의 75mm(= 32°)가 다릅니다. 시작 이미지가 이기므로 32°". 이음새와 사건 수(5개 > 3, 3-1에서 같은 구성 승인) 2항목을 제안값+이유로 물음 |
| 2 | PASS | 15블록 전문 코드블록 하나. `ACTION_TIMING` 3줄·`PHYSICS` CHARACTER/PROP 줄 글자 그대로(`motion_3-1.lines` 통과), 3-1 입 잠금(`GRANDPA does not say a single word; no attempt to speak, no lip movement`)·Forbidden `GRANDPA moving his lips or speaking` 옮김, `[OPTICS]` 32° + 관찰 결과 3개(mm 없음), 의상·가방·LIGHT LOCK 글자 그대로. 본문에 "3-1"·"previous shot" 없음. 블록 밖에 모드·참조 4(순서)·모델·480p·8초·16:9·소리·폴더. 3-1에서 옮긴 줄/바꾼 줄을 보고. 위험 7개(마지막은 막는 문장 없음과 "추정" 표기). 카드 3-2 v2: [4] 렌즈, [5] 끝·동선·시선, [6] 타이밍·이음새 `(제안값)`, [7] `가져온 OK: 3-1 영상 — 모션(ACTION_TIMING, PHYSICS, 속도 문장), 연기, 대사` (diff 확인) |

검사기: `check_prompt.py --kind video --refs 4 --seconds 8 --must-include grandpa+girl+bag+light+motion_3-1` → `OK — video 프롬프트 5213자, 걸린 항목 없음`
추가 발견: 1턴에 `cut-card.md`까지 열어 읽은 파일이 13개로 많음(질문 턴). 카드에 없던 "an arm's length from its pole"를 시작 이미지 프롬프트 기준으로 더했다고 밝힘. 감나무가 프레임에 있는지 모르면 LOCATION_MAP에서 뺀 것은 합리적(추정 표기).
키트 결함: 없음.
총평: real8과 같은 PASS 2. G1: mcp__ 없음, 생성 없음.
