# 에셋·폴더 대장 — 「빈 정류장」

> 고정 설명문은 프롬프트에 글자 그대로 붙인다. 바꿔야 하면 새 버전(v2)을 만들고, 옛 것은 폐기 목록으로 옮긴다.
> 확정 이미지의 정본은 Higgsfield 저장본이다. job ID로 직접 열어 확인한다.
> 확정 에셋을 만든 프롬프트와 설정은 OK 대장(`ok-cuts.md`)의 에셋 ID 카드에 있다.

## Higgsfield 저장 폴더

| 항목 | 이름 | ID |
|---|---|---|
| 워크스페이스 | 팀 워크스페이스 | `ws-sim-0001` |
| 프로젝트 | 「빈 정류장」 | `prj-sim-0001` |
| 공통 에셋 | 00 에셋 / 인물 · 장소 · 소품 · 그림체 | `fld-chars` · `fld-locs` · `fld-props` · `fld-style` |
| 시험·보관 | 99 시험·보관 | `fld-archive` |

| 컷 | 컷 폴더 | 승인 | 거절 |
|---|---|---|---|
| 1-1 | `fld-1-1` | `fld-1-1-ok` | `fld-1-1-ng` |
| 1-2 | `fld-1-2` | `fld-1-2-ok` | `fld-1-2-ng` |
| 1-3 | `fld-1-3` | `fld-1-3-ok` | `fld-1-3-ng` |
| 2-1 | `fld-2-1` | `fld-2-1-ok` | `fld-2-1-ng` |
| 2-2 | `fld-2-2` | `fld-2-2-ok` | `fld-2-2-ng` |
| 3-1 | `fld-3-1` | `fld-3-1-ok` | `fld-3-1-ng` |
| 3-2 | `fld-3-2` | `fld-3-2-ok` | `fld-3-2-ng` |
| 3-3 | `fld-3-3` | `fld-3-3-ok` | `fld-3-3-ng` |
| 3-4 | `fld-3-4` | `fld-3-4-ok` | `fld-3-4-ng` |
| 3-5 | `fld-3-5` | `fld-3-5-ok` | `fld-3-5-ng` |

## 이름 규칙

| 종류 | ID | Higgsfield 요소 이름 |
|---|---|---|
| 인물 | `CH-001` | `char_<인물>_<상태>_v1` |
| 장소 | `LC-001` / 뷰 `LC-001-V1` | `loc_<장소>_<뷰>_v1` |
| 소품 | `PR-001` | `prop_<물건>_v1` |
| 그림체 | `ST-001` | `style_<이름>_v1` |

## 인물

### CH-001 할아버지

| 확정 시트 job | 처리 모델 | 요소 ID | 파생 | 한계 |
|---|---|---|---|---|
| `job-ch001` | GPT Image 2.5 | `char_grandpa_autumn_v1` | — | 없음 |

```text
IDENTITY: A Korean man in his early seventies with weathered tan skin, deep-set dark eyes, a short grey crew cut, a lean build and slightly stooped shoulders.
WARDROBE: A faded olive work jacket over a cream knit vest and a white collared shirt, dark grey wool trousers, scuffed brown leather shoes.
ACTING PROFILE: Character acting as GRANDPA. Seventy-two, lean, slightly stooped. He has stopped expecting things and does not let it show. Few words, slow hands, eyes that settle on one point and stay.
VOICE: "A man in his seventies from the rural countryside. Low, dry voice; slow, few words; goes quiet under pressure."
```

### CH-002 손녀

| 확정 시트 job | 처리 모델 | 요소 ID | 파생 | 한계 |
|---|---|---|---|---|
| `job-ch002` | GPT Image 2.5 | `char_girl_raincoat_v1` | — | 주근깨 약함 |

```text
IDENTITY: A Korean girl of about ten with a round face, straight black hair in a low ponytail and a slim build.
WARDROBE: A yellow raincoat over a navy school uniform, white knee socks and red rain boots.
ACTING PROFILE: Character acting as GIRL. Ten, quick, practical. Hides worry by doing something with her hands.
VOICE: "A ten-year-old girl's clear, slightly hoarse voice, quiet and careful."
```

### CH-003 버스 기사

