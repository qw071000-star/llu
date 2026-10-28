# 03 영상 프롬프트 가이드

근거: 「어머니와 고등어」 씬 1(Seedance 2.5, 약 100회 생성), 다른 작품 The Prompter 씬 1(Seedance 2.5 영상 66개 분석), 나부코 배경 영상(Kling 4.0 76회). 빈 틀은 `templates/video-prompt.md`.

---

## 0. 먼저 기억할 일곱 줄

1. **글자 수보다 한 생성에 넣는 사건 수가 성패를 가른다.** 풀린 판은 대개 컷·동작·요소·대사 수를 줄인 판이었다.
2. **상태를 쓴다. 전환을 쓰지 않는다.** "점점 무너진다"가 아니라 시작 상태와 끝 상태를 각각 고정하고, 그 사이가 길면 생성을 나눈다.
3. **첫 프레임 = 영상 0:00 상태.** 시작 이미지를 쓰면 그 이미지가 0:00이고, 프롬프트의 첫 프레임 문단은 그 이미지와 같아야 한다(E-19).
4. **한 생성에 카메라 동작 하나.** 고정이면 끝까지 고정. 고정 + 궤도, 달리 + 줌 같은 겹침을 쓰지 않는다.
5. **좌우는 화면 기준이고, 본문에서는 화면 속 물건으로 가리킨다.** "화면 오른쪽 손"도 인물의 오른손으로 읽힌다 → "신발장 쪽 손"(E-14).
6. **참조마다 통제 범위를 적는다.** 장소 참조는 카메라·구도를 통제하지 않는다. 인물 참조는 얼굴·의상만.
7. **쓰기 전에 실패 위험을 꼽고, 위험마다 막는 문장 한 줄.** 금지 목록을 끝없이 늘리지 않는다.

---

## 1. 생성 단위(샷) 설계 — 프롬프트를 쓰기 전에

| 정할 것 | 기준 |
|---|---|
| 길이 | 대사·동작 있는 실사 컷 5~10초, 배경·풍경 10~15초. 30초 + 끝 프레임은 속도가 한쪽에 몰리고 질감이 떨렸다(E-25). 15초를 넘으면 둘로 나눈다 |
| 이어 붙이기 | 나눈 생성은 앞 생성의 지정 프레임을 `start_image`로 받는다. 앞에 '여백'을 붙이지 않는다. Extend(영상 연장)는 모델이 지원하고 꼭 필요할 때만 |
| 장소 | 한 생성에 한 장소. 한 클립에서 장소가 세 번 바뀌면 모델이 빈 곳을 자기 스타일로 채웠다(E-26). **새 장소는 먼저 이미지로 확정**한다 |
| 사건 수 | 한 생성에 사건 1~3개. 인물별 할 일은 하나씩. 대사는 한 줄당 2~4초 |
| 끝 프레임 | 꼭 도착해야 할 구도가 있을 때만. 없으면 쓰지 않고, 다음 컷 첫 프레임을 말로 설계해 컷으로 잇는다 |
| 형식 | 인물·소품·대사가 있는 실사 → 15블록(§2). 인물 없는 배경·풍경·그림체 영상 → 4문단(§3) |

**반복 실패의 신호**: 같은 핵심 실패가 연속 2회 또는 최근 4회 중 3회 → 문장을 더하지 말고 **샷을 바꾼다**(컷 삭제, 동작 삭제, 요소 삭제, 둘로 쪼개기, 개념 단순화).

---

## 2. 15블록 형식 (실사·인물 컷)

블록 순서와 제목은 고정한다. 쓸 게 없는 블록도 제목은 두고 비워 둔다. `PRE_SHOT_CONTINUITY`는 필요할 때만 맨 앞에.

