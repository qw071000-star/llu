# real7-C04 인물 시트 의상 수정 (2턴) — PASS 2 / 부분 0 / FAIL 0 (real6: PASS 2)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | image-prompt SKILL + character-edit.md(character.md 안 엶). CH-001 `job-ch001` 기준 편집. 코트 색·재질·길이·여밈 / 안에 입는 것 / 목둘레 / 의상 참조 이미지 유무 / 새 상태 `char_grandpa_winter_v1`·정본(늦가을)과 계절 충돌·적용 컷 5항목 제안값+이유 |
| 2 | PASS | 틀 1: CHANGE / REMOVE COMPLETELY(faded olive work jacket, 가슴 주머니, 단추) / PRESERVE EXACTLY(HEADLESS not an injury, 얼굴 보존 문장만) / ONLY CHANGE. 얼굴 재묘사 없음. 참조 `job-ch001` 하나. 위험 5개, 전 → 후 2줄. 대장에 겨울 상태 초안(제안값) 기록. 생성 안 함 |

검사기: `--kind image --refs 1` (답 코드블록) → `OK — image 프롬프트 2844자, 걸린 항목 없음`
추가 발견: 임시 `ch001-winter-prompt.txt`, `ch001-winter-must.txt`를 RUN 루트에 남김(경미, 답에서 알림).
키트 결함: 없음.
총평: PASS 2 유지. G1: tools에 mcp__ 없음, generate_* 없음.
