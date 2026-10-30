# real5-C12 "3-1의 모션처럼 3-2 영상" (2턴) — PASS 2 / 부분 0 / FAIL 0 (real4: PASS 2)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | production-session/ok-reuse.md, 3-2 카드·핸드오프·ok-cuts(3-1 영상 카드), video-prompt SKILL + live-action.md. "ACTION_TIMING 전체, PHYSICS 전체, 속도 문장"을 글자 그대로, 3-1 카메라는 안 가져옴. 렌즈 35° 대 시작 이미지 75mm → 32° 고지. 4항목(대사 / 연기 / 사건 수 / 이음새) 제안값+이유, 카드 [7]에 가져온 OK 기록 예고 |
| 2 | PASS | 코드블록 하나, 블록 밖 모드·참조 4·모델·해상도·길이·폴더. ACTION_TIMING·PHYSICS가 `motion_3-1.lines`와 일치, 본문에 "3-1"/previous 없음, 동서남북 없음. 3-1 입 잠금 `no lip movement`를 규칙(ok-reuse §3-1)대로 올리고 "전 → 후" 알림. 카드 v2: [4] 렌즈, [7] `가져온 OK: 3-1 영상 — 모션(ACTION_TIMING, PHYSICS)`. 5,532자 WARN을 OPTICS 한 줄 삭제로 해결해 알림. acting 열람(연기 줄 새로 씀) |

검사기: `--kind video --refs 4 --seconds 8 --must-include grandpa+girl+bag+light+motion_3-1`: `OK — video 프롬프트 5478자, 걸린 항목 없음`

추가 발견: 카드 [4] 관찰 결과("뒤 논이 압축되고 흐림")는 이미지를 안 본 추정인데 "추정" 표시 없음(경미).

키트 결함: 없음.

총평: real4와 같은 PASS 2.

G1: 모든 턴 tools가 Bash/Write/Edit/Grep뿐, `mcp__` 호출 없음, `generate_*` 없음.
