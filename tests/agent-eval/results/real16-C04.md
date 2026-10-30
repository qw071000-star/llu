# real16-C04 인물 시트 의상 수정 (2턴) — PASS 9 / 부분 2 / FAIL 0

## 턴별 판정

| 턴 | 기대 | 판정 | 근거 |
|---|---|---|---|
| 1 | 첫 줄 | PASS | "5번 인물 시트 고치기으로 진행합니다." (번호·작업명 맞음, 조사는 키트 문형 그대로) |
| 1 | CH-001 카드(job-ch001) 기준 편집, character-edit.md (신규 아님) (G8) | PASS | reads: image-prompt/SKILL.md, character-edit.md, ok-cuts.md; "기준 시트 `job-ch001`" |
| 1 | 코트 색·재질·길이·여밈 제안값 + 새 상태 요소 `char_grandpa_winter_v1` | PASS | "1. 적용 범위: 제안 — 새 상태 시트(`char_grandpa_winter_v1`)"; "3. 코트 재단 4가지…" |
| 1 | 지울 옛 옷·목선 칸 질문 | PASS | "4. 완전히 지울 옛 옷과 목선: 제안 — 낡은 올리브색 작업 재킷을 세 패널 모두에서 지웁니다." |
| 2 | 틀 1: CHANGE / REMOVE COMPLETELY(옛 재킷 이름) / PRESERVE EXACTLY / ONLY CHANGE | PASS | 프롬프트에 네 블록, "The faded olive work jacket, its two flapped chest pockets and its olive collar are GONE in every panel" |
| 2 | 얼굴 재묘사 없음, 참조 1개 | PASS | "preserve the exact same face…" 보존 지시만, `--refs 1` |
| 2 | 사용자 답(더플코트)에 맞춰 연동 항목(칼라·여밈·주머니) 고침을 알림 | PASS | "코트가 더플이라 3번 재단과 4번 목선을 이렇게 고쳤습니다." |
| 2 | 새 옷의 재단 4가지 + `No profession-signaling props.` (character-edit.md:26) | 부분 | 재단 4가지는 있으나 "No belt, no scarf, no hat, no gloves, no logos, no prints."뿐 — profession-signaling 문장 누락(검사기 미검출) |
| 2 | 바뀐 값 "전 → 후", 위험 목록, 생성 안 함 | PASS | "겉옷: 낡은 올리브색 작업 재킷 → 남색 울 더플코트(무릎 길이)"; "이 프롬프트로 시트를 만들어 볼까요?" |
| 2 | 검사 후 표시 (G7) | PASS | Bash check_prompt --kind image tmp/ch001_winter.txt --refs 1 --must-include tmp/must.txt |
| 2 | G2 한국어 | 부분 | "Check passed, so I'll delete the tmp files and add the answers to the registry draft line." (영어 서술) |

## 검사기 결과

- C04 t2 코드블록 1: `--kind image --refs 1 --must-include 좌표문장+바지·신발 문장`: OK — image 프롬프트 2578자, 걸린 항목 없음

## 추가 발견

- character-edit.md:26 요구 문장 `No profession-signaling props.` 누락(위 표).

## 키트 결함

- kit/skills/image-prompt/character-edit.md:26 vs :39–52 — `No profession-signaling props.`가 규칙 불릿에만 있고 틀 1 문장에는 없어 누락됨. 고침: 틀 1의 CHANGE 줄 `No [things not worn], no logos, no prints.` 뒤에 `No profession-signaling props.`를 넣는다.
- kit/context/tasks.md:8 — "짧은 줄도 한국어"가 긴 괄호 안에 묻혀 도구 사이 영어 한 줄이 나옴. 고침: kit/instructions.md:12에 "코드블록 밖의 모든 줄(도구 사이 한마디 포함)은 한국어"를 독립 문장으로.

## 총평

구조·권한·목선 칸이 틀 1대로 정확. 영어 서술 1줄과 직업 소품 금지 문장 누락으로 부분 2건.
