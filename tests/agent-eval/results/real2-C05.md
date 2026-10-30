# real2-C05 장소 반대 방향 뷰 (2턴) — PASS 0 / 부분 2 / FAIL 0 (지난: PASS 2)
| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | 부분 | `image-prompt`(Skill)+`location.md`+`location-view.md`. 6항목(카메라 방식·높이·렌즈·랜드마크·종점·뒤집힌 LIGHT LOCK "from screen right, the persimmon-tree side")과 "먼저 짚을 것: 카메라가 쉘터 안 → `Except:` 한 줄" 좋음. 감점: 카메라 방식을 "제자리 180° 회전"으로 제안했는데 부모 카메라는 길 건너편이라 사용자 말("정류장 안에서 길 쪽")과 안 맞음 → 2턴에 스스로 "정정". 랜드마크 ② 문장도 뒤죽박죽("감나무 쪽 풍경이 아니라 시간표 표지판 뒷면"). |
| 2 | 부분 | 프롬프트 내용 PASS: `Do not inherit its camera angle…`, `WITHOUT reframing` 없음, CAMERA "far end… looking back along the same central axis toward the original camera position", `not a horizontal mirror`, MASTER GEOMETRY "(as seen from across the road…)" + `Except:` 줄, "sign pole at screen LEFT … persimmon tree at screen RIGHT. Low dusk sun from screen right, the persimmon-tree side", 동서남북 없음. 감점: (1) 검사기 WARN(태그 없음)을 남김 — 참조를 `<<<…>>>` 없이 `loc_busstop_road_v1`로만 불러 참조 지정이 불확실. (2) 모드·참조·모델 줄을 `~~~` 코드블록에 넣어 코드블록이 둘("코드블록 하나"). |
검사기(채점자 `--kind image --refs 1`): `WARN  붙일 참조 1개인데 프롬프트에 <<<…>>> 태그가 없다…` / `— FAIL 0 · WARN 1 · 2536자` → 근거 있는 WARN(오탐 아님). `--refs` 없이는 OK.
추가 발견: 높이 "벤치 높이"를 0.45m로 정하고 1.1m 가능성을 고지한 것은 키트(`location-view.md` 공통)대로.
## 지난 회차 대비
- 지난 키트 결함 `Except:` 규칙 공백: `location-view.md`에 "카메라가 구조물 안에 들어가면 … `Except:`" 추가되어 플레이어가 규칙으로 적용 → 해결.
- 새로 생긴 문제: 태그 WARN, 카메라 방식 오제안.
## 키트 결함
- `image-prompt/SKILL.md:21`: "실제 요소 이름(`loc_…_v1`)으로 바꾼다"가 꺾쇠까지 지우라는 뜻으로 읽힘(C05가 그렇게 씀, 검사기는 `<<<…>>>`를 요구) → "꺾쇠는 그대로 두고 안의 이름만 바꾼다(`<<<loc_busstop_road_v1>>>`)"로 고친다.
- `image-prompt/location-view.md:13,35-37`: 카메라 방식 두 가지 중 어느 쪽인지 고르는 기준이 없음(부모 카메라가 공간 밖에서 안을 보고 있으면 "제자리 회전"은 쉘터에서 멀어지는 쪽) → "부모 카메라가 대상 밖에 있고 사용자가 안에서 본다면 '먼 끝으로 이동' 방식"을 한 줄 추가.
총평: 지난 결함은 고쳐졌으나 제안 오류와 태그 WARN으로 후퇴.
