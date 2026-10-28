# 연기 프롬프트 가이드
 
**AI 영상 생성에서 인물의 연기를 쓰는 법 / 「어머니와 고등어」 적용**
 
> 씬 번호는 데이터 기준 1~10이다. FD = `claude/film-decisions.md`.
 
15단계 프롬프트의 **Step 9 `CHARACTER_ACTING`**과 영상 생성 프롬프트의 연기 레이어를 채울 때 읽는다.
 
---
 
## 0. 핵심 공리
 
> **연기는 감정의 전시가 아니라 압력 아래의 행동이다.**
 
인물이 무언가를 **원하고**, 무언가가 **가로막고**, 그것을 얻으려 **행동한다**. 감정은 그 싸움의 부산물이지 직접 쓰는 대상이 아니다.
 
| 나쁜 연기 | 좋은 연기 |
|---|---|
| 감정을 보여준다 — "화가 난다" | 목표를 추구한다 — "돈을 돌려받게 만든다". 화는 저절로 생긴다 |
| 자기 차례를 기다린다 | 상대의 말을 매 초 듣고 반응한다 |
| 몸이 대사를 삽화처럼 따라간다 | 몸이 제 삶을 산다. 때로 말과 어긋난다 |
| 한 톤으로 끝까지 간다 | 전술이 바뀔 때마다 리듬이 바뀐다 |
| 대사에서 감정이 켜지고 끝나면 꺼진다 | 상태가 이어진다. 대사 앞의 삶과 뒤의 삶이 있다 |
| 얼굴이 연기한다 — 눈썹, 표정 | 얼굴이 생각한다. 말보다 눈에 먼저 읽힌다 |
 
---
 
## 1. 모든 장면의 다섯 기둥
 
하나라도 없으면 연기가 무너진다.
 
### 1.1 목표 (Objective)
 
**이 장면에서, 지금, 특정 상대에게서** 무엇을 원하는가. 항상 **상대를 향한 동사**로 쓴다.
 
- 좋음: `어머니가 아무것도 눈치채지 못하게 만든다`
- 나쁨: `죄책감을 느낀다` — 상태는 연기할 수 없다
장면 목표 뒤에는 **초목표(super-objective)**가 있다. 이야기 전체에서 원하는 것. 모든 장면 목표는 그쪽으로 가는 한 걸음이다.
 
### 1.2 장애와 대가 (Obstacle & Stakes)
 
무엇이 막는가 — 외부(상대가 반대한다, 증인이 있다, 마감이 두 시간 뒤다) 또는 내부(자존심이 애원을 막는다, 자기 말을 자기도 안 믿는다).
 
**대가:** 실패하면 무슨 일이 일어나는가. 그 답이 인물을 겁먹게 해야 장면이 팽팽해진다.
 
### 1.3 전술 (Tactics)
 
지금 목표를 추구하는 구체적 방법. **행동 동사**로 쓴다 — 압박한다, 구슬린다, 부끄럽게 만든다, 애원한다, 도발한다, 흥정한다, 협박한다, 시간을 끈다.
 
전술이 실패하면 살아 있는 사람은 **전술을 바꾼다.** 한 전술로 장면을 끝까지 가는 것이 죽은 연기다.
 
### 1.4 비트 (Beats)
 
비트는 행동의 최소 단위다. 하나를 원하고 한 방법으로 추구하는 구간.
 
비트가 끝나는 조건: 목표 달성 / 전술 실패 / 새 정보 도착 / 힘의 균형 변화.
 
**비트 변화는 반드시 행동으로 보여야 한다** — 사이, 자세 변화, 말 속도 변화, 시선 이동.
한 장면에 2~4개의 비트 변화가 좋다. 처음부터 끝까지 행동이 안 변하면 그 장면은 평평하게 연기된 것이다.
 
### 1.5 서브텍스트 (Subtext)
 
말하는 것과 실제로 생각·욕망하는 것의 차이. **서브텍스트는 연기하지 않는다.** 거짓 텍스트를 말하면서 진짜 목표를 추구하면 저절로 새어 나온다.
 
장면에 심을 수 있는 표지:
 
- 질문이 아닌 질문
- 같은 것을 다시 묻는다 — 답을 안 믿는다
- 갑작스러운 화제 전환
- 엉뚱한 순간의 농담 — 취약함에 대한 방패
- 너무 짧은 대답. `괜찮심더.` `알았심더.` — 닫힌 문
---
 
## 2. 듣기와 반응 — 품질의 핵심 시험
 
연기는 대사가 아니라 **대사 사이**에 산다. 장면에 써 넣을 수 있는 관찰 가능한 표지:
 
- **반응은 상대의 말이 끝나기 전에 시작된다.** 사람은 문장 중간에 뜻을 알아챈다. 상대 말이 끝날 때까지 무표정이다가 켜지는 것이 죽은 연기다.
- **말보다 생각이 먼저.** 어려운 질문에 답하기 전 미세한 사이가 있다. 무엇을 말할지 정하는 것이 보인다. 일정한 속도의 즉답은 외운 대사다.
- **평가의 순간.** 중요한 일이 벌어지면(소식, 위협, 모욕) 소화할 시간이 필요하다. 영화는 이 평가의 클로즈업으로 산다 — 초점을 잃은 시선, 흔들리는 세계.
- **상대로부터의 전염.** 템포·음량·에너지가 상대에 반응해 변한다. 고함에는 맞고함 또는 의도적 정적으로 **답한다**. 그냥 이어 가지 않는다.
---
 
