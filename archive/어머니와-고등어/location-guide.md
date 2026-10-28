# 장소 프롬프트 작성 가이드 — 「어머니와 고등어」
 
이미지·영상 생성에서 **장소를 통제하는 방법**을 정리한 문서다.
인물은 `character-sheet-guide.md`, 연기는 `acting-guide.md`,
프롬프트 전체 구조는 `production-os-prompt-guide.md`가 담당한다.
이 문서는 그중 **Step 3 (LOCATION_MAP)** 한 칸만 깊게 판다.
 
데이터는 `embeddedAssetData.json`이 정본이고(→ §9), 이 문서는 쓰는 법만 다룬다.
작업별 템플릿은 `location-templates.md`(§01~§12), 그 근거가 된 실제 프롬프트는 `힉스필드_장소_에셋_실제_프롬프트_모음.md`(원문 N)에 있다.
§3.2·§3.3·§6의 "분석 §N"은 다른 작품의 영상 생성 기록 `claude/the-prompter-씬1-분석.md`다.
 
---
 
## 0. 가장 먼저 하는 판별 — LOCKED EDIT인가 DERIVED VIEW인가
 
프롬프트를 한 글자도 쓰기 전에 이것부터 정한다. 나머지 규칙이 전부 여기서 갈린다.
 
**카메라를 유지하는가.**
 
유지한다 → `LOCKED EDIT`. 같은 사진의 수정본이다.
 
```
Edit <<<image_1>>> WITHOUT reframing: camera position, angle, lens and framing are LOCKED.
```
 
바꾼다 → `DERIVED VIEW`. 같은 장소의 새 사진이다.
 
```
Using <<<image_1>>> as the exact same location, generate a new view from [새 카메라 위치], looking [방향].
```
 
둘을 한 프롬프트에 섞으면 모델이 중간값으로 타협한다. 현관에서 열 번 넘게 돌아간 원인이 이 혼선이다.
**컷의 퍼스트 프레임 이미지는 거의 전부 DERIVED VIEW다** — 장소 뷰 이미지를 물리고 카메라는 콘티가 정한다.
 
**두 번째 판별 — 픽셀 구조를 유지하는가, 배치 개념만 가져오는가.**
 
| 가져오는 것 | 표현 | 모드 |
|---|---|---|
| 벽선·가구 위치까지 픽셀 단위 | `exact same photograph` | LOCKED EDIT |
| 장소 정체성만, 새 시점 허용 | `exact same room / location` | DERIVED VIEW |
| 문·창·가구의 상대 위치만 | `only for the LAYOUT` | 새 이미지 생성 |
| 건물 공통 재료 체계만 | `same building's material register` | 새 공간 생성 |
 
이 네 표현은 **서로 다른 권한**이다. 아무거나 바꿔 쓰면 안 된다(다섯 번째 `only for [element]`까지 → §6).
 
---
 
## 1. 장소가 무너지는 일곱 가지와 그 자리
 
| 증상 | 원인 | 고치는 곳 |
|---|---|---|
| 컷마다 주방 구조가 바뀐다 | 컷마다 장소를 새 문장으로 묘사했다 | MASTER GEOMETRY 고정 |
| 인물이 랜드마크에서 멀리 서 있다 | "근처에", "옆에"를 썼다 | §4 |
| 첫 프레임이 빈 방으로 시작한다 | 첫 프레임 점유를 안 썼다 | §5 |
| 좌우가 뒤집힌다 | 카메라가 어느 쪽인지, 좌우가 어느 기준인지 안 썼다 | §3 Camera 줄 · §3.1 |
| 레퍼런스의 앵글까지 따라온다 | 권한 범위를 안 적었다 | §6 |
| 시대가 흐릿하다 | 시대를 색으로 설명했다 | §7 |
| 1980년 방에 현대 소품이 섞인다 | 물건 목록을 안 닫았다 | §14.2 `Nothing else:` |
 
---
 
## 2. 장소 시트는 대장에 있다
 
장소마다 한 번 쓰는 시트(MASTER GEOMETRY · LIGHT LOCK · MATERIALS · LANDMARKS · DEPTH ·
CAMERA SIDE · FORBIDDEN)의 양식과 실제 내용은 **`location-assets.md` §2**에 있다.
이 문서는 그 시트를 **컷 프롬프트로 옮기는 방법**만 다룬다.
 
---
 
## 3. 컷별 LOCATION MAP — 좌표 한 줄 + 네 줄
 
장소 시트를 통째로 컷 프롬프트에 넣지 않는다. 컷마다 필요한 것만 뽑는다.
 
```
LOCATION MAP
좌표: 이 프롬프트의 왼쪽·오른쪽은 모두 화면 기준(SCREEN)이다. 인물 자신의 좌우가 아니다.
Camera: 거실 쪽에서 주방을 향해, 아이레벨 1.5m, 식탁에서 2.5m.
전·중·후경: 식탁 상판 화면 오른쪽 1/3, 검은 비닐봉지 / 아내, 식탁 반대편 / 열린 주방과 싱크대.
Light: 식탁 위 펜던트가 유일한 주광, 위에서 약간 앞. 주방 후드등이 후경을 약하게 받친다.
```
 
(위는 형식 예시다. 주방 보조광이 후드등인지 상부장 하부등인지는 `location-assets.md` LC-002 LIGHT LOCK에서 확정한다.)
 
