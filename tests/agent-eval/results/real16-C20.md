# real16-C20 장소 상태판: 형광등 켜기 (두 변경으로 읽힘) (2턴) — PASS 9 / 부분 0 / FAIL 0

## 턴별 판정

| 턴 | 기대 | 판정 | 근거 |
|---|---|---|---|
| 1 | 첫 줄 | PASS | "8번 장소 고치기로 진행합니다." |
| 1 | location.md + location-edit.md, 계보 STATE, 부모 job-lc001v1 (G8) | PASS | reads location-edit.md, location.md, ok-cuts.md; "LOCKED EDIT… STATE 파생"; "부모 `job-lc001v1`" |
| 1 | "형광등 켜기"+"해 진 직후"를 두 변경으로 짚고 형광등 먼저로 분리 제안 (기능 20) | PASS | "1. 한 번에 할지 나눌지: 제안 — 2단계로 나눕니다. 1단계는 형광등만 켭니다… 2단계는 해 진 직후 하늘과 빛으로 바꿉니다." |
| 1 | LIGHT LOCK(해=유일한 키)과 부딪침을 알림 | PASS | "2. 형광등 위치… 이 빛이 이 뷰의 새 LIGHT LOCK이 되어 화면 쪽과 물건 기준으로 적어야 합니다."; T2 "LIGHT LOCK 전 → 후" |
| 2 | 1턴에 프롬프트가 없었으므로 1턴 기대를 적용, 시간대 변경은 다음 단계 | PASS | T2 "1번은 '형광등만 먼저'로 확정"; "이 1단계 결과는 아직 '해 지고 난 직후'가 아닙니다." |
| 2 | LOCKED EDIT 표준형 여는 문장, STATE 공식, 번짐 방지 문장, 장소 재묘사 없음 | PASS | "Edit <<<image_1>>> WITHOUT reframing: …zero reframing…"; "the tube is off and becomes lit"; "It is lit but does NOT glow: no halo, no bloom, no light spilling onto the roof edge" |
| 2 | 빛이 바뀌므로 부모 LIGHT LOCK을 PRESERVE에서 빼고 바뀌는 광원만 CHANGE에 (location-edit.md:23) | PASS | PRESERVE에 "fluorescent tube is off" 없음; 해는 "stays the key light"로 별도 보존 |
| 2 | 검사 후 표시 (G7), 생성 안 함, 위치 추정 표시 | PASS | Bash check_prompt --kind image tmp/lc001v1_tube_on.txt --refs 1 …; "형광등 위치… '추정'입니다"; "보내려면 '이미지로 만들어'라고 해 주세요." |
| 전체 | G1·G2·G9 | PASS | mcp 없음, 한국어, LEFT/RIGHT 화면 기준 |

## 검사기 결과

- C20 t2 코드블록 1: `--kind image --refs 1`: OK — image 프롬프트 1634자, 걸린 항목 없음

## 추가 발견

- 없음

## 키트 결함

- 없음 (이 체인에서 플레이어 오류의 원인이 된 키트 문서 결함은 발견하지 못함)

## 총평

두 변경 분리와 STATE 공식이 기대대로.