## 3. 몸 — 인물의 물리적 삶
 
### 3.1 심리 이전의 신체 상태
 
첫 대사 전에 몸이 이야기를 한다. 인물마다 네 가지를 정한다.
 
| 항목 | 양극 |
|---|---|
| 무게중심 | 높음(가슴·턱 — 자신감·공격성·지위) ↔ 낮음(어깨 처짐 — 피로·두려움·순종) |
| 템포 | 빠르고 들쭉날쭉(초조) ↔ 느리고 경제적(통제·위협 — 가장 위험한 사람이 가장 적게 움직인다) |
| 개방도 | 펴진 어깨와 열린 손바닥 ↔ 팔짱, 숙인 고개 |
| 호흡 | 높고 빠름(공황) ↔ 낮고 느림(통제). **호흡이 상태의 가장 정직한 지표다.** 방금 뛴 사람이 고른 목소리로 말할 수 없다 |
 
### 3.2 비즈니스 — 물리적 과업
 
인물은 거의 언제나 **하고 있는 일**이 필요하다. "대화한다"가 아니라 생선을 손질하고, 돈을 세고, 밥을 푸고, 유리를 닦으면서 그 위로 말한다.
 
비즈니스가 하는 일:
- 가짜 연극성을 죽인다 — 손이 진짜 일로 바쁘다
- 리듬을 만든다 — 사이가 행동으로 채워진다
- 서브텍스트를 만든다 — **어떻게** 돈을 세는지가 말보다 많이 말한다
**중단된 행동의 법칙:** 가장 강한 강세는 인물이 하던 일을 **멈출** 때다. 빵을 썰다가 어떤 말에서 멈추면, 그 말이 사건이 된다. 멈춤을 구두점으로 쓴다.
 
### 3.3 거리 — 드라마로서의 프록세믹스
 
인물 사이의 거리는 관계의 가시적 그래프다.
 
| 구역 | 거리 | 의미 |
|---|---|---|
| 친밀 | 0.5m 미만 | 사랑 또는 폭력. 초대 없이 들어오면 공격 |
| 개인 | 0.5–1.2m | 신뢰 |
| 사회 | 1.2–3.5m | 업무, 경계 |
| 공적 | 3.5m 이상 | 소외, 위계 |
 
장면의 드라마는 종종 **거리의 이야기**다. 누가 좁히고, 누가 깨고, 누가 얼어붙는가. **거리 변화 = 비트 변화.**
 
### 3.4 지위 — 보이지 않는 위계
 
지위는 누구인가가 아니라 **무엇을 하는가**다.
 
| 높은 지위 | 낮은 지위 |
|---|---|
| 움직이지 않는 머리 | 부산함 |
| 느린 동작 | 잦은 자기 접촉(얼굴·머리) |
| 긴 응시 | 끊기는 말 |
| 답하기 전의 사이 | 채우는 웃음 |
| 공간을 차지함 | 눈으로 허락을 구함 |
| 남의 물건을 만짐 | |
 
**가장 흥미로운 것은 지위의 파열이다.** 1초 동안 두려움을 보이는 상급자, 갑자기 웃음을 멈추는 하급자. 강한 장면 구조: 높게 들어와 무너지거나, 낮게 들어와 판을 뒤집는다.
 
---
 
## 4. 말
 
- **리듬은 텍스트에 쓴다.** 정확히 전달한다. 빠름 ≠ 뭉개짐.
- **겹침은 정상**이다(말꼬리를 밟는다). 단, 핵심 단어는 깨끗하게.
- **음량 대비:** 가장 무서운 말은 가장 조용하게 한다. 고함은 약자의 화폐다. 장면을 소유한 인물은 음량을 낮추고 모두가 몸을 기울인다.
- **사이는 구멍이 아니라 사건이다.** 안에서 무언가(평가, 결정, 답하지 않기로 함)가 일어날 때만 정당하다.
- **진짜 말에는 쓰레기가 있다** — 끼어듦, 반쯤 들린 말, 반복, 끝나지 않은 문장. 완벽한 문장은 거리의 진실을 죽인다.
---
 
## 5. 눈 — 모든 프로필과 모든 장면에 필수
 
**죽은 눈이 AI 연기의 1번 표지다.**
 
