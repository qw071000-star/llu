# real7 C20

**PASS 2 / 부분 0 / FAIL 0** (real6 PASS 2 유지)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `location.md`+`location-edit.md`(+SKILL.md)만; STATE·부모 `job-lc001v1`; '불 켜기와 시간대는 떼어 낼 수 있어서 한 생성에 하나만, 말씀하신 순서대로 불을 먼저'; ①의 결과는 '요청하신 상태가 아닙니다'; 새 LIGHT LOCK 제안(②) |
| 2 | PASS | 표준 LOCKED EDIT 여는 문장; `CHANGE — … one state change only: the tube is off and becomes lit`; `lit but does NOT glow: no halo, no bloom, no light spilling onto the road …`; PRESERVE EXACTLY/ONLY CHANGE; 장소 재묘사 없음; 위험 목록; '해 진 직후는 ②단계'; 대장 `초안(제안값)` 줄 |

## 검사기
내 실행 `--kind image --refs 1`: `OK — image 프롬프트 1497자, 걸린 항목 없음` (`light.lines`를 must-include로 주면 FAIL이나, 이 편집은 LIGHT LOCK의 `tube is off`를 바꾸는 작업이라 정상 — 플레이어도 PRESERVE에 해만 남기고 바뀐 줄을 '전 → 후'로 보임).

## 추가 발견
G1(mcp 호출·생성) 위반 없음, RUN 밖 읽기 없음. 없음.

## 키트 결함
없음.

## 총평
1턴 분리 제안 → 2턴 형광등 프롬프트, 기대 전부 충족.