| 확정 시트 job | 처리 모델 | 요소 ID | 파생 | 한계 |
|---|---|---|---|---|
| | | | | |

```text
IDENTITY: [ ]
WARDROBE: [ ]
ACTING PROFILE: [ ]
VOICE: "[ ]"
```

## 장소

### LC-001 시골 버스 정류장

```text
MASTER GEOMETRY (as seen from the road, looking north): A concrete bus shelter with a corrugated tin roof stands at the centre, its open front facing the road. A wooden bench runs along its back wall. A painted metal timetable sign stands on a pole at the east side of the shelter. A bare persimmon tree stands at the west side. Harvested rice paddies stretch behind it to low hills.
LIGHT LOCK (장소 기준 방향으로): Low dusk sun from the west, the persimmon-tree side, is the only key; the shelter's single fluorescent tube is off.
Nothing else: no other buildings, no cars, no people, no legible text.
```

| 뷰 | 계보 | 카메라(어디서 어디를) | 화면 좌 = / 우 = | 부모 job | 확정 job | 처리 모델 | 상태 | 한계 |
|---|---|---|---|---|---|---|---|---|
| `LC-001-V1` | MASTER | 길 건너편 서서 눈높이, 북쪽(정류장 정면)을 봄 | 서(감나무) / 동(시간표) | — | `job-lc001v1` | GPT Image 2.5 | 확정 | 감 열매 조금 많음 |

요소 이름: `loc_busstop_road_v1` = LC-001-V1

## 소품

### PR-001 왕진 가방

| 요소 ID | 출처 | 크기 (cm · 신체 기준) | 물성 | 상태 머신 |
|---|---|---|---|---|
| `prop_doctor_bag_v1` | 3-1 장면 프레임에서 잘라 만듦 | 폭 약 40cm, 할아버지 무릎 폭 | 무겁다, 손잡이에서 처진다, 각이 서지 않는다 | 닫힘 → 열림 (3-4에서 한 번) |

고정 설명문: `A worn brown leather doctor's bag with a brass clasp, about 40 cm wide, hanging heavy from its handles.`

### PR-002 할머니 사진 액자 (확정 전)

| 요소 ID | 출처 | 크기 (cm · 신체 기준) | 물성 | 상태 머신 |
|---|---|---|---|---|
| `prop_photo_frame_v1` (제안값) | 회색 스튜디오 신규 생성 예정 (영상용은 장면 프레임에서 잘라 만듦) | 약 15×20cm, 사진 10×15cm, 할아버지 손바닥 하나 반 (제안값) | 가볍고 단단하다, 휘지 않는다, 유리가 빛을 한 줄 반사한다 (제안값) | 가방 PR-001 안(안 보임) → 3-4에서 할아버지가 두 손으로 꺼내 무릎 위 가방에 기대 세움 → 3-5 할아버지 손에 듦 (제안값) |

초안(제안값): 할머니 사진이 든 액자 · 3-4에서 PR-001 가방 안에서 나온다 (2026-10-28 · 사용자 말). 짙은 갈색 나무 테, 유리, 뒤 받침다리, 바랜 컬러 사진 속 60대 한국 여성 상반신 정면·짧은 파마머리·옅은 미소, 모서리 칠 벗겨짐·유리 잔 흠집·사진 가장자리 변색 (2026-10-28 · 사용자 "그대로" → 제안값). 저장 `fld-props`. 미정: 영상에서 할머니 얼굴이 또렷이 보이는지

고정 설명문 (확정 전 초안, 제안값): `A small dark brown wooden standing photo frame, about 15 x 20 cm (one and a half times an old man's palm), with a glass front and a folding wooden easel stand at the back, holding a faded colour 10 x 15 cm portrait photograph of a Korean woman in her sixties, head and shoulders, facing the camera, short permed hair, a faint smile; paint worn off at the frame corners, fine scratches on the glass, the photograph's edges yellowed with age.`

## 그림체

### ST-001 (없음 — 실사 작품)

## 폐기 목록

| ID / job | 이유 | 날짜 |
|---|---|---|
| `job-ff-3-2-old` | 할아버지 시선이 카메라를 봄 | 2026-10-27 |
