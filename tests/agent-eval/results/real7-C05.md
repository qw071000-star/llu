# real7-C05 장소 반대 방향 뷰 (2턴) — PASS 2 / 부분 0 / FAIL 0 (real6: PASS 2)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | image-prompt SKILL + location.md + location-view.md. 부모 LC-001-V1 `job-lc001v1`. 카메라(정류장 안으로 이동, 눈높이) / 랜드마크(감나무 화면 오른쪽·시간표 화면 왼쪽) / 길 건너 종점 / 새 LIGHT LOCK(해 화면 오른쪽, 감나무 쪽) 4항목. 좌우 뒤집힘을 이유에서 짚음. 프롬프트·생성 없음 |
| 2 | PASS | `Do not inherit its camera angle, framing or composition.`, `not a horizontal mirror of the reference`, 카메라를 원본과의 관계로("far end, inside the shelter, looking back along the same central axis"), MASTER GEOMETRY에 `as seen from across the road`, 새 LIGHT LOCK `Low dusk sun from screen right, the persimmon-tree side …`, `persimmon tree is at screen right … sign pole at screen left`. `WITHOUT reframing` 없음, 동서남북 없음. "벤치 높이"를 앉은 눈높이 1.1m로 해석했다고 알리고 좌면 0.45m 가능성 되물음 |

검사기: `--kind image --refs 1` (답 코드블록 및 플레이어 must 파일) → `OK — image 프롬프트 2655자, 걸린 항목 없음`
추가 발견: 임시 `lc001v2_prompt.txt`, `lc001v2_must.txt`를 RUN 루트에 남김(경미).
키트 결함: 없음.
총평: PASS 2 유지. 좌우·빛 뒤집기를 화면 기준으로 정확히 처리. G1: tools에 mcp__ 없음, generate_* 없음.
