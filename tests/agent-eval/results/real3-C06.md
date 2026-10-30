# real3-C06 새 소품 (2턴) — PASS 2 / 부분 0 / FAIL 0 (real2: PASS 2)
| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `image-prompt/SKILL.md`+`prop.md`(+decisions·asset-registry·shot-list). 7항목(시트 필요 / 형태·재질 / 사진 속 얼굴 / 사용 흔적 / 크기 13×18cm+손바닥 기준·무게 / 나오면 안 되는 재질 / 상태 변화·화면 왼쪽 손) 제안값+이유, PR-002 매김. 3-4 카드 없음을 밝힘. |
| 2 | PASS | 소품 틀 그대로(회색 무배경, `no hands, no people`(사진 속 인물만 예외), `Avoid:` 줄). 블록 밖 모드·참조·GPT Image 2.5·1k·16:9·`fld-props`. 에셋 대장 PR-002 초안 줄을 "제안만, 아직 쓰지 않음"으로 보임, 컷 목록 수정 안 함(git status 확인). 검사 실행. 생성 안 함. |
검사기(`--kind image --refs 0`): `OK — image 프롬프트 1114자, 걸린 항목 없음`
추가 발견: 틀에 없는 `LEFT and RIGHT are SCREEN …` 문장(무해). 검사용 임시 파일을 하네스 scratchpad에 둠(RUN/tmp 아님, 경미).
키트 결함: 없음.
총평: real2와 동일.