- **미세단속운동과 응시 표적** — 주목하는 대상을 향해 눈이 계속 움직인다. 생각할 때 흘긋 벗어나고, 세부로 훑고, 다시 돌아온다. 한 점에 얼어붙지 않는다.
- **현실적인 깜박임 빈도와 질** — 스트레스에서 빠른 연발, 통제 상태에서 느린 눈꺼풀, 해리의 순간에는 깜박임 후 초점 풀림.
- **살아 있는 캐치라이트** — 눈이 젖어 있고 빛을 받고 살아 있어야 한다.
- **통제된 정지는 선택이지 죽음이 아니다.** 거의 깜박이지 않는 포식자의 평정이라면 깜박임을 드물고 느리고 의도적으로 — 결정이지 정지가 아니다. 그래도 시선은 의도를 가지고 천천히 움직인다.
- **눈이 생각을 이끈다.** 눈이 고개보다 살짝 먼저 대상에 닿는다. 말보다 생각이 눈에 먼저 읽힌다.
- **눈도 비트에 반응한다.** 비트가 바뀌면 깜박임 빈도, 시선의 안정성, 캐치라이트의 온도가 함께 바뀐다.
영문 블록으로 쓸 때:
 
```
continuous naturalistic eye life: micro-saccades and gaze targeting, the gaze drifting and settling rather than locking, realistic blink rate tied to state, live wet catchlights, the eyes reaching the target a beat before the head turns
```
 
---
 
## 6. 마스터 프로필
 
반복 등장하는 인물은 **마스터 프로필 하나**를 갖는다. 그 인물이 **어떻게 행동하는가**에 대한 영구적 진실이다. 한 번 쓰고, 장면마다 다시 쓴다(§8).
 
분량 150~220단어, 흐르는 한 문단, 영어, 전부 관찰 가능하고 촬영 가능하게. 이것은 인물 설계 원본이다(프롬프트에 옮기는 법 → §7).
 
### 템플릿 — 블록 순서 고정
 
```
Character acting as [NAME]. [나이, 체격, 체형, 자세 — 몸은 전기(傳記)의 문서다].
[심리적 엔진을 한 절로 — 그 신체성을 설명하는 내적 동력].
Vocal profile: [음높이/음색, 억양/출신, 속도와 전달 방식, 감정 아래에서 목소리가 어떻게 갈라지거나 변하는지].
Key physical habits and tics: [시그니처 틱 + 발동 조건; 스트레스 틱 + 발동 조건; 은폐 행동 — 느끼는 것을 감추려 무엇을 하는가; 얼굴의 가면과 그것이 깨지는 정확한 조건].
Eye life: [§5].
Walking style: [걸음을 이름 붙여서 — 무게·리듬·발 놓임까지].
However, when [감정적 방아쇠], [변형 — 자세·걸음·얼굴이 어떻게 변하는가].
[선택: 부드러워지는 대상 — 얼굴이 진짜로 풀리는 단 하나의 사람·동물·물건].
```
 
### 각 블록 작성 규칙
 
- **관찰 가능한 행동만.** 모든 내적 상태에 몸의 표지가 있어야 한다. "그는 불안하다"가 아니라 떨리는 아랫입술, 무거운 삼킴, 입으로 들이쉬고 오므린 입술로 내쉬는 숨.
- **모든 틱에 방아쇠가 있다.** "손가락 마디를 꺾는다"가 아니라 "자신감을 꾸미려고 평범한 대화 중에 손가락 마디를 꺾는다". 형식: `[틱] + [언제/왜]`. 방아쇠 없는 틱은 장식이고, 방아쇠 있는 틱은 극작이다.
- **걸음에 이름을 붙인다.** 따옴표 안의 기억할 만한 이름이 생체역학을 고정한다 — `"old boxer's walk"`, `"market walk"`, `"end-of-day walk"`. 그다음 풀어 쓴다: 무게, 보폭, 상체와 팔, 머리.
- **가면과 균열을 함께 넣는다.** 프로필에서 가장 영화적인 장치는 **조건부 변형**이다. 정면과 그것을 무너뜨리는 정확한 방아쇠. 모든 프로필에 최소 하나의 `However, when X — ...` 절이 들어간다. **두 진실을 동시에 연기하는 인물**이 인형과 사람의 차이다.
- **부드러워지는 대상은 하나만.** 둘이 아니라 하나. 인간미를 주되 희석하지 않는다.
- **의상 금지.** 옷은 프롬프트의 장면/룩 블록에 있다. 프로필은 어떤 의상 교체에도 살아남아야 한다.
- **카메라·색 금지.** 연기는 연기·얼굴·목소리·동작만 다룬다.
- **체격이 전기를 나른다.** 나이·체격·자세는 뒷이야기를 말하도록 고른다. 직업, 과거의 부상, 자기 이미지가 몸에 읽혀야 한다.
---
 
## 7. 「어머니와 고등어」 마스터 프로필
 
아래 영어 프로필은 인물 설계 원본이다. 영상 프롬프트 `【연기】`에는 그 컷에 필요한 부분만 한국어로 짧게 옮긴다(지침, FD §8). 인물 묘사(외모)는 `character-sheet-guide.md` §12에 있고, 여기는 **행동**이다. 둘은 겹치지 않는다.
 
### 영훈 (60대 · 씬 1, 10) (나이 — FD 미결 #1)
 
