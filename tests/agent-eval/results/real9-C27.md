# real9-C27 나이 바꾸기 — 할아버지 50대 (2턴) — PASS 2 / 부분 0 / FAIL 0 (real8: PASS 2 / 부분 0 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `image-prompt/SKILL.md`+`character-edit.md` Read(`character.md` 안 열림). 시작 보고 세 줄(판단·읽은 것·할 일). 기준 CH-001 `job-ch001`, 신규 아님("새 인물이 아니라 틀 2(젊게)"). 4개 제안값: 목표 55세, 나이 표지(주름·머리색·어깨·손), 의상 그대로(회상 옷이 다르면 시트 확정 뒤 따로 — 한 생성에 하나), 쓰임 `char_grandpa_50s_v1`. 2k. 생성 없음 |
| 2 | PASS | 틀 2 전문: `IDENTITY BONES: … Do not replace the face with a different person.`, `LEFT PANEL: keep it intentionally HEADLESS, an editorial clothing crop, not an injury.`, `OUTFIT: the exact same clothes in every panel.`, 끝 줄은 `[젊게]` 줄 `no babyface, no beauty filter`. 얼굴 새 묘사 없음(뼈대 보존만). `LEFT and RIGHT are SCREEN directions` 포함. 위험 5개, "72세 → 55세" 바뀐 값 줄. 대장 CH-001에 `초안(제안값)` |

## 검사기
내 실행 `--kind image --refs 1`: `OK — image 프롬프트 1575자, 걸린 항목 없음`

## 추가 발견
- G1 위반 없음. `tmp/` 삭제 확인.
- 위험 목록을 코드블록 앞에 두었다(지침 규칙 7 "위험 목록과 프롬프트를 먼저 보인다" 충족).

## 키트 결함
없음.

## 총평
틀 2 충실, 의상 고정·한 생성 한 가지 지킴.
