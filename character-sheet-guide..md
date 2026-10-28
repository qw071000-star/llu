# 인물 시트 프롬프트 가이드
 
**3패널 캐릭터 레퍼런스 시트 / Higgsfield · Nano Banana Pro 기준 · 2026.09**
 
> 씬 번호는 데이터 기준 1~10이다.
> 모델은 `nano_banana_pro`로 요청해도 서버가 `nano_banana_2`로 처리한 전례가 있다(장소 V3). 확정 전에 **실제 처리 모델**을 확인해 기록한다.
 
---
 
## 0. 이 시트가 하는 일
 
컷마다 프롬프트를 새로 넣으면 인물 얼굴이 매번 달라집니다. 텍스트만으로는 같은 사람을 두 번 만들 수 없습니다. 그래서 인물별로 **시트 한 장**을 먼저 확정하고, 이후 모든 컷 이미지는 그 시트를 참조로 물려서 뽑습니다.
 
시트는 네 가지로 쓰입니다.
 
1. **얼굴 고정** — 컷 생성 시 참조 이미지로 물립니다.
2. **의상 확정** — 미술팀과 합의하는 기준물. 앞뒤 어느 쪽에서 봐도 뭘 입었는지 보입니다.
3. **캐스팅 기준** — 배우 미팅 때 "이런 얼굴, 이런 체형"의 출발점.
4. **파생의 원본** — 같은 인물의 시대·복장 변형을 여기서 갈라냅니다(§6).
---
 
## 1. 고정 규격
 
시트끼리 규격이 다르면 두 인물을 한 컷에 넣을 때 세계가 어긋납니다. 아래는 바꾸지 않습니다.
 
| 항목 | 값 |
|---|---|
| 모델 | `nano_banana_pro` (Nano Banana Pro) |
| 해상도 | `2k` → 2752 × 1536 |
| 화면비 | `16:9` |
| 구성 | 가로 1장, 세로 3분할, 얇은 흰 거터 |
| 배경 | 얼룩진 따뜻한 회벽 + 옅은 콘크리트 바닥, 세 패널 동일 |
| 조명 | 부드러운 확산광, 방향 동일, 세 패널 동일 |
 
### 패널별 지정 항목
 
`character sheet`라고만 쓰면 배치가 재현되지 않습니다. 패널마다 **방향·프레이밍·머리 포함 여부·손**을 따로 지정합니다.
 
| 항목 | 왼쪽 | 가운데 | 오른쪽 |
|---|---|---|---|
| 방향 | 정면 | 정확한 후면 | 정면 |
| 프레이밍 | 목 아래 ~ 발끝 | 머리 ~ 발끝 | 가슴 위 클로즈업 |
| 머리 | **의도적으로 없음** | 있음 | 있음 |
| 손 | 양손 보이고 비어 있음 | 자연스럽게 내림, 비어 있음 | 대개 프레임 밖 |
| 목적 | 의상 앞면·실루엣 | 의상 뒷면·헤어 후면 | 얼굴 정체성 |
 
**각 패널이 왜 그 형태인가** — 좌측에서 머리를 빼는 건 옷만 보게 하려는 것입니다. 얼굴이 있으면 시선이 얼굴로 가서 의상 검토가 안 됩니다. 손과 신발은 남깁니다. 손이 없으면 소매 길이를, 신발이 없으면 바지 기장을 판단할 수 없습니다. 중앙을 후면으로 두는 건 뒷모습이 콘티에 자주 나오기 때문이고(걸어 나가는 컷, 등을 보인 컷), 우측 얼굴은 실제 컷 생성 때 참조로 물리는 패널입니다.
 
---
 
## 2. 프롬프트는 두 종류뿐이다
 
| | |
|---|---|
| **A. 신규 생성** | 인물당 딱 한 번. §3 |
| **B. 수정** | 그 이후 전부. §6 |
 
**가장 중요한 원칙:** 마음에 드는 얼굴이 한 번 나오면 **다시 생성하지 않습니다.** 옷을 바꾸든 머리를 바꾸든 패널을 갈아치우든, 항상 그 결과를 참조 이미지로 물려 **수정**합니다. 신규 생성을 다시 돌리는 순간 얼굴은 다른 사람이 됩니다.
 
```
신규 생성 → job_id 기록 → 수정1(참조: job_id) → 수정2(참조: 수정1의 job_id) → …
```
 
job_id를 남기는 법은 §13.
 
---
 
## 3. 신규 생성
 
### 3.1 정보 순서
 
큰 구조에서 작은 디테일 순으로 씁니다. 이미지 모델은 앞쪽 토큰에 더 큰 가중치를 줍니다.
 
```
[결과물 종류] → [인물 정체성] → [패널 레이아웃] → [체형] →
[의상: 전 패널 공통] → [헤어: 중앙·우측] → [배경·조명] →
[일관성 잠금] → [금지 목록]
```
 
### 3.2 슬롯별 작성 규칙
 
| 슬롯 | 규칙 | 나쁜 예 → 좋은 예 |
|---|---|---|
| 정체성 | 나이대 + 출신 + 피부톤. 실존 인물 금지 | `beautiful, elegant` → `a Korean woman in her early sixties with warm light skin` |
| 얼굴 | 얼굴형·턱선·광대·코·입을 각각 한 마디씩. **성인은 성숙한 골격 명시** | "평범한 얼굴" → `round face with mature bone structure, defined nasolabial folds, gentle hollowing beneath the cheekbones, slightly softened jawline` |
| 눈 | 형태 + 색 + **반사광 억제 문장** 필수 | `warm dark brown eyes with lightly hooded upper lids and naturally muted catchlights, no oversized specular glare in the iris` |
| 헤어 | 길이 → 질감 → 가르마 → 얼굴 주변 형태 → **뒷모습** → 광택 → 색 | "단발" → `short softly permed dark brown hair just below the ears with grey showing at the roots, matching shape and volume in the rear view, soft everyday home-permed finish rather than a salon blowout` |
| 체형 | 삶이 몸에 남긴 것을 쓴다 | "보통 체형" → `a sturdy average-height build with a softened thickened waist and slightly rounded shoulders from a lifetime of standing work` |
| 의상 | **겉옷 → 여밈·실루엣 → 칼라·주머니 → 안쪽 상의·목선 → 하의 → 신발 → 허용 소품 → 금지 소품** 순. 없으면 `no bag`처럼 명시 | "앞치마" → `a faded indigo cotton apron with a chest bib and long waist ties knotted at the back` |
 