| # | 블록 | 쓰는 것 | 자주 틀리는 것 |
|---|---|---|---|
| — | `PRE_SHOT_CONTINUITY` | 앞 숏에서 이어받는 상태만(위치·자세·소품 소유·문 상태·빛). 이어받지 않는 것도 적는다(이전 프레이밍·렌즈) | AI가 관찰한 상태를 확인 없이 계승 |
| 1 | `SCENE_CONTEXT` | 시대·장소·상황, 이 클립에서 일어나는 일 2~4문장 | 카메라·연기를 여기 몰아넣기 |
| 2 | `ACTIVE_REFERENCES` | 실제로 붙인 참조마다 한 줄: ID · 역할 · Authority. 인물 줄은 나이·체형·머리·의상·신발 + `100% matches the reference` | 붙이지 않은 태그를 쓰거나, 붙이고 안 씀 |
| 3 | `LOCATION_MAP` | 좌표 문장 + 카메라 위치 + 전·중·후경 + 광원(+이동 경로). 랜드마크는 대문자 이름으로 | "근처에", "그 문"처럼 여럿을 가리키는 말 |
| 4 | `FIRST_FRAME_AND_SPATIAL_BLOCKING` | 0:00에 누가·어디서·무슨 동작 **도중인지**, 소품 위치·소유, 보이는 인원 수. "이 블록은 첫 프레임 범위" | 첫 프레임 조건을 숏 전체로 확대 |
| 5 | `FORMAT_MODE` | 실사/단일 연속 테이크/길이. 컷이 있으면 "지정한 지점에서만 하드컷" | 단일 테이크라 해 놓고 컷 요구 |
| 6 | `OPTICS` | 대각 화각(도) + 관찰 가능한 결과 3개. 심도 | mm·조리개·렌즈 브랜드(영상 모델은 안 듣는다) |
| 7 | `CAMERA` | 위치·높이·방향·고정 여부·움직임(속도까지) | 복합 움직임, "역동적인 카메라" |
| 8 | `ACTION_TIMING` | `0:00–0:03 —` 구간별 행동·대사, 상태 전이, 마지막 프레임 | 설명 안 된 빈 구간, 횟수 잃음(한 번 → 계속) |
| 9 | `CHARACTER_ACTING` | 목표와 행동, 눈의 삶, 감정 허용 범위의 양 끝 = 실패 (`05_acting.md`) | 감정 형용사 |
| 10 | `PHYSICS` | `motion_owner = CHARACTER / PROP / CAMERA / ENVIRONMENT` 별로 무게·마찰·접촉 | 누가 움직이는지 불분명 |
| 11 | `LIGHTING` | 실제 광원 하나를 지배광으로, 방향, "모든 컷에서 같은 조명 논리" | 참조 사진의 룩으로 색온도 단정 |
| 12 | `AUDIO` | 대사 원문(따옴표), 횟수, 목소리, 효과음, "No music". 말하지 않는 인물은 "한마디도 하지 않는다" | 모델이 소리를 지원하지 않는데 길게 씀 |
| 13 | `STYLE` | 매체 질감·색조 한두 줄 | 스타일이 얼굴까지 통제한다고 가정 |
| 14 | `QUALITY` | 해상감·피부/직물 질감·손가락 왜곡 억제 | 스타일과 섞기 |
| 15 | `REQUIRED_AND_FORBIDDEN_CONSTRAINTS` | Required: 지킬 상태·횟수·범위. Forbidden: **실제로 나온 실패**만, 범위 태그(`ENTIRE_SHOT`, `INTERVAL 0:03–0:06`, `FINAL_FRAME`) | 과거 실패를 끝없이 누적 |

### 블록에 그대로 쓰는 문장 (검증된 것)

```text
[좌표] LEFT and RIGHT are SCREEN directions. Places are named by the objects on screen.

[참조 권한] The start image has sole authority over camera, framing, the room, furniture, light,
colour and the 0:00 positions of people and props. The character references have authority only
over faces, hair, bodies and clothes. The [prop] reference has authority only over its material,
shape and state; its size follows the start image. Do not take the background, lighting, pose,
hand, sleeve, trousers, shoes or panel layout from any reference.

[장소 참조] Controls geometry, materials, light and atmosphere ONLY — not framing.

[시작 이미지] The start image is the exact frame at 0:00. The video begins from this image and
continues from it without any cut, jump or reframing.

[첫 프레임] [Person] is already in place at 0:00, mid-[action]. No empty establishing frame.
Exactly [N] people are visible.

[카메라 고정] Fixed on a tripod, eye level, at the same position as in the start image,
completely locked from 0:00 to 0:0N. No pan, no tilt, no zoom, no push-in, no reframing.

[광각 관찰 결과] Diagonal field of view about 63°. The [A], [B] and [C] are fully visible in one
frame / straight lines stay straight / no telephoto compression.

[망원 관찰 결과] Diagonal field of view about 29°. The background is compressed and soft / only
[person] is sharp / the camera is physically far away.

[속도] All movement is slow and even; nothing accelerates suddenly, and each action flows into the
next without a hard start or stop.

[상태 머신] [OBJECT] state: ON_TABLE -> LIFTED -> CARRIED, exactly one transition, never reversed.

[연기 범위] Between [state A] and [state B]. [one extreme] = failed take; [other extreme] = failed take.

[말하지 않음] [Person] does not say a single word; no attempt to speak, no lip movement.

[대사] The dialogue is in [language], exactly once. [PERSON]: "[line]" — [voice description].
No music.

[조명 색] The whole frame does not lean orange or amber and does not sink into darkness.
The lamps are on, but their light does not bloom or spread.
```

