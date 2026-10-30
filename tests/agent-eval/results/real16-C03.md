# real16-C03 새 인물 시트, 정보 없음 (2턴) — PASS 11 / 부분 0 / FAIL 0

## 턴별 판정

| 턴 | 기대 | 판정 | 근거 |
|---|---|---|---|
| 1 | 첫 줄 | PASS | "4번 인물 시트 만들기로 진행합니다." |
| 1 | image-prompt + character.md 열기 (G8) | PASS | reads: image-prompt/SKILL.md, character.md (acting 안 엶) |
| 1 | CH-003 정보를 제안값·이유와 함께 한 번에(5개), 의상은 1990년대 초 시골 기사 | PASS | "3. 의상: 제안 — 짙은 남색 점퍼… (이유: …1990년대 초 시골 노선 기사 설정…)" |
| 1 | 모델·해상도·저장 폴더는 묻지 않고 "기본값으로 씀" (기능 13) | PASS | "기본값으로 씀: 모델: GPT Image 2.5 · 해상도: 2k (인물 시트는 처음부터 2k)… 저장 폴더: `fld-chars`" |
| 1 | 프롬프트·기록 없음 | PASS | "답을 받기 전에는 카드나 대장에 아무것도 쓰지 않았고 프롬프트도 쓰지 않았습니다." |
| 2 | 틀 1 전문: 3분할, HEADLESS `not an injury`, ghost-mannequin 오용 없음 | PASS | "including the intentionally HEADLESS left panel… not an injury"; mannequin 단어 없음 |
| 2 | 성숙한 골격·일관성 잠금 전문·리얼리즘·눈 블록, 실존 인물 안 닮게 | PASS | "Mature adult bone structure, defined nasolabial folds"; "CONSISTENCY RULES: …identical face, age, skin tone"; REALISM 블록 |
| 2 | 블록 밖에 모델·2k·16:9·저장 폴더, 직업 소품 문장 | PASS | "모델: GPT Image 2.5 · 해상도: 2k · 비율: 16:9, 1장 · 저장 폴더: `fld-chars`"; "No profession-signaling props unless explicitly requested." (정본 §2 1k와 다름을 알리는 선택 항목은 없음) |
| 2 | 생성 안 함, 제안값을 대장에 기록 | PASS | "이 프롬프트로 이미지를 보낼까요?"; diff: asset-registry `초안(제안값, 2026-10-30 · "그대로")` 4줄 |
| 2 | 검사 후 표시, FAIL·WARN 없음 (G7) | PASS | Bash 2회: check_prompt --kind image tmp/ch003.txt --refs 0 --must-include tmp/must.txt (첫 회 고정 문장 FAIL 1 → 수정) |
| 전체 | G1·G2·G9 | PASS | mcp 없음, 한국어, 손은 "empty"만 |

## 검사기 결과

- C03 t2 코드블록 1: `--kind image --refs 0`: OK — image 프롬프트 4648자, 걸린 항목 없음

## 추가 발견

- BODY AND PROPORTIONS에 "upright seated-worker posture" — 가운데 패널 "standing… not sitting" 문장과 어긋날 여지(WARN 없음, 경미).

## 키트 결함

- 없음 (이 체인에서 플레이어 오류의 원인이 된 키트 문서 결함은 발견하지 못함)

## 총평

틀 1을 정확히 따른 모범 사례. 결함 없음.
