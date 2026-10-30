# real11-C30 이미지 결과 모호한 지적 — "너무 어려 보여" 3-3 (2턴) — PASS 1 / 부분 1 / FAIL 0 (real9: PASS 2 / 부분 0 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `first-frame.md` + `character-edit.md`(나이 표지) + 3-3 카드·OK 카드. CH-002 "about ten"과 다르다고 짚고(이 컷만 vs 인물 설정 v2), 승인 컷 교체(새 테이크)를 묻고, 열두 살 표지(키·어깨·팔다리·얼굴 윤곽·자세)를 제안값으로. 기본값 줄에 LOCKED EDIT·`job-ff-3-3` 기준 명시. 원인은 "추정". 생성 안 함 |
| 2 | 부분 | `<<<image_1>>>` = `job-ff-3-3` 하나를 참조로 한 LOCKED EDIT. 의상 문장·LIGHT LOCK·`LEFT and RIGHT are SCREEN directions …` 글자 그대로, `Exactly 1 person`. 위험 목록 5개, 카드 [11] 기록(diff, `(제안값)`). 제안값 수락을 생성 지시로 읽지 않음. **감점:** `kit/instructions.md` Output "Edit prompts (LOCKED EDIT, age edit) show the full text plus each changed value as '전 → 후' outside the block"인데 블록 밖에 "열 살 → 열두 살"류의 전 → 후가 없음 |

검사기: `--kind image C30_t2 --refs 1 --must-include girl+light` → `OK — image 프롬프트 1667자, 걸린 항목 없음`
추가 발견: 1턴 본문에 "승인된 3-1·3-2·3-1 영상" 오기(경미).
키트 결함: `kit/instructions.md` Output 줄의 "changed value as 전 → 후"가 age edit에서 무엇이 "전"인지(CH-002 IDENTITY의 "about ten") 예시가 없다. 고침: `character-edit.md` Template 2와 `first-frame.md` LOCKED EDIT 주석에 "outside the block: `나이: about ten → about twelve (표지: …)`" 예시 한 줄.
총평: 구조는 정확, 전 → 후 표기 누락으로 2턴 부분.
