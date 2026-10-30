# real16-C13 "3-1의 색감과 질감으로 3-5 퍼스트 프레임" (2턴) — PASS 8 / 부분 1 / FAIL 0

## 턴별 판정

| 턴 | 기대 | 판정 | 근거 |
|---|---|---|---|
| 1 | 첫 줄 | 부분 | "11번 퍼스트·끝 프레임으로 진행합니다. (색감·질감은 \"3-1처럼\"이라 16번 다른 OK처럼을 함께 씁니다.)" — 첫 줄에 괄호를 덧붙임 |
| 1 | ok-reuse.md + 3-1 시작 이미지 카드 (G8) | PASS | reads first-frame.md, ok-reuse.md, ok-cuts.md; "OK 대장의 3-1 시작 이미지 카드" |
| 1 | 그 프롬프트에 색·질감 문장이 없음을 알아채고 새 문장을 짓지 않음 | PASS | "3-1 시작 이미지 프롬프트에는 색·질감 문장이 따로 없습니다… 새 문장은 쓰지 않고, `job-ff-3-1`을 색·질감 참조로만 붙입니다" |
| 1 | 3-5 정보(가방 열림=3-4 이후 이음새, 카메라, 손·시선)를 묻거나 제안 | PASS | "1. 3-4와의 이음새: 제안 — …가방은 열린 채 할아버지 무릎 위"; 2. 카메라; 3. 손과 시선 |
| 2 | 참조 수=태그 수, 색·질감 전용 권한 문장 | PASS | "<<<image_4>>> controls only colour, grade, contrast and texture. Never take its subjects, composition, people or light direction."; checker --refs 4 OK |
| 2 | 틀 2(카메라 다름) + 가방·LIGHT LOCK·의상 글자 그대로 | PASS | "Using <<<loc_busstop_road_v1>>> as the exact same location, generate a new view…"; "PROP: A worn brown leather doctor's bag… Except: the bag lies open…"; checker bag+light OK |
| 2 | 컷 카드 3-5 v0에 `(제안값)`, shot-list 불변, 3-4 가정 알림 | PASS | 새 project/cuts/3-5.md "카드 버전: v0 … (초안, 총괄 확인 전)"; "`shot-list.md`는 건드리지 않았습니다." |
| 2 | 검사 후 표시 (G7), 생성 안 함 | PASS | Bash check_prompt --kind image tmp/ff35.txt --refs 4 --must-include tmp/ff35_must.txt; "'좋아'나 '그대로'는 생성 지시로 받지 않습니다." |
| 전체 | G9 손은 화면 쪽 + 물건 | PASS | "The screen-left hand, nearer the bag's open mouth… The screen-right hand, nearer the undone brass clasp" |

## 검사기 결과

- C13 t2 코드블록 1: `--kind image --refs 4 --must-include bag+light`: OK — image 프롬프트 2653자, 걸린 항목 없음

## 추가 발견

- 없음

## 키트 결함

- kit/context/tasks.md:8·29 — 첫 줄 번호 규칙 불명(C12 결함과 동일).

## 총평

색·질감 문장이 없는 OK에서 문장을 지어내지 않고 참조로 좁힌 것이 핵심 통과. 첫 줄 괄호 덧붙임 1건.
