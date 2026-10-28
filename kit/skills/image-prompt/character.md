# 인물 + 의상 시트

## 필요한 정보

| 필요한 정보 | 틀의 자리 |
|---|---|
| 나이, 출신, 피부, 얼굴 구조(눈·눈썹·코·입) | `CHARACTER IDENTITY` |
| 체형, 어깨, 자세 | `BODY AND PROPORTIONS` |
| 의상: 겉옷 → 여밈 → 깃·주머니 → 안옷 → 하의 → 신발, 허용 액세서리 | `OUTFIT` |
| 헤어: 길이, 질감, 가르마, 뒷모습, 색, 마감 | `HAIR` |
| 배경 색·질감, 조명 방향과 질 | `BACKGROUND AND LIGHTING` |
| 시트 규격(작품 공통, 바꾸지 않음) | `PANEL LAYOUT` |
| 수정이면: 기준 시트 job, 바꿀 것 하나(의상 또는 헤어), 없앨 옛 항목 | 틀 2 `CHANGE`, `REMOVE COMPLETELY` |
| 대사가 있는 인물이면: 연기 프로필, 목소리 문장 | 에셋 대장 (`acting` §6·§7) |

## 규칙

**규격 (작품 안에서 바꾸지 않는다):** 16:9 한 장을 세로로 3분할한다. 세 패널은 같은 배경, 같은 조명이다.
- 왼쪽: 목 아래 정면 전신
- 가운데: 후면 전신
- 오른쪽: 가슴 위 정면 클로즈업

**신규 작성 순서:** 결과물 → 정체성 → 패널 → 체형 → 의상(겉옷부터 신발, 허용·금지 소품) → 헤어 → 배경·조명 → 일관성 잠금 → 금지.

**자주 나는 사고와 막는 법**
- 머리 없는 패널이 상처처럼 보이거나 머리가 생긴다 → `intentionally HEADLESS … not an injury`
- `mannequin`만 쓰면 플라스틱 마네킹이 나온다 → `hollow ghost-mannequin, invisible person, empty collar`
- 직업을 나타내는 소품이 저절로 생긴다 → `No profession-signaling props unless explicitly requested`

**수정할 때**
- 한 번에 의상이나 헤어 하나만 바꾼다.
- 얼굴은 다시 묘사하지 않고 보존만 지시한다.

**파생과 요소**
- 파생은 확정본에서만 갈라낸다. 파생의 파생은 만들지 않는다.
- 영상 요소는 의상·헤어 상태마다 따로 만든다(`char_<인물>_<상태>_v1`).

**기록:** 확정되면 에셋 대장에 IDENTITY·WARDROBE 고정 문장, job ID, 실제 처리 모델, 한계를 적는다. 이후 모든 프롬프트는 그 문장을 글자 그대로 쓴다. 프롬프트와 설정은 OK 대장의 에셋 ID 카드에 둔다.

## 틀 1 — 신규

```text
Create a photorealistic single wide horizontal three-panel character reference sheet of the same
[woman/man]. The image is divided into three clean vertical sections with no borders, captions or text.

CHARACTER IDENTITY:
[age, origin, skin tone and texture, face shape and bone structure, eyes, brows, nose, mouth,
neutral expression]. The same exact identity must be maintained wherever the face is visible.

PANEL LAYOUT:
- LEFT PANEL: a front-facing full-body wardrobe view shown strictly from the neck down. The panel is
  intentionally HEADLESS and ends cleanly at the base of the neck. This is an editorial clothing crop,
  not an injury: no head, no face, no wound, no gore, no dark opening. The plain background continues
  cleanly above the neckline. Both hands visible and empty, feet fully visible.
- CENTER PANEL: a full-body rear view of the same person from head to toe, same neutral pose.
- RIGHT PANEL: a large front-facing close-up portrait from the upper chest upward, calm neutral
  expression, the gaze with a definite focal distance just behind the lens.

BODY AND PROPORTIONS: [build, shoulders, posture].
OUTFIT — IDENTICAL IN ALL THREE PANELS: [outer → closure → collar/pockets → inner/neckline → bottoms
→ shoes → allowed accessories]. One physically identical outfit seen from different views. No logos,
no prints, no unintended accessories. No profession-signaling props unless explicitly requested.
HAIR — CENTER AND RIGHT PANELS: [length, texture, parting, rear view, colour, finish].
REALISM: visible fine skin texture with natural pores, fine lines, subtle asymmetries and uneven skin
tone, no digital smoothing, no beauty filter, matte natural complexion. Eyes have genuine moisture and
a small specular catchlight, one eyelid very slightly lower than the other, real iris texture.
BACKGROUND AND LIGHTING: one continuous plain [colour/texture] backdrop across all panels, [light
direction and quality]. All panels share the same lighting direction, exposure, palette and finish.
CONSISTENCY RULES: one person only. Do not create three similar models. Preserve the exact left-to-right
order: headless front outfit view / full-body rear view / front close-up portrait.
no text, no watermark, no logos, no frame borders, no other people, no duplicate figures, no extra panels,
no props, no beauty filter, no plastic skin, no extra fingers
```

## 틀 2 — 수정 (의상 또는 헤어 하나)

```text
Edit reference image 1: change only the character's [outfit / hair], while keeping the character's
identity exactly and preserving the sheet's existing three-panel structure exactly, including the
intentionally HEADLESS left panel.

CHANGE — [OUTFIT / HAIR]:
[In all three panels / Only in the center and right panels], [new state, head to foot].

REMOVE COMPLETELY:
[Old items by name] are GONE in every panel. Do not layer, merge or hybridize old and new clothing.

PRESERVE EXACTLY:
- LEFT PANEL: keep it intentionally HEADLESS, an editorial clothing crop, not an injury: no head, no face, no wound. Do not add, infer, reconstruct or complete a head or face.
- IDENTITY: preserve the exact same face; do not regenerate, reinterpret, beautify, age or reshape the face.
- STRUCTURE: preserve all three poses, body proportions, crop boundaries, panel widths, panel order, empty hands.
- ENVIRONMENT: preserve the backdrop, lighting direction, exposure, shadows, palette, contrast and grain.

ONLY CHANGE: [same as CHANGE]. The face and identity 100% identical to reference image 1.
```