`beautiful`, `elegant`, `cinematic` 같은 주관어는 분위기 보조로만 씁니다. 얼굴 구조를 나타내는 객관적 특징이 먼저입니다.
 
### 3.3 일관성 잠금 — 그대로 복사
 
```
The three panels must depict one and the same person: identical face, age, skin tone, body proportions, hair color, outfit materials and color. Do not create three similar models.
```
 
`Do not create three similar models` 한 줄이 생각보다 크게 작동합니다.
 
### 3.4 신규 생성 완성 템플릿
 
대괄호만 교체합니다.
 
```
Create a photorealistic single wide horizontal three-panel character reference sheet of the same [woman/man]. The image is divided into three clean vertical sections with no borders, captions or text.
 
CHARACTER IDENTITY:
[나이대, 얼굴형, 피부톤과 질감, 눈, 눈썹, 코, 입, 무표정.] The same exact identity must be maintained wherever the face is visible.
 
PANEL LAYOUT:
- LEFT PANEL: a front-facing full-body wardrobe view shown strictly from the neck down. The panel is intentionally HEADLESS and ends cleanly at the base of the neck. This is an editorial clothing crop, not an injury: no head, no face, no wound, no gore, no dark opening. The plain background continues cleanly above the neckline. The figure stands straight, both arms relaxed slightly away from the sides, both hands visible and empty, feet fully visible.
- CENTER PANEL: a full-body rear view of the same person from head to toe, standing straight in the same neutral pose. The back of the hair, clothing and shoes are clearly visible. Hands empty.
- RIGHT PANEL: a large front-facing close-up portrait of the same person, framed from the upper chest upward, looking directly at camera with the same calm neutral expression. The face is centered and unobstructed.
 
BODY AND PROPORTIONS:
[체형, 어깨너비, 인상.] Keep exactly the same body proportions in the left and center panels.
 
OUTFIT — IDENTICAL IN ALL THREE PANELS:
[겉옷 종류·색·소재·길이·핏·여밈 상태·칼라·주머니.] Under it, [안쪽 상의와 목선]. [하의.] [신발.] [허용 소품.] The neckline and every visible clothing layer must match between panels. The garment is one physically identical outfit seen from different views, with matching fabric, color, length, fit, construction and layering. No logos, no prints, no visible brands, no unintended accessories.
 
HAIR — CENTER AND RIGHT PANELS:
[길이, 커트, 질감, 가르마, 얼굴 주변 형태, 뒷모습, 색, 마감.] The haircut and color must match perfectly between the rear view and the portrait.
 
REALISM:
[§4 리얼리즘 모듈을 통째로]
 
BACKGROUND AND LIGHTING:
One continuous plain [색·질감] studio backdrop across all panels. [조명 방향과 질], gentle realistic shadows, [색조], realistic skin and fabric texture, [그레인·콘트라스트·폴오프]. All panels share the same lighting direction, exposure, palette and photographic finish.
 
CONSISTENCY RULES:
- One person only, represented consistently across all three panels. Do not create three similar models.
- Identical outfit, materials, colors and layering in every panel.
- Identical body proportions in both full-body panels.
- Identical identity, age and facial structure wherever the face appears.
- No extra panels, duplicate people, props, text, labels, borders or collage decorations.
- Preserve the exact left-to-right order: headless front outfit view / full-body rear view / front close-up portrait.
 
[§8 금지 목록]
```
 
---
 
## 4. 리얼리즘 모듈 — 그대로 복사
 
AI 특유의 매끈한 피부를 없애는 블록입니다. **실사 인물 시트에는 예외 없이 넣습니다.**
 
```
visible fine skin texture with natural pores, age spots, fine lines, subtle asymmetries and uneven skin tone, no digital smoothing, no beauty filter, no AI-airbrushed look, skin completely free of artificial glare shine or highlight blooms, matte natural complexion
```
 
나이 든 인물이면 덧붙입니다.
 
```
lined forehead and crow's feet at the outer eyes, reddened knuckles and short unpainted nails
```
 
`realistic`이라는 단어는 아무 일도 하지 않습니다. 모공·잡티·비대칭을 직접 요구해야 합니다.
 
---
 
## 4-B. 눈 — AI 티가 가장 먼저 나는 곳
 
피부를 아무리 거칠게 만들어도 **눈이 죽어 있으면** 그 인물은 사람으로 안 읽힙니다.
AI 인물의 1번 실패 신호는 주름이 아니라 눈입니다. 초점 없이 정면을 보고, 습기가 없고,
눈꺼풀이 완전 대칭이고, 눈동자가 렌즈 한가운데 박혀 있습니다.
 
인물 시트에도 **눈 블록을 반드시 넣습니다.** 시트의 눈이 죽어 있으면 그 시트를 물린 모든 컷이 죽습니다.
 
```
eyes have genuine moisture and a small specular catchlight, the gaze has a definite
focal distance rather than staring blankly at the lens, one eyelid sits very slightly
lower than the other, faint capillaries at the inner corner, natural tear-line, the
iris shows real fibrous texture and a soft pupil edge
```
 
