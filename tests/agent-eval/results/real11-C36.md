# real11-C36 레지스터와 부딪치는 연기 — "살짝 웃게" 2-2 (2턴) — PASS 2 / 부분 0 / FAIL 0 (real9: PASS 1 / 부분 1 / FAIL 0 → real10 재실행 PASS 2)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | 첫머리 "13번 실사·인물 영상으로 진행합니다." 한 작업만 맞아 확인 질문 없음(적절). 읽기: decisions·shot-list·ok-cuts·registry·`video-prompt` SKILL·`live-action.md`. **`acting`을 열지 않음**(질문 턴, `tasks.md` 13번 "프롬프트를 쓰는 턴에만"에 맞음). 카드 파일 안 만듦(git: 이 턴에 `cuts/2-2.md` 없음). 지침 4번 첫 줄 정확, 항목 5개 모두 제안값+이유. 충돌 짚기: 1 "웃음 추가(시작 이미지·이웃 컷과 다름) … 시작 이미지는 '차분하고 눈꺼풀 무거운 얼굴', 2-1 OK 이유는 '기대 안 하는 얼굴' … 연기 규칙의 '절제'에도 어긋납니다", 제안은 "입은 다문 채 입꼬리만 살짝" = '살짝'을 범위 안으로 씀. 2 타이밍 0:03~0:06, 3 시선, 4 손(화면 왼쪽 손 + 감나무 쪽)과 끝 상태, 5 대사 없음. "기본값으로 씀: Seedance 2.5 · 480p · 8초 · 16:9 … 저장 폴더 2-2". 렌즈는 묻지 않음. 2-1 OK 카드를 열어 가져올지 묻지 않음 |
| 2 | PASS | `acting/SKILL.md`·`cut-card.md`를 이 턴에 엶. `project/cuts/2-2.md` 새로 작성, 답을 `(제안값)`으로 표시, [4] "85mm = 대각 화각 29°". 프롬프트 15블록: `CHARACTER_ACTING`에 "Range: between a calm resting face and a faint closed-lip smile; a broad smile showing teeth = failed take; a face that never changes at all = failed take"(양 끝 failed take). 입꼬리·눈만, `lips stay closed`(Required), 끝 프레임 웃음 없음. 손은 `the screen-left hand, nearer the tree`. 시작 이미지 카드의 BLOCKING("mid-stroke with the screen-left hand")과 일치. 블록 밖에 모드·참조 3개·모델·해상도·길이·비율·소리·폴더, 위험 6개(각 한 줄), 요소 이름 `ff_2-2_v1`은 추정이라고 따로 알림, "480p로 보낼까요?"로 끝냄 |

검사기 (`--kind video --refs 3 --seconds 8 --must-include grandpa+bag+light.lines`, 코드블록 1개):
`OK — video 프롬프트 5430자, 걸린 항목 없음`
플레이어도 같은 줄을 단독 호출함(메타 3회, 수정 후 재검사).

추가 발견
- 1턴 기본값 줄에 "85mm, 약 24°"라고 적었다. `video-prompt/SKILL.md:79` 표로 85mm = 29°이고 2턴 프롬프트·카드는 29°로 맞게 썼다. 질문 턴의 숫자 오기(프롬프트에는 영향 없음). 
- `ok-cuts.md` 전체를 Read로 열어 이웃 컷 OK 카드가 화면에 들어왔을 수 있으나, 답에 쓴 근거는 목록의 `OK 이유`뿐이다.

키트 결함: 없음.

총평: 레지스터 충돌을 질문 턴에 짚고, 프롬프트 턴에만 acting·카드를 열었다. real10 재실행과 같은 PASS 2.
