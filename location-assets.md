# 장소 에셋 대장 — 「어머니와 고등어」
 
> **정본은 `~/Documents/LucianWork_Page/pages/어머니와_고등어_Main_V3.1.data/embeddedAssetData.json`이다.**
> 에셋 ID·태그·이미지·상태·컷 배정은 전부 거기 있고, 둘이 어긋나면 JSON을 따른다(이미지는 `film-decisions.md`(이하 FD) §8과 어긋남 — 미결 #13). 구조는 `01_콘티데이터-구조.md`.
> 이 문서는 JSON이 담지 못하는 것만 보관한다 — **MASTER GEOMETRY·LIGHT LOCK 영문 문장, 계보의 이유, 부모 job·요청/처리 모델, 검수 결과, JSON과 어긋난 곳.**
>
> 작성 방법은 `location-guide.md`, 작업별 문법은 `location-templates.md`, 참조 권한 규칙은 `location-guide.md` §6.
> 출처: 2026-09-24 `embeddedAssetData.json`(revision 15) 대조.
 
---
 
## 0. 이 대장이 존재하는 이유
 
한 장소를 사진 한 장으로 대표하면, 다른 각도의 컷을 만들 때마다 **모델에게 카메라를 옮겨 달라고 부탁하게 된다.**
그 부탁은 거의 듣지 않는다. 방향, 높이, 왜곡이 번갈아 틀리고, 하나를 고치면 다른 하나가 틀어진다.
현관 한 컷에 열 번 넘게 생성이 들어간 이유가 그것이다.
 
> 새 축이 필요하면 프롬프트로 카메라를 돌리지 말고, **뷰를 하나 더 확정해서 JSON에 올린다.**
 
---
 
## 1. 이름 — JSON을 그대로 쓴다
 
| 무엇 | 형식 | 예 |
|---|---|---|
| 장소 에셋 | `LC-NNN` (부모, `image: null`) | `LC-002` |
| 뷰 | `LC-NNN-VN` (`parentId`로 부모에 묶임) | `LC-002-V3` |
| 프롬프트·Higgsfield 요소에서 부르는 이름 | JSON의 `tag` **그대로** | `@loc_yh_home_current_v3` |
 
- `LOC_[location]_MASTER_v01` 명명(옛 장소가이드 12)은 이 영화에서 쓰지 않는다. 계보 유형(MASTER·VIEW·STATE…)은 이 문서의 **계보 표에만** 적는다.
### 자식 유형 — 계보
 
```
MASTER  공간 전체와 영구 지리. 그 장소의 정본
CLEAN   MASTER에서 구조·배치만 정리한 판
VIEW    카메라를 바꾼 판 (DERIVED VIEW)
PROP    장소 속 소품을 확대한 판
STATE   조명·점유·소품 상태만 바꾼 판 (LOCKED EDIT)
FIX     단순 오류 제거
```
 
- `VIEW`는 카메라를 바꾸고, `STATE`·`FIX`는 카메라를 잠근다. `STATE`에 카메라 변경이 섞이면 그건 `VIEW`다.
- **승인된 자식만 다음 단계의 부모가 된다.** 폐기한 변형에서 파생하지 않는다.
- 뷰는 **축이 바뀔 때만** 늘린다. 같은 방향에서 거리·사이즈·인물 위치만 다른 건 같은 뷰다.
| 상황 | 새 뷰? |
|---|---|
| 같은 방향, 더 가깝게 / 더 넓게 | ✕ |
| 같은 방향, 인물 위치만 다름 | ✕ |
| 180° 반대에서 봄 | ○ |
| 아이레벨 → 부감 | ○ |
| 다른 방 / 문턱 너머 | ○ |
 
---
 
## 2. 에셋 레코드 양식
 
새 장소를 이 대장에 올릴 때 이 틀을 채운다. ID·태그는 머리 줄로만 쓰고 이미지·상태는 JSON에만 둔다. 나머지를 여기서 확정한다.
 
```
ASSET      LC-NNN   @tag
NAME       (JSON name)
PERIOD     (연도 — 콘티 SC chronology 기준)
SCENES     (데이터 씬 번호)
 
MASTER GEOMETRY   ← 전 컷에 토씨 하나 안 바꾸고 들어가는 3~4문장. JSON description과 어긋나면 안 된다
(영문. 어느 시점 기준의 방향인지 먼저 밝히고, 대문자 방향 앵커로. At the FAR END / The RIGHT wall / At the LEFT.
 미터는 근거가 있을 때만 쓴다)
 
LIGHT LOCK        ← 전 컷 공통 조명 한 문장 (광원 개수·높이·방향·색온도)
 
MATERIALS / LANDMARKS / DEPTH / CAMERA SIDE / FORBIDDEN(`Nothing else:`의 재료)
 
VIEWS    뷰마다 계보·부모 job·요청/처리 모델·검수 결과만 (태그·이미지·상태는 JSON)
```
 
---
 
## 3. LC-001 — 현재 아파트 외경 `@loc_apartment_exterior_dusk`
 
| | |
|---|---|
| PERIOD | 현재 (씬 1·10과 같은 날 저녁) |
| SCENES | 1 (C#1) |
 
집 내부와 **다른 에셋**이다. 같은 에셋으로 묶으면 실내 지오메트리가 오염된다.
 
---
 
## 4. LC-002 — 현재 집 현관·거실·식탁·주방 `@loc_yh_home_current` ★주력
 
| | |
|---|---|
| PERIOD | 현재 (씬 1·10 같은 날 저녁, 같은 조명 — FD §5) |
| SCENES | 1 (C#2–C#10), 10 (C#106–C#110) |
 
### MASTER GEOMETRY — 승인 대기 (FD 미결 #3)
 
확정된 V2 이미지를 보고 아래 **초안**을 고치거나 승인한 뒤에 컷에 쓴다. 그 전까지 컷 프롬프트에 MASTER GEOMETRY를 넣지 않는다.
 
초안 (JSON 설명만 옮김. 미터·높이는 근거가 없어 넣지 않았다):
 
```
A lived-in present-day Korean apartment with ivory walls and a light oak floor,
where the entryway, living room, dining table and kitchen read as one continuous space.
Directions as seen on the floor plan: the living-room window at the bottom, the kitchen
at the top, the entryway at the LEFT. A sofa runs lengthwise along the living room's
RIGHT wall with a low TV on the opposite wall and a floor lamp at the sofa's kitchen-side
end. A dark solid-wood dining table stands against the wall to the right of the kitchen
entrance. An L-shaped counter runs from the sink under the kitchen window to the gas
range on its right.
```
 
### LIGHT LOCK
 
```
A single pendant over the dining table is the key light, slightly above and
in front; soft under-cabinet light fills the kitchen and a floor lamp lifts
the living room. Warm neutral throughout — the kitchen is never cooler or
bluer than the rest of the room.
```
 
`location-guide.md` §3 예시는 주방 보조광을 "후드등"이라고 쓴다. 이 대장의 `under-cabinet light`와 다르다. V2 이미지로 어느 쪽인지 확인하고 하나로 맞춘다.
 
### VIEWS — 계보·job
 
태그·이미지·status는 JSON에 있다. 부모 job은 되돌릴 지점이다. 틀 번호는 `location-templates.md`.
 
| 뷰 | 계보 (틀) | 부모 job | 결과 job | 그 생성에서 한 일 · 모델 | 검수 (이 대장) |
|---|---|---|---|---|---|
| `LC-002-V1` | MASTER — 현관. 문턱 너머라 별도 정본 (§07) | `8b6d25ba` | `5016eb3b` | 재질 정리 → 문 오른쪽 여분 문짝 제거 | ★확정 |
| `LC-002-V2` | MASTER — 거실→주방. 이 집의 정본 | `2ee0fbf7` | `8d39a88e` | 스탠드 조명을 소파 옆 벽으로 이동 | ★확정 |
| `LC-002-V3` | VIEW ← V2 — 180° 리버스 (§05·§06) | 요소 `loc_yh_home_current`(`9fe698af`)를 `<<<UUID>>>`로 물림 | `c9ca0cad` | DERIVED VIEW. 요청 `nano_banana_pro` → 서버 처리 `nano_banana_2`. 2K, 16:9 | 검수 통과 |
| `LC-002-V4` | VIEW ← V2 — 식탁 상판 직부감 (§06) | — | `296ec4c7`(이전 기록) / `fc717b3b`(JSON 이미지) | — | — |
| `LC-002-V5` | VIEW ← V2 — 조리대 근접 (§06) | — | `af6619dc` (이전 기록은 "미제작") | — | — |
| `LC-002-V6` | VIEW ← V2 — 스탠드 옆→식탁·현관 통로 (§06) | — | `c1228ece` | 참조: v2(동일 장소)·평면도(배치만)·v1·v4·v5(요소만) | 검수 대기 |
 
**JSON·Higgsfield와 어긋난 곳**
- V1·V2는 이 대장에 ★확정인데 JSON `status`가 비어 있다(V4·V5도 비어 있다). 확정이면 `★확정`으로 채운다.
- V3: JSON 주소 `c9ca0cad`는 열리지 않았다 → FD §8.
- V4: `296ec4c7`과 `fc717b3b` 중 어느 쪽이 확정인지 미확인 — Higgsfield 저장본으로 확인한다(FD §8).
- V6: JSON `c1228ece` ≠ Higgsfield 저장본 `661a6476` → FD §8. 검수를 통과하면 `★확정`.
**계보의 이유**
- **현관이 V2의 자식이 아닌 이유**: 문턱 한 단 아래의 다른 구역이고 바닥 재질도 다르다. 같은 집이라는 보증은 MASTER GEOMETRY 문장이 잡는다.
- **씬 10의 식탁 인서트는 새 뷰가 아니라 STATE다.** V4(빈 상판)를 물려 `location-templates.md` §02 방식으로 접시를 얹는다. 빈 상판을 확정해 둔 덕분에 씬 1(봉지)과 씬 10(접시)이 같은 뷰를 쓴다.
- V2와 V3는 **소파–주방을 잇는 선 위에서** 앞뒤로 본다. 축을 넘지 않는다.
### V3 프롬프트 기록
 
- 이전 대장에 "교정본"으로 남아 있던 V3 프롬프트는 실제 전송본과 글자까지 같은지 기록이 없고(이전 기록은 지배 요소·`Nothing else:`까지 넣었다고 적었지만 그 문장에는 없었다), 구판 지오메트리(`grey fabric sofa against the far wall`, 주방–식탁 1.5 m)와 폐기된 요소 이름(`<<<loc_home_v2_liv_kit>>>`)을 담고 있어 전문을 싣지 않는다.
- 부모 job·요청/처리 모델·결과 job은 위 표 V3 행.
- 그 문장이 한 일: `WITHOUT reframing` 없이 카메라 관계를 물리적으로 서술하고, 이동형 하나만 고르고, 미러 금지를 넣었다.
- 그 문장의 문제: 렌즈를 영상식(`63 degree diagonal field of view`)으로 적었고(이미지는 장비·필름 스톡 — `location-guide.md` §8.1), 팔레트 `grey tile, off-white walls`가 JSON 설명(아이보리 벽·오크 마루)과 달랐다.
- DERIVED VIEW 템플릿은 `location-templates.md` §05·§06.
### CUT MAP — 데이터에서 보이는 빈칸 (2026-09-24)
 
컷별 뷰 배정은 JSON `assignments`의 `image:N` / `video:C#N`에 있다. 고칠지는 사용자 결정이다.
- C#3: 이미지 V2 / 영상 V6 (FD 미결 #10). V6 설명은 C#3용이라고 적혀 있다. V6 확정 뒤 이미지 배정도 V6으로 맞출지 결정.
- C#10: 카메라가 "거실 창·TV 쪽에서 소파의 영훈을 비껴 보는" 자리인데 V2(거실→주방)에 배정돼 있다.
- 씬 10 영상(C#106–C#110)은 전부 부모 LC-002에만 배정돼 있다. C#107·C#108은 이미지도 부모뿐이다(식탁 짧은 변 쪽 시점의 뷰가 없다).
- 짝 컷 C#9↔C#110, C#10↔C#109(FD §5): 이미지는 넷 다 V2인데, 영상은 C#9·C#10이 V2, C#110·C#109가 부모 LC-002다. 짝끼리 뷰를 맞춘다.
### 붙여넣기용 블록
 
`〔〕` 안만 컷마다 바꾼다. 이 블록을 통째로 컷 프롬프트에 넣는 것은 `location-guide.md` §3(좌표 줄 + 네 줄)과 어긋난다 — FD 미결 #16.
 
```
REFERENCE
〔태그, 예: @loc_yh_home_current_v2〕 is the exact same location.
Use this reference for geography, materials, landmarks and light direction only.
Do not inherit its camera angle, framing or composition.
The CAMERA block below defines the shot and overrides the reference.
 
MASTER GEOMETRY
〔재확정 후 삽입〕
 
LIGHT
〔위 LIGHT LOCK 문장 그대로〕
 
CAMERA
〔콘티 카메라 설명을 물리적으로: 위치 · 높이 · 방향 · 거리 · 샷 크기.
 이미지 → ARRI Alexa LF, Cooke S4 〔콘티 mm〕, Kodak Vision3 500T 5219.
 영상 → 대각 화각(도) + 관찰 가능한 결과 3개.〕
 
BLOCKING
〔전경 / 중경 / 후경. 인물은 거리와 접촉으로. 좌우는 화면 기준.〕
```
 
---
 
## 5. 나머지 장소 (LC-003~022)
 
ID·태그·이름·씬·컷 배정은 JSON에 있다. **뷰 계획은 아직 없다** — 장소마다 콘티 카메라 자리를 모아 축이 몇 개인지 센 뒤 뷰를 연다.
 
카탈로그 자리만 있고 LC 번호·컷 배정이 없는 것: `LOC_UNIV_EXTERIOR`(대학교 외경, 씬 3), `LOC_SCAM_OFFICE_ACTIVE`(유학 사무실 정상 운영, 씬 5), `LOC_MOTHER_FISH_STORE_PAST`(어머니의 옛 생선가게, 씬 9).
 
**같은 에셋을 두 시대에 쓰는 곳** — 가르는 법과 시대 잠금 연도는 `location-guide.md` §13.1(`location-templates.md` §10·§08).
- LC-008 시골집 안방: 씬 6(중학생 시절 회상, 1970년대 후반) (연도 미지정 — FD 미결 #15) / 씬 8(1981년 겨울).
- LC-003 우리네슈퍼 골목: 씬 2(1980년 초가을) / 씬 8(1981년 겨울).
**시장 네 곳(LC-019~022)은 JSON에서 별도 에셋이다.** 한 시장으로 읽히게 하는 일은 MASTER GEOMETRY가 아니라 공통 재료 체계(`location-templates.md` §07의 `material register`)로 한다.
 
---
 
## 6. 확정 절차
 
1. 뷰 하나를 목표로 **인물 없는 빈 공간**을 생성한다. 한 번에 한 축만.
2. 마음에 들면 JSON에 뷰 항목을 추가하거나 갱신하고(필드·수정 순서는 `01_콘티데이터-구조.md` §4·§6), 이 대장 VIEWS 표에 부모 job·요청/처리 모델·검수 결과를 적는다.
3. 마음에 안 들면 그 결과를 참조로 물려 **한 번에 한 가지만** 고친다(카메라 높이 / 왜곡 / 재질 중 하나).
4. 컷 생성은 확정 뷰를 물리고 `MASTER GEOMETRY` + `LIGHT`를 그대로 붙인 뒤 카메라·인물만 쓴다.