# 인물 + 의상 시트 — 신규

이미 확정된 시트를 고치는 일(의상·헤어·나이)은 `character-edit.md`를 연다. 이 파일은 열지 않아도 된다.

## 필요한 정보

| 필요한 정보 | 틀의 자리 |
|---|---|
| 나이, 출신, 피부, 얼굴 구조(얼굴형·턱·광대·코·입, 성인은 성숙한 골격), 눈(형태·색) | `CHARACTER IDENTITY` |
| 체형(삶이 몸에 남긴 것), 어깨, 자세 | `BODY AND PROPORTIONS` |
| 의상: 겉옷 → 여밈 → 깃·주머니 → 안옷·목선 → 하의 → 신발, 허용 액세서리, 없는 것(`no bag`) | `OUTFIT` |
| 헤어: 길이, 질감, 가르마, 얼굴 주변 형태, 뒷모습, 색, 마감 | `HAIR` |
| 머리 없는 패널 변형: A 머리 없는 인체 / B 고스트 마네킹 (작품 공통, 첫 시트에서 정함) | `PANEL LAYOUT`의 왼쪽 줄 |
| 배경 색·질감, 조명 방향과 질 (작품 공통. 첫 확정 시트의 줄을 그대로 쓴다) | `BACKGROUND AND LIGHTING` |
| 시대물인가 | 금지 줄 |
| 대사가 있는 인물이면: 연기 프로필, 목소리 문장 | 에셋 대장 (`acting` §7·§8) |

## 규칙

**규격 (작품 안에서 바꾸지 않는다):** 16:9 한 장을 세로로 3분할한다. 세 패널은 같은 배경, 같은 조명이다. 시트는 컷마다 참조로 물리는 원본이라 처음부터 확정 해상도(2k)로 만든다. 1k로 확인하고 2k로 다시 뽑으면 다른 사람이 된다. 모델은 작품 기본값을 쓰고 실제 처리 모델을 기록한다.
- 왼쪽: 목 아래 정면 전신. 손과 신발을 남긴다(소매·기장을 보려고)
- 가운데: 후면 전신
- 오른쪽: 가슴 위 정면 클로즈업. 컷 생성 때 얼굴 참조로 쓰는 패널

**신규는 틀 1 전문으로 쓴다.** OK 대장에 있는 다른 시트의 프롬프트를 예로 베끼지 않는다(더 짧거나 옛 판일 수 있다).

**신규 작성 순서:** 결과물 → 정체성 → 패널 → 체형 → 의상 → 헤어 → 리얼리즘 → 배경·조명 → 일관성 잠금 → 금지.

**정체성:** 실존 배우·유명인을 닮게 만들지 않는다. 참조 이미지는 얼굴의 출처가 아니다. `beautiful`, `elegant` 같은 주관어보다 얼굴 구조의 객관적 특징을 먼저 쓴다.

**머리 없는 패널 변형 — 작품 안에서 하나로 통일한다**
- A 머리 없는 인체: 착용감·실루엣 검토용. 위험은 상해 이미지. `not an injury` 문장이 반드시 들어간다(틀 1).
- B 고스트 마네킹: 의상 재단 확정용. 위험은 플라스틱 마네킹. `mannequin`만 쓰지 않는다. 틀 1의 왼쪽 줄을 다음으로 바꾼다:
  `LEFT PANEL: a front-facing full-body wardrobe view: the outfit holds its own shape as if worn by an invisible person, hollow ghost-mannequin product photography, no mannequin material visible anywhere, the collar opening is empty and shows the dark hollow inside the garment, cut off cleanly just above the shoulder line with NO head, NO neck and no shoulder stump protruding, no plastic torso, no stand, no pole, no base, real human hands emerge from the ends of both sleeves hanging relaxed slightly away from the sides, the shoes stay on the floor at the bottom of the trousers.`

**자주 나는 사고와 덧붙일 문장**

| 증상 | 문장 |
|---|---|
| 왼쪽 목 위에 머리가 생김 | 여는 문장에 `including the intentionally HEADLESS left panel` + `Do not add, infer, reconstruct or complete a head or face in that panel` |
| 플라스틱 마네킹 | `hollow ghost-mannequin, invisible person, empty collar, no dress form, no stand` |
| 직업 소품이 저절로 생김 | `No profession-signaling props unless explicitly requested: no stethoscope, instruments, clipboard, pen, bag or visible logo.` |
| 옷이 바닥에서 뜸 | `the garment stands on the floor with a natural contact shadow, not floating, not tilted` |
| 나이가 어려 보임 | `mature adult bone structure, defined nasolabial folds, no babyface` |
| 헤어가 시대를 못 벗음 | `matte and modern, no pomade shine, no sculpted vintage wave` (현재로 옮길 때) |
| 배지·명찰 글자 깨짐 | `a plain blank badge, no writing, no photo, no logo` |
| 톤·그레인이 달라짐 | "같은 룩" 대신 `palette, contrast, grain, falloff` 네 단어 |