인물이 정면을 보는 패널이라도 **렌즈를 뚫고 보는 눈은 쓰지 않습니다.**
"카메라 뒤 어딘가에 초점이 맺혀 있다"로 씁니다.
 
| 증상 | 고치는 문장 |
|---|---|
| 눈이 유리구슬 같다 | `genuine moisture, a small specular catchlight, soft pupil edge` |
| 초점이 없다 | `the gaze has a definite focal distance, not a blank stare at the lens` |
| 좌우가 너무 대칭이다 | `one eyelid sits very slightly lower than the other` |
| 눈만 젊다 | `the skin around the eyes ages with the rest of the face` |
 
인물이 **어떤 눈을 가진 사람인가**(시선을 먼저 주는지, 먼저 피하는지, 응시가 무거운지)는
시트가 아니라 연기의 영역입니다. `acting-guide.md` §5를 봅니다.
시트에는 **눈의 물리**만 쓰고, 눈의 성격은 컷 생성에서 씁니다.
 
---
 
## 5. 머리 없는 좌측 패널
 
### 5.1 두 가지 변형 — 먼저 고른다
 
| | **A. 머리 없는 인체** | **B. 고스트 마네킹** |
|---|---|---|
| 몸 | 있음. 목 위만 잘림 | 없음. 옷만 형태를 유지 |
| 목둘레 | 목 밑동과 옷깃이 보임 | 옷깃이 비어 있고 안쪽 어둠이 보임 |
| 손·발 | 실제 손과 신발 | 실제 손과 신발 (남김) |
| 무엇을 보나 | 착용감·실루엣·핏 | 의상 자체의 재단 |
| 실패 위험 | 상해 이미지로 해석됨 | 플라스틱 마네킹이 나옴 |
 
**A**는 배우 미팅·의상 피팅 검토에, **B**는 의상 카탈로그식 확정에 맞습니다. 한 프로젝트 안에서는 하나로 통일하세요.
 
### 5.2 변형 A — 머리 없는 인체
 
```
a front-facing full-body wardrobe view shown strictly from the neck down, intentionally HEADLESS, the frame ending cleanly at the base of the neck. This is an editorial clothing crop, not a severed or injured body: no head, no face, no wound, no gore, no blood, no dark opening. The plain background continues cleanly above the neckline. Both arms rest naturally at the sides, both hands visible and empty.
```
 
**`not an injury` 문구를 반드시 넣습니다.** `headless`만 쓰면 모델이 상해나 절단으로 해석해 목 단면을 어둡게 뚫어 놓거나 불쾌한 결과를 냅니다. "편집용 의상 크롭"이라고 성격을 규정하고, 목 위로 **배경이 깨끗하게 이어진다**고 적어야 합니다.
 
### 5.3 변형 B — 고스트 마네킹
 
```
the outfit holds its own shape as if worn by an invisible person, hollow ghost-mannequin product photography, no mannequin material visible anywhere, the collar opening is empty and shows the dark hollow inside the garment, cut off cleanly just above the shoulder line with NO head, NO neck and no shoulder stump protruding, no plastic torso, no stand, no pole, no base, real human hands emerge from the ends of both sleeves hanging relaxed slightly away from the sides, the shoes stay on the floor at the bottom of the trousers
```
 
**`mannequin`이라고만 쓰면 진짜 플라스틱 마네킹이 나옵니다.** 원하는 건 마네킹이 아니라 **속이 빈 옷**입니다. `ghost-mannequin` · `invisible person` · `empty collar` · `hollow`를 함께 써야 합니다.
 
---
 
## 6. 수정 프롬프트 — 실전 문법
 
시트가 한 장 확정된 뒤의 모든 작업은 수정입니다. 의상 교체, 헤어 변경, 시대 이동, 패널 교체가 전부 여기 속합니다.
 
### 6.1 전체 골격
 
```
Edit reference image 1: [한 줄 요약 — 무엇을 바꾸고 무엇을 지키는지].
 
CHANGE: [바뀐 뒤의 상태. 일곱 조각을 순서대로]
 
PRESERVE EXACTLY:
- [네 줄 고정]
 
ONLY CHANGE: [한 문장으로 다시 잠금]
 
[금지 목록]
```
 
**변경사항보다 보존사항을 더 구체적으로 씁니다.** 바꿀 것만 적으면 모델이 나머지도 조금씩 새로 그립니다.
 
### 6.2 여는 문장 — 공식
 
첫 문장에서 세 가지를 동시에 선언하고, 머리 없는 패널을 **이름으로** 부릅니다.
 
아래 예시는 의상과 헤어를 한 번에 바꾸지만, 지침 #6에 따라 실제로는 두 번에 나눠 생성합니다(§6.13).
 
```
Edit reference image 1: change only the character's outfit and hair, while keeping the character's identity exactly and preserving the sheet's existing three-panel structure exactly, including the intentionally HEADLESS left panel.
```
 
`including the intentionally HEADLESS left panel`이 첫 문장에 없으면, 모델이 편집 과정에서 왼쪽 패널에 머리를 만들어 붙입니다. 뒤에서 한 번 더 말하지만 첫 문장에 있는 것과 없는 것의 차이가 큽니다.
 
### 6.3 CHANGE — 일곱 조각
 
| # | 조각 | 예 |
|---|---|---|
| 1 | **범위 선언** | `In all three panels, replace the current outfit with…` |
| 2 | **새 의상 머리→발** | §6.10 CHANGE — OUTFIT |
| 3 | **없는 것 열거** | §6.10 CHANGE — OUTFIT 끝의 `No scarf, no gloves, …` |
| 4 | **시대 중화** *(시대를 옮길 때만)* | `nothing that dates the decade` |
| 5 | **옛 의상 명명 삭제** | §6.5 |
| 6 | **목둘레 지시** | §6.4 |
| 7 | **헤어 — 패널 범위 지정** | `Only in the center and right panels, change the hair to…` |
 
