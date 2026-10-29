# real11-C06 새 소품 (2턴) — PASS 2 / 부분 0 / FAIL 0 (real9: PASS 2 / 부분 0 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `image-prompt` SKILL + `prop.md`. PR-002 매김. 크기(24×18×2cm, 가방 40cm·손바닥 기준), 재질·사용 흔적, 무게감, 나오면 안 되는 재질(플라스틱·금색·현대 금속·글씨), 상태 변화·꺼내는 손(화면 왼쪽 손 + 감나무 쪽, "추정")을 제안값+이유로 6개 한 묶음. 기본값 한 줄. 카드 파일 안 만듦 |
| 2 | PASS | 소품 틀: `isolated on a plain seamless light grey studio background … no hands, no people`, `Avoid: plastic, gold ornament …`. 에셋 대장에 PR-002 항목 신설(`(제안값)`, diff 확인). 3-4 shot-list 행은 고치지 않고 알림. 생성 안 함 |

검사기: `--kind image C06_t2 --refs 0` → `OK — image 프롬프트 755자, 걸린 항목 없음`
추가 발견: 인물이 없어 LEFT/RIGHT 문장을 안 넣었다고 밝힘(규칙 6은 사람이 있는 프롬프트만). "스튜디오 컷이라 크기가 어긋난다" 권고는 prop.md 근거.
키트 결함: 없음.
총평: real9와 같은 PASS 2.
