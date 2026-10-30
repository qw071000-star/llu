# real16-C14 "표정은 2-1처럼, 2-2 영상" (2턴) — PASS 11 / 부분 0 / FAIL 0

## 턴별 판정

| 턴 | 기대 | 판정 | 근거 |
|---|---|---|---|
| 1 | 첫 줄 | PASS | "13번 실사·인물 영상으로 진행합니다." |
| 1 | ok-reuse.md + 2-1 영상 카드의 할아버지 `CHARACTER_ACTING`만 가져옴, 모션은 안 가져옴, 시작 이미지 job-ff-2-2 | PASS | "2-1의 모션(엄지, 낙엽)은 가져오지 않습니다."; reads ok-reuse.md, live-action.md, ok-cuts.md |
| 1 | 질문 턴에 acting을 열지 않음 (기능 75) | PASS | T1 reads에 acting 없음 |
| 1 | Higgsfield 2-2 폴더 조회를 [TOOL]로, 빈 칸(쓰다듬는 구간·끝 상태·요소 이름)을 3개로 | PASS | [TOOL] list_folders / list_project_assets 2줄; "1. 쓰다듬는 동작 구간… 2. 마지막 프레임 상태… 3. 시작 이미지 요소 이름" |
| 2 | 프롬프트 쓰는 턴에 acting 열기 | PASS | T2 reads .claude/skills/acting/SKILL.md |
| 2 | 2-1의 할아버지 `CHARACTER_ACTING` 줄 글자 그대로 | PASS | "GRANDPA: waits without hoping. Between stillness and quiet resignation; a sigh or a frown = failed take, a smile = failed take. His eyes stay on the empty road on the tree side with slow, heavy blinks." (acting_2-1.lines 일치) |
| 2 | 입 잠금 상향 + 2-1 위험(입 움직임 금지) 동반, 본문에 컷 번호 없음 | PASS | "GRANDPA does not say a single word: no attempt to speak, no parted lips, no mouthing."; "Forbidden: GRANDPA moving his lips" |
| 2 | 카드 2-2 v0, 참조 3=태그 3, 가져온 OK 기록 | PASS | 새 project/cuts/2-2.md "가져온 OK: 2-1 영상 — 표정(CHARACTER_ACTING 할아버지 줄)…" |
| 2 | 검사 후 표시 (G7), 생성 안 함 | PASS | Bash check_prompt --kind video … --refs 3 --seconds 8 (5회 반복 후 WARN 해소, 5,086자); "보낼까요? '영상으로 만들어'나 '보내'라고 해 주세요." |
| 2 | 연기 새 문장: 목표·몸·눈·감정 범위 양 끝, 절제 범위 | PASS | "stillness and quiet resignation; a sigh or a frown = failed take, a smile = failed take"; 손 줄 "it does not startle, it simply stops" |
| 전체 | G9·G2 | PASS | "screen-left hand, nearer the tree"; 한국어(T2에서 첫 줄 문장이 두 번 반복되는 경미한 중복) |

## 검사기 결과

- C14 t2 코드블록 1: `--kind video --refs 3 --seconds 8 --must-include grandpa+bag+light+acting_2-1`: OK — video 프롬프트 5086자, 걸린 항목 없음

## 추가 발견

- 없음

## 키트 결함

- 없음 (이 체인에서 플레이어 오류의 원인이 된 키트 문서 결함은 발견하지 못함)

## 총평

표정만 정확히 가져오고 모션은 거절한 모범 사례. 결함 없음.
