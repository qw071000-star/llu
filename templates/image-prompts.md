# 이미지 프롬프트 빈 틀

규칙은 `guide/04_image-prompt.md`. 블록 밖에 한국어로: 모드(신규 / LOCKED EDIT / DERIVED VIEW / 새 공간) · 참조(요소 ID와 역할, 첨부 순서) · 모델 · 해상도 · 부모 job.

---

## 1. 인물 시트 — 신규 (인물당 한 번)

```text
Create a photorealistic single wide horizontal three-panel character reference sheet of the same
[woman/man]. The image is divided into three clean vertical sections with no borders, captions or text.

CHARACTER IDENTITY:
[age, origin, skin tone and texture, face shape with mature bone structure, eyes, brows, nose, mouth,
neutral expression]. The same exact identity must be maintained wherever the face is visible.

PANEL LAYOUT:
- LEFT PANEL: a front-facing full-body wardrobe view shown strictly from the neck down. The panel is
  intentionally HEADLESS and ends cleanly at the base of the neck. This is an editorial clothing crop,
  not an injury: no head, no face, no wound, no gore, no dark opening. The plain background continues
  cleanly above the neckline. Both hands visible and empty, feet fully visible.
- CENTER PANEL: a full-body rear view of the same person from head to toe, same neutral pose.
- RIGHT PANEL: a large front-facing close-up portrait from the upper chest upward, calm neutral
  expression, the gaze with a definite focal distance just behind the lens.

BODY AND PROPORTIONS: [build, shoulders, life written on the body].
OUTFIT — IDENTICAL IN ALL THREE PANELS: [outer → closure → collar/pockets → inner/neckline → bottoms
→ shoes → allowed accessories]. One physically identical outfit seen from different views. No logos,
no prints, no unintended accessories. No profession-signaling props unless explicitly requested.
HAIR — CENTER AND RIGHT PANELS: [length, texture, parting, rear view, colour, finish].
REALISM: visible fine skin texture with natural pores, age spots, fine lines, subtle asymmetries and
uneven skin tone, no digital smoothing, no beauty filter, matte natural complexion. Eyes have genuine
moisture and a small specular catchlight, one eyelid very slightly lower than the other, real iris texture.
BACKGROUND AND LIGHTING: one continuous plain [colour/texture] backdrop across all panels, [light
direction and quality]. All panels share the same lighting direction, exposure, palette and finish.
CONSISTENCY RULES: one person only. Do not create three similar models. Preserve the exact left-to-right
order: headless front outfit view / full-body rear view / front close-up portrait.
no text, no watermark, no logos, no frame borders, no other people, no duplicate figures, no extra panels,
no props, no babyface, no beauty filter, no plastic skin, no extra fingers
```

## 2. 인물 시트 — 수정 (한 번에 한 가지)

```text
Edit reference image 1: change only the character's [outfit / hair], while keeping the character's
identity exactly and preserving the sheet's existing three-panel structure exactly, including the
intentionally HEADLESS left panel.

CHANGE — [OUTFIT / HAIR]:
[In all three panels / Only in the center and right panels], [new state, head to foot].
[Nothing that dates the decade — only when moving eras.]

REMOVE COMPLETELY:
[Old items by name] are GONE in every panel. Do not layer, merge or hybridize old and new clothing.
At the neckline, only [new collar] is visible at the base of the neck, including in the headless LEFT panel.

PRESERVE EXACTLY:
- LEFT PANEL: keep it intentionally HEADLESS … Do not add, infer, reconstruct or complete a head or face.
  Its clothes change fully: [new list], no [old 1], no [old 2]
- IDENTITY: preserve the exact same face … do not regenerate, reinterpret, beautify, age or reshape the face.
- STRUCTURE: preserve all three poses, body proportions, crop boundaries, panel widths, panel order, empty hands.
- ENVIRONMENT: preserve the backdrop, lighting direction, exposure, shadows, palette, contrast, grain and falloff.

ONLY CHANGE: [same as CHANGE]. The face and identity 100% identical to reference image 1.
```

## 3. 장소 마스터 (빈 공간, 새로)