#### 조각 2 — 재단을 쓴다
 
`white coat`가 아니라 `knee-length, worn open, notched collar, patch pockets at the hips and one breast pocket`입니다. 길이·여밈·칼라·주머니 네 가지를 적으면 같은 옷이 반복 생성됩니다.
 
#### 조각 3 — 직업 소품을 미리 막는다
 
모델은 빈자리를 채웁니다. 의사 가운을 입히면 청진기를 걸고, 코트를 입히면 목도리를 두르고, 사무직을 지정하면 클립보드를 쥐어 줍니다.
 
```
No profession-signaling props unless explicitly requested: no stethoscope, instruments, clipboard, pen, bag or visible logo.
```
 
### 6.4 목둘레 지시 — 머리 없는 패널의 핵심
 
**수정 프롬프트에서 가장 자주 실패하는 지점입니다.**
 
왼쪽 패널에는 머리가 없습니다. 목이 잘려 있으니 모델은 그 단면에서 옷깃이 어떻게 보여야 하는지 알 수 없습니다. **목 아래에 무엇이 보이는지를 직접 묘사해야** 합니다. 안 쓰면 옛 옷깃이 남거나, 목 단면이 뭉개지거나, 머리가 생깁니다.
 
예: §6.10 REMOVE COMPLETELY의 `At the neckline, …` 이하 두 문장. 세 부분으로 씁니다.
 
1. 새 옷깃이 목 밑동에서 어떻게 앉는지
2. 옛 옷의 흔적이 남지 않는다는 선언
3. `including in the headless LEFT panel` — 명시적 확장
### 6.5 옛 의상 명명 삭제
 
새 옷만 묘사하면 옛 옷이 부분적으로 살아남습니다. 카디건 소매가 코트 밑에 남거나, 앞치마 끈이 그대로 있거나, 귀 뒤의 연필이 안 없어집니다.
 
**없앨 것을 이름으로 부르고, 섞지 말라고 씁니다.** 예: §6.10 REMOVE COMPLETELY의 첫 두 문장(`… are GONE in every panel. Do not layer, merge or hybridize old and new clothing.`).
 
`Do not layer, merge or hybridize`가 핵심입니다. 모델은 옛 옷과 새 옷을 합성하려는 경향이 있습니다.
 
빠뜨리기 쉬운 것들입니다.
 
- 귀 뒤의 연필, 머리띠, 헤어핀
- 앞치마 끈, 소매 토시
- 목도리, 장갑, 시계, 반지
- 명찰·배지
- **신발** — 옷만 바꾸고 신발을 안 적으면 옛 신발이 남습니다
### 6.6 패널별 범위 지정
 
수정 대상이 패널마다 다르면 **어느 패널인지 적습니다.**
 
- 의상 → `in all three panels` (머리 없는 패널 포함)
- 헤어 → `only in the center and right panels` (머리가 있는 두 패널만)
- 얼굴 → 건드리지 않음
헤어에 `in all three panels`을 쓰면 모델이 왼쪽 패널에도 머리를 만들려 합니다.
 
### 6.7 PRESERVE EXACTLY — 네 줄 고정
 
순서와 내용을 바꾸지 말고 매번 씁니다. 바꾸지 않는 수정이라도 전부 적습니다.
 
```
PRESERVE EXACTLY:
- LEFT PANEL: keep it intentionally HEADLESS, front-facing and framed from the neck down. Do not add, infer, reconstruct or complete a head or face in that panel. Keep the clean neck crop and the uninterrupted plain background above it. Its clothes change fully: [새 의상 요약], no [옛 의상 1], no [옛 의상 2]
- IDENTITY: preserve the exact same face in the right portrait — identical facial features, bone structure, skin, age, eye shape, nose, lips and expression. Change the hair around the existing face; do not regenerate, reinterpret, beautify, age or reshape the face. Do not borrow a face from another reference.
- STRUCTURE: preserve all three poses, body proportions, crop boundaries, panel widths, panel order and empty hands.
- ENVIRONMENT: preserve the existing background, lighting direction, exposure, shadows, palette, contrast, grain and falloff.
```
 
각 줄이 막는 것:
 
| 줄 | 막는 실패 |
|---|---|
| LEFT PANEL | 왼쪽에 머리가 생기는 것. `add, infer, reconstruct, complete` 네 동사를 다 씁니다 — 모델은 불완전한 사람을 완성하려는 본능이 있습니다 |
| IDENTITY | 얼굴이 미묘하게 달라지는 것. `beautify, age, reshape`까지 막아야 합니다 |
| STRUCTURE | 포즈·패널 폭이 흔들리는 것. `empty hands`는 소품이 생기는 것을 막습니다 |
| ENVIRONMENT | 톤·그레인이 달라지는 것. `palette, contrast, grain, falloff`를 그대로 씁니다. "같은 룩"으로는 안 됩니다 |
 
**LEFT PANEL 줄의 함정:** 이 패널은 "보존"과 "변경"이 동시에 걸립니다. 머리 없음은 보존, 옷은 변경입니다. 그래서 한 줄 안에 `Its clothes change fully:`를 붙여 두 지시를 함께 담습니다.
 
### 6.8 ONLY CHANGE — 한 문장
 
앞에서 길게 설명한 뒤 마지막에 한 줄로 요약하면 적중률이 올라갑니다.
 
아래 예시는 의상과 헤어를 한 번에 바꾸지만, 지침 #6에 따라 실제로는 두 번에 나눠 생성합니다(§6.13).
 
```
ONLY CHANGE: the outfit in all three panels including the neckline of the headless panel, and the hair in the center and right panels. The face and identity 100% identical to reference image 1. Everything else remains consistent with reference image 1 wherever possible.
```
 
`including the neckline of the headless panel`을 여기서도 반복합니다. 목둘레를 세 번째로 못 박는 자리입니다.
 
