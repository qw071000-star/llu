# real9-C13 "3-1의 색감과 질감으로 3-5 퍼스트 프레임" (2턴) — PASS 2 / 부분 0 / FAIL 0 (real8: PASS 2 / 부분 0 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `image-prompt` SKILL + `first-frame.md` + `ok-reuse.md` + OK 대장 3-1 시작 이미지 카드. "3-1 프롬프트에는 색·질감 문장이 없어서 색은 이미지에서 옵니다. 그래서 질감 문장은 새로 쓰지 않습니다"(문장 지어내지 않음), 3-1 시작 이미지(`job-ff-3-1`)를 색 참조로 붙이고 인물·구도·빛은 안 가져옴. 카메라가 달라 틀 2. 시점 사용 컷 / 카메라 / 손 동작 / 가방 안쪽 / 3-4 이음 / 빛(화면 기준) 6항목을 제안값+이유로. 가방 열림(`decisions.md` §6)·인원 1명은 정본에서 제시 |
| 2 | PASS | 틀 2 전문. 권한 줄 `<<<image_ok_3_1>>> controls only colour, grade, contrast and texture. Never take its subjects, composition, people or light direction.`(ok-reuse.md:31과 글자 일치), `DO NOT TRANSFER`에 색 참조의 손녀·시간표·구도 명시, 참조 4개=태그 4개. PROP 고정 설명문+`Except:` 열림 줄, WARDROBE·LIGHT LOCK 글자 그대로, 클로즈업에 감나무가 안 보여 `the bench end nearer the persimmon tree` 보조. `Exactly one person is visible`. 위험 7개, 카드 `project/cuts/3-5.md` 신규(제안값), 생성 안 함 |

검사기: `check_prompt.py --kind image --refs 4 --must-include bag+light` → `OK — image 프롬프트 2847자, 걸린 항목 없음`
추가 발견: 2턴에 `check_prompt.py --help | head -30`을 돌려 문법을 확인함(C10과 같은 원인, 아래 결함). 컷 목록 3-5 줄은 고치지 않고 제안만(규칙 부합).
키트 결함: `kit/instructions.md:54-55` 검사 명령에 `--must-include` 플래그 자리가 없어 `--help`를 부름(경미). 고칠 곳은 C10과 같다.
총평: real8과 같은 PASS 2. G1: mcp__ 없음, 생성 없음.