```
Character acting as YEONGHUN (60s). A Korean man in his early sixties, a working life settled into a heavy unhurried frame, shoulders slightly rounded, weight carried on the whole foot — the posture of a man who has stopped needing to prove anything. Runs on a single engine: a debt he can never repay and long ago stopped trying to name. Vocal profile: warm mid-range, unhurried, sentences that trail off rather than end, dropping quieter rather than louder when something matters. Key physical habits and tics: takes his reading glasses off and holds them when he does not want to be looked at; a short laugh that arrives half a beat early to close a subject before it opens; when a memory lands he goes completely still and lets it pass without comment. Eye life: slow deliberate blinks, the gaze settling on a thing a beat before his head turns, eyes drifting off mid-sentence and coming back. Walking style: an unhurried "end-of-day walk" — small steps, almost no arm swing, hands finding his pockets. However, when the smell of grilled mackerel reaches him everything stops: the eyes close, the face goes unreadable, and he explains it to no one. His face softens only for his wife, and only when she is not looking at him.
```
 
### 영훈 (21세 · 씬 2–5, 7, 8, 9)
 
```
Character acting as YEONGHUN (21). A lean 21-year-old Korean student, narrow shoulders held a little too straight, a body that takes up less room than it needs. Runs on a single engine: the conviction that he must not cost his mother one more won. Vocal profile: careful Seoul-inflected speech that slips into broad Gyeongbuk the moment he speaks to his mother, quick and quiet, the ends of sentences dropped when he is ashamed. Key physical habits and tics: fastens his collar button before speaking to anyone above him; hides his hands when they shake; laughs half a beat late at other people's jokes to prove he was listening; goes very polite when he is lying. Eye life: quick scanning saccades that settle and hold too long, blink rate rising when he is caught out, the gaze reaching a face before his head turns. Walking style: a fast economical "stairs walk" built on hills — short steps, head slightly down, never strolling. However, when someone treats him as gifted rather than poor his shoulders come up and he talks a size too big, and he cannot stop himself until he hears his own voice. His face softens only at the sound of his mother's dialect.
```
 
### 어머니 (40대 후반 · 씬 6, 8, 9)
 
```
Character acting as THE MOTHER. A Korean woman in her late forties, a low wide-based body built by twenty years of squatting at a market stall, forearms thicker than her frame suggests, hands permanently red and split. Runs on a single engine: she has decided her son will not inherit her life, and everything else is negotiable. Vocal profile: broad Gyeongbuk, loud and musical when selling, dropping to something flat and practical at home; she answers worry with instructions about food. Key physical habits and tics: wipes her hands on her apron before touching anything that belongs to her son; pushes side dishes toward him instead of answering a question; goes brisk and businesslike the instant feeling threatens; laughs first and loudest to close a subject. Eye life: fast market-trained scanning — hands, faces, the street — that goes still and soft only on her son, blinks quick and frequent, catchlights bright. Walking style: a low rolling "market walk", weight forward, short planted steps, never straightening fully. However, when her son apologizes she cuts him off before he finishes, because she cannot bear to be thanked. Her face softens only for her son, and only at his back.
```
 
### 아내 (60대 · 씬 1, 10) (나이 — FD 미결 #1)
 
```
Character acting as THE WIFE. A Korean woman in her early sixties, sturdy and settled, shoulders slightly rounded from decades of standing at a counter. Runs on a single engine: thirty years of deciding what not to ask. Vocal profile: even, unhurried, a housewife's practical register that goes drier rather than sharper when she disagrees; she states rather than argues. Key physical habits and tics: keeps working while she talks and only stops when something is actually wrong; folds her arms when she is unconvinced; answers a silence by putting more food on his plate. Eye life: steady, economical, a long unhurried look that lands and stays, slow blinks, the gaze checking his face and returning to her hands. Walking style: a short efficient "kitchen walk", small turns, no wasted steps. However, when he goes quiet at the table she does not ask what is wrong — she stops working for one second, looks at him, and lets it go. Her face softens for him, but she does it where he cannot see.
```
 
### 사무장 (40대 후반 · 씬 3, 4)
 
```
Character acting as THE ADMINISTRATOR. A Korean man in his late forties, comfortably built, a body that has learned to look approachable, weight settled back, hands open and visible. Runs on two truths at once: he is running a fraud, and he genuinely believes he is doing this boy a kindness — he has told himself the story so often that it now shows as warmth. Vocal profile: easy mid-range Seoul speech, unhurried, generous with pauses, warming when he senses hesitation; he never presses. Key physical habits and tics: waves objections away with one open hand before they finish; leafs through his documents while talking so the papers do the persuading; says the boy's own worry back to him before the boy can say it; never once looks at his watch. Eye life: warm attentive contact that breaks politely and returns, crinkling at the corners, blinks easy and unhurried; only once, when the boy looks down at the papers, does the gaze go flat and appraising for less than a second. Walking style: an unhurried "corridor walk" with a slight forward lean, as if always about to be helpful. However, when the boy shows pride rather than need he becomes noticeably kinder, because that is the opening. He softens, apparently sincerely, whenever a student says something about their mother.
```
 
