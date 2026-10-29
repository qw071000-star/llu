# real11-C40 한 번에 여러 수정 — "머리 풀고, 장화 파란색으로, 하늘 더 붉게" 3-3 (2턴) — PASS 1 / 부분 1 / FAIL 0 (real9: PASS 2 / 부분 0 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `image-prompt/SKILL.md`+`first-frame.md`, 자기 컷(카드·OK 카드)만. 세 변경을 나눔: "한 번에 하나씩만 바꾸므로 머리 → 장화 → 하늘 순서로 하고, 지금은 머리만 다룹니다". 정본 충돌: "대장의 CH-002는 낮은 포니테일이고 장화는 빨간색이라 캐논과 다릅니다 … 이 컷만" 질문, "하늘은 PALETTE·LIGHT LOCK이 걸려 있어 따로 물어야 합니다". 승인본 새 테이크 질문, 머리 모양 제안값(어깨 아래, 3/4 뒷모습). 질문 5개 한 묶음, 생성 없음. (장화 항목이 2번 안에 접혀 있어 눈에 덜 띔, 경미) |
| 2 | 부분 | "이 컷만. 제안대로 머리부터 해"를 보지 않은 프롬프트에 대한 생성 지시로 받지 않고 프롬프트를 쓴 뒤 "보낼까요?"로 끝냄(지침 2번 충족). 머리 하나만: `CHANGE — the girl's hair …`, PRESERVE에 얼굴·옷·빨간 장화·`the screen-right hand, nearer the sign`, WARDROBE·LIGHT LOCK 글자 그대로, `LEFT and RIGHT are SCREEN directions …`, `Exactly 1 person is visible.`, 블록 밖 모드·참조·모델·1k·폴더, 위험 4개, 카드 3-3 [5][11] 기록(diff 확인, `(제안값)` 표시). **빠진 것:** 지침 Output의 "Edit prompts … each changed value as 전 → 후" 줄이 블록 밖에 없음 |

## 검사기
내 실행 `--kind image --refs 1 --must-include girl+light`: `OK — image 프롬프트 1744자, 걸린 항목 없음`

## 추가 발견
- G1 위반 없음. `tmp/` 삭제 확인. 컷 카드 [8]·[10]의 `[ ]`는 카드 빈칸이고 프롬프트에는 빈칸 없음(G5 충족).
- 2턴 카드 갱신이 [5]에 "머리: …" 줄을 새로 넣어 카드 틀의 [5] 항목 이름과 다른 줄이 늘었으나 허용 범위.

## 키트 결함
- C31과 같다: LOCKED EDIT 답에서 "전 → 후"가 빠질 수 있다. `kit/instructions.md` Output "Editing a confirmed prompt" 줄이 한 불릿에 여러 규칙을 담고 있다. 제안: 같은 문장을 `kit/skills/image-prompt/SKILL.md` §3 끝에 "After the code block, list each changed value as 전 → 후" 한 줄로 반복한다.

## 총평
세 변경 분리·정본 충돌·승인 컷 처리는 정확했으나 2턴 답에 전 → 후 줄이 없다.
