# real9-C40 한 번에 여러 수정 — "머리 풀고, 장화 파란색으로, 하늘 더 붉게" 3-3 (2턴) — PASS 2 / 부분 0 / FAIL 0 (real8: PASS 2 / 부분 0 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `image-prompt/SKILL.md`+`first-frame.md`+`character-edit.md` Read, 3-3 카드·OK 카드(자기 컷). `머리·장화·하늘은 세 가지 변경이라 한 생성에 넣을 수 없습니다(지침 3번). 세 번으로 나누고` 순서 머리 → 장화 → 하늘(하늘은 전체 색에 영향이라 마지막). 장화는 정본 WARDROBE `red rain boots`·CH-002 `low ponytail`과 다름을 짚고 "이 컷만이면 `Except:` 한 줄, 3-1·3-2와 이어질 때 달라 보임" 질문. 하늘은 대장 PALETTE `15% deep blue dusk sky`와 부딪침 + LIGHT LOCK 유지 + 인물·정류장 빛은 건드리지 않음. 승인 컷 새 테이크 대체 질문. 6개 제안값, 하늘 면적은 "추정". 생성 없음 |
| 2 | PASS | "이 컷만. 제안대로 머리부터 해." — 아직 보지 못한 프롬프트이므로 생성 지시로 보지 않음(`이 프롬프트는 방금 처음 보시는 것이라 "머리부터 해"는 생성 지시로 보지 않았습니다`, 규칙 2). 1단계 LOCKED EDIT는 머리 하나만: `CHANGE — the girl's hair`, `do not regenerate … the face`, `No ponytail, no elastic, no braid`, WARDROBE·LIGHT LOCK·`the screen-right hand, nearer the sign` 글자 그대로, `LEFT and RIGHT are SCREEN directions`, `Exactly 1 person is visible.` 블록 밖 모드·참조 1·모델·1k·폴더, 전 → 후 한 줄, 위험 5개, 맞은 것/미달 구분. 카드 3-3 [5][8][11]에 `(제안값)`과 `Except` 기록 |

## 검사기
내 실행 `--kind image --refs 1 --must-include girl+light`: `OK — image 프롬프트 1821자, 걸린 항목 없음`

## 추가 발견
- G1 위반 없음. `tmp/` 삭제 확인.
- WARDROBE 문장에 `red rain boots`가 그대로 남고 `Except:`는 머리만 적음 — 1단계는 머리만 바꾸므로 올바름(장화 `Except`는 2단계에서).
- 카드 [8] 고정 설명문 칸에 이 컷 `Except` 줄을 덧붙였는데, 고정 설명문 칸 자체는 정본 글자 그대로 두었다 — 규칙 5 충족.

## 키트 결함
없음.

## 총평
세 변경을 순서대로 분리하고 정본 충돌을 `Except`로 처리, "해"를 생성 지시로 오해하지 않음.
