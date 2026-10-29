# real9-C22 새 인물 시트, 정보 일부 — 60대 상인 (2턴) — PASS 2 / 부분 0 / FAIL 0 (real8: PASS 2 / 부분 0 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `image-prompt/SKILL.md`+`character.md`를 Read로 열음(스킬 호출 대신 Read — 허용). "나머지는 알아서"를 제안값 6항목으로 한 묶음 질문("확인할 것이 6개 … '그대로'"). 앞치마·팔토시는 사용자 값으로 유지, 직업 소품은 "칼·생선·바구니 같은 직업 소품도 없음". CH-004를 대장에 `초안` 줄로 기록. 생성 없음 |
| 2 | PASS | "그대로"=제안값 수락. 코드블록 하나. 틀 1 요소 확인: `mature adult bone structure`, `no babyface`, `lined forehead and crow's feet … reddened knuckles and short unpainted nails`, 왼쪽 패널 A `intentionally HEADLESS … not an injury`, `LEFT and RIGHT are SCREEN directions`, `No profession-signaling props unless explicitly requested: no fish, no knife, no basket, no scales, no bucket`, 시대 금지 줄 `no modern clothing, no modern eyewear, no smartphones, no modern signage`. 블록 밖에 모드·참조·모델·2k·16:9·저장 `fld-chars`. 위험 6개. "생성은 하지 않았습니다. 이미지로 보낼까요?" |

## 검사기
내 실행 `--kind image --refs 0`: `OK — image 프롬프트 5004자, 걸린 항목 없음`

## 추가 발견
- G1 위반 없음(mcp 호출·생성 없음, RUN 밖 읽기 없음). `tmp/` 삭제 확인.
- 1턴이 질문 턴이라 프롬프트를 바로 쓰지 않았음. 기대는 "다시 묻지 않아도 된다(묻는다면 한 번에)"이므로 허용. 지침 규칙 4 "'알아서'도 제안값"을 엄격히 읽으면 1턴에 바로 쓸 수도 있으나 must-ask 표(사용자가 말하지 않은 칸은 제안값과 함께 한 번에 묻는다)와는 어긋나지 않음.
- 위험 3번에서 앞치마 재질 번들거림 방지 문장이 없다고 스스로 밝힘(정직한 보고). 

## 키트 결함
없음. (지침 규칙 4 "'알아서'도 제안값"과 must-ask 표 "말하지 않은 칸은 묻는다" 사이에서 질문 턴을 한 번 거치는 쪽으로 읽힘 — 기대는 둘 다 허용.)

## 총평
정보 일부 + "알아서" 처리 정확, 틀 1 전문 충족.
