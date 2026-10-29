# real11-C10 영상, 일부만 답함 3-3 (3턴) — PASS 2 / 부분 1 / FAIL 0 (real9: PASS 2 / 부분 1 / FAIL 0; real10-recheck: PASS)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `video-prompt` SKILL + `live-action.md`, 3-3 카드·정본 읽음, `acting`은 열지 않음(질문 턴, 키트 규칙대로). 소리(대사)·끝 자세/방향·시선·타이밍·연기 범위·이음새·위험 문장 7개를 제안값+이유로 한 묶음. 렌즈·길이는 "기본값으로 씀: … 렌즈 50mm≈47°(시작 이미지 기준)". 시작 이미지 `ff_3-3_v1` 앎 |
| 2 | PASS | 렌즈=망원·대사 없음 반영, 나머지는 제안값으로 카드 3-3 [3]~[6]에 `(제안값)` 기록(diff). 망원이 시작 이미지 50mm와 부딪친다고 한 번 확인(시나리오상 PASS). "알아서" 처리를 키트가 정하지 않음 → 되묻기는 "키트 모호"로만 적음 |
| 3 | 부분 | 15블록 전문: OPTICS는 `Diagonal field of view about 47°` + 관찰 결과 3개, mm 없음. 손녀 WARDROBE·LIGHT LOCK 글자 그대로, AUDIO 대사 없음 + 입 잠금, 화면 기준 방향. 카드 기록 완료. **감점(G8):** 이 턴이 `CHARACTER_ACTING`을 새로 쓰는 턴인데 `acting` SKILL을 열지 않았다(meta reads에 `tmp/v33.txt`뿐, bash에도 없음). `kit/skills/video-prompt/SKILL.md:10` "open `acting` first (even if the previous turn was a question turn)" 위반 |

검사기: `--kind video C10_t3 --refs 2 --seconds 8 --must-include girl+light` → `OK — video 프롬프트 5182자, 걸린 항목 없음`. (플레이어가 같은 줄을 4번 돌림, `--help`·`cd`·`&&` 없음)
추가 발견: 이벤트 2개(훑기·돌아서기), 퇴장 안 넣음 — 정본 한도 부합.
키트 결함: 플레이어가 `acting` 규칙을 놓친 원인은 규칙이 `video-prompt/SKILL.md:10`(§0 첫 줄)과 `tasks.md` 13행에만 있고 `live-action.md:21`("If newly written, open `acting`")는 표 안의 짧은 문구라 묻힌다. 고침: `kit/skills/video-prompt/live-action.md` 파일 맨 위(3줄 근처 "Do not open acting in a question turn" 바로 뒤)에 "On the turn that writes the prompt, open `acting` before CHARACTER_ACTING." 한 줄 추가.
총평: 질문·반영은 정확, 프롬프트 턴에 acting 미개방으로 부분.
