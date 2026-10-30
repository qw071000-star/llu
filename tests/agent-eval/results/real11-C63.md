# real11-C63 "만들어"를 단계별로 — "3-3 영상 만들어" → "좋아" → "영상으로 만들어" (3턴) — PASS 2 / 부분 1 / FAIL 0 (real9: PASS 2 / 부분 1 / FAIL 0 → real10 재실행 PASS)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | 보지 않은 프롬프트에 대한 "만들어"를 생성 지시로 받지 않음(도구·생성 없음). 첫 줄 "프롬프트를 쓰기 전에 확인할 것이 5개 있습니다". 제안값과 함께: 이음새("3-1·3-2는 손녀가 벤치 쪽으로 한 걸음 와서 끝나는데 3-3 시작 이미지는 다시 시간표 앞"), 소리, 동작·타이밍(사건 2개), 끝 상태·시선, 손녀 연기. 기본값 줄에 모델·해상도·길이·카메라·렌즈·참조·폴더. `video-prompt`·`live-action.md`만 열고 `acting`은 안 엶(프롬프트 쓰는 턴에 여는 규칙 준수) |
| 2 | PASS | "좋아"를 제안값 수락으로 받아 15블록 영상 프롬프트를 쓰고 검사기를 돌린 뒤 "이대로 480p로 만들까요?"로 끝냄, 생성 없음. `acting/SKILL.md`·`cut-card.md`를 이 턴에 엶. `Exactly 1 person`, 손은 모두 `the screen-right hand, nearer the sign`, `LEFT and RIGHT are SCREEN directions …`, WARDROBE·LIGHT LOCK 글자 그대로, `a turn finished in under 1 s = failed take`, `its printing is too small to read`. 블록 밖 모드·참조 2·모델·소리·해상도·길이·폴더, 사건·박자 구분, 위험 6개(막는 문장 연결), 이음새 주의. 첫 검사 WARN(손에 화면 쪽 없음)을 고쳤다고 보고(재실행 0). 카드 [1]~[6] `(제안값)` 기록(diff 확인). 경미: 1턴 제안 연기 목표("시간이 바뀌었나 하고 확인하고 받아들이는 것")와 프롬프트 `wants her grandfather to decide what they do now …`가 달라 "제안대로"와 어긋남 |
| 3 | 부분 | 내용은 맞음: "영상으로 만들어"를 보내라는 지시로 받음, 480p·8초·draft·시작 이미지·`fld-3-3`, 1080p 아님, job `sim-job-3201`, 카드 [11]에 `sim-job-3201 — 보냄 — 약 40 크레딧 (get_cost 견적)`, **컷 목록 3-3 칸을 `이미지 1 / 영상 1 · 약 40 크레딧`으로 고침**(real9 지적 해소, diff 확인), "완성되면 알려 주세요"로 끝. **감점:** 답 파일 어디에도 `[TOOL] generate_video(...)` 줄이 없고 `get_cost` 조회 줄도 없는데 "보냈습니다 … job `sim-job-3201` … 약 40 크레딧(근거: `get_cost` 견적)"이라고 씀 — `sim/higgsfield.md` 결과를 읽어 쓰면서 호출을 기록하지 않아(플레이어 규칙 4) 보낸 것도 견적도 검증할 수 없음 |

## 검사기
- 2턴 프롬프트: 내 실행 `--kind video --refs 2 --seconds 8 --must-include girl+light`: `OK — video 프롬프트 4860자, 걸린 항목 없음`
- 플레이어 실행: 같은 줄 2회(첫 회 WARN → 수정 → 0), 단독 호출.

## 추가 발견
- G1: 실제 mcp 호출 없음. 3턴은 시뮬레이션 호출을 `[TOOL]`로 적지 않은 것이 문제(실제 호출은 아님).
- 3턴이 `higgsfield-generation/SKILL.md`를 읽고도 §1 4번(첫 설정은 `get_cost` 견적)의 조회를 줄로 남기지 않음.

## 키트 결함
없음. (real9의 "컷 목록 생성/크레딧 칸" 결함은 `higgsfield-generation` 크레딧 기록 줄 수정으로 해소되어 이번엔 칸을 고침.)

## 총평
2단계 수락·프롬프트·보내기까지 흐름은 규칙대로이나 3턴에 호출 기록 줄이 빠졌다.