**파생과 요소**
- 파생은 확정본에서만 갈라낸다. 파생의 파생은 만들지 않는다. 확정본은 지우지 않는다.
- 영상 요소는 의상·헤어 상태마다 따로 만든다(`char_<인물>_<상태>_v1`). 한 영상 안에서 상태가 바뀌면 두 요소를 함께 붙이고 시간 구간으로 나눈다.

**기록:** 확정되면 에셋 대장에 IDENTITY·WARDROBE 고정 문장, job ID, 실제 처리 모델, 변형(A/B), 한계를 적는다. 컷 프롬프트에는 WARDROBE 문장만 글자 그대로 넣는다. 얼굴은 참조가 맡는다. 프롬프트와 설정은 OK 대장의 에셋 ID 카드에 둔다.

## 틀 1 — 신규

```text
Create a photorealistic single wide horizontal three-panel character reference sheet of the same
[woman/man]. The image is divided into three clean vertical sections with no borders, captions or text.

CHARACTER IDENTITY:
[age, origin, skin tone and texture, face shape and bone structure (adults: mature adult bone structure,
defined nasolabial folds), eye shape and colour, brows, nose, mouth, neutral expression]. The eyes have
naturally muted catchlights and no oversized specular glare in the iris. The same exact identity must be
maintained wherever the face is visible.

PANEL LAYOUT:
- LEFT PANEL: a front-facing full-body wardrobe view shown strictly from the neck down. The panel is
  intentionally HEADLESS and ends cleanly at the base of the neck. This is an editorial clothing crop,
  not an injury: no head, no face, no wound, no gore, no dark opening. The plain background continues
  cleanly above the neckline. The figure stands straight, both arms relaxed slightly away from the sides,
  both hands visible and empty, feet fully visible.
- CENTER PANEL: a full-body rear view of the same person from head to toe, standing straight in the same
  neutral pose. The back of the hair, clothing and shoes are clearly visible. Hands empty.
- RIGHT PANEL: a large front-facing close-up portrait of the same person, framed from the upper chest
  upward, with the same calm neutral expression, the gaze with a definite focal distance just behind the
  lens. The face is centered and unobstructed.

BODY AND PROPORTIONS: [build, shoulders, posture]. Keep exactly the same body proportions in the left and
center panels.
OUTFIT — IDENTICAL IN ALL THREE PANELS: [outer → closure → collar/pockets → inner/neckline → bottoms
→ shoes → allowed accessories]. The neckline and every visible clothing layer must match between panels.
The garment is one physically identical outfit seen from different views, with matching fabric, color,
length, fit, construction and layering. No logos, no prints, no visible brands, no unintended accessories.
No profession-signaling props unless explicitly requested.
HAIR — CENTER AND RIGHT PANELS: [length, texture, parting, shape around the face, rear view, colour,
finish]. The haircut and color must match perfectly between the rear view and the portrait.
REALISM: visible fine skin texture with natural pores, age spots, fine lines, subtle asymmetries and
uneven skin tone, no digital smoothing, no beauty filter, no AI-airbrushed look, skin completely free of
artificial glare shine or highlight blooms, matte natural complexion[; older: lined forehead and crow's
feet at the outer eyes, reddened knuckles and short unpainted nails]. Eyes have genuine moisture and a
small specular catchlight, one eyelid sits very slightly lower than the other, faint capillaries at the
inner corner, natural tear-line, the iris shows real fibrous texture and a soft pupil edge.
BACKGROUND AND LIGHTING: one continuous plain [colour/texture] studio backdrop across all panels, [light
direction and quality], gentle realistic shadows. All panels share the same lighting direction, exposure,
palette and photographic finish.
CONSISTENCY RULES: The three panels must depict one and the same person: identical face, age, skin tone,
body proportions, hair color, outfit materials and color. Do not create three similar models. Preserve the
exact left-to-right order: headless front outfit view / full-body rear view / front close-up portrait.
no text, no watermark, no logos, no frame borders, no captions, no labels, no other people, no duplicate
figures, no extra panels, no props, no furniture, no background objects, no collage decorations,
[adults: no babyface, no overly youthful rounded proportions,] no beauty filter, no airbrushing, no plastic
skin, no glossy skin, no distorted anatomy, no extra fingers, centre panel standing full-body head-to-toe
not cropped not sitting, right panel a tight close-up not a full body[, period: no modern clothing, no
modern eyewear, no smartphones, no modern signage]
```

