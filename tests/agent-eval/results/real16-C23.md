# real16-C23 의상 수정 + 의상 참조 이미지 (2턴) — PASS 11 / 부분 0 / FAIL 0

> 채점: tests/agent-eval/grader-rules.md. 출력 `runs-real16/C23/out/turn*.md`, 메타 `turn*.meta.json`, 정본 diff, 기대 `scenarios.md`. G1: 모든 턴에서 `mcp__` 도구 호출 없음, RUN 밖 파일 읽기 없음, 시킨 적 없는 생성 없음(확인함).

## 턴별 판정

| 턴 | 항목 | 판정 | 근거 |
|---|---|---|---|
| 1 | 첫 줄·작업 번호 | PASS | `5번 인물 시트 고치기로 진행합니다.` |
| 1 | 읽기 G4/G8 | PASS | image-prompt SKILL + character-edit.md + 정본. character.md(신규용)는 열지 않음 |
| 1 | 질문 한 묶음·형식 | PASS | `프롬프트를 쓰기 전에 확인할 것이 4개 있습니다 …` 여밈·후드 / 안에 입는 것 / 주머니 / 적용 범위, 제안+이유 |
| 1 | 정본과 다름 짚기, 참조 이미지 유무 확인 | PASS | `대장의 손녀 WARDROBE 문장은 "노란 우비 + 남색 교복…"이고, 이번 요청은 이 문장과 다릅니다`; 사진은 사용자가 준 `job-ref-coat` |
| 1 | 질문 턴에 정본 안 씀 | PASS | `답을 받기 전에는 대장이나 카드에 아무것도 적지 않았고, 생성도 하지 않았습니다` |
| 2 | 틀 1 + 참조 2개 권한 세 줄 | PASS | `Reference image 1 controls … Reference image 2 controls only … Do not transfer the face, body, pose, background or lighting from reference image 2.` |
| 2 | 목둘레 세 곳 | PASS | REMOVE `At the neckline, only the navy school uniform collar…`, PRESERVE LEFT `Its clothes change fully:`, ONLY CHANGE `including the neckline of the headless panel` |
| 2 | REMOVE GONE 목록 = LEFT 줄 `no …` 목록, 나머지 의상 유지 | PASS | `yellow raincoat, … yellow hood … two yellow flap pockets are GONE` = `no yellow raincoat, no yellow hood, no yellow flap pockets`; 교복·양말·장화 유지 |
| 2 | 얼굴 재서술 없음, 좌표 문장 | PASS | `IDENTITY: preserve the exact same face …` 보존 지시만, `LEFT and RIGHT are SCREEN directions…` 있음 |
| 2 | G7 검사 / G6 블록 밖 / 전→후 / 위험 / 대장 `(제안값)` | PASS | check_prompt --refs 2 통과, `char_girl_duffle_v1` 초안(제안값) 줄 diff |
| 2 | G1 생성 통제 | PASS | `"그대로"나 "좋아"는 생성 지시로 받지 않습니다` |

## 검사기 결과

- `python3 kit/skills/higgsfield-generation/check_prompt.py --kind image --refs 2 C23_turn2_b1.txt`
  - 결과: `OK — image 프롬프트 2795자, 걸린 항목 없음`
- (참고) `--must-include girl.lines` 를 넣으면 FAIL — 의상이 바뀌는 시험이라 정상(옛 우비 문장이 없어야 함). 오탐 아님·기대대로
  - 결과: `FAIL 고정 문장이 글자 그대로 들어 있지 않다: A yellow raincoat …`

## 추가 발견

- 참조 사진 내용(`job-ref-coat`)은 sim 파일의 사용자 업로드 설명에서 가져왔다. 도구 호출이 아니라 업로드 설명이므로 [TOOL] 줄 없음은 위반 아님.

## 키트 결함

- 결함 없음.

## 총평

틀 1의 세 목둘레·권한 세 줄을 모두 지킨 정확한 옷 교체 프롬프트.