### 15블록에서 덜어내는 법

- 장소 정보는 좌표 줄 + 네 줄(카메라 / 전·중·후경 / 빛 / 필요 시 경로)을 넘기지 않는다. 길게 쓸수록 인물 참조가 밀린다.
- 인물·장소 설명문은 **에셋 대장의 고정 문장을 글자 그대로** 쓴다. 같은 인물을 29개 프롬프트에서 같은 문장으로 쓴 작품이 일관성이 높았다.
- 이 샷에 나오지 않는 인물·태그·씬 번호·"앞과 같음"·"계속"은 넣지 않는다(문맥 격리).
- Forbidden은 "원하는 상태"를 Required에 먼저 쓰고, Forbidden에는 실제로 나왔던 실패만 둔다.
- 예외: 같은 컷에서 여러 종류의 실패가 반복됐고 사용자가 "금지할 것을 다 넣으라"고 하면 길게 쓴다. 이때는 범주별로 묶는다(`[Faces and clothing]` `[Colour and image]` `[The bag]` `[Camera and editing]` …). 고등어 C#4는 이렇게 쓴 판이 확정됐다. 길게 쓸수록 사건 수는 더 엄격하게 줄인다.

---

## 3. 4문단 형식 (배경·풍경·그림체 영상, 시작 이미지 사용)

인물 연기가 없고 시작 이미지가 장면을 다 담고 있을 때. 나부코 배경 영상에서 Kling 4.0 가이드에 맞춰 정착한 형식이다.

```text
Camera: [한 가지 움직임과 양 — 예: a slow, steady forward glide, easing about six percent closer
over the whole clip]. The horizon stays level; no rotation, no tilt, no zoom.

Motion: [이미지에 이미 있는 것 중 움직일 것만, 방향과 속도로 — 구름, 연기, 안개, 인물의 작은 일].

Keep the hand-painted [style] look, every [house, lane and cloud] shape, and the light direction
from the [left] exactly as in the image; only the things named above move, slowly and without
morphing or melting.

Silent: no dialogue, no music, no sound effects.
```

규칙
- 이미지에 이미 있는 것을 다시 묘사하지 않는다. 그 뒤에 **일어나는 움직임**만 쓴다.
- 끝 상태, 페이드인, 다음 컷과의 이음새를 쓰지 않는다(필요한 프레임아웃은 그 컷 안의 움직임으로 적는다).
- 움직임의 양은 **화면 비율(%)**로 쓴다. 미터·초 단위 위치는 지키지 못한다(E-23).
- 서두르는 것처럼 보이면 문장을 늘리지 말고 사건을 하나 뺀다.
- 소리를 끌 수 있으면 옵션에서 끄고, 못 끄면 Silent 문장.

---

## 4. 모델별 메모 (관찰한 것)

| 모델 | 메모 |
|---|---|
| Seedance 2.5 | 참조 요소를 `<<<요소ID>>>`로 부르고 붙인 요소와 프롬프트 속 요소를 정확히 맞춘다. 음성 생성 기본 켜짐 → 대사·효과음·"No music"을 AUDIO에. 음성 파일 참조는 붙인 순서대로 audio_1, audio_2. Extend 결과는 원본이 21:9여도 16:9 1280×720이었다. 멀티샷 옵션 대신 컷은 글로 지시 |
| Kling 4.0 | 이미지→영상. 이미지에 있는 것을 다시 쓰지 않고 움직임 + 유지할 것. 3~30초. 소리를 만든다 → 끌 수 있으면 끈다. 카메라는 별도 문단, 끝 상태는 쓰지 않음, 고정 카메라와 궤도 이동을 한 컷에 섞지 않음 |
| 공통 한계 | 정확한 이동 거리, 몇 초에 나타나고 사라지는 타이밍, 작고 어두운 풀의 흔들림, 별 반짝임, 그림에 칠해진 빛줄기의 회전은 거의 안 지켜졌다 → 2회 시도 후 후반 작업(E-23) |