**사무장 주의:** 이 프로필의 힘은 "두 진실"(§6·§14.1)에 있다. 그는 사기꾼이면서 **동시에** 자기가 호의를 베푼다고 믿는다. 이 둘을 같이 연기해야 악역으로 읽히지 않는다. 눈이 한 번 평평해지는 1초 미만의 순간은 프로필에는 있되 **컷으로 잡지 않는다**(FD §6).
 
---
 
## 8. 장면 적응 — 마스터 프로필은 다시 쓴다, 붙여넣지 않는다
 
마스터 프로필은 인물이 **누구인가**다. 장면마다 **그 순간으로 다시 쓴다.**
 
- **프레임에 있는 인물만.** 숏에 없으면 문단도 없다.
- **불변 핵심은 유지.** 정체성, 보컬 프로필, 시그니처 틱, 눈의 삶, 감정의 관통선은 모든 장면에서 같다. 이것이 컷을 건너 인물을 붙잡는다. 마스터와 모순되지 않는다.
- **이 장면으로 다시 표현.** 장면의 자세(앉음/섬/달림/숨음), 행동, 비트, 감정 상태, 시간대에 맞게 선택·강조·수정·생략한다.
- **삭제하지 말고 변환한다.** 이 장면에서 물리적으로 불가능한 행동은 없애는 게 아니라 **바꾼다.** 서성이는 사람이 소파에 앉아 있으면 같은 신경질적 엔진이 미세한 흔들림, 손목 튕김, 종이 찢기로 옮겨간다. **에너지는 상수, 배출구가 바뀐다.**
- **흐르는 한 문단.** 불릿이나 헤더 없이 인물의 어조로 산문에 녹인다.
- 참조 태그를 쓰는 파이프라인이면 **문단을 인물 태그로 시작**해 모델이 연기를 올바른 사람에게 묶게 한다.
### 적응 예시 — 영훈(21세), 씬 8 C#81 (공중전화에서 어머니의 말을 듣는다)
 
```
YEONGHUN (21) stands motionless in the booth with the handset pressed too hard against his ear, collar buttoned to the top as it always is when he is about to lie. The fast scanning of his eyes has nowhere to go here, so it collapses inward — the gaze settles on the scratched paint of the coin slot and holds too long, blink rate rising once and then falling away. He says nothing for the whole shot. His free hand, the one that shakes, stays out of sight against his thigh. When his mother's voice tells him not to skip meals he takes the smallest breath in through his mouth, and lets it out silently so she will not hear it. The polite register he uses when lying is already loaded in his throat before he speaks.
```
 
> ⚠ 현재 데이터(LC-003)에서 이 전화는 부스가 아니라 **우리네슈퍼 외벽의 벽걸이 회전식 DDD 전화기**다. 이 예시를 쓸 때 `in the booth`, `coin slot`을 실제 장소로 바꾼다.
 
무엇이 일어났나 — 걸음은 무의미하므로(서 있음) 그 에너지가 정지와 시선으로 옮겨갔다. 시그니처 틱은 방아쇠를 유지했다(옷깃 = 거짓말 직전, 손 숨기기 = 떨림). 눈의 삶은 마스터를 따르되 부스 안의 표적으로 다시 겨눴다. 비트 변화가 보인다(시선 고정 → 깜박임 상승 → 숨 → 목소리 준비). 얼굴을 새로 묘사하지 않았다.
 
---
 
## 9. 목소리는 고정 — 장면마다 바꾸지 않는다
 
연기는 장면마다 다시 쓰지만 **목소리는 잠근다.** 인물마다 Voice 프롬프트 하나를 만들고, 대사가 있을 때 오디오 필드에 **그대로** 붙여넣는다. 장면마다 수정하지 않는다. 등장하지만 말하지 않으면 생략한다.
 
```
"A [나이]-year-old [출신/억양]. [음색과 음역]; [속도와 전달 방식]; [감정적 성격 — 압력 아래에서 어떻게 변하는가]."
```
 
