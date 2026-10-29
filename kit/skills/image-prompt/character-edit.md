# 인물 + 의상 시트 — 확정된 시트 고치기

기준은 OK 대장의 그 인물 시트 카드(job)다. 새로 만들지 않는다. 고치기에는 이 파일만 연다(`character.md`는 새 시트용이다). 틀에 필요한 문장은 이미 들어 있다.

## 필요한 정보

| 필요한 정보 | 틀의 자리 |
|---|---|
| 기준 시트 job, 바꿀 것(의상 = `Outfit` 줄 / 헤어), 새 상태(머리→발, 신발까지) | 틀 1 `CHANGE` |
| 없앨 옛 항목(신발·작은 소품까지 이름으로), 새 목둘레 | 틀 1 `REMOVE COMPLETELY` |
| 시대를 옮기는 수정인가 | 틀 1 `Era move` 줄 |
| 사용자가 의상·헤어 참조 이미지를 가리켰는가("이걸로"인데 이미지가 없으면 묻는다) | 틀 1 권한 줄 |
| 나이를 바꾸는가("50대처럼"): 목표 나이, 나이 표지(주름·피부·헤어 색·자세·손) | 틀 2 `CHANGE — AGE`, `IDENTITY BONES` |
| 머리 없는 패널 변형 A / B(기준 시트와 같게) | 틀 1 LEFT PANEL 줄(A / B) |

## 규칙

**수정할 때**
- 한 번에 의상이나 헤어 하나만 바꾼다. 예외는 시대 이동처럼 떼면 성립하지 않는 두 변경이다(헤어가 의상보다 시대를 강하게 드러낸다). 예외로 묶었으면 이유를 한 줄 적는다.
- 얼굴은 다시 묘사하지 않고 보존만 지시한다. 얼굴 문장이 참조 이미지와 경쟁하면 얼굴이 새로 생성된다.
- 의상 범위는 `In all three panels`, 헤어 범위는 `Only in the center and right panels`. 헤어에 세 패널을 쓰면 왼쪽에 머리가 생긴다.
- **목둘레를 세 곳에 쓴다:** REMOVE의 `At the neckline …`, PRESERVE LEFT 줄, ONLY CHANGE의 `including the neckline of the headless panel`. 수정에서 가장 자주 실패하는 곳이다.
- **목록을 맞춘다:** CHANGE의 새 의상 목록 = PRESERVE LEFT 줄의 `Its clothes change fully:` 뒤 목록, REMOVE의 GONE 목록(옛 항목마다 이름으로, 신발·작은 장신구까지) = 그 줄 끝의 `no [old 1], no [old 2], no [old 3]`(같은 항목, 같은 수). 어긋나면 옛 옷이 반쯤 그려진다.
- 시대를 옮기면 CHANGE에 `nothing that dates the decade`를 붙이고 그 시대를 만드는 요소(머리 기름, 넓은 넥타이, 로고, 스니커즈 등)를 이름으로 지운다.
- 새 의상은 재단 네 가지(길이·여밈·칼라·주머니)를 쓰고, 직업을 드러내는 소품이 붙지 않게 `No profession-signaling props.`를 넣는다.
- 의상·헤어 참조 이미지를 붙이면 틀 1의 권한 줄 세 개를 넣는다. `Do not transfer the face …` 줄은 예외 없이 넣는다.
- 나이를 바꾸면 틀 2를 쓴다. `IDENTITY BONES` 줄은 틀 그대로 쓰고 얼굴 특징(코·눈 모양 등)을 새로 지어 넣지 않는다.
- 결과에서 오른쪽 얼굴이 딴 사람이 되면: 얼굴 묘사를 지우고 `Change the hair around the existing face; do not regenerate, reinterpret, beautify, age or reshape the face.`
- 확정되면 에셋 대장의 그 인물에 새 상태 줄(WARDROBE 고정 문장, job)을 더한다. 옛 상태는 지우지 않는다.

## 틀 1 — 의상 또는 헤어 하나

