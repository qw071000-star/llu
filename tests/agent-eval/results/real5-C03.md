# real5-C03 새 인물 시트 (2턴) — PASS 2 / 부분 0 / FAIL 0 (real4: PASS 2)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | image-prompt SKILL + character.md. 5항목(나이·피부·얼굴·눈 / 체형 / 의상 90년대 초 기사 / 헤어 / 대사·연기) 제안값+이유 한 번에. 모델·2k·16:9·`fld-chars`·패널 A·배경·조명은 "기본값으로 씀". 프롬프트 안 보임 |
| 2 | PASS | 틀 1 전문 코드블록 하나, 3분할, HEADLESS `not an injury`, `Mature adult bone structure`, `identical face, age, skin tone …`, 리얼리즘·눈 블록, ghost-mannequin 없음. 블록 밖 모드·참조 없음·GPT Image 2.5·2k·16:9·`00 에셋/인물`. 위험 6줄. 생성 안 함. 검사 실행 |

검사기: 내가 `--kind image --refs 0`로 돌림: `OK — image 프롬프트 4704자, 걸린 항목 없음`

추가 발견: 프롬프트 파일을 `out/ch003_prompt.txt`에 둠(RUN/tmp 아님, 경미). 정본 §2 "확인 1k"와 다르다는 한 줄은 없음(선택 사항).

키트 결함: 없음.

총평: real4와 같은 PASS 2.

G1: 모든 턴 tools가 Bash/Write/Edit/Grep뿐, `mcp__` 호출 없음, `generate_*` 없음.
