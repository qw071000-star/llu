# real13-C31 장소 시간대 바꾸기 — "밤으로, 형광등 켜진 걸로" (2턴) — PASS 1 / 부분 1 / FAIL 0 (real12-recheck: PASS 2 / 부분 0 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | 부분 | 내용은 맞다. `location-edit.md`를 열고 "밤"과 "형광등 켬"을 둘로 읽어 두 번에 나누는 안(밤 먼저, "1단계 결과는 아직 '형광등 켜진 밤'이 아닙니다"), 1단계 LIGHT LOCK을 화면 기준(`from screen left, the persimmon-tree side`)으로 새로 제안, 형광등 위치는 대장에 없어 제안값으로 질문. 생성 없음. 그러나 첫 줄이 `**읽은 것:**`이고 "[N]번 [작업명]으로 진행합니다."(8번)가 없다 → 형식만 부분 |
| 2 | PASS | "그대로"를 수락으로 받아 1단계(밤) LOCKED EDIT. 여는 문장, `CHANGE — the sky and the light …`, 부모 LIGHT LOCK을 PRESERVE에서 빼고 바뀐 광원만 CHANGE에 씀(`location-edit.md:23`), 켜지 않는 형광등은 PRESERVE에 `stays off`. 해 질 녘 LIGHT LOCK 문장을 남기지 않음. 블록 밖 "전 → 후" 3줄, 위험 4개, "이 1단계 결과는 아직 '형광등 켜진 밤'이 아닙니다" 재고지. 대장에 `(제안값)` 기록(diff). 생성 안 함 |

검사기: `--kind image C31t2_1.txt --refs 1` → `OK — image 프롬프트 1636자, 걸린 항목 없음` (밤 LIGHT LOCK은 새 문장이라 must-include 대상이 없음)

추가 발견
- 프롬프트의 `cracked asphalt edge`, `orange fruits`는 OK 대장 V1 카드 문장에서 온 것(`ok-cuts.md:106`)이라 지어낸 것이 아님.
- 형광등 위치 질문 3번은 대장에 위치가 없어 "확인 필요"라고 정직하게 표시(`location-edit.md:23`).

키트 결함
- `kit/instructions.md:41`: 장소 만들기·고치기 질문 턴에서도 첫 줄이 "[N]번 …"이 아니다(C24·C25와 같음).

총평: 시간대와 조명을 나누는 판단과 LIGHT LOCK 재작성은 맞았고, 질문 턴 첫 줄만 빠졌다.
