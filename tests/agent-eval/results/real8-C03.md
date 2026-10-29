# real8-C03 새 인물 시트 (2턴) — PASS 1 / 부분 1 / FAIL 0 (real7: PASS 2)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | 부분 | image-prompt SKILL + character.md, 5항목(나이·얼굴 / 체형 / 의상 / 헤어 / 대사·연기) 제안값+이유 한 번에, 모델·2k·`fld-chars`·패널 A·배경·조명은 "기본값으로 씀". 감점: 기사 정보를 찾느라 `grep -n "버스\|운전" project/shot-list.md project/cuts/*.md`, `grep -n "버스 기사\|기사" project/shot-list.md project/cuts/*.md`를 돌려 다른 컷 카드를 훑음 — routing.md §3 "다른 컷 카드는 열지 않는다 … head·grep으로도" 위반 (G4) |
| 2 | PASS | 틀 1 전문 코드블록 하나: 3분할, `intentionally HEADLESS … not an injury`, `mature adult bone structure`, 일관성 잠금(`identical face, age, skin tone …`), 리얼리즘·눈 블록, ghost-mannequin 없음. 블록 밖 신규·참조 없음·GPT Image 2.5·2k·16:9·`fld-chars`. 위험 6개. CH-003 `초안(제안값)` 기록. 생성 안 함, "보낼까요?" |

검사기: `--kind image --refs 0` (답 코드블록) → `OK — image 프롬프트 4664자, 걸린 항목 없음`. `tmp/` 파일 삭제 확인(빈 디렉터리만 남음).
추가 발견: 2턴에 "인물 시트는 확정 해상도로 바로"라고만 하고 정본 §2 "확인 1k"와 다르다는 설명은 한 줄(권장 사항이라 경미).
키트 결함: 경미 — routing.md:30 "다른 컷 카드는 열지 않는다" 규칙이 "컷 세션" 맥락에 묻혀 에셋 시트 작업(기사처럼 컷 목록에서 등장 컷을 찾는 경우)에는 안 읽힌다. 고칠 한 줄: routing.md §3 첫 불릿에 "에셋 세션도 마찬가지 — 등장 컷은 컷 목록 한 줄로만 보고 `cuts/*.md`를 grep하지 않는다".
총평: 2턴은 PASS, 1턴 컷 카드 grep으로 부분. G1: tools에 mcp__ 없음, generate_* 없음.
