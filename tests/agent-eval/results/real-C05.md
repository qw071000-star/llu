# real-C05 장소 반대 방향 뷰 (2턴)
| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | image-prompt+location+location-view 열람. 부모 `job-lc001v1`, 높이·랜드마크·종점·뒤집힌 LIGHT LOCK 4개 제안, 좌우/빛 뒤집힘 짚음. 프롬프트·생성 없음. |
| 2 | PASS | `Do not inherit its camera angle…` 있음, `WITHOUT reframing` 없음, 카메라는 "looking back along the same central axis toward the original camera position", `not a horizontal mirror`, 해 "from screen right, the persimmon-tree side", 폴 LEFT·감나무 RIGHT, MASTER GEOMETRY에 "as seen from across the road", 동서남북 없음. |
검사기(채점자, `--kind image --refs 1 --must-include` 대장 LIGHT/PALETTE/ERA): `OK — image 프롬프트 2882자, 걸린 항목 없음`
추가 발견: MASTER GEOMETRY를 글자 그대로 넣은 뒤 틀에 없는 `Except:` 줄을 플레이어가 만들어 덮음(벤치·뒷벽·"정류장이 가운데"가 새 카메라와 모순).
## 키트 결함
- `image-prompt/location-view.md:22,45`: 카메라가 장소 안쪽에 들어가면 verbatim MASTER GEOMETRY(정면에서 본 서술)와 충돌하는데 처리 규칙이 없음 → "카메라가 구조물 안이면 부모 줄 뒤에 `Except: …` 한 줄로 이 뷰에서 보이는 것만 덮는다"를 규칙으로 넣는다.
총평: 기대 모두 충족, 키트 공백만 하나.
