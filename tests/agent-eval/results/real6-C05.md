# real6-C05 장소 반대 방향 뷰 (2턴) — PASS 2 / 부분 0 / FAIL 0 (real5: PASS 2)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | image-prompt SKILL + location.md + location-view.md. 카메라 위치·높이·샷 크기 / 랜드마크 / 길 건너 종점 / 빛(좌우가 뒤집힘, "해가 화면 오른쪽, 감나무 쪽")을 제안값+이유로 4항목. 부모 `job-lc001v1`. 프롬프트·생성 없음 |
| 2 | PASS | `Do not inherit its camera angle, framing or composition.` / `not a horizontal mirror of the reference` / 카메라를 원본 관계로("far end, inside the shelter … looking back along the same central axis") / MASTER GEOMETRY에 `as seen from across the road` / 새 LIGHT LOCK `Low dusk sun from screen right, the persimmon-tree side` / `sign is at screen LEFT and the persimmon tree is at screen RIGHT`. 동서남북 없음. `WITHOUT reframing` 없음 |

검사기: `check_prompt --kind image --refs 1 --must-include <player 고정문장>` → `OK — image 프롬프트 2896자, 걸린 항목 없음` (V2 LIGHT LOCK·`not a horizontal mirror`·`Do not inherit` 포함 확인 파일로 재실행도 OK)
추가 발견: 임시 파일 `lc001v2_prompt.txt`, `lc001v2_fixed.txt`를 RUN 루트에 남김(player-rules는 `RUN/tmp/`). "벤치 높이"를 좌면 0.45m로 옮기고 되짚을 수 있게 알림(좋음).
키트 결함: 없음.
총평: PASS 2 유지. 이전에 문제 되던 좌우·빛 뒤집기를 화면 기준으로 정확히 처리.
