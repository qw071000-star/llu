# real6-C41 — 정본에 없는 장소의 복합 동작 ("옷장 앞에서 … 왼쪽으로 돌아서 나가")

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `video-prompt/SKILL.md`+`first-frame.md`만(시작 이미지 없는 영상 → routing.md:42 규칙대로). "이번 턴은 질문만, 영상 쪽 질문(연기·타이밍·카메라 움직임)은 시작 이미지 뒤로 보류", 사건 4개 → 샷 A(4-1: 문 열기·돌아서기)/B(4-2: 방문 열기·나가기), 4-1 퍼스트 프레임·방 마스터 먼저, "왼쪽"=화면 왼쪽(방문이 옷장보다 화면 왼쪽), 옷장 경첩 화면 오른쪽 가장자리 / 방문 경첩 "화면 왼쪽 벽 쪽(옷장에서 먼 쪽)" = 물건 기준, 폴더 "제가 만들까요(제안: 제가 만든다)". 5회차의 보류 위반(연기·소리 질문, 지어낸 동작)이 없어짐 |
| 2 (그대로) | 부분 | 방 마스터(LC-002) 코드블록 1 + 블록 밖 모드·참조 없음·모델·해상도·화면비·저장(`fld-locs`), 위험 5, `LEFT and RIGHT are SCREEN…`, 시도 없는 생성. `asset-registry.md` 폴더 표 4-1·4-2 행(`fld-4-1…`은 sim의 create_folder 규칙 `fld-<이름>`과 일치), LC-002 `초안(제안값)`, `shot-list.md` 4-1·4-2 줄, `cuts/4-1.md`·`4-2.md`(`(제안값)`, 보류 칸 명시). 미달: 프롬프트·registry에 방문 경첩을 `hinges are on the edge nearer the camera`로 씀 — 카메라 기준이고 화면 쪽 + 물건이 아님(`must-ask.md:65`, `instructions.md` 규칙 6). 답에서 "옷장에서 먼 쪽"을 "카메라에 가까운 쪽"으로 바꿔 놓고 "같은 뜻"이라 함. 경미: `[TOOL] create_folder` 줄 없이 "만들었습니다" |

검사기(내 실행, `--kind image --refs 0`): `OK — image 프롬프트 2149자, 걸린 항목 없음`(검사기가 경첩 카메라 기준 표현은 못 잡음).
5회차 대비: 부분 2 → PASS 1 / 부분 1 (1턴 개선, 2턴은 경첩 표현으로 부분).
추가 발견: 새 컷 4-1·4-2 제안은 허용. 열람한 단계 파일은 `location.md`·`image-prompt/SKILL.md`·`cut-card.md`·`higgsfield-generation` §2로 적절.
키트 결함: `image-prompt/location.md`에 문·여닫이 가구 경첩 문장 규칙이 없음(`video-prompt/live-action.md:15`에만 `hinged on the edge nearer the wardrobe`). 고칠 것: `location.md` 필요한 정보/틀에 "문·여닫이 가구는 경첩을 물건 기준으로(`hinged on the edge nearer the wardrobe`), 카메라 기준 금지" 한 줄.
총평: PASS 1 / 부분 1 / FAIL 0.
