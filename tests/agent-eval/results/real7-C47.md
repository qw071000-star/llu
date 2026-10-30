# real7-C47 — 두 인물 접촉 ("손 잡게")

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `video-prompt` SKILL·`live-action.md`·`ok-reuse.md`·OK 3-1 영상 카드(카드 [1] "3-1과 같은 동작"이라 `routing.md` 표 3행 해당). `acting` 안 엶(질문 턴). 3-1과 다른 동작이라 이 컷만 고칠지(1), 어느 손: 할아버지 `screen-right hand, nearer the sign` / 손녀 `screen-left hand, nearer the bench`, 다른 손은 닫힌 가방 위(2), 접촉 모양·할아버지 반응 절제(3, `decisions.md` §5), 사건 3개 한도·4개면 샷 나누기(4), 렌즈 카드 35° ↔ 시작 이미지 75mm 불일치 짚음. 생성 없음. 경미: 연속성 표의 "두 손을 위에"와의 충돌을 그 말로 명시하진 않음 |
| 2 (그대로, 프롬프트 턴) | PASS | `acting/SKILL.md`·`cut-card.md` 엶. 코드블록 1(15블록, `PRE_SHOT_CONTINUITY` 포함), 블록 밖 모드·참조 4·모델·해상도·길이·소리·폴더, 위험 6, 연기 양 끝 `tears … bright smile = failed take` / `pulling away … clasping back … no reaction at all = failed take`, 손 화면 쪽 + 물건. 길이 WARN을 숫자 6,291자와 이유(인물 2·참조 4, 권한 설명·눈 묘사 −400자)로 남김(`live-action.md:31` 허용). 카드 `cuts/3-2.md` [1]·[3]~[6]을 `(제안값)`으로 갱신(git diff), 컷 목록·이음새는 총괄에 올릴 것으로. "보낼까요?" 생성 없음 |

검사기(내 실행, `--kind video --refs 4 --seconds 8`, must-include grandpa+girl+bag+light): `WARN  길이 6291자. 5,500자 이하가 안전했다. 남기려면 이 숫자를 그대로 적고 이유를 쓴다` / `— FAIL 0 · WARN 1 · 6291자`. 숫자 일치.
추가 발견: 6회차(5,998자)보다 길어짐(6,291자). 프롬프트 초안과 `3-2_must_include.txt`를 `project/log/`에 남김(정본 로그에 쓰레기 파일).
키트 결함: 임시 파일 위치 규칙 없음(C44와 같음). `video-prompt/SKILL.md:92`에 "임시 파일은 `tmp/`에, 검사 뒤 지운다".
6회차 대비: PASS 2 유지.
총평: PASS 2 / 부분 0 / FAIL 0.