| 줄 | 통제하는 것 |
|---|---|
| 좌표 | 좌우의 기준 → 인물 기준·화면 기준 혼동을 막는다 |
| Camera | 카메라 위치·방향·높이·거리 → 좌우 뒤집힘과 축 넘김을 막는다 |
| 전·중·후경 | 깊이 세 층 → 평면적 이미지를 막는다 |
| Light | 광원 방향 → 컷 사이 조명 점프를 막는다 |
| (필요할 때) Path | 이동 경로 → 영상 프롬프트에서만 |
 
**규칙: 컷 프롬프트 안의 장소 정보는 좌표 줄 + 네 줄을 넘지 않는다.**
장소를 길게 쓸수록 인물 레퍼런스가 밀려난다.
 
### 3.1 좌우는 화면 기준 (사용자 확정 · 2026-09-24)
 
- 콘티와 프롬프트의 **왼쪽·오른쪽은 모두 화면 기준**이다. 콘티의 `오른손`은 "화면 오른쪽에 있는 손", `왼쪽 구두`는 "화면 왼쪽 구두"로 읽는다.
- 영상 프롬프트는 `[LOCATION_MAP]` 첫 줄에 좌표 문장을 넣는다. 본문의 좌우는 `오른손`·`화면 오른쪽 손`이 아니라 **화면 속 물건으로** 적는다 — 예: 신발장 쪽 손, 우산꽂이 쪽 손. 근거: `film-decisions.md` §8("화면 오른쪽 손"은 네 번 연속 인물 자신의 오른손으로 읽혔다).
- 이미지 프롬프트(영문)는 머리말에 `LEFT and RIGHT in this prompt are always SCREEN directions, never the character's own left or right.`
- 같은 동작이 카메라가 반대편인 두 컷에 걸치면 화면 기준 좌우가 바뀐다. 그 경우는 콘티에서 확인하고 추측으로 맞추지 않는다.
### 3.2 한 생성 안에 카메라가 둘 이상일 때 — 카메라마다 방향을 적는다 (영상, 참고 사례)
 
하드컷으로 카메라 위치가 바뀌면 같은 문이 한 숏에서는 화면 왼쪽, 다음 숏에서는 화면 오른쪽에 온다(`production-os-prompt-guide.md` §10 — 화면 좌우는 그 숏에만 해당한다). 모델에게 맡기지 않고 **카메라 위치마다** 적는다.
 
```
[문]은 방의 [왼쪽 벽]에 있다. (장소 기준)
[설치 숏]: 카메라는 [인물]의 어깨 뒤에서 [거울]을 본다. [문]은 화면 왼쪽 끝에 있다.
[클로즈업]: 카메라는 [문] 쪽에서 [인물]을 거의 정면으로 본다. [문]은 화면 오른쪽 밖에 있다 — 그래서 [인물]은 화면 오른쪽으로 돌아본다.
```
 
문·서랍처럼 방향이 있는 물건은 카메라 기준 좌우 대신 **옆 물건 기준**으로 쓴다: "손잡이는 [화장대]에 가까운 쪽, 경첩은 먼 쪽". `film-decisions.md` §8(좌우는 화면 속 물건으로)과 같은 방향이다.
 
근거: The Prompter 분장실 장면에서 문 경첩을 "카메라 기준 왼쪽 가장자리"로 쓴 판을 세 번 생성한 뒤, 물건 기준 + 카메라별 방향으로 바꾼 판이 채택됐다(분석 §5.4).
이 영화는 한 생성에 카메라 하나가 기본이라(`production-os-prompt-guide.md` 38.6) 자주 쓰지 않는다. 한 생성 안에 컷이 들어갈 때만 쓴다. 서로 다른 두 컷 사이의 좌우는 §3.1 마지막 줄대로 콘티에서 확인한다.
 
### 3.3 거울·유리처럼 비치는 면 — 무엇이 비치는지 적는다 (참고 사례)
 
비치는 면이 화면에 있으면 무엇을 비출지 모델이 정하게 두지 않는다. **비치는 것과 비치지 않는 것**을 함께 적는다.
 
```
거울은 [인물]과 뒤의 흐린 방만 비춘다. [문]과 [다른 인물]은 거울에 비치지 않는다.
```
 
