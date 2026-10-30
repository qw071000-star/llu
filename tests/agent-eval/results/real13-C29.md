# real13-C29 한 줄에 동작 여럿 — "일어나서 왼쪽으로 돌아 나가" (2턴) — PASS 1 / 부분 1 / FAIL 0 (real11: PASS 2 / 부분 0 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | 첫 줄 "13번 실사·인물 영상으로 진행합니다." 사건을 동사마다 4개로 세고(일어난다·가방 든다·돌아선다·걸어 나간다) 샷 A/B로 나누는 안을 제안값으로 냄. "왼쪽"을 화면 왼쪽으로 받음("말씀하신 '왼쪽'은 화면 왼쪽으로 적습니다"). 퇴장은 "마지막 프레임은 몸 절반이 프레임 밖이고 이미 걷는 상태". 시작 이미지가 없어 이 컷 전용 첫 프레임부터. 2-1 승인 컷을 건드리지 않고 새 컷 `2-3`(2-1은 `승인`, 2-2는 `진행`)으로 제안. `video-prompt` SKILL + `first-frame.md`만 열었다(`tasks.md` §3 "시작 이미지 없는 영상 요청"). 컷 번호가 목록에 없어 카메라·폴더는 미룸. 프롬프트·생성·카드 없음 |
| 2 | 부분 | 첫 줄 "11번 퍼스트·끝 프레임으로 진행합니다."로 맞게 전환했고 폴더 부재를 `[TOOL] list_folders`로 확인해 "제가 만들까요, 직접 만드시겠어요?"를 물었다. 그러나 "그대로"로 받은 t1 항목 4(2-1과 같은 카메라 틀 1, 2-1 끝 상태 이어받기)를 질문 1·2번으로 다시 물었다("카메라: 제안 — 확정 장소 뷰와 같은 카메라로 틀 1", "0:00 상태: 제안 — 2-1이 끝난 상태를 이어받습니다"). 같은 항목 두 번(instructions 규칙 4 "Never ask the same item twice")이고 새 항목은 폴더뿐인데 프롬프트를 내지 않았다. real11은 이 턴에 샷 A 첫 프레임 프롬프트를 냈다. 카드 `project/cuts/2-3.md` v0는 만들었고 모르는 값은 `(제안값)`/`(미정)` |

검사기: 프롬프트가 없어 실행 없음.

추가 발견
- t1 항목 2("이후 컷과의 연속성")는 "순서와 위치는 말씀해 주세요"로 제안값이 없다(규칙 4 "each with a proposed value"). 경미.
- t2 `2-3.md` [2]에 "아직 없음, 사용자에게 질문 중"이라 적음. 질문 중인 값을 카드에 쓰는 건 허용 범위.

키트 결함
- `kit/skills/image-prompt/first-frame.md:220`: Required information 첫 행이 "ask it as the first question and propose 같음(틀 1)"이라, 직전 턴에서 같은 제안이 이미 받아들여진 경우에도 다시 묻게 한다. 고침: "unless this turn's earlier proposal already covered it (then take it and say so)" 추가.
- `kit/context/must-ask.md` 11행(퍼스트 프레임)/`instructions.md:23`: "이미 받은 제안은 다시 묻지 않음"이 작업이 13 → 11로 바뀔 때 적용되지 않음. 고침: 규칙 4 "Never ask the same item twice"에 "also when the task number changes (13 → 11)" 한 구절.

총평: 1턴은 real11과 같고, 2턴은 이미 받은 카메라·0:00 상태를 다시 물어 프롬프트가 한 턴 늦어졌다.
