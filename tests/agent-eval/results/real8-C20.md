# real8 C20

**PASS 2 / 부분 0 / FAIL 0** (real7 PASS 2 유지)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `location.md`+`location-edit.md`만; '광원 켜기와 시간대는 따로 떼어낼 수 있어서 한 생성에는 한 가지만', 1단계=형광등(사용자가 먼저 말함); '1단계 결과는 아직 요청하신 "해 진 직후" 상태가 아닙니다'; 형광등 위치(화면 가운데·벤치 위) 제안값; STATE·부모 `job-lc001v1` |
| 2 | PASS | 표준 LOCKED EDIT 여는 문장; `one state change only: the tube is off and becomes switched on`; `lit but does NOT glow: no halo, no bloom, no light spilling past the shelter`; PRESERVE에 해 LIGHT LOCK만 남김; `ONLY CHANGE: the shelter's single fluorescent tube, from off to on`; 위험 5개; '이 결과는 아직 해 진 직후가 아닙니다'; 보낼지 물음 |

## 검사기
내 실행 `--kind image --refs 1`: `OK — image 프롬프트 1644자, 걸린 항목 없음`. (`light.lines` must-include를 주면 FAIL이나, 이 편집이 LIGHT LOCK의 `tube is off`를 바꾸는 작업이라 정상.)

## 추가 발견
G1(mcp 호출·생성) 위반 없음, RUN 밖 읽기 없음. 번짐 방지 문장 끝이 키트 문구 `no light spilling onto [surfaces]`가 아니라 `past the shelter`(경미, 의미 동일). 프롬프트 쓰기 전 LIGHT LOCK 충돌을 '새 LIGHT LOCK도 이 위치로 씁니다'로만 짚음. `tmp/` 파일 삭제 확인.

## 키트 결함
없음.

## 총평
1턴 분리 제안 → 2턴 형광등 프롬프트, 기대 충족.
