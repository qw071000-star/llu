# real11-C03 새 인물 시트, 정보 없음 (2턴) — PASS 2 / 부분 0 / FAIL 0 (real9: PASS 2 / 부분 0 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `image-prompt` SKILL + `character.md`만 엶(정본은 bash로 읽음). 첫 줄 정해진 문장, 5개 질문(나이·출신·얼굴 / 체형 / 옷 "짙은 남색 지퍼 제복 점퍼… 1990년대 초 시골 기사" / 머리 / 대사 여부)을 제안값+이유로 한 묶음. "기본값으로 씀: GPT Image 2.5 · 2k(인물 시트는 처음부터 최종 해상도) · 16:9 · `fld-chars` …". 프롬프트 안 보임, 생성 없음 |
| 2 | PASS | 틀 1 전문: 3분할, `intentionally HEADLESS … not an injury`, `ghost-mannequin` 없음, `Mature adult bone structure … no babyface`, 일관성 잠금 `identical face, age, skin tone, body proportions…`, REALISM·눈 블록, 시대 금지(`no modern clothing…`). 블록 밖에 모드·모델 GPT Image 2.5·2k·16:9·저장 `00 에셋/인물`. 실패 위험 6줄. CH-003 `초안(제안값)` 기록(`git diff`로 확인). 생성 안 함, "이 시트를 이미지로 보낼까요?" |

검사기: `check_prompt.py --kind image C03_t2 --refs 0` → `OK — image 프롬프트 4468자, 걸린 항목 없음`
추가 발견: 정본 §2 "확인 1k"와 다르다는 한 줄은 없음(가산점 항목). 플레이어 검사 호출은 `--must-include` 포함 단독 호출.
키트 결함: 없음.
총평: real9와 같은 PASS 2.
