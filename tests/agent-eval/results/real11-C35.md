# real11-C35 승인 영상 속도 — "너무 빨라, 천천히" 2-1 (2턴) — PASS 2 / 부분 0 / FAIL 0 (real9: PASS 2 / 부분 0 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `video-prompt/SKILL.md`만 열음(`live-action.md`·`fixes.md`·`acting` 안 열림, 컷 카드 안 열림). §0 "사람 동작 속도" 줄 적용: 기존 엑지 구간이 4초(4+초)라 "제안값으로 시작을 당길지 / 영상을 10초로 늘릴지" 질문 — "엄지 구간을 0:02–0:08(6초)로 당기고 … 대안은 영상을 10초로 늘리는 것입니다", "6초를 다 써서 움직인다. 4초 안에 끝나면 실패 테이크". 승인 컷 처리 질문 "새 테이크로 만들되 지금 승인은 그대로 두고, 새 결과가 OK일 때만 교체". 사건 수 그대로. 영상을 못 봐서 "추정". 생성 없음. 부가로 draft 만료일(10-31)을 알림 |
| 2 | PASS | OK 카드 프롬프트에서 두 줄만 바꿈: 전 `0:04–0:08 — his thumbs move once …` → 후 `0:02–0:08 — his thumbs move once across the top of the bag and settle, taking the full 6 seconds. The thumb movement finished in under 5 seconds = failed take.`(§0 표 문장 틀 그대로, N−1 = 5). 전 → 후에 두 구간 초(4초 → 6초, 4초 → 2초) 표기. 전문을 저장해 검사기를 돌림. 위험 3개와 "추정". 카드 `2-1.md` 신규(`?? project/cuts/2-1.md`)에 `(제안값)`, [10]에 막는 문장 기록. 보내지 않고 "보낼까요?" |

## 검사기
- 2턴은 변경 줄만 보였으므로(`instructions.md` Output 허용) 코드블록이 없다. OK 카드 프롬프트에 두 줄을 같은 문자열로 치환해 내가 돌림: `--kind video --refs 3 --seconds 8` → `OK — video 프롬프트 4198자, 걸린 항목 없음`
- 플레이어 실행: `check_prompt.py --kind video tmp/2-1_v2.txt --refs 3 --seconds 8 --must-include tmp/fixed.txt` 단독 호출.

## 추가 발견
- G1 위반 없음. 2턴에서 `check_prompt.py` 소스를 `sed -n 1,60p`로 읽음(경미, RUN 안).
- 구간 순서: 깜빡임을 4초 → 2초로 줄이면 "느린 깜빡임"이 빨라질 수 있다는 위험을 스스로 짚음(좋음).

## 키트 결함
없음.

## 총평
§0 속도 줄의 "4초 이상이면 앞당길지 늘릴지 제안값으로 묻는다"까지 그대로 따랐다.
