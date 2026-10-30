# real8-C36 — 레지스터와 부딪치는 연기 ("웃게")

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | reads: production-session SKILL·video-prompt SKILL·ok-cuts(2-2 시작 이미지 카드, 목록표). `acting` 안 엶(질문 턴). "2-1 OK 이유가 '기대 안 하는 얼굴'이라 요청과 반대입니다" 먼저 짚음(1), "살짝"을 "입은 다문 채 입꼬리만, 이는 보이지 않고"로 `decisions.md` §5 범위 안에 둠(3), 양 끝 "무표정 ↔ 입꼬리만 살짝 웃음"(7), 이 컷만인지 질문, 기본값 줄·시작 보고, 생성 없음. real7의 미달(2-1 연기 미지적) 해소 |
| 2 (그대로, 프롬프트 턴) | PASS | `acting/SKILL.md`·`live-action.md`·`cut-card.md` 엶. 코드블록 1, 블록 밖 모드·참조 3·모델·해상도·길이·폴더, 위험 8, 연기 `teeth or lifts the cheeks high = failed take`·`smile appearing within one second = failed take`, 손 `the screen-left hand, nearer the persimmon tree`. `cuts/2-2.md` v0 신규 + `(제안값)`. 생성 없음, "보내" 요청. `tmp/` 삭제 확인 |

검사기(내 실행, `--kind video --refs 3 --seconds 8`, must-include grandpa+bag+light): `WARN  길이 5730자. 5,500자 이하가 안전했다…` / `— FAIL 0 · WARN 1 · 5730자`. 플레이어는 숫자를 그대로 적고 이유(고정 문장·연기 양 끝 빼면 안 됨)를 붙임 → 허용.
추가 발견: 없음.
키트 결함: 없음(real7의 `must-ask.md` "OK 이유 칸" 수정이 효과).
7회차 대비: PASS 1 / 부분 1 → PASS 2.
총평: PASS 2 / 부분 0 / FAIL 0.
