# real16-C08 퍼스트 프레임, 정보 부족 (3-4) (2턴) — PASS 9 / 부분 1 / FAIL 0

## 턴별 판정

| 턴 | 기대 | 판정 | 근거 |
|---|---|---|---|
| 1 | 첫 줄 | PASS | "11번 퍼스트·끝 프레임으로 진행합니다." |
| 1 | 카드 3-4 없음 → 정본(shot-list·연속성 표)에서, first-frame.md 열기 (G8) | PASS | "3-4는 `대기` 컷이라 카드와 핸드오프가 아직 없습니다."; reads first-frame.md, shot-list.md |
| 1 | 모드(카메라가 LC-001-V1과 같은가)를 첫 질문으로, 자리·자세·시선·손을 앞 컷과 맞춰 제안 | PASS | "1. 카메라와 모드: 제안 — 확정 뷰 LC-001-V1과 같은 카메라(틀 1…)"; "3. …감나무 쪽 벤치 절반… 화면 왼쪽 손(감나무 쪽)은 놋쇠 걸쇠 위" |
| 1 | 모델·해상도·폴더는 묻지 않음, 가방 닫힘·인원은 제시 | PASS | "기본값으로 씀: GPT Image 2.5 · 1k… 저장 `fld-3-4`… 가방은 0:00에 닫힘" |
| 1 | 질문 턴: 카드·정본 쓰지 않음 (기능 46) | PASS | "지금은 질문만 하므로 카드와 정본에는 아무것도 쓰지 않았습니다."; tools=[Bash(ls)] |
| 2 | 틀 1: `WITHOUT reframing`, DERIVED 안 섞임, 좌표 문장, `Exactly one person`, 태그 잔여 없음, 손은 물건 기준 | PASS | 1행 "Edit <<<loc_busstop_road_v1>>> WITHOUT reframing…"; "the screen-left hand, nearer the persimmon tree, resting on the brass clasp"; "Exactly one person is visible." |
| 2 | 의상·가방·LIGHT LOCK 글자 그대로 | PASS | checker --must-include grandpa+bag+light OK |
| 2 | 컷 카드 3-4 [4][5]에 값 기록, 말한 것 외 `(제안값)` | PASS | 새 파일 project/cuts/3-4.md: "…화면 왼쪽 손(감나무 쪽)은 놋쇠 걸쇠 위… (제안값)"; 카드 [3]은 "모델 (기본값)" 문구(값 이름 없음, 경미) |
| 2 | 검사 후 표시 (G7), 생성 안 함 | PASS | Bash check_prompt --kind image tmp/ff-3-4.txt --refs 3 --must-include tmp/must-3-4.txt; "'그대로'나 '좋아'는 생성 지시가 아닙니다." |
| 전체 | G2 한국어 | 부분 | T1 "캔on과 이 작업의 스킬 파일을 먼저 읽겠습니다" (canon 음차 혼입) |

## 검사기 결과

- C08 t2 코드블록 1: `--kind image --refs 3 --must-include grandpa+bag+light`: OK — image 프롬프트 2235자, 걸린 항목 없음

## 추가 발견

- T2 마지막 Bash가 `mv tmp/ff-3-4.txt .claude/../tmp/ff-3-4.keep`로 임시 파일을 옮긴 뒤 곧바로 rm — 불필요하지만 RUN 안.

## 키트 결함

- 없음 (이 체인에서 플레이어 오류의 원인이 된 키트 문서 결함은 발견하지 못함)

## 총평

틀 1과 연속성(가방 닫힘, 감나무 쪽 자리)을 정확히 따름. 음차 오탈자 1건.
