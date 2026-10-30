# real7-C03 새 인물 시트 (2턴) — PASS 2 / 부분 0 / FAIL 0 (real6: PASS 2)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | image-prompt SKILL + character.md. 나이·얼굴 / 체형 / 의상 / 헤어 / 대사·연기 5항목 제안값+이유 한 번에. 모델·2k·16:9·`fld-chars`·패널 A·배경·조명은 "기본값으로 씀". 프롬프트 안 보임 |
| 2 | PASS | 틀 1 전문 코드블록 하나: 3분할, `intentionally HEADLESS`, `not an injury`, `mature adult bone structure`, 일관성 잠금(`identical face, age, skin tone …`), 리얼리즘·눈 블록, ghost-mannequin 없음. 블록 밖 모드 신규·참조 없음·GPT Image 2.5·2k·16:9·`fld-chars`. "인물 시트는 처음부터 2k" 알림. 위험 7개. CH-003 `초안(제안값)` 기록. 생성 안 함, "이 프롬프트로 생성할까요?" |

검사기: `check_prompt --kind image` (내가 답 코드블록에서 뽑아 실행) → `OK — image 프롬프트 4956자, 걸린 항목 없음`
추가 발견: 플레이어 보관본 `project/ch003-sheet-prompt.txt`를 정본 폴더에 남김(경미, 코드블록과 동일). 1턴 의상 제안에 "1990년대 초"는 기본값 줄에만 있고 의상 이유엔 안 씀(경미).
키트 결함: 없음.
총평: PASS 2 유지. G1: tools에 mcp__ 없음, generate_* 없음.