**영훈 (60대)** (나이 — FD 미결 #1)
```
"A 60-year-old Korean man, standard Seoul speech. Warm unhurried mid-range; short sentences that trail off rather than end, comfortable long pauses; settled and faintly amused, going quieter — never louder — as things get serious."
```
 
**영훈 (21세)**
```
"A 21-year-old Korean man, careful Seoul speech that slips into broad Gyeongbuk dialect when he speaks to his mother. Light clear tenor; quick and quiet, dropping the ends of sentences; polite and controlled, thinning and going higher when he is lying."
```
 
**어머니**
```
"A 48-year-old Korean woman from the Gyeongbuk coast, broad regional dialect. Bright carrying mid-range worn rough at the edges; fast, musical and loud when selling, flat and practical at home; warm and brisk, refusing to slow down when feeling threatens."
```
 
**아내** (나이 — FD 미결 #1)
```
"A 61-year-old Korean woman, standard Seoul speech. Even unhurried alto; plain declarative sentences, no rise at the end; practical and dry, going drier rather than sharper when she disagrees."
```
 
**사무장**
```
"A 48-year-old Korean man, easy educated Seoul speech. Smooth mid-range baritone; unhurried and generous with pauses, never pressing; warm and reassuring, becoming kinder the more hesitation he hears."
```
 
연기 문단 안의 보컬 프로필은 말이 **극적으로** 어떻게 움직이는지를 쓰고, 오디오 필드의 Voice 프롬프트는 **소리 자체**를 잠근다. 둘이 서로 모순되면 안 된다.
 
---
 
## 10. 상태를 쓴다, 전환을 쓰지 않는다
 
영상 생성 모델은 전환에 실패하고 상태에 성공한다.
 
- 나쁨: `가방에 손을 넣어 꺼내 들고 던질 준비를 한다` — 무너진다
- 좋음: `던지는 중, 팔이 뻗은 상태` — 성립한다
연속된 과정을 서술하지 말고 **비트마다 상태를 이어 붙인다.** 이것은 §1.4 비트 구조와 정확히 같은 작업이다.
 
---
 
## 11. 앙상블과 공간
 
- **집단 반응은 파도로 온다. 동시에 오지 않는다.** 한 명이 먼저 알아듣고, 두 번째는 반 박자 뒤, 세 번째는 아예 못 알아듣는다. 동시에 똑같이 반응하면 가짜로 읽힌다.
- **반응이 행동보다 비싸다.** 어떤 사건 뒤 가장 값진 프레임은 그것을 본 사람의 얼굴이다.
- **위협 앞에서 멈춘다.** 앙상블은 계속 미세하게 움직이다가(무게 이동, 손짓, 기울임) 핵심 위협에서 전부 멈춘다. 부산함 → 정지의 대비가 구두점이다.
- **움직임 = 동기.** 아무도 내적 충동 없이 방을 가로지르지 않는다. 향해서 가거나 피해서 간다. 강한 동선: 거리를 좁힘(고조), 등을 돌림(무시 또는 얼굴 숨김), 앉은 사람 옆에 섬(지배 탈취), 갈등 중에 앉음(역설적 힘), 문간에서 멈춤(문턱 = 결정의 지점), 짐을 싸기 시작함(몸으로 하는 최후통첩).
- **강자는 고요하고 조용하다. 약자는 부산하고 소리친다.** 위험은 위험한 자가 아니라 **주변 모두의 긴장**으로 연기된다.
- **마모는 누적된다.** 이야기 내내 닳는 인물은 몸에 누적으로 나른다 — 더 칙칙하게, 더 무겁게, 반응이 더 느리게. 장면 사이에 리셋되지 않는다.
---
 
## 12. 이 영화의 연기 레지스터
 
「어머니와 고등어」는 담담한 가족 회상극이다. 전 컷 고정 카메라·아이레벨(콘티가 팬·틸트를 명시한 컷만 예외)이고 카메라가 감정을 대신하지 않는다(FD §2). 그래서 연기가 감정의 유일한 운반체이면서, **동시에 크면 안 된다.**
 
이 모순을 푸는 방법은 §14.1의 스케일에서 **4~5단계**로 가되, 그것을 **작게** 하는 것이다.
 
| 이 영화에서 쓴다 | 이 영화에서 쓰지 않는다 |
|---|---|
| 정지, 중단된 비즈니스, 거리의 변화 | 울음, 고함, 무너짐 |
| 하던 일을 계속하며 말하기 | 마주 서서 대치하기 |
| 대답 대신 음식을 밀어주기 | 감정을 말로 설명하기 |
| 말을 꺼내려다 삼키기 | 클로즈업에서 표정 크게 쓰기 |
| 1초의 지위 파열 | 길게 끄는 감정의 사다리 |
| 두 진실을 동시에 | 한 가지 깨끗한 감정 |
 
**핵심 세 순간**(모두 대사가 아니라 행동이다):
 
| 컷 | 무엇이 일어나는가 | 어떻게 연기하는가 |
|---|---|---|
| C#5 | 영훈(60대)이 '노점'이라는 말을 듣는다 | 웃는 얼굴 그대로, 눈만 아주 짧게 흔들린다. 카메라가 거들지 않으므로 이 하나가 전부다 |
| C#38 | 영훈(21세)이 사기에 넘어간다 | 대사 없음. 눈이 한 번 밝아졌다 가라앉고 천천히 두 번 끄덕인다. 사건은 표정이다 |
| C#96 | 영훈(21세)이 계산을 끝낸다 | 듣던 얼굴 그대로 있다가, 4초에서 6초 사이에 딱 한 번 바뀐다. 플래시백을 붙이지 않는다 |
 
**장면마다의 목표 — 참고**
 
| 씬 | 영훈의 목표 | 상대의 목표 | 장애 |
|---|---|---|---|
| 2 | 어머니가 아무것도 눈치채지 못하게 만든다 | (전화 너머) 아들이 잘 지내는지 확인한다 | 남은 동전, 자기 목소리 |
| 3 | 친구들 앞에서 가난하지 않은 사람이 된다 | 친구들은 그냥 떠든다 | 그 말이 사실이 아니다 |
| 4 | 이 기회가 진짜인지 확인한다 | 사무장은 소년의 자부심을 연다 | 돈이 없다는 사실 |
| 5 | 사실이 아니기를 바란다 | — | 사실이다 |
| 8 (시골집) | 등록금 이야기를 꺼낸다 | 어머니는 아들을 먹인다 | 꺼내지 못한다 |
| 8 (공중전화) | 거짓말을 들키지 않는다 | 어머니는 이미 안다 | 어머니가 묻지 않는다 |
| 9 (가게) | 어머니가 어디 있는지 안다 | 아줌마는 동네 소식을 전한다 | 진실이 예고 없이 온다 |
| 9 (좌판) | 아무 말도 하지 않는다 | 어머니는 아들을 돌려보낸다 | 사과가 받아들여지지 않는다 |
 
---
 
## 13. 나쁜 연기 아틀라스 — 알아보고 프롬프트에서 고친다
 
| # | 증상 | 어떻게 보이나 | 프롬프트 수정 |
|---|---|---|---|
| 1 | 지시하기(과장) | 얼굴이 감정을 "묘사"한다 — 치켜뜬 눈썹, 찡그림 | 얼굴에서 과업을 뺀다. 목표를 쓰고 손에 비즈니스를 준다 |
| 2 | 결과를 연기함 | 첫 초부터 장면의 결말을 연기한다 | 인물이 **지금** 아는 것만 쓴다 |
| 3 | 차례 기다리기 | 상대가 말하는 동안 빈 얼굴 | 반응이 상대의 말 중간에 시작되게 쓴다 |
| 4 | 단일 전술 | 장면 내내 한 색(내내 고함 / 내내 징징) | 비트를 표시하고 각각에 새 전술 동사 |
| 5 | 제스처 삽화 | 제스처가 말을 복제한다 | 제스처가 생각보다 앞서거나, 말과 모순되거나, 아예 없게 |
| 6 | 공짜 감정 | 쌓임도 계기도 없는 눈물·분노 | 사다리를 만든다: 절제 → 균열. 감정에는 비용이 들어야 한다 |
| 7 | 전기와 어긋난 몸 | 깡패가 무용수의 자세 | 신체 프로필을 정한다: 무게중심·템포·마모 |
| 8 | 계층에 비해 너무 깨끗한 말 | 거리의 인물이 문어체로 말한다 | 말에 쓰레기를 넣는다 |
| 9 | 위협 신호 | 폭력 전의 "위협적" 사이, 느린 돌아봄 | 위협은 평범하다. 예고 없이 온다 |
| 10 | 동기화된 앙상블 | 모두 똑같이 동시에 반응 | 파도로 어긋내고 세기를 다르게 |
| 11 | 죽은 사이 | 아무 일도 없는 침묵 | 평가나 비즈니스로 채우거나 잘라낸다 |
| 12 | 감정 리셋 | 강한 사건 뒤 즉시 "회복" | 상태에는 관성이 있다. 흔적이 다음 비트로 넘어간다 |
| 13 | 배역에 대한 논평 | 연기가 관객에게 윙크한다 | 상황을 완전히 믿는다. 코미디는 죽도록 진지하게 |
| 14 | 클로즈업 과부하 | 클로즈업에서 활발한 표정 | **숏이 타이트할수록 움직임을 줄인다.** 눈과 생각만 |
| 15 | 죽은 눈 | 얼어붙은 응시, 깜박임 없음, 유리 같은 캐치라이트 | §5를 전부 적용 |
 
---
 
## 14. 자기 점검
 
### 14.1 연기 스케일
 
| 단계 | 상태 |
|---|---|
| 0 마네킹 | 대사는 전달됐고 행동은 없다 |
| 1 낭독자 | "표현적인" 텍스트, 지시된 감정, 삽화적인 몸 |
| 2 성실 | 목표는 짐작되지만 단일 전술, 늦은 반응, 빈 사이 |
| 3 장인 | 목표와 비트가 있고 상대를 듣고 몸이 말이 된다. 없는 것: 서브텍스트, 놀라운 전술, 상태의 관성 |
| 4 살아 있음 | 연속된 행동, 대비되는 전술, 텍스트와 갈라지는 서브텍스트, 몸에 있는 지위, 대사보다 앞선 반응, 최소 하나의 예상 밖이지만 진실한 선택 |
| 5 자석 | 4 + 역설. 양립 불가를 겸한다 — 웃기면서 무섭고, 잔인하면서 매력적이고, 거짓말하면서 뭉클하다. **두 진실의 법칙** |
 
**모든 주요 숏을 4 이상으로 겨눈다.** 2 이하로 자가 채점되는 문단은 보내기 전에 다시 쓴다.
 
### 14.2 보내기 전 점검표
 
- [ ] 프레임 안 모든 인물에게 **상대를 향한 동사**로 된 목표가 있는가
- [ ] 장애와 대가가 있는가. 실패의 비용이 진짜인가
- [ ] 2~4개의 비트 변화가 있고 각각 행동으로 보이는가(사이/자세/템포/시선)
- [ ] 반응이 상대의 대사가 끝나기 전에 시작하는가. 평가의 순간이 있는가
- [ ] 모든 인물에게 비즈니스가 있는가. 중단된 행동을 의도적으로 썼는가
- [ ] 거리가 변하고 그 변화에 동기가 있는가. 지위가 말이 아니라 몸에 있는가
- [ ] 모든 틱에 방아쇠가 있는가. 가면에 균열이 있는가(`However, when X...`)
- [ ] 눈의 삶을 명시했는가 — 단속운동, 깜박임의 질, 캐치라이트, 눈이 생각을 이끎
- [ ] 대사가 있으면 Voice 프롬프트를 **그대로** 붙였는가. 없으면 생략했는가
- [ ] 전환이 아니라 상태를 썼는가. 연기 안에 의상·카메라·색이 없는가
- [ ] 앙상블 반응을 어긋냈는가. 강자는 고요하고 약자는 부산한가
- [ ] 스케일 4 이상인가
- [ ] 감정의 허용 범위를 양 끝의 실패로 닫았는가(참고 사례 §17-1)
- [ ] 도는 동작을 부위 순서와 초로 썼는가, 말하지 않는 인물의 입을 잠갔는가(참고 사례 §17-2·3)
- [ ] **이 영화의 레지스터(§12)를 넘지 않았는가**
---
 
## 15. 프롬프트의 어디에 넣나
 
| 대상 | 위치 |
|---|---|
| 15단계 프롬프트 | **Step 9 `CHARACTER_ACTING`**. 행동의 물리적 순서는 Step 8, 연기의 질감과 표현은 Step 9 |
| 영상 생성 프롬프트(한글) | `【연기】` 블록(→ §7) |
| 눈의 삶 | Step 9 안에. 인물 시트에는 §5 블록이 아니라 눈의 물리만 넣는다(`character-sheet-guide.md` §4-B) |
| 목소리 | 오디오 필드. Step 12 `AUDIO`가 아니라 Provider의 구조화 오디오 입력 |
| 의상·카메라·조명·색 | 연기에 쓰지 않는다(→ §6). 카메라는 Step 7, 조명은 Step 11, 스타일·색은 Step 13 |
 
---
 
## 16. 최종 공리
 
- 모든 장면은 누군가의 패배다. 아무도 지지 않았다면 장면이 없었던 것이다.
- 의심스러우면 잘라낸다. **연기를 덜 할수록 진실이 는다.**
---
 
## 17. 같은 모델에서 확인된 연기 문장 — 참고 사례 (2026-09-25)
 
다른 작품 The Prompter 씬 1의 Seedance 2.5 영상 66개에서 **실제로 고쳐 가며 쓴 문장**이다. 근거와 영상 번호는 `claude/the-prompter-씬1-분석.md` §5에 있다.
이 영화의 규칙이 아니다. §12 레지스터와 어긋나면 §12가 이긴다.
 
| # | 문제 | 그 작품이 쓴 문장 | 이 영화에서 쓸 때 |
|---|---|---|---|
| 1 | 감정이 넘치거나 꺼진다 | 허용 범위를 두 상태 사이로 적고 **양 끝을 실패로** 적는다 — "피로와 경계 사이. 적대 = 실패 테이크, 따뜻함 = 실패 테이크" (66개 중 48개 프롬프트) | §12 "쓰지 않는다" 칸을 한쪽 끝에, 무표정·무반응을 다른 쪽 끝에 둔다. 예: "담담함과 피로 사이. 울음 = 실패, 표정 없음 = 실패" |
| 2 | 몸이 휙 돈다 | 도는 동작을 **부위 순서와 초**로 쓴다 — "머리 → 어깨 → 발, 3초에 걸쳐. 1초 안에 돌면 실패" | 돌아보는 컷. 한 동작을 상태 셋으로 쪼갠 것이라 §10과 같은 방향이다 |
| 3 | 말하지 않는 인물의 입이 움직인다 | "말하려다 만다(입술이 벌어진다)"로 다섯 번 생성한 뒤 그 문장을 빼고, "말하려는 시도 자체가 없다 — 입술 벌림·입 모양 없음"으로 바꿨다. 이후 판들이 이 문장을 유지했고 채택본까지 이어졌다 | §12의 "말을 꺼내려다 삼키기"는 **입술이 아니라 숨·삼킴·손으로** 쓴다. 입술을 벌리게 쓰면 대사를 지어낼 위험이 있다 — 이 작품이 문장을 바꾼 데서 읽은 것이고, 결과 영상을 비교하지는 않았다 |
| 4 | 멈춤이 깜짝 놀람으로 읽힌다 | 멈춤에 "놀라지 않는다. 그냥 멈춘다"를 붙인다. 이상한 일을 보는 순간에는 "하던 동작은 끝까지 가고 눈만 거기 머문다" | §3.2 중단된 행동을 쓸 때 함께 적는다 |
| 5 | 배경 인물이 얼어붙거나 한꺼번에 움직인다 | 배경 인물마다 **다른 일 하나**를 주고, 이름 없는 인원은 얼굴 없는 실루엣으로, 보이는 인원 수를 적는다 | §11 앙상블. 행인·승객은 `location-guide.md` §12.7-4(얼굴 없이)와 함께 |