### 6.9 얼굴을 다시 묘사하지 않는다
 
**수정 프롬프트에서는 얼굴을 새로 묘사하지 않습니다.** 의상이나 헤어만 바꾸면서 인물 묘사를 길게 붙이면, 그 텍스트가 참조 이미지와 경쟁해 얼굴이 새로 생성될 확률이 올라갑니다.
 
- 수정할 때 얼굴에 대해 쓸 것은 **보존 지시뿐**입니다.
- 새 인물 묘사는 §3(신규 생성)에서만 씁니다.
- 컷 생성은 경우가 다릅니다 — §14를 보세요.
### 6.10 완성 예시
 
아내(60대)를 집 앞치마 차림에서 외출복으로 바꾸는 편집입니다.
 
```
Edit reference image 1: change only the character's outfit to present-day contemporary outerwear, while keeping the character's identity exactly and preserving the sheet's existing three-panel structure exactly, including the intentionally HEADLESS left panel.
 
CHANGE — OUTFIT:
In all three panels, replace the current outfit with simple contemporary everyday wear for a cool day: a long unstructured wool coat in soft charcoal grey, worn open, over a fine cream knit jumper, plain straight-leg dark trousers and plain dark ankle boots. The new outfit is one physically identical outfit seen from different views, with matching fabric, color, length, fit and layering. No scarf, no gloves, no bag, no jewellery beyond what is preserved below, no logos, no prints, no visible brands.
 
REMOVE COMPLETELY:
The existing muted olive knit top, the faded indigo cotton apron with its chest bib and waist ties, and the grey house slippers are GONE in every panel. Do not layer, merge or hybridize old and new clothing. At the neckline, only the cream jumper's plain round collar is visible at the base of the neck under the open coat. No trace of the apron or the olive knit remains, including in the headless LEFT panel, where the coat and jumper are visible below the neck cut.
 
PRESERVE EXACTLY:
- LEFT PANEL: keep it intentionally HEADLESS, front-facing and framed from the neck down. Do not add, infer, reconstruct or complete a head or face in that panel. Keep the clean neck crop and the uninterrupted mottled warm grey plaster background above it. Its clothes change fully: open wool coat over jumper and trousers, no apron, no olive knit, no slippers
- IDENTITY: preserve the exact same face and the exact same hair in the right portrait and the center rear view — identical facial features, bone structure, skin, age, eye shape, nose, lips and expression. Do not regenerate, reinterpret, beautify, age or reshape the face.
- STRUCTURE: preserve all three poses, body proportions, crop boundaries, panel widths, panel order, and her hands with their reddened knuckles, short unpainted nails, thin gold wedding band and scuffed leather wristwatch.
- ENVIRONMENT: preserve the mottled warm grey plaster backdrop, pale concrete floor, lighting direction, exposure, soft shadows, floor contact shadow, palette, contrast, grain and falloff.
 
ONLY CHANGE: the outfit in all three panels including the neckline of the headless panel. The face, hair and identity 100% identical to reference image 1.
 
no head on the left panel, no mannequin, no other people, no duplicate figures, no props, no text, no watermark, no logos, no frame borders
```
 
### 6.11 CHANGE와 PRESERVE의 목록을 맞춘다
 
**실제로 자주 나는 사고입니다.** CHANGE에서 "재킷 없음"이라고 써놓고 PRESERVE에 `shirt and jacket over jeans`라고 적으면, 모델이 두 지시를 섞어 재킷을 반쯤 그립니다.
 
보내기 전 이것만 확인하세요.
 
- CHANGE 조각 2의 의상 목록 **==** PRESERVE LEFT PANEL 줄의 `Its clothes change fully:` 뒤 목록
- CHANGE 조각 5의 GONE 목록 **==** PRESERVE LEFT PANEL 줄 끝의 `no A, no B` 목록
템플릿을 복사해 쓰면 여기가 가장 먼저 어긋납니다.
 
### 6.12 시대를 옮길 때
 
같은 인물을 1980년에서 현재로(또는 반대로) 옮길 때만 추가합니다.
 
```
nothing that dates the decade
```
 
그리고 시대를 만드는 요소를 이름으로 지웁니다.
 
| 옮기는 방향 | 이름으로 지울 것 |
|---|---|
| 1980 → 현재 | 기름 발라 넘긴 머리, 넓은 넥타이, 폴리에스터 광택, 두꺼운 뿔테, 몸뻬 바지 |
| 현재 → 1980 | 로고·프린트, 매트한 현대 커트, 스니커즈, 손목 웨어러블 |
 
**헤어가 의상보다 시대를 강하게 드러냅니다.** 시대 이동 편집에서는 헤어를 반드시 함께 지정하세요.
 
### 6.13 한 번에 하나만
 
