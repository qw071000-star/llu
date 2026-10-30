# real2-C22

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | image-prompt SKILL·character.md. CH-004 매김(요소 `char_fishmonger_apron_v1`), "알아서"를 받아 얼굴·체형·의상·헤어에 제안값+이유를 한 묶음(5문항), 기본값으로 쓴 것(2k·16:9·fld-chars·A형 패널·배경)은 묻지 않음. 앞치마·팔토시 반영, 직업 소품 없음 |
| 2 | PASS | "그대로"를 제안값 수락으로 처리, 생성 안 함, "보낼까요?". 틀 1: `Mature adult bone structure…no babyface`, `lined forehead and crow's feet…reddened knuckles and short unpainted nails`, 왼쪽 패널 `HEADLESS…not an injury`, `No profession-signaling props unless explicitly requested: no fish, no knife, no bucket`, `no modern clothing`. 블록 밖 모델·2k·16:9·fld-chars. 검사 내가: `--kind image` → `OK — image 프롬프트 4977자, 걸린 항목 없음`(플레이어 보고 4977자와 일치) |

**PASS 2 / 부분 0 / FAIL 0** (지난 회차 PASS 2 유지; 검사 실행 확인)

키트 결함: 없음.
총평: 정확.
