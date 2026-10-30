# real16-C11 배경 영상 (1-1) + 모호한 수정 (C26 4~6턴) (6턴) — PASS 10 / 부분 1 / FAIL 0

## 턴별 판정

| 턴 | 기대 | 판정 | 근거 |
|---|---|---|---|
| 1 | 첫 줄 | PASS | "14번 배경 영상으로 진행합니다." |
| 1 | background.md를 질문 전에 열고 움직일 것·유지할 것만 묻고 카메라·소리·길이는 "기본값으로 씀" | PASS | reads background.md; "기본값으로 씀: Seedance 2.5, 480p 확인, 16:9, 8초, 카메라 완전 고정… 시작 이미지 `job-ff-1-1`"; 질문 2개 |
| 2 | 정본과 부딪침을 짚음 (감나무 잎 없음, 컷당 8초) | PASS | "1. 감나무 '잎'… 맨나무입니다"; "2. 길이: 제안 — 8초 (이유: `decisions.md`에 컷당 8초…)" |
| 3 | 4문단 Camera/Motion/Keep/Silent, %로 양, 끝 상태·페이드 없음 | PASS | 프롬프트 4문단 "about 4 percent", "about 3 percent of the frame width"; Keep 문단은 템플릿 `every [shape list]`대로(background.md:8과 충돌, 결함 5) |
| 3 | 카드 1-1 기록(값 있는 턴), 이 컷만 10초라 decisions 불변 | PASS | 새 project/cuts/1-1.md 길이 "10초 (사용자 답 · 이 컷만…)"; "`decisions.md`는 바꾸지 않았습니다" |
| 3 | 검사 후 표시 (G7) | PASS | Bash check_prompt --kind video tmp/1-1_bg.txt --refs 0 --seconds 10 … |
| 4 | "구름 더 느리게": 구름 `Motion` 줄만 "전 → 후"(양 절반), 다른 문단 그대로, fixes.md 안 엶 (기능 10, 65) | PASS | "전: …about 3 percent… 후: …very slowly… about 1.5 percent"; 전체 프롬프트로 검사 OK(915자); reads 없음 |
| 5 | "풀도 흔들리게": 사건 한도(카메라+대상 3) 초과를 알리고 하나 빼기 제안, 프롬프트 불변 | PASS | "풀 흔들림을 넣으면 움직임이 4개가 됩니다… 그래서 프롬프트는 고치지 않았습니다."; "뺄 것: 감나무 가지·남은 감" |
| 6 | "별도 더 반짝": 시작 이미지에 별 없음 짚음, 모델 한계, 후반 오버레이 제안, 생성 없음 | PASS | "별이나 새 떼처럼 작고 반복되는 점은 이 모델이 잘 유지하지 못합니다… 1. 후반 작업에서 별 반짝임을 위에 덧입힙니다." |
| 6 | 같은 것을 두 번 묻지 않음 (G3) | 부분 | "2. 이전에 물은 것: 제안 — 감나무 가지·남은 감 흔들림을 빼고 풀 흔들림을 넣음" — T5와 같은 항목 재질문 |
| 전체 | G1·G2·G9 | PASS | mcp·generate 없음, 한국어, 방향 "screen left, the persimmon-tree side" |

## 검사기 결과

- C11 t3 코드블록 1: `--kind video --refs 0 --seconds 10`: OK — video 프롬프트 908자, 걸린 항목 없음
- C11 t4 전체 프롬프트(코드블록 아님, bash 인자로 저장해 검사; 내가 재구성해 재검사): OK — video 프롬프트 915자, 걸린 항목 없음

## 추가 발견

- T3 Keep 문단이 정류장·감나무·길·논·산을 나열 — 템플릿대로이나 "이미지에 있는 것을 다시 묘사하지 않는다" 기대와 긴장.

## 키트 결함

- kit/skills/video-prompt/background.md:8 vs 템플릿 `every [shape list]` — 재묘사 금지와 Keep 목록 요구가 부딪침. 고침: 템플릿 주석에 "shape list = 이름만, 속성 없이 5개 이하" 추가.

## 총평

배경 영상 4문단과 모호한 말 표(속도·움직임 추가·별)를 정확히 적용. T6의 재질문 1건만 부분.