해상도·비용은 `06_qa-and-cost.md`.

---

## 5. 실패 → 수정 패턴 (실제로 효과를 본 것)

| 증상 | 수정 |
|---|---|
| 빈 방으로 시작해 인물이 걸어 들어옴 | 첫 프레임에 이미 정위치·동작 도중. 문을 열고 들어오는 등장은 "이미 걷는 중, 문은 뒤에서 닫히는 중"으로 |
| 문이 저절로 열리고 닫히는 사건이 어색함 | 그 환경 사건을 빼고 문은 숏 내내 닫힌 상태로(고등어 C#2: 이 수정판이 확정) |
| 인물이 휙 돈다 | 부위 순서와 초: "eyes → head → shoulders, about 1.5 s; snapping = failed take" |
| 말하지 않을 인물의 입이 움직임 | "말하려다 만다"를 빼고 "말하려는 시도 자체가 없다 — 입술 벌림·입 모양 없음" |
| 고개를 돌렸다가 되돌림 | "From then until the end his eyes and head stay on her. Turning back toward X = forbidden" |
| 다른 인물이 반응해 버림 | 반응하지 않을 인물의 시선·머리·손을 끝까지 고정: "does not react in any way, never looks at him" |
| 소품이 다른 손으로 감, 커짐, 다른 탁자로 감 | 소품 요소를 붙이고 "[물건 기준 손]·내려놓지 않음·크기는 시작 이미지와 같음". 장소에 같은 종류 물건이 둘이면 이름으로 구분(E-17·E-18) |
| 참조 사진의 얼굴·색·조명이 섞임 | 그 사진을 참조로 붙이지 않는다. 구도는 그 구도로 만든 빈 장소 이미지로 잡는다(E-16) |
| 카메라 기준 좌우로 쓴 문 방향이 틀림 | 옆 물건 기준("화장대에 가까운 가장자리")으로 + 카메라마다 그 물건이 화면 어느 쪽인지 |
| 거울·유리에 엉뚱한 것이 비침 | 비치는 것과 비치지 않는 것을 함께 적는다 |
| 해가 납작한 원반으로 떠오름 | 모양이 아니라 윤곽 없이 번지는 빛. 원반·공·테두리 금지, 아랫부분은 지평선 안개에 |
| 새 떼가 점으로 뭉개짐 | "카메라와 같은 속도로 같은 크기와 위치를 유지". 멀어지며 작아진다고 쓰지 않는다. 그래도 안 되면 오버레이 소재로 따로 |
| 카메라가 지정한 지점이 아니라 화면 가운데로 직진 | 목적지 좌표 대신 "피사체를 따라가는 추적 촬영"으로 바꾸기, 확대량을 줄여 쓰기(2배 요청 → 3.5배 나옴) |
| 연기가 크거나 무표정 | 감정 허용 범위의 양 끝을 failed take로 |
| 배경 인물이 얼어붙거나 한꺼번에 움직임 | 인원 수를 적고 각자 다른 일 하나, 이름 없는 인원은 얼굴 없는 실루엣 |
| 같은 프롬프트를 4번 돌려도 안 됨 | 개념 단순화(요소 제거, 효과를 다른 방식으로) 또는 샷 분리 |

---

## 6. 보내기 전 점검

- [ ] 사건 수가 3개 이하인가. 15초를 넘지 않는가
- [ ] 첫 프레임 문단이 시작 이미지(0:00)와 같은가
- [ ] 좌표 문장이 있고, 본문의 좌우가 화면 속 물건으로 적혔는가
- [ ] 붙인 참조와 프롬프트 속 참조가 정확히 일치하고, 각각 Authority가 적혔는가
- [ ] 장소 참조에 FRAMING 권한을 주지 않았는가
- [ ] 카메라 동작이 하나인가. 렌즈는 화각(도) + 관찰 결과 3개인가
- [ ] 횟수(한 번/정확히 두 번/계속)와 범위(첫 프레임/구간/전체/마지막)가 바뀌지 않았는가
- [ ] 인물·장소 설명문이 에셋 대장 문장과 글자까지 같은가
- [ ] 이 샷에 없는 인물·옛 문장·"앞과 같음"이 남아 있지 않은가
- [ ] 위험 목록의 위험마다 막는 문장이 한 줄씩 있는가
- [ ] 해상도·길이가 "확인용"(저해상도·짧게)인가 — 확정 뒤에만 고해상도