사람 수는 실제 인물과 비친 얼굴을 따로 센다(`production-os-prompt-guide.md` §11).
근거: The Prompter 분장실 장면. 첫 판(#63)은 거울 속 눈으로 문을 보게 썼고, 다음 판(#18)부터 이 문장이 들어가 이후 분장실 프롬프트에 모두 남았다(분석 §5.5).
이 영화의 씬에 거울·유리·TV 화면이 있는지는 콘티에서 확인한다.
 
---
 
## 4. 랜드마크 근접 앵커 — 위치는 거리로 쓴다
 
AI는 "옆에", "근처에", "앞에"를 거의 못 지킨다. 인물이 랜드마크에서 3미터 떨어진 그림이 나온다.
 
**약함**
 
- 식탁 근처에 선다
- 좌판 앞에 앉아 있다
- 게시판 쪽을 본다
- 공중전화 주변
**강함**
 
- 식탁에서 1미터 안, 한 손이 식탁 모서리에 닿아 있다
- 좌판 뒤 낮은 플라스틱 의자에 앉아, 무릎이 좌판 판자에 닿는다
- 게시판에서 팔 하나 거리, 코끝이 포스터에서 40cm
- 수화기를 귀에 댄 채 가게 외벽에 어깨가 닿아 있다
**접촉이 있으면 접촉을 쓴다.** 손이 어디 닿았는지가 가장 강한 앵커다.
접촉이 없으면 미터를 쓴다. 형용사는 마지막 선택지다.
 
---
 
## 5. 첫 프레임 점유 잠금 (영상 전용)
 
영상 생성은 방치하면 **빈 방으로 시작해서 인물이 걸어 들어오는** 그림을 만든다.
이 영화의 컷 대부분은 그렇지 않다.
 
```
첫 프레임에 필요한 인물이 이미 정위치에 있다.
빈 설정 프레임 없음. 인물이 늦게 등장하지 않는다.
공간 관계가 1프레임에서 바로 읽힌다.
```
 
빈 프레임으로 시작해야 하는 컷은 **콘티가 명시한 경우에만** 그렇게 쓴다.
 
### 5.1 퍼스트 프레임 이미지 (사용자 확정 · 2026-09-24)
 
- 컷의 이미지 프롬프트는 **그 컷 영상의 0:00 상태**를 만드는 퍼스트 프레임이다. 썸네일 시점(`SHOT.moment`)이 아니다.
- 15초를 넘어 두 번에 나눠 생성하는 컷은 **생성 1/2의 0:00**만 이미지로 만든다. 생성 2/2는 1/2의 **지정 프레임**을 `start_image`로만 계승한다(`film-decisions.md` §3).
- 썸네일보다 **콘티 텍스트**(desc·note·카메라·대사)가 우선한다. C#4는 예외다(`film-decisions.md` §3).
---
 
## 6. 레퍼런스 권한 — 다섯 단계
 
장소 사진을 넣을 때 "참고해"라고 쓰지 않는다. **무엇을 통제하는지 단계로 선언한다.**
 
| 권한 | 영어 표현 | 통제하는 것 |
|---|---|---|
| Exact photograph | `the exact same photograph` | 카메라·프레이밍·기하까지 잠금 |
| Same location | `the exact same room / location` | 장소 정체성. **새 시점 허용** |
| Material register | `the same building's material register` | 재료·창호·조명 태도만 |
| Layout only | `only for the LAYOUT` | 문·창·가구의 상대 위치만 |
| Element only | `only for [element]` | 명명한 요소 하나만 |
 
이 영화의 컷 생성은 거의 전부 **Same location**이다. 장소는 지리와 재질을 대고, 카메라는 컷이 정한다.
 
### 보조 참조는 `only`로 좁힌다
 
참조가 둘 이상이면 참조마다 역할을 한 명사구로 줄이고, 가져오면 안 되는 것을 적는다. 카메라 권한의 수는 지침 4항대로다.
 
```
REFERENCE AUTHORITY:
- <<<집_v2>>> is the exact same location. It controls geography, materials, landmarks and light direction.
- <<<아내>>> controls only the woman's face, hair and wardrobe.
- <<<봉지>>> controls only the black plastic bag's shape, material and state.
 
DO NOT TRANSFER:
- From <<<아내>>>: the studio backdrop, its lighting, its framing or its pose.
- From <<<봉지>>>: its background, surface or camera angle.
 
PRIORITY:
If the references conflict, <<<집_v2>>> controls the space and the light;
the character reference controls identity and wardrobe only.
Camera and shot size are defined below and override every reference.
```
 
**충돌 규칙은 한 줄로 닫는다.** 안 적으면 모델이 임의로 고른다.
 
**인물 레퍼런스와 충돌하면 인물이 이긴다.** 얼굴·의상·체형은 장소 사진이 못 건드린다.
반대로 조명과 공간은 인물 시트가 못 건드린다 — 시트의 스튜디오 조명이 컷에 따라오면 안 된다.
 
### "앵글은 상속하지 않는다"와 `WITHOUT reframing`은 다른 문장이다
 
쓰임은 지침 2항이다. 권한 선언의 전체 문장은 `Do not inherit its camera angle, framing or composition`(컷 생성에도 쓴다)이고, 함께 붙이는 CAMERA 블록은 새 카메라의 위치·높이·방향·거리를 적는다.
 
### 자주 나는 사고와 교정 문장
 
| 사고 | 교정 |
|---|---|
| 보조 참조의 카메라까지 복사됨 | `Reference 2 controls only [element]. Do not transfer its camera, framing, lighting or surroundings.` |
| 레이아웃 참고가 사진 복제가 됨 | `Use the reference only for the relative placement of [anchors]. Do not copy its framing, materials or lighting.` |
| 두 참조가 같은 영역을 다르게 지시 | `If the references conflict, <<<A>>> has authority over [domain]. <<<B>>> only over [domain].` |
 
### Higgsfield 요소와 참조 이미지
 
- `@이름`으로 부를 수 있는 것은 Higgsfield에 **요소로 등록된 것**뿐이다. 요소 이름과 `embeddedAssetData.json`의 `tag`를 같게 둔다.
- 요소가 없으면 `[참조 이미지] <ID> <이름>`으로 적고 이미지를 직접 첨부한다. 요소 이미지가 JSON의 `image`와 다르면 요소(Higgsfield 저장본)를 참조로 쓰고 JSON 주소를 그 이미지에 맞춘다(`film-decisions.md` §8 · 미결 #13).
- 프롬프트 안의 참조 표기(`<<<image_1>>>`, `Reference image 2`, `<<<UUID>>>`)는 **실제로 첨부·연결된 순서와 대상**에 맞춘다. 원문 모음은 네 가지 표기를 섞어 쓴다 — 한 프롬프트 안에서는 하나로 통일한다.
- **요소 이미지를 바꾸면 프롬프트 속 그 요소의 설명문도 새 이미지에 맞게 고친다.** 참조판만 바꾸고 옛 설명문을 두면 참조와 텍스트가 어긋난다. The Prompter는 복도 장소판을 바꾼 판(#21)에서 옛 설명문을 그대로 두었다가, 다음 판(#53)에서 새 판의 문·벽등·창에 맞게 다시 썼다(분석 §5.5). `film-decisions.md` §8(이미지 정본은 Higgsfield 에셋)과 짝이다.
---
 
## 7. 시대는 색이 아니라 물건으로 쓴다
 
이 영화의 확정 지침: **과거를 노랗게도 세피아로도 만들지 않는다.**
과거는 채도를 아주 약하게만 내린다. 그러면 시대는 무엇으로 드러나는가 — **물건, 재질, 글자, 마감**이다.
 
| 시대 | 장소에 박아 넣을 물건 |
|---|---|
| 1970년대 후반 시골집 (연도 미지정 — §13.1, `film-decisions.md` 미결 #15) | 앉은뱅이 상, 장판 바닥, 문살 창호지, 백열등 하나, 풍로 |
| 1980년 산동네 | 슬레이트 지붕, 시멘트 계단, 연탄, 알루미늄 새시 |
| 1980년 대학 | 나무 창구, 등사 전단, 녹색 칠판, 형광등, 손글씨 게시물 |
| 1980년 시장 | 함석 차양, 스티로폼 상자, 고무 대야, 저울, 손글씨 가격표 |
| 1980년 교통 | 비둘기호 객차, 인조가죽 좌석, 철제 기둥, 동전식 공중전화 |
| 현재 | 무광 주방 수납장, 스테인리스 싱크, 원목 식탁, 패브릭 소파 |
 
**한글 글자** — 간판·포스터·가격표·서류는 "hand-lettered signage, text not legible" 로 처리한다.
실제 문구를 따옴표로 넣으면 모델이 쓰려고 한다. 실제 소품의 글자는 미술팀이 만든다.
 
---
 
## 8. 광학 — 카메라와 렌즈
 
이 영화는 **전 컷 고정 카메라, 전 컷 아이레벨**이 기본이다(콘티가 팬·틸트를 명시한 컷만 예외).
그래서 감정은 렌즈와 거리로 조절된다.
 
영상 렌즈 표(mm→대각 화각)와 내용-화각 정합·관찰 가능한 결과는 `production-os-prompt-guide.md` 부록 H 38.1~38.3에 있다.
 
**쓰지 않는 표현**: extreme wide-angle, ultra wide, f/1.4, ISO, "wide shot"을 렌즈 지시로 쓰기.
 
### 8.1 이미지와 영상은 렌즈 표기가 다르다
 
- **정지 이미지(Nano Banana 계열)**: 장비명·필름 스톡이 룩 프리셋처럼 작동한다. 이 영화의 표준 — 현재 실내 `ARRI Alexa LF, Cooke S4 <mm>, Kodak Vision3 500T 5219`, 과거 낮 `… Kodak Vision3 250D 5207`. 콘티 mm를 그대로 쓴다.
  (과거 밤·저녁 실내 — 씬 6 시골집 저녁, 서울 자취방 밤 — 의 스톡은 아직 정하지 않았다. 정해지면 여기 적는다.)
- **영상(Seedance 계열)**: 장비명은 듣지 않는다. 대각 화각(도)과 관찰 가능한 결과를 쓴다.
같은 컷이라도 **이미지판과 영상판에서 렌즈를 다르게 적는다.** 콘티의 mm는 그대로 둔다.
 
### 8.2 카메라 높이와 방향은 함께 쓴다
 
"아이레벨"은 카메라 **높이**다. 높이 1.5m에서 발·신발을 담는 인서트처럼 콘티 구도가 아래를 향해야만 성립하면,
높이와 **고정된 아래 방향**을 함께 적는다. 높이만 쓰고 구도를 맡기면 모델이 수평으로 찍어 발이 잘린다.
 
---
 
## 9. 장소 목록은 대장에 있다
 
장소의 ID·씬 매핑·뷰·재사용 관계는 **`embeddedAssetData.json`**이 정본이고,
JSON이 담지 못하는 문장(MASTER GEOMETRY·LIGHT LOCK)과 계보·검수 기록은 **`location-assets.md`**에 있다.
 
---
 
## 10. 고등어가 보이는 장소
 
확정 지침이다. 고등어는 **실제로 존재하는 장면에서만** 보여준다.
빈 유학 사무실이나 강의실에 상징적으로 끼워 넣지 않는다.
 
### 씬 1 봉지·고등어 상태표 — 현재 콘티 기준 (2026-09-24)
 
| 컷 | 상태 |
|---|---|
| C#2 | 검은 비닐봉지가 영훈의 화면 오른쪽 손에 들려 있다(영상 본문에는 물건 기준으로 — §3.1). 안에 신문지에 싼 생고등어 **두 마리** |
| C#3 | 봉지를 들고 들어와 식탁 상판에 **한 번** 내려놓고 손을 뗀다. 봉지는 열리지 않았다 |
| C#4 | 아내가 식탁에서 봉지를 열어 안을 들여다본다. 고등어는 봉지 밖으로 나오지 않는다 |
| C#5 | 봉지는 화면에 없다 |
| C#6 | 아내가 열린 봉지를 들어 주방으로 가져간다 |
| C#8 | 팬 위에서 고등어 **한 마리**가 구워진다. 봉지·신문지는 없다 |
| C#9 | 식탁 위에 봉지가 없다. 아내가 주방 조리대에서 조리 중 |
 
**봉지의 물성 (사용자 확정)** — 두 마리의 무게 때문에 봉지는 빵빵하게 부풀지 않고 아래로 처진다.
손잡이에 들리면 바닥 쪽이 늘어지고, 상판에 놓이면 모양이 조금 무너져 옆으로 퍼진다. 공기로 부푼 봉지, 각이 선 봉지는 금지.
 
| 장소 | 상태 |
|---|---|
| 현재 집(씬 1) | 위 표 |
| 시골집(씬 6) | 상 위 구이 한 마리 |
| 시장 좌판(씬 9) | 고무 대야와 신문지 위, 생물 |
| 현재 집(씬 10) | 식탁 위 구운 고등어 한 상 |
 
---
 
## 11. 붙여넣기용 프롬프트 블록은 대장에 있다
 
실제 컷에 복사해 넣는 블록(REFERENCE / MASTER GEOMETRY / LIGHT / CAMERA / BLOCKING)과
확정된 뷰별 기록은 **`location-assets.md`**에 있다.
 
---
 
## 12. 원문 20개에 반복되는데 템플릿(`location-templates.md`)이 규칙화하지 않은 것
 
장소 마스터판마다 반복되는 **마감 문법** 여섯 개. 이 영화의 빈 공간 레퍼런스와 퍼스트 프레임 이미지에 그대로 쓴다.
 
### 12.1 팔레트 비율 — 80 / 15 / 5
 
색을 형용사로 쓰지 않고 **비율로 배분**한다.
 
```
Palette of roughly 80% [주조] — [구체 항목 나열] — 15% [보조] — 5% [악센트].
```
 
```
현재 집  : 80% warm neutral — pale cabinets, ivory walls, light oak floor
           — 15% the dark wood table and the fabric sofa
           — 5% the pendant's warm glow
시골집   : 80% muted browns and ochres — vinyl floor, paper screens, timber
           — 15% the dark corners of the room
           — 5% the single bare bulb
죽도시장 : 80% wet greys — tin awnings, concrete, styrofoam, ice
           — 15% the rubber basins and blue crates
           — 5% the mackerel's blue-silver backs
```
 
5% 악센트를 색으로 쓰면 시대가 색으로 설명되지 않으면서도 화면이 죽지 않는다.
 
### 12.2 `Real material truth:` 블록
 
`photorealistic` 한 단어로는 아무 일도 일어나지 않는다. **증거를 나열한다.** 마모의 **위치까지** 적는다.
 
```
Real material truth: honed stone with fine tonal variation, brushed metal, faint reflections.
Real aged surfaces: scuffs on the painted walls at chair height, worn linoleum tracks,
fingermarks around the door handle, powder dust on the table.
```
 
### 12.3 단일 광원 논리 선언
 
광원을 나열하는 데서 그치지 않고 **논리를 한 문장으로 닫는다.**
시골집은 `A single bare bulb overhead; everything falls off into the corners`,
현재 집은 `Pendant over the table as the only key; the kitchen is never cooler than the room`.
 
### 12.4 `Empty deserted [place], still air.`
 
인물이 없는 빈 공간 레퍼런스에는 이 문장을 그대로 쓴다. `no people`보다 강하게 듣는다.
 
### 12.5 인물 없이 스케일 주기
 
`A person standing here would be small in all this space.` / 좁은 공간은 `A person standing here would fill most of the room.`
 
### 12.6 구도를 부정으로 닫는다
 
사선 구도(`the room read at an angle, not square-on`)와 `Rule of thirds composition.`은 **빈 공간 레퍼런스판에만** 쓴다.
실제 컷(퍼스트 프레임 포함)은 콘티의 앵글을 따른다.
 
### 12.7 원문 재독해 — §14.4가 놓친 여섯 가지 (2026-09-24)
 
1. **일점 투시와 Rule of thirds는 같이 쓰지 않는다.** 원문 4는 `strict one-point perspective`와 `Rule of thirds composition.`을 한 프롬프트에 함께 쓴다. 소실점을 가운데 두라는 말과 3분할에 두라는 말이 부딪친다.
   포항역 플랫폼(LC-015), 객차 통로(LC-016), 대학 복도(LC-006)처럼 **축이 긴 공간**은 `Rule of thirds`를 빼고 소실점 위치를 직접 쓴다.
2. **다른 장소로 문장을 옮기면 명사가 샌다.** 원문 10은 황동 벽등이 달린 1930년대 카펫 복도인데 `the light strips … converging`이 들어 있다. 원문 4 현대 복도의 문장이 복사되며 남은 것이다.
   §14.3의 형제판 규칙은 **같은 장소 안에서만** 성립한다. 현재 집 블록을 시골집이나 자취방으로 옮길 때는 광원·재질·가구 명사를 한 줄씩 다시 검사한다.
3. **실내 광원은 발광을 제한한다.** 원문 6·7·19·20: `lit but do NOT glow: no halo, no bloom, no light spilling onto [surfaces]`.
   이 영화의 백열등 하나, 형광등, 공중전화 불빛, 탁상등이 LIGHT LOCK을 깨지 않게 할 때 쓴다. 광원 논리(§12.3)의 짝이다.
4. **군중은 얼굴 없이.** 원문 12: `seen from behind … no faces visible anywhere, dissolving into darkness toward the edges`.
   시장 행인·상인, 객차 승객, 강의실 학생처럼 **대본상 얼굴이 필요 없는** 인원에 쓴다. AI 얼굴 품질 문제와 실존 인물을 닮는 위험을 함께 줄인다. 대본에 이름이 있는 인물(아줌마, 손님, 단속반)에는 쓰지 않는다.
5. **형태는 화면에 보이는 모양으로 쓴다.** 원문 6: `reads as a TALL NARROW RECTANGLE, clearly TALLER THAN IT IS WIDE`. 3D 사실("세로로 돌렸다")이 아니라 그 카메라에서 **투영된 결과**를 쓴다.
   처진 봉지(`its bottom sags lower than its handles`), 도마·밥상의 방향처럼 형태가 자꾸 틀리는 물건에 쓴다.
6. **"거의 읽히지만 읽히지 않는" 글자.** 원문 7: `Small, precise, … almost readable but not quite.`
   한글 가격표·게시물·구인 쪽지에 `text not legible` 대신 시도해 볼 수 있다. **근거 원문 1건이라 규칙이 아니다** — 결과를 보고 §7에 올릴지 정한다.
---
 
## 13. 템플릿에 없는데 이 영화에 필요한 두 가지
 
### 13.1 시대 장소를 참조 없이 새로 만들기
 
```
1. 카메라   : 샷 크기 + 높이 + 방향 (사선, not square-on — 축이 긴 공간은 §12.7-1)
2. 주 랜드마크 : 가장 먼저 눈에 들어오는 것 하나. 그것이 광원이면 더 좋다
3. 벽·바닥·문·창 : 재료와 색
4. 가구·집기  : 기능 순서대로, 위치와 함께
5. 시대 표식  : 물건으로. 색으로 쓰지 않는다
6. 마모     : 위치까지 (§12.2)
7. 비어 있음  : Empty deserted ~, still air
8. 팔레트   : 80 / 15 / 5 (§12.1)
9. 광원 논리  : 한 문장 (§12.3)
10. 마감    : 촬영 스펙 + 시대 잠금 + 무문자 + Rule of thirds (§14.6)
```
 
**시대 잠금 문장을 반드시 넣는다.** 연도는 콘티 SC의 `chronology`를 따른다. 한 줄로 뭉뚱그리지 않는다.
 
| 데이터 씬 | 콘티 chronology | 시대 잠금 문장 |
|---|---|---|
| 1, 10 | 현재 저녁 (같은 날) | `Present day, South Korea.` |
| 2, 3, 4 | 1980년 초가을 | `Early autumn 1980, South Korea. Nothing more recent anywhere in frame.` |
| 5, 7, 8 | 1981년 1~2월 겨울 | `Winter 1981, South Korea. Nothing more recent anywhere in frame.` |
| 6 (시골집) | 중학생 시절 회상 | 연도 미지정 — `character-sheet-guide.md` §12는 15세 영훈을 1970년대 후반으로 둔다. 확정 전에는 `Late 1970s, rural South Korea.` 를 쓰고 표시한다 (`film-decisions.md` 미결 #15) |
| 6 (자취방) | 1981년 겨울 | `Winter 1981, South Korea. …` |
| 9 | 1981년 여름 (9-9~9-11만 중학생 시절 회상) | `Summer 1981, South Korea. …` / 회상 컷은 씬 6 시골집과 같은 연도 |
 
같은 에셋을 두 시대에 쓰는 곳(LC-008 시골집: 씬 6 회상 / 씬 8 1981 겨울, LC-003 골목: 씬 2 1980 가을 / 씬 8 1981 겨울)은 STATE로 가른다.
 
### 13.2 장소 + 인물 + 소품을 한 컷에 합치기 (퍼스트 프레임 이미지)
 
> 이 영문 템플릿은 **Higgsfield에 직접 보내는 생성용**이다. 콘티 `image:N`에 저장하는 형식이 아니다(지침 「항상」, `01_콘티데이터-구조.md` §2, `film-decisions.md` 미결 #5).
 
```
FIRST FRAME of a film shot — the exact state at 0:00 of the video … LEFT and RIGHT are SCREEN directions.
 
Using <<<집_v2>>> as the exact same location, generate a new view. The camera …
This is a newly observed direction of the same physical room, not a horizontal mirror of the reference.
 
REFERENCE AUTHORITY
- <<<집_v2>>>  : geography, materials, landmarks, light direction
- <<<아내>>>   : face, hair, wardrobe only — Use the person in this reference. Same face, same bone structure,
                 same hair, same wardrobe. Change only the pose, framing, location and lighting.
- <<<봉지>>>   : the bag's shape, material and state only
DO NOT TRANSFER: the character sheet's backdrop, studio lighting, pose or framing.
PRIORITY: … the CAMERA block overrides every reference.
 
CAMERA        : [콘티의 높이·방향·거리·샷 크기 + 장비·필름 스톡]
BLOCKING      : [거리와 접촉으로] (§4), 좌우는 화면 기준
ACTING        : [상태로. acting-guide.md]
WARDROBE      : [character-sheet-guide.md §12 문장 그대로]
마감           : Nothing else / 팔레트 / material truth / 광원 논리 / 시대 잠금
```
 
**인물은 기존 앵커에 배치한다** — 새 위치를 발명하지 않는다. `standing within half a metre of the table, one hand on the knot` 처럼.
 
### 13.3 근거가 부족해 규칙으로 만들지 않은 것
 
| 작업 | 이 영화에서 | 대응 |
|---|---|---|
| 조명·시간대만 변경 | 씬 1 저녁 ↔ 씬 10 저녁(같은 날) | 둘 다 실내 인공광이라 사실상 동일. 부분 근거: 원문 14 CHANGE 3(아침빛), 원문 8(조명 체계 교체) — 둘 다 다른 변경과 묶여 있어 단독 규칙은 아니다 |
| 사물을 A→B로 이동 | 봉지가 식탁 위치를 옮김 | 이동 대신 **뷰를 나누거나** `location-templates.md` §03의 제거+추가 두 단계로 |
| 점유 인원만 변경 | 시장 통로의 행인 | 원문 12 방식(기존 앵커 + 얼굴 없음, §12.7-4)으로 가능 |
 
---
 
## 14. 원문 정밀 독해 — 베낄 구조와 베끼면 안 되는 것
 
### 14.1 마스터판의 13블록 순서
 
| # | 블록 | 이 영화에서 |
|---:|---|---|
| 1 | 참조·권한 + 생성 선언 | `Using <<<...>>> as the exact same location, generate ...` |
| 2 | 카메라·구도 | 샷 크기 + 높이 + 방향. 레퍼런스판은 사선 |
| 3 | **지배 요소** | 가장 먼저 눈에 들어오는 것 하나 |
| 4 | 방향별 벽 | `At the FAR END` / `The RIGHT wall` / `At the LEFT` |
| 5 | 바닥·천장·광원 배치 | |
| 6 | **부정 목록** | `Nothing else: no ...` |
| 7 | 비어 있음 | `Empty deserted ~, still air.` |
| 8 | 팔레트 80/15/5 | §12.1 |
| 9 | `Real material truth:` | §12.2 |
| 10 | 광원 논리 한 문장 | §12.3 (+ 발광 제한 §12.7-3) |
| 11 | 촬영 마감 | 이미지판은 장비·필름 스톡 (§8.1) |
| 12 | **시대·장르 잠금** | 씬별 연도 (§13.1 표) |
| 13 | 구도 마감 | `Rule of thirds composition.`(레퍼런스판만. 축이 긴 공간은 빼고 소실점을 쓴다) |
 
**3번(지배 요소)이 빠지면 화면이 평평해진다.**
 
### 14.2 방향 대문자 앵커와 `Nothing else:`
 
**대문자 방향 앵커**로 무엇이 어느 쪽인지 못 박는다 — `At the FAR END …`, `The RIGHT wall …`, `At the LEFT …`.
MASTER GEOMETRY에서는 **어느 시점 기준의 방향인지**를 괄호로 먼저 밝힌다(예: `directions as seen from the living-room window end, looking toward the kitchen`).
 
**`Nothing else:` 로 물건 목록을 닫는다.**
 
```
시골집   Nothing else: no modern appliance, no plastic container, no printed packaging,
         no wall calendar with legible text, no electric light other than the single bulb.
시장     Nothing else: no modern signage, no plastic crates in current colours,
         no legible Korean text, no vehicles, no mobile phones.
현재 집  Nothing else: no decorative styling, no display shelves, no artwork,
         no visible brand logos.
```
 
### 14.3 형제판 규칙 — 카메라만 다르고 나머지는 같은 문장
 
> **형제 뷰의 프롬프트는 부모 뷰의 프롬프트에서 CAMERA 블록과 전·중·후경 블록만 바꾼 것이어야 한다.**
> MASTER GEOMETRY, LIGHT, 팔레트, material truth, 시대 잠금, 마감은 **글자까지 같게 둔다.**
 
자식끼리 물려 쓰지 않는다. 승인된 부모 하나에서 각자 갈라져 나온다.
**다른 장소로 옮길 때는 이 규칙이 거꾸로 위험하다** — §12.7-2.
 
### 14.4 그대로 베끼면 사고 나는 원문 다섯
 
1. **원문 10** — `WITHOUT reframing`으로 카메라를 잠그고 같은 문장에서 180도 돌린다. 연속성 문장(`same one-point perspective, same corridor width …`)만 살리고 잠금 어투는 버린다. 역방향은 원문 4(`the camera now stands at the far end`)를 본으로.
2. **원문 6·16** — 보조 참조에 권한도 제외도 없다. 두 참조 이상이면 `location-templates.md` §01의 템플릿을 쓴다.
3. **원문 5** — 변경 개수를 안 세고 lens를 안 잠근다. LOCKED EDIT 본보기는 원문 12·18.
4. **잠금 문장에서 lens가 빠지는 게 다수다.** 표준은 lens 포함 + `zero reframing, zero recentering, zero zoom`.
5. **원문 17** — 짧아서 통한 게 아니라 변경이 사소해서 통했다. 제거 후 표면 처리(`no residual shadow, indentation, fragment or duplicate`)를 덧붙인다.
원문 1~20에는 **모델·부모·성공 여부 기록이 없다.** "검증 원문"은 존재가 확인됐다는 뜻이지 결과가 좋았다는 뜻이 아니다.
 
### 14.5 잠금 문장 표준형
 
LOCKED EDIT:
 
```
Edit <<<image_1>>> WITHOUT reframing: camera position, camera height, angle, lens,
framing, horizon line and perspective are LOCKED — zero reframing, zero recentering,
zero zoom — this is the same photograph with [N] change(s) only.
```
 
`[N]`은 보통 `one`이다 — 한 생성에 한 가지(지침 #6). 떼면 성립하지 않는 두 변경(예: 켠 화면과 그 화면빛)일 때만 `two`.
 
DERIVED VIEW — **`WITHOUT reframing`이 없다.**
 
```
Using <<<image_1>>> as the exact same room — same [재료·랜드마크·광원 논리] — generate
[새 시점]. The camera [이동 또는 제자리 회전 중 하나], at [높이], looking [방향].
This is a newly observed direction of the same physical room, not a horizontal mirror
of the reference.
```
 
### 14.6 이 영화용 마감 세트 — 그대로 복사
 
**과거**
 
```
Empty deserted [place], still air.            ← 빈 공간 레퍼런스판만
Palette of roughly 80% [주조] — [항목] — 15% [보조] — 5% [악센트].
Real aged surfaces: [마모의 위치까지].
[광원 논리 한 문장].
Photorealistic cinematic film still, ARRI Alexa LF, Cooke S4 [콘티 mm], Kodak Vision3 250D 5207,
organic film grain, soft falloff, crisp natural detail.      ← 낮 기준. 밤·저녁 실내 스톡은 §8.1 미정
[§13.1 표의 시대 잠금 문장]
Hand-lettered Korean signage, text not legible. No legible text anywhere.
```
 
**현재**
 
```
Empty deserted room, still air.               ← 빈 공간 레퍼런스판만
Palette of roughly 80% warm neutral — [항목] — 15% [보조] — 5% [악센트].
Real material truth: [재질 증거, 마모의 위치까지].
[광원 논리 한 문장].
Photorealistic contemporary Korean apartment interior, ARRI Alexa LF, Cooke S4 [콘티 mm],
Kodak Vision3 500T 5219, crisp natural detail, cinematic film still quality. Present day, South Korea.
No brand logos, no legible text anywhere.
```
 
과거판과 현재판은 **색이 아니라 질감으로** 가른다 — 과거판은 `organic film grain`을 명시하고 현재판은 명시하지 않는다.
 
---
 
## 15. 보내기 전 점검
 
지침의 1~9항(「이미지 생성 전에 매번 확인하는 것」)과 그 아래 렌즈 줄, 「항상」의 좌우·0:00·한글 글자 규칙에 더해 아래를 본다.
 
- [ ] 좌표 줄이 있는가 — 영상 본문의 좌우를 `오른손`이 아니라 화면 속 물건으로 적었는가(§3.1)
- [ ] 이 컷의 장소 정보가 좌표 + 네 줄(Camera / 깊이 / Light / 필요시 Path)을 넘지 않는가
- [ ] 인물 위치가 미터나 접촉으로 쓰였는가 — "근처에"가 남아 있지 않은가
- [ ] 카메라가 어느 쪽에 있는지 썼는가 — 같은 씬 안에서 축을 넘지 않았는가
- [ ] 첫 프레임에 누가 있는지 지정했는가(§5)
- [ ] 참조 표기가 실제 첨부 순서·요소와 맞는가(§6)
- [ ] 마스터판이면 13블록이 순서대로 있는가(§14.1)
- [ ] 축이 긴 공간에서 `Rule of thirds`를 뺐는가
- [ ] MASTER GEOMETRY를 토씨 하나 바꾸지 않고 붙였는가
- [ ] 시대를 색이 아니라 물건으로 썼는가
- [ ] 고등어가 실제로 있어야 할 장소인가 — 마릿수와 봉지 물성이 §10과 맞는가
- [ ] 콘티가 명시하지 않은 카메라 움직임을 넣지 않았는가
- [ ] 한 생성에 카메라가 둘 이상이면 카메라마다 고정 물건의 화면 방향을 적었는가(§3.2)
- [ ] 거울·유리 같은 반사면이 있으면 무엇이 비치고 무엇이 안 비치는지 적었는가(§3.3)
- [ ] 요소 이미지를 바꿨다면 프롬프트 속 설명문도 새 이미지에 맞췄는가(§6)