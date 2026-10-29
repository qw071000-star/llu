# real14-C35 승인 영상 속도 — "너무 빨라, 천천히" 2-1 (2턴) — PASS 2 / 부분 0 / FAIL 0 (real13: PASS 1 / 부분 1 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | 첫 줄 "15번 영상 결과 고치기로 진행합니다." `video-prompt` SKILL만 열음(`production-session` SKILL 안 엶, 존재하지 않는 `cuts/2-1.md` 시도도 없음). 2-1이 승인 컷(`job-v-2-1`)이라 새 테이크로 대체할지 묻고(Q3), 엄지 구간이 이미 4초라 "앞당길지 영상을 늘릴지"를 제안값으로 물음(Q2, `video-prompt/SKILL.md:53` "already 4+ seconds → ask whether to start earlier or lengthen"). 어느 움직임인지 후보 제시(추정 표기). 사건 수 그대로. 전 → 후 미리보기, draft 만료일 2026-10-31 고지. 생성 없음 |
| 2 | PASS | OK 카드 프롬프트에서 `[ACTION_TIMING]` 두 줄만 "전 → 후": `0:00–0:04 → 0:00–0:02`, `0:04–0:08 → 0:02–0:08 (longer interval than before) — … taking the full 6 seconds. The move finished in under 5 seconds = failed take.` 두 구간의 초를 모두 적고 나머지 블록·`CHARACTER_ACTING` 그대로. 전체를 저장해 검사 실행. 카드 `cuts/2-1.md` v0 신설(값을 쓰는 턴). 낙엽은 건드리지 않고 알림. 승인 컷 덮어쓰기 없음. "이 프롬프트로 영상을 보낼까요?" |

검사기(플레이어가 지운 임시 파일을 OK 카드+두 줄 수정으로 재구성): `python3 kit/skills/higgsfield-generation/check_prompt.py --kind video C35_new.txt --refs 3 --seconds 8 --must-include grandpa+bag+light` → `OK — video 프롬프트 4219자, 걸린 항목 없음`

real13 감점 해소: ① 첫 줄 누락 — 해소. ② 15번 행에 불필요한 `production-session` 열기 — 해소.

추가 발견: 깜빡임 구간을 4초 → 2초로 줄였다(엄지 구간을 앞당긴 부수 변경). 답에서 "깜빡임 구간은 4초에서 2초로 줄였습니다"라고 알려 숨기진 않았다.

키트 결함: 없음.

총평: 속도 수정 값이 규칙표와 정확히 맞고 real13의 두 감점이 해소돼 PASS 2.
