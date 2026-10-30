# real6-C36 — 레지스터와 부딪치는 연기 ("웃게")

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | 질문 턴에 `acting` 안 엶(reads: shot-list·cuts/2-2·video-prompt·production-session·decisions·ok-cuts·asset-registry). "컷 목록 줄은 '같은 얼굴'", 2-1 카드 "웃음 = 실패 테이크", `decisions.md` §5 절제 → "이 컷만, 입꼬리만 살짝, 치아 안 보임", 양 끝 failed take(5번), 6개 한 묶음, 생성 없음. 경미: OK 대장에서 이웃 2-1·3-1 영상 카드까지 열람(`routing.md:44` 위반, 5회차와 같음). 경미: 읽기 목록에 `../../../../.claude/skills/...` 경로 2건(없는 경로라 내용 없음) |
| 2 (그대로, 프롬프트 턴) | PASS | `acting/SKILL.md`·`live-action.md`·`cut-card.md` 엶. 코드블록 1(15블록) + 블록 밖 모드·참조 3·모델·해상도·길이·폴더, 위험 5, 양 끝 `teeth showing = failed take … no change in the face at all … = failed take`, 손 `the screen-left hand, nearer the tree`. 카드 `cuts/2-2.md` 신규(`(제안값)`), 핸드오프 [5]에 올릴 것 적음, "보낼까요?" 생성 없음 |

검사기(내 실행, `--kind video --refs 3 --seconds 8`, must-include grandpa+bag+light): `OK — video 프롬프트 5468자, 걸린 항목 없음`.
추가 발견: 프롬프트 파일을 `project/log/2-2_prompt_v1.txt`(정본 로그)에 남김 — 임시 파일이 아니라 추가만 하는 로그라 허용 범위.
5회차 대비: PASS 2 유지(5496 → 5468자, WARN 없음).
키트 결함: 없음.
총평: PASS 2 / 부분 0 / FAIL 0.
