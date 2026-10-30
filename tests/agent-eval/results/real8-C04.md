# real8-C04 인물 시트 의상 수정 (2턴) — PASS 2 / 부분 0 / FAIL 0 (real7: PASS 2)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | image-prompt SKILL + character-edit.md(character.md 안 엶). CH-001 `job-ch001` 기준 편집. 새 의상(머리→발) / 없앨 옛 항목·목둘레 / 적용 범위·새 상태 `char_grandpa_winter_v1` / 의상 참조 이미지 유무 4항목 제안값+이유 |
| 2 | PASS | 틀 1: CHANGE / REMOVE COMPLETELY(faded olive work jacket·가슴 주머니·칼라) / PRESERVE EXACTLY(HEADLESS not an injury, 얼굴 보존 문장만) / ONLY CHANGE. 얼굴 재묘사 없음. 참조 `job-ch001` 하나. 위험 3개, 바꾼 값 전 → 후 2줄. 대장에 겨울 상태 `초안(제안값)` 기록. 생성 안 함 |

검사기: `--kind image --refs 1 --must-include`(LEFT/RIGHT 문장) → `OK — image 프롬프트 2717자, 걸린 항목 없음`. `tmp/` 삭제(빈 디렉터리).
추가 발견: 없음. 더플코트 세부(토글·후드·패치 주머니)를 제안값으로 정하고 알림.
키트 결함: 없음.
총평: PASS 2 유지. G1: tools에 mcp__ 없음, generate_* 없음.