```text
Edit reference image 1: change only the character's [outfit / hair], while keeping the character's
identity exactly and preserving the sheet's existing three-panel structure exactly, including the
intentionally HEADLESS left panel.

CHANGE — [OUTFIT / HAIR]:
[In all three panels, replace the current outfit with / Only in the center and right panels, change the
hair to] [new state, head to foot, including shoes]. [Outfit: The new outfit is one physically identical
outfit seen from different views, with matching fabric, color, length, fit and layering. No [things not
worn], no logos, no prints.] [Era move: nothing that dates the decade.]

REMOVE COMPLETELY:
[old 1], [old 2], [old 3] are GONE in every panel. Do not layer, merge or
hybridize old and new clothing. [Outfit: At the neckline, only [the new collar] is visible at the base of
the neck. No trace of [old 1], [old 2], [old 3] remains, including in the headless LEFT panel.]

[Clothing or hair reference attached:
Reference image 1 controls identity, face, body proportions, poses, panel layout, framing, background,
lighting and photographic finish. Reference image 2 controls only the design, cut, length, material and
details of [the new item]. Do not transfer the face, body, pose, background or lighting from reference image 2.]

PRESERVE EXACTLY:
- LEFT PANEL: keep it intentionally HEADLESS, front-facing and framed from the neck down, an editorial
  clothing crop, not an injury. Do not add, infer, reconstruct or complete a head or face in that panel.
  Keep the clean neck crop and the uninterrupted plain background above it. [Outfit: Its clothes change
  fully: [new outfit summary], no [old 1], no [old 2], no [old 3].]
- [B ghost-mannequin sheet: instead of the LEFT PANEL line above] LEFT PANEL: a front-facing full-body wardrobe view: the outfit holds its own shape as if worn by an invisible person, hollow ghost-mannequin product photography, no mannequin material visible anywhere, the collar opening is empty and shows the dark hollow inside the garment, cut off cleanly just above the shoulder line with NO head, NO neck and no shoulder stump protruding, no plastic torso, no stand, no pole, no base, real human hands emerge from the ends of both sleeves hanging relaxed slightly away from the sides, the shoes stay on the floor at the bottom of the trousers.
  [Outfit: Its clothes change fully: [new outfit summary], no [old 1], no [old 2], no [old 3].]
- IDENTITY: preserve the exact same face — identical facial features, bone structure, skin, age, eye
  shape, nose, lips and expression. Do not regenerate, reinterpret, beautify, age or reshape the face.
- STRUCTURE: preserve all three poses, body proportions, crop boundaries, panel widths, panel order and
  empty hands.
- ENVIRONMENT: preserve the existing background, lighting direction, exposure, shadows, palette, contrast,
  grain and falloff.

ONLY CHANGE: [the outfit in all three panels including the neckline of the headless panel / the hair in
the center and right panels]. The face and identity 100% identical to reference image 1.
no head on the left panel, no mannequin, no other people, no duplicate figures, no props, no text,
no watermark, no logos, no frame borders
```

## 틀 2 — 나이만 바꾸기 (같은 사람, 다른 나이)

"20대인데 50대처럼 보이게" 같은 요청이다. 얼굴을 새로 묘사하지 않는다. 뼈대는 남기고 나이 표지만 바꾼다. 나이 표지(주름·피부·헤어 색·자세)는 떼면 성립하지 않으니 한 변경으로 친다. 의상은 그대로 둔다. 결과는 새 상태 요소(`char_<인물>_<나이>_v1`)로 따로 둔다.

```text
Edit reference image 1: age the same person to [target age], while keeping the character's identity
and preserving the sheet's existing three-panel structure exactly, including the intentionally HEADLESS
left panel.

CHANGE — AGE:
In the center and right panels, the same person is now [target age]: [age markers — forehead lines and
crow's feet, softened jawline, slight sagging under the eyes, thinner lips, greying at the temples,
skin texture of that age]. In the left and center panels, the posture settles slightly with age:
[shoulders, stance]. Hands in every panel show the same age: [knuckles, veins, skin].

PRESERVE EXACTLY:
- IDENTITY BONES: the same face shape, bone structure, eye shape and colour, nose shape, mouth shape and
  ear shape. The person must be recognisable as the same person at a different age. Do not replace
  the face with a different person.
- LEFT PANEL: keep it intentionally HEADLESS, an editorial clothing crop, not an injury. Do not add,
  infer, reconstruct or complete a head or face in that panel.
- OUTFIT: the exact same clothes in every panel.
- STRUCTURE and ENVIRONMENT: panel widths, panel order, crop boundaries, empty hands, backdrop,
  lighting direction, exposure, palette, contrast, grain and falloff.

[늙게]
ONLY CHANGE: the visible age of the same person. no babyface, no exaggerated old-age makeup, no other people, no text, no watermark, no frame borders
[젊게]
ONLY CHANGE: the visible age of the same person. no babyface, no beauty filter, no other people, no text, no watermark, no frame borders
```

**젊게 할 때** `[age markers]`를 반대로 쓴다: 주름 얕게, 머리색(흰머리를 줄이거나 없앰), 곧은 어깨, 탄탄한 손. 끝 줄은 `[젊게]` 줄 하나만 쓴다(늙게면 `[늙게]` 줄). **어린이 나이**(10세 → 12세)는 키·어깨·팔다리 비율·얼굴 길이·자세로 쓰고 피부는 그대로 둔다.