```text
[Using <<<A>>> as the same building's material register — … — generate a NEW / Generate] [SPACE].
CAMERA: [shot size], camera at [height and position], looking [direction] — [the room read at an
angle, not square-on / for a long axis: the vanishing point at …].
THE DOMINANT ELEMENT: [the one thing seen first, ideally the light source].
SPATIAL GEOGRAPHY (directions as seen from [camera position]; LEFT and RIGHT are SCREEN directions):
At the FAR END, [ ]. The RIGHT wall [ ]. At the LEFT, [ ]. [Floor, ceiling, openings.]
Nothing else: no [ ].
Empty deserted [space], still air.
Palette of roughly 80% [ ] — 15% [ ] — 5% [ ].
Real material truth: [ ]. Real aged surfaces: [wear with location].
[Light logic, one sentence.] [Practicals lit but do not glow.]
[Image finish: camera body, lens mm, film stock.] [Era lock.] No legible text anywhere.
```

## 4. LOCKED EDIT (같은 사진, 한 가지)

```text
Edit <<<image_1>>> WITHOUT reframing: camera position, camera height, angle, lens, framing, horizon
line and perspective are LOCKED — zero reframing, zero recentering, zero zoom — this is the same
photograph with one change only.
CHANGE — [TARGET AND LOCATION]: [ROTATE / STATE / ADD / REMOVE formula].
PRESERVE EXACTLY: [camera · architecture · every unnamed object · light · grade]
ONLY CHANGE: [same]. Everything else remains 100% identical.
```

## 5. DERIVED VIEW (같은 장소, 새 시점)

```text
Using <<<image_1>>> as the exact same [location] — same [materials, landmarks and light logic] —
generate a NEW [reverse view / close-up / top view / oblique view].
Do not inherit its camera angle, framing or composition.
CAMERA: [relation to the reference camera]. At [height], looking [direction]. [Negative range.]
FRAMING: [subject] fills [amount]. Keep [1–3 landmarks]. [Excluded objects] fall outside the frame.
CONTINUITY: preserve the exact design, materials, wear, state and placement relationships.
This is a newly observed direction of the same physical room, not a horizontal mirror of the reference.
[Parent's MASTER GEOMETRY · LIGHT · palette · era lock · finish — verbatim]
```

## 6. 소품 독립 에셋

```text
Photorealistic product-reference photograph of [prop: material, wear, size cue], isolated on a plain
seamless light grey studio background, nothing else in frame — no scene, no room, no other objects,
no hands, no people. [Use marks.] Soft even studio lighting from the front-top, minimal shadow.
Sharp focus throughout. Avoid: [wrong materials], brand logos, text, watermarks.
```

## 7. 퍼스트 프레임 (장소 + 인물 + 소품, 영상 0:00)

```text
FIRST FRAME of a film shot — the exact state at 0:00 of the video. LEFT and RIGHT are SCREEN directions.
Using <<<LOC>>> as the exact same location, generate a new view. [CAMERA: position by objects, height,
direction, distance, shot size + camera body/lens/film stock.]
REFERENCE AUTHORITY:
- <<<LOC>>>: geography, materials, landmarks, light direction
- <<<CHAR>>>: face, hair, wardrobe only — Same face, same bone structure, same hair, same wardrobe.
  Change only the pose, framing, location and lighting.
- <<<PROP>>>: shape, material and state only; size as described below
DO NOT TRANSFER: the character sheet's backdrop, studio lighting, pose or framing.
PRIORITY: the CAMERA block overrides every reference.
BLOCKING: [each person at an existing anchor, by distance and contact, mid-action].
WARDROBE: [asset registry sentence, verbatim].
[Nothing else / palette / material truth / light logic / era lock]
```

## 8. 그림체 장면 (수채 등, 참조 다섯 장)

```text
A [very loose, grainy wet-on-wet watercolor] painting on [rough cold-press paper], ultra-wide [21:9],
of the following scene.
Reference images: the first is [base cut] and sets the painting style above all ([technique]); the
second, third and fourth are further style paintings of the same kind. Take only technique, brushwork
and paper texture from these four, never their subjects, colors or composition. The fifth is [colour
cut]: take only its colors, light and mood, never its landscape and never its direction of light.
Scene: [viewpoint and angle; zones by thirds; people few and well apart].
Light: [time, sun side, shadow direction, colour range — never orange, deep or black].
Style: [surface handling — large smooth washes for walls, tiny dabs for sky]; soft lost edges, no outlines.
Look of the place: [period-accurate objects and materials; same city, same houses, same clothing as other cuts].
Composition: [crop band; occlusion zone holds only minor details; calm edges if it will be extended].
Not a photograph, 3D render, game art or detailed digital illustration; no pen outlines, vignette, text,
border, [period-wrong items].
```
