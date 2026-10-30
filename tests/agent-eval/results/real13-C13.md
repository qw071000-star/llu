# real13-C13 "3-1의 색감과 질감으로 3-5 퍼스트 프레임" (2턴) — PASS 2 / 부분 0 / FAIL 0 (real12: PASS 2 / 부분 0 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | "11번 … ("3-1처럼"은 16번 다른 OK처럼을 함께 씁니다.)" `ok-reuse.md`·`first-frame.md` 엶, 카드 파일 없음. 3-1 시작 이미지 프롬프트에 색·질감 문장이 없음을 알아채고 "새 문장을 쓰지 않고 이 OK 이미지를 색 참조로 붙입니다". 질문 4개(카메라 거리 / 가방 열린 모양 / 0:00 손 자세 / 얼굴·인원). 가방 열림은 3-4 이후라 맞음 |
| 2 | PASS | 틀 2. 참조 4=태그 4(장소·인물·소품·`ff_3-1_v2`). 색 참조 권한 `controls only colour, grade, contrast and texture. Never take its subjects, composition, people or light direction.` 색 문장 지어내지 않음. WARDROBE·PROP·LIGHT LOCK 글자 그대로, `Except:` 가방 열림, `Exactly 1 person`, 손은 `screen-left hand, at the bag's left end` 형태. 거리 1m → 2m 변경을 "전 → 후"와 계산 이유로 보고(추정). `cuts/3-5.md` 생성(값을 쓰는 턴) |

검사기: `--kind image --refs 4 --must-include bag+light` → `OK — image 프롬프트 2602자, 걸린 항목 없음` (refs 2로 돌리면 태그 4개 FAIL이므로 4가 맞음)
추가 발견: 없음.
키트 결함: 없음.
총평: PASS 2.
