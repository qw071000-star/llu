# real9-C03 새 인물 시트, 정보 없음 (2턴) — PASS 2 / 부분 0 / FAIL 0 (real8: PASS 1 / 부분 1 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `image-prompt` SKILL + `character.md` + 대장/정본 읽음. 5항목(얼굴, 체형·자세, 의상, 헤어, 대사·연기·목소리)을 제안값+이유와 한 묶음으로 물음. 의상 "짙은 남색 지퍼 근무 점퍼 … 1990년대 초 시골 버스 기사 복장". "기본값으로 씀: GPT Image 2.5, 2k, 16:9 … 저장 `fld-chars` … 머리 없는 패널 변형 A … 배경 …"로 모델·해상도·폴더는 묻지 않음. "인물 시트는 처음부터 2k". 프롬프트 미표시, 생성 안 함 |
| 2 | PASS | 틀 1 전문 코드블록 하나. 3분할, `This is an editorial clothing crop, not an injury`, `Mature adult bone structure`, 일관성 잠금 전문(`identical face, age, skin tone, body proportions …`), 리얼리즘·눈 블록 있음, `ghost-mannequin` 없음, `No profession-signaling props unless explicitly requested`, 시대 금지 줄. 블록 밖에 모드·참조 0·모델·2k·16:9·저장 `fld-chars`. 위험 목록+막는 문장, 대장 CH-003에 `초안(제안값)` 기록(diff 확인), 생성 안 함 |

검사기: `check_prompt.py --kind image` → `OK — image 프롬프트 4669자, 걸린 항목 없음`
추가 발견: 플레이어 답에 "정본 §2의 확인 1k와 다르다"는 명시 문장은 없으나 "인물 시트는 처음부터 2k"로 갈음(더 좋은 쪽 보너스 미충족, 감점 아님). 검사 때 쓴 `tmp/` 파일을 지움.
키트 결함: 없음.
총평: real8의 부분(1턴 쪽 빈틈)이 해소돼 PASS 2. G1: tools에 Bash/Edit/Write만.
