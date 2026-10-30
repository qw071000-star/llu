# real11-C12 "3-1의 모션처럼 3-2 영상" (2턴) — PASS 2 / 부분 0 / FAIL 0 (real9: PASS 2 / 부분 0 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `production-session` SKILL + `ok-reuse.md`, 3-2 카드·핸드오프·OK 대장(3-1 영상 카드, 3-2·3-3 시작 이미지). `[TOOL] list_project_assets(folder_id=fld-3-2)`. 가져올 것은 `ACTION_TIMING`+`PHYSICS`만, 카메라는 안 가져옴(이유 적음). 이음새(3-3 시작 이미지와 불일치)·이벤트 4개·대사·연기를 제안값+이유로 4개 묶음. 렌즈 알림 "카드 35°, 시작 이미지 75mm → 32° 사용". 3-1 입 잠금이 약해 올림도 알림. 카드 [7] `가져온 OK`를 기존 카드에 기록 |
| 2 | PASS | 15블록 전문. `ACTION_TIMING`·`PHYSICS`가 3-1 줄과 글자 그대로(`motion_3-1.lines` 통과). 할아버지 입 잠금 Forbidden 포함. OPTICS 32°+관찰 3개. 본문에 "3-1"·"previous shot" 없음. "3-1에서 바꾼 부분"을 블록 밖 "전 → 후"로 나열. 카드 [4]~[7] 기록(diff) |

검사기: `--kind video C12_t2 --refs 4 --seconds 8 --must-include grandpa+girl+bag+light+motion_3-1` → `OK — video 프롬프트 5134자, 걸린 항목 없음`
추가 발견: 이벤트 4개(3 초과)를 "3-1이 이 구성으로 승인됨, 섞어 쓰려면 같아야 함"으로 유지하고 위험에 적음 — must-ask 13행 "more than 3 events → split"을 짚긴 했으나 사용자에게 분할 대안은 제시하지 않음(허용 범위).
키트 결함: 없음.
총평: real9와 같은 PASS 2.
