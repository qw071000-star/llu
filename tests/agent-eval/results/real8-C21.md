# real8 C21

**PASS 0 / 부분 2 / FAIL 0** (real7 PASS 2 → 하락)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | 부분 | 시대 정본 충돌(`decisions.md` 1990년대 초)을 짚고 '별도 2020년대 판' vs 작품 전체 질문, '한 생성에 한 층만' 알림은 ✓. 그러나 층 순서 제안의 3단계가 `STRUCTURAL SURFACES`와 `LIGHTING` 두 층을 한 단계로 묶음('3단계: … 지붕·도로 포장을 정리하고, 형광등 → LED는 따로 다룹니다'), `IDENTITY AND TEXT`(표지판 판) 단계는 아예 없음 → '한 생성에 한 층' 위반 계획 |
| 2 | 부분 | `this step changes only its FURNITURE / VEHICLES / FIXTURES`, 요소마다 목표 시대 대응물, `REMOVE:`, PRESERVE에 다른 층·건물 볼륨·LIGHT LOCK, `ONLY CHANGE: FURNITURE / VEHICLES / FIXTURES`, 1990s 잠금 없음 ✓. 그러나 CHANGE에 '표지판 판'(`flat-panel bus-stop information sign … its panel shows only blurred unreadable shapes`)까지 바꿈 → `location-edit.md:50` '표지판 판은 IDENTITY AND TEXT, 그 기둥은 FIXTURES' 위반(한 요소는 한 층) |

## 검사기
내 실행 `--kind image --refs 1 --must-include light.lines`: `OK — image 프롬프트 1891자, 걸린 항목 없음`. (검사기가 층 혼합은 못 잡음.)

## 추가 발견
G1(mcp 호출·생성) 위반 없음, RUN 밖 읽기 없음. T2 첫 줄 '순서는 말씀대로 받았습니다'인데 사용자가 '순서는 제안대로'라 한 것과 같은 뜻(무해). `tmp/` 삭제 확인.

## 키트 결함
`.claude/skills/image-prompt/location-edit.md:50` 층 목록에 권장 순서와 '한 단계 = 한 층(두 층 묶음 금지)'이 없어 계획 단계에서 층이 섞임 → 층 목록 뒤에 '권장 순서: IDENTITY AND TEXT → STRUCTURAL SURFACES → DOORS… → FIXTURES → LIGHTING → IMAGE CHARACTER. 순서 제안의 한 단계에도 층은 하나만'을 한 줄 추가.

## 총평
층 개념은 이해했으나 단계 설계와 표지판 판/기둥 구분에서 어김.