한 번의 수정에서는 **한 가지만** 바꿉니다(지침 #6). 의상과 헤어도 두 번에 나눠 생성합니다. 예외는 떼면 성립하지 않는 두 변경뿐입니다. 여러 가지를 한 번에 바꾸면 실패했을 때 어느 지시가 무시됐는지 알 수 없습니다.
 
---
 
## 7. 참조 이미지가 여러 장일 때 — 역할을 분리한다
 
두 장 이상을 넣으면 각 이미지의 **권한을 문장으로 분리**합니다. 안 하면 의상 참고 이미지의 얼굴이나 체형까지 섞입니다.
 
```
Reference image 1 controls identity, face, body proportions, poses, panel layout, framing, background, lighting and photographic finish.
Reference image 2 controls only the design, cut, length, material and details of the new coat.
Do not transfer the face, body, pose, background or lighting from reference image 2.
```
 
### 권한 우선순위
 
1. **정체성 레퍼런스** — 얼굴, 피부, 연령감
2. **시트 레퍼런스** — 패널 구조, 포즈, 크롭, 배경
3. **의상 레퍼런스** — 디자인과 소재만
4. **헤어 레퍼런스** — 헤어 형태와 색만
하나의 이미지가 여러 역할을 맡아도 되지만, 프롬프트 안에서는 역할을 문장으로 나눠 둡니다.
 
`Do NOT take the face from image 2` 는 의상 참조를 쓸 때 **예외 없이** 넣습니다.
 
---
 
## 8. 금지 목록 — 그대로 복사
 
**공통**
```
no text, no watermark, no logos, no frame borders, no captions, no labels, no other people, no duplicate figures, no extra panels, no props, no furniture, no background objects, no collage decorations
```
 
**성인 인물**
```
no babyface, no overly youthful rounded proportions
```
 
**실사**
```
no beauty filter, no digital smoothing, no airbrushing, no plastic skin, no glossy skin, no glamour retouching, no distorted anatomy, no extra fingers
```
 
**3분할 전용**
```
left panel headless with no head and no face, centre and right panels the same single person, centre panel standing full-body head-to-toe not cropped not sitting, right panel a tight close-up not a full body, preserve the left-to-right panel order
```
 
**시대물**
```
no modern clothing, no modern eyewear, no smartphones, no modern signage
```
 
---
 
## 9. 자주 깨지는 것과 고치는 문장
 
| 증상 | 원인 | 덧붙일 문장 |
|---|---|---|
| 좌측 목 위에 머리가 생김 | 여는 문장에 HEADLESS 선언 없음 | `Do not add, infer, reconstruct or complete a head or face in that panel` + 여는 문장 수정 |
| 목 단면이 상처처럼 나옴 | 성격 규정 누락 | §5.2 문장 그대로 (`editorial clothing crop, not a severed or injured body` + 목 위 배경이 이어진다) |
| 좌측에 플라스틱 마네킹 | `mannequin`이라고 씀 | `hollow ghost-mannequin, invisible person, empty collar, no dress form, no stand` |
| 옛 옷이 부분적으로 남음 | GONE 선언 누락 | `The old [items] are GONE in every panel. Do not layer, merge or hybridize old and new clothing.` |
| 목선에 옛 터틀넥이 남음 | 목둘레 지시 누락 | §6.4 세 부분 전부 |
| 귀 뒤 연필·머리띠가 안 없어짐 | 작은 소품을 이름으로 안 부름 | 이름을 직접 적어 GONE 목록에 |
| 신발만 옛것 | 신발을 새 의상 목록에 안 적음 | 의상은 항상 머리→발 전부 |
| 청진기·클립보드가 생김 | 직업 소품 금지 누락 | `No profession-signaling props unless explicitly requested` |
| 옷이 바닥에서 떠 있음 | 접지 미지정 | `the garment stands on the floor with a natural contact shadow, not floating, not tilted` |
| 두 이미지의 얼굴이 섞임 | 권한 분리 누락 | §7 세 줄 전부 |
| 오른쪽 얼굴이 딴 사람 | 수정에서 얼굴을 재묘사함 | 얼굴 묘사를 지우고 `Change the hair around the existing face; do not regenerate, reinterpret, beautify, age or reshape the face.` |
| 수정했더니 전부 딴 사람 | 신규 생성을 돌림 | 참조 이미지를 물렸는지 먼저 확인 |
| 패널마다 의상이 다름 | 동일 의상 선언 누락 | `one physically identical outfit seen from different views, with matching fabric, color, length, fit, construction and layering` |
| 세 명의 비슷한 사람이 나옴 | 동일인 잠금 누락 | `Do not create three similar models` |
| 톤·그레인이 달라짐 | "같은 룩"으로 적음 | `palette, contrast, grain, falloff` 네 단어 그대로 |
| 재킷이 반쯤 그려짐 | CHANGE와 PRESERVE 불일치 | §6.11 대조 |
| 헤어가 시대를 못 벗음 | 헤어 미지정 | `matte and modern, no pomade shine, no sculpted vintage wave` |
| 패널 폭이 제각각 | 레이아웃 보존 누락 | `panel widths, panel order` 를 STRUCTURE 줄에 |
| 피부가 너무 매끈 | 리얼리즘 모듈 누락 | §4를 통째로 |
| 나이가 어려 보임 | 성숙 골격 미지정 | `mature adult bone structure, defined nasolabial folds, no babyface` |
| 배지·명찰 글자 깨짐 | 글자를 요구함 | `a plain blank badge, no writing, no photo, no logo` |
| 세 패널 조명이 다름 | 조명 통일 누락 | `All panels share the same lighting direction, exposure, palette and photographic finish` |
 
---
 
## 10. 문장 작성 원칙
 
### 원하는 상태를 먼저, 금지는 나중에
 
금지만 길게 나열하지 말고 원하는 상태를 정확히 정의한 뒤, 자주 생기는 오류만 막습니다. 예: §6.10의 목둘레 문장(`At the neckline, only the cream jumper's plain round collar is visible …`).
 
### 모호한 시대 표현을 시각 특징으로 푼다
 
`modern hair` 보다 아래가 정확합니다.
 
```
Short at the sides, naturally textured on top, matte finish, no pomade shine, no sculpted vintage wave.
```
 
### 한 프롬프트 안에서 충돌하지 않는다
 
실제로 자주 나는 오기입니다.
 
- `few loose strands` 와 `no strands loose` 를 같이 쓰지 않는다
- 본문과 요약부의 의상 목록을 다르게 쓰지 않는다 → §6.11
- `worn open` 과 `fully buttoned` 을 같이 쓰지 않는다
템플릿을 복사해 고칠 때 요약부를 안 고쳐서 생깁니다.
 
### 핵심 조건만 반복한다
 
반복 가치가 높은 것은 다섯입니다.
 
1. 왼쪽 패널은 목 없는 크롭
2. 세 패널은 동일 의상
3. 얼굴 정체성 고정
4. 기존 의상 완전 제거
5. 허용된 부분만 변경
단, **같은 프롬프트 전체를 두 번 붙여넣지 않습니다.** 중복은 우선순위를 높이지 않고 길이만 늘리며, 한쪽만 고쳐서 모순이 생깁니다.
 
---
 
## 11. 생성 전 점검표
 
- [ ] 신규 생성인지 기존 이미지 편집인지 첫 문장에 분명한가
- [ ] 한 장의 가로형 3패널 시트라고 명시했는가
- [ ] 왼쪽·가운데·오른쪽 패널을 각각 설명했는가
- [ ] 왼쪽 패널이 **의도적인** 목 없는 크롭이고 **상해가 아니라고** 적었는가
- [ ] 세 패널이 동일 인물임을 명시했는가 (`Do not create three similar models`)
- [ ] 의상의 겉옷·안쪽 옷·하의·신발·목선을 모두 적었는가
- [ ] 후면에서 보여야 할 의상·헤어 특징을 적었는가
- [ ] 배경·조명·색감이 세 패널에서 같다고 명시했는가
- [ ] 소품·로고·문자·추가 패널을 금지했는가
- [ ] 편집이라면 제거할 옛 의상을 **이름으로** 전부 적었는가
- [ ] 편집이라면 얼굴을 다시 묘사하지 **않았는가**
- [ ] 참조가 여러 장이면 역할과 우선순위를 나눴는가
- [ ] CHANGE 목록과 PRESERVE 목록이 어긋나지 않는가
- [ ] 같은 프롬프트를 중복해 붙여넣지 않았는가
---
 
## 12. 「어머니와 고등어」 인물 명세
 
> ⚠ 콘티 씬 1의 cast는 **영훈 60대 후반, 아내 50대 후반**이다. 아래 명세(둘 다 60대 초반)와 어긋난다 — `film-decisions.md` 미결 #1. 결정 전에는 아래 문장을 바꾸지 않는다.
 
시트를 만들 때 아래 문장을 §3 템플릿의 정체성·의상 슬롯에 그대로 넣습니다.
 
### 주연
 
**영훈 (60대 초반 · 현재 · 씬 1, 10)**
```
IDENTITY: a Korean man in his early sixties, greying hair thinning at the temples, deep lines from nose to mouth, a heavier settled jaw, thin metal-framed reading glasses, calm settled expression
WARDROBE: a soft charcoal cardigan over a pale collared shirt, comfortable dark home trousers, grey house slippers, a thin worn gold wedding band
```
 
**영훈 (21세 · 1980 · 씬 2–5, 7, 8, 9)**
```
IDENTITY: a lean 21-year-old Korean man, short neatly parted black hair, a thin face with faintly hollow cheeks, serious dark eyes, no glasses
WARDROBE: a faded navy jacket over a white shirt buttoned to the top, worn dark grey trousers, plain canvas sneakers, no bag
```
 
**영훈 (15세 · 1970년대 후반(연도 미지정 — `film-decisions.md` 미결 #15) · 씬 6, 9 회상)**
```
IDENTITY: a thin 15-year-old Korean boy, close-cropped hair, a narrow face with the same eye shape as the adult version, sunburnt neck
WARDROBE: a worn navy school shirt, patched cotton trousers, rubber shoes
```
 
**어머니 (40대 후반 · 씬 6, 8, 9)**
```
IDENTITY: a Korean woman in her late forties, hair pulled back with grey at the temples, a weathered face with deep lines around the eyes, reddened cracked hands, short unpainted nails
WARDROBE: a worn sweater under a rubber apron, monpe work trousers, black rubber boots, a cotton towel tied over her hair, sleeve protectors
```
 
**아내 (60대 초반 · 현재 · 씬 1, 10)** — *시트 확정 · Higgsfield job `c108ad62` · 변형 B(고스트 마네킹)*
```
IDENTITY: a Korean woman in her early sixties with warm light skin, round face with mature bone structure, defined nasolabial folds, gentle hollowing beneath the cheekbones, lined forehead and crow's feet, warm dark brown eyes with lightly hooded upper lids, sparse naturally thinning eyebrows, bare lips with a dry matte finish, short softly permed dark brown hair just below the ears with grey showing at the roots, soft everyday home-permed finish
WARDROBE: a muted olive fine-knit long-sleeve top, a faded indigo cotton apron with a chest bib and long waist ties knotted at the back, loose charcoal cotton trousers, plain grey house slippers, a thin worn gold wedding band, small gold stud earrings, a simple wristwatch with a scuffed leather strap, no bag
```
 
### 조연
 
**사무장 (40대 후반 · 씬 3, 4)**
```
IDENTITY: a Korean man in his late forties, a well-fed face, eyes that crinkle when he smiles, oiled side-parted hair, gold-rimmed glasses. He must read as completely trustworthy — no smirk, no sidelong glance, no sinister lighting
WARDROBE: a brown polyester suit with a faint sheen, a wide patterned tie, a slightly frayed shirt cuff, a worn leather briefcase
```
 
**친구1 (21세 · 씬 3, 5)**
```
IDENTITY: a taller, well-dressed 21-year-old Korean student, tidy fashionable haircut, relaxed confident posture
WARDROBE: a navy nylon windbreaker over a bright polo shirt, pressed jeans, clean white sneakers
```
 
**친구2 (21세 · 씬 3, 5, 9)**
```
IDENTITY: a shorter, round-faced 21-year-old Korean student, thick black-framed glasses
WARDROBE: a bulky hand-knitted sweater, corduroy trousers, a canvas book bag slung across the chest
```
 
**아줌마 (50대 · 씬 9)**
```
IDENTITY: a Korean woman in her fifties, a broad practical face, hair under a cotton cap, entirely without malice
WARDROBE: a rubber apron over a floral blouse, sleeve protectors, black rubber boots
```
 
**단속반 (30대 · 씬 9)**
```
IDENTITY: a Korean man in his thirties, an ordinary tired face — not a villain, doing a job he is sick of
WARDROBE: a municipal inspector's windbreaker over a shirt and tie, an armband, a clipboard
```
 
### 단역 — 시트 불필요, 컷 프롬프트에 한 줄로
 
- 교수(50대): `a Korean professor in his fifties in a worn suit`
- 학생1·2·3(21세): `Korean students in 1980 campus clothing — grey school jackets, knitted vests, cloth book bundles`
- 상인 3명(40~60대): `market fishmongers in rubber aprons and boots`
- 손님(30대 여자): `a young Korean housewife in a quilted winter coat`
- 서무직원(40대): `a Korean clerk in his forties with sleeve protectors`
---
 
## 13. 파일·버전 관리
 
```
sheet_아내60_v1_de1959a1.png        ← 신규 생성
sheet_아내60_v2_3f4460ea.png        ← 좌측 머리 제거
sheet_아내60_v3_c108ad62.png        ← 좌측 고스트 마네킹  ★확정
sheet_아내60_외출복_v1_xxxxxxxx.png  ← ★확정본에서 파생
```
 
- 파일명 끝에 **job_id 앞 8자리**를 붙입니다. 되돌아가거나 이어서 수정할 때 필요합니다.
- 인물별로 `★확정` 한 장을 정하고 그 job_id를 §12에 적어 둡니다.
- **파생본은 항상 ★확정본에서 갈라냅니다.** 파생본을 다시 파생시키면 원본에서 멀어집니다.
- 확정본을 지우지 마세요. 이후 모든 컷이 그것을 참조합니다.
---
 
## 14. 시트를 컷 생성에 쓰는 법
 
컷 이미지를 뽑을 때 확정 시트를 참조 이미지로 물리고, 프롬프트 앞에 한 줄 넣습니다.
 
```
Use the person in reference image 1. Same face, same bone structure, same hair, same wardrobe. Change only the pose, framing, location and lighting.
```
 
그다음에 컷의 세트·순간·렌즈 문장을 이어 붙입니다.
 
### 얼굴 묘사는 어디까지 반복하나
 
| 상황 | 얼굴 묘사 |
|---|---|
| **시트 수정**(§6) | 쓰지 않는다 → §6.9 |
| **컷 생성** | 참조가 얼굴을 통제하므로 얼굴은 반복하지 않는다. 대신 **의상은 §12 문장을 그대로** 반복한다 |
 
참조 이미지와 텍스트가 어긋나면 모델이 둘을 섞습니다. 그래서 반복할 때는 **토씨 하나 바꾸지 않고** 반복하고, 반복할 필요가 없는 것은 아예 쓰지 않습니다.
 
### 시트가 통제하지 않는 것
 
시트는 **얼굴과 의상까지**입니다. 시트의 스튜디오 조명이나 회벽 배경이 컷에 따라오면 안 되므로, 컷 프롬프트에서 세트와 조명을 반드시 새로 씁니다.
 
컷 프롬프트에서 시트가 비워 둔 칸을 채우는 문서는 따로 있습니다.
 
| 칸 | 문서 |
|---|---|
| 세트·조명·카메라 위치·공간 배치 | `location-guide.md` |
| 표정·시선·손·호흡·무게중심 | `acting-guide.md` |
| 프롬프트 전체 구조와 참조 권한 | `production-os-prompt-guide.md` (Step 2 · 3 · 9) |
 
### 영상 생성에서 요소로 쓸 때 — 참고 사례 (2026-09-25)
 
다른 작품 The Prompter 씬 1(Seedance 2.5 영상 66개)이 인물 요소를 쓴 방식이다. 근거는 `claude/the-prompter-씬1-분석.md` §4.2. 이 영화의 규칙이 아니다.
 
- **의상·헤어 상태마다 요소가 따로 있었다.** 같은 인물이 무대 의상·가운과 수건·가운과 푼 머리·사복으로 각각 등록됐다(`char_<인물>_<상태>_v1`). 이 영화에서는 §13의 파생본(예: `sheet_아내60_외출복_v1`)이 그런 상태별 요소에 해당한다.
- **한 영상 안에서 상태가 바뀌면 두 요소를 함께 붙이고 시간을 나눴다.** "수건을 쓴 동안은 요소 A, 0:09부터는 요소 B". 한 요소로 두 상태를 설명하지 않았다(`production-os-prompt-guide.md` §9).
- **인물 줄 문장을 바꾸지 않았다.** 같은 인물 설명문이 29개 영상에서 한 문장뿐이었다 — 위의 "토씨 하나 바꾸지 않고"와 같다.
- **참조판을 바꾸면 설명문도 새 판에 맞췄다.** 그 작품은 장소판을 바꾼 뒤 설명문을 새 판에 맞게 다시 썼다. 인물 요소 이미지를 바꿀 때도 인물 줄을 새 이미지와 대조한다(위의 "참조 이미지와 텍스트가 어긋나면").
---
 
## 15. 하지 말 것
 
- 실존 배우나 유명인을 닮게 만들지 않습니다. 레퍼런스 이미지는 **구성과 분위기 참고**이지 얼굴 출처가 아닙니다.
- 마음에 든 얼굴이 나온 뒤 신규 생성을 다시 돌리지 않습니다(§2).
- 수정 프롬프트에서 얼굴을 다시 묘사하지 않습니다(§6.9).
- 한 번의 수정에서 두 가지 이상을 바꾸지 않습니다(§6.13).
- 시트의 배경·조명·화면비를 인물마다 다르게 하지 않습니다(§1).
- 같은 프롬프트를 중복해 붙여넣지 않습니다(§10).
- 눈 블록을 빼지 않습니다(§4-B).