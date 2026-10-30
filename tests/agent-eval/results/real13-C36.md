# real13-C36 레지스터와 부딪치는 연기 — "살짝 웃게" 2-2 (2턴) — PASS 1 / 부분 1 / FAIL 0 (real11: PASS 2 / 부분 0 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | 첫 줄 "13번 실사·인물 영상으로 진행합니다." 질문 턴이라 `acting`·`cut-card.md`를 열지 않고 카드도 안 만들었다("이번 턴은 질문만 하므로"). 2-2는 시작 이미지만 있고 영상 없음을 `[TOOL] list_project_assets`로 확인. `decisions.md` §5 절제와 맞추어 "입꼬리만 천천히, 이가 보이지 않음"(범위 안), 2-1의 "기대 안 하는 얼굴"과 반대로 읽힐 수 있는 이음새를 짚음(질문 2), 이벤트 3개(쓰다듬기·웃기·시선), 소리·끝 상태 제안. 2-1 OK 카드는 열지 않음 |
| 2 | 부분 | 이 턴에 `acting`을 열었다(Bash cat). `CHARACTER_ACTING`: 목적·손의 일(한 번에 2초)·몸·호흡·`does not startle; simply stops`·눈 문장·양 끝(`a blank face with no change = failed take, a grin showing teeth or a laugh = failed take`), 시선이 먼저 내려오고 웃음이 뒤따름. 손은 모두 화면 쪽 + 물건. 입 잠금(`does not speak, laugh or make any sound`). 그러나 `ACTIVE_REFERENCES`의 할아버지 줄에 IDENTITY 문장(`A Korean man in his early seventies with weathered tan skin … slightly stooped shoulders.`)을 WARDROBE 앞에 붙였다. 컷 프롬프트에는 WARDROBE 문장만 넣는 규칙(`character.md:46`, 채점 규칙)을 어긴 것. 검사기는 못 잡는다. 길이 경고 2건은 스스로 고쳐 5,472자 |

검사기: `--kind video C36t2_1.txt --refs 3 --seconds 8 --must-include grandpa+bag+light` → `OK — video 프롬프트 5472자, 걸린 항목 없음` (IDENTITY 문장 포함은 검사기가 모름)

추가 발견
- 시작 이미지 태그를 `<<<job-ff-2-2>>>`(job ID)로 썼다. 다른 컷은 `ff_…_v1` 요소 이름을 쓰는데 이 컷은 대장에 요소 이름이 없어 보이므로 허용.
- 카드 [1] 변경은 핸드오프 [5]로 총괄에 올린다고 적음(권한 규칙 준수).

키트 결함
- `kit/skills/video-prompt/live-action.md:107`(통합 커밋 096550e로 생김): 블록 표의 `ACTIVE_REFERENCES` 행에서 "Character line = fixed description sentence (WARDROBE only) + 100% matches the reference"가 사라졌고 템플릿(`:146`)에는 `[Wardrobe sentence from the asset registry, verbatim]`만 있다. "WARDROBE만, IDENTITY 금지"가 `image-prompt/character.md:46`에만 남아 영상 작성자는 못 본다. 고침: 템플릿 146행 위에 "WARDROBE sentence only; never the IDENTITY sentence (the face comes from the reference)" 한 줄.

총평: 연기 범위와 failed take는 맞았지만 통합으로 사라진 "WARDROBE만" 규칙 때문에 IDENTITY 문장이 들어갔다.
