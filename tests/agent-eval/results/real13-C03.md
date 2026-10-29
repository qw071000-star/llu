# real13-C03 새 인물 시트, 정보 없음 (2턴) — PASS 2 / 부분 0 / FAIL 0 (real11: PASS 2 / 부분 0 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | "4번 인물 시트 만들기로 진행합니다." `image-prompt` SKILL+`character.md`, CH-001 카드로 시트 형식 가져옴. 5개 질문(나이·얼굴 / 체격 / 옷 "짙은 남색 단추 제복 재킷… 90년대 초 시골 버스 기사" / 머리 / 대사·연기 프로필)을 제안·이유로 한 묶음. "기본값으로 씀: GPT Image 2.5 · 2k(인물 시트는 처음부터 2k) · 16:9 · `fld-chars` …". 프롬프트·생성 없음 |
| 2 | PASS | 틀 1 전문: 3분할, 첫 문단 `including the intentionally HEADLESS left panel. Do not add, infer, reconstruct or complete a head…`, `not an injury`, `mature adult bone structure`, `LEFT and RIGHT are SCREEN directions…`, 일관성 잠금, REALISM·눈 블록, `no babyface`, `no modern clothing…`, `a plain blank badge, no writing…`, `the garment stands on the floor…`. 블록 밖 모드·모델·2k·16:9·`fld-chars`, 위험 5줄. registry에 `초안(제안값, 2026-10-29 "그대로")` 기록(diff). 생성 안 함 |

검사기: `--kind image --refs 0` (C03_t2) → `OK — image 프롬프트 4689자, 걸린 항목 없음` (플레이어도 `--must-include`로 단독 호출, cd 없음)
추가 발견: 정본 §2 "확인 1k"와 다르다는 한 줄은 있음("시트는 확인 단계 없이 처음부터 2k").
키트 결함: 없음. 통합 후에도 인물 시트 세부(머리 없는 패널 문장·계약 문장·고정 문장)가 모두 `character.md`에서 정상 전달됨.
총평: PASS 2.
