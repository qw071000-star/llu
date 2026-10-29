# real9-C10 영상, 일부만 답함 3-3 (3턴) — PASS 2 / 부분 1 / FAIL 0 (real8: PASS 3 / 부분 0 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `video-prompt` SKILL + `live-action.md` + 컷 카드 3-3·정본·OK 3-3 시작 이미지 카드. 8항목(사건 수 3개, 돌아서는 쪽·끝 프레임, 손 `the screen-right hand, nearer the sign`, 시선, 타이밍, 연기 양 끝, 대사 유무, 앞뒤 이음새)을 제안값+이유로 한 묶음. 길이·모델·소리·카메라 고정은 "기본값으로 씀", 렌즈는 "시작 이미지의 50mm(약 47°)"로 묻지 않음. `acting`은 질문 턴이라 열지 않음(routing 부합) |
| 2 | PASS | 망원을 쓰면 시작 이미지(`job-ff-3-3`, 50mm)와 부딪친다고 짚고 "1. 새 시작 이미지를 망원으로 / 2. 기존 유지"를 한 번 묻는 것(시나리오가 PASS로 허용). 대사 없음·나머지 제안값을 컷 카드 3-3 [1][3]~[6]에 `(제안값)`으로 기록(diff 확인). 프롬프트는 3턴로 미룸 |
| 3 | 부분 | 내용은 PASS: 15블록 전문 코드블록 하나, `[OPTICS]`는 `Diagonal field of view about 47°` + 관찰 결과 3개 + 심도(mm 없음), 의상(girl)·LIGHT LOCK 글자 그대로, 대사 없음 → `No dialogue … Sound effects only`, `Exactly one person is visible`, 손은 `the screen-right hand, nearer the sign`(검사 후 `her right hand` 류를 sed로 고침), `acting` 열어 `CHARACTER_ACTING`(목표·손의 일·몸·눈·양 끝 failed take). 블록 밖에 모드·참조 2·모델·480p·8초·16:9·소리·폴더. 감점: 검사 방법을 찾느라 `higgsfield-generation/SKILL.md`를 `grep`으로 열고 `check_prompt.py --help`를 돌림(프롬프트만 쓰는 턴, G7), 검사 호출이 `cd … && pwd && python3 … --help; grep …` 합성 명령(지침 "cd·&& 없이 단독 Bash"와 어긋남). 원인은 키트(아래 결함) |

검사기: `check_prompt.py --kind video --refs 2 --seconds 8 --must-include girl+light` → `OK — video 프롬프트 5484자, 걸린 항목 없음`
추가 발견:
- `[CHARACTER_ACTING]`에 `so she can tell Grandpa for certain`로 화면에 없는 인물 이름이 들어감. 생성 모델이 할아버지를 화면에 끌어올 위험(검사기는 못 잡음). 플레이어도 "연기 목표의 한 단어일 뿐"이라고 스스로 주의로 적음.
- 5,484자는 5,500자 한도에 16자 남음(WARN 직전).
- 3-2 끝 자리가 정본에 없어 가정했음을 사용자에게 알림(좋음).
키트 결함:
- `kit/instructions.md:54-55`의 검사 명령 두 줄에 `--must-include` 플래그가 없다. 같은 항목(53줄)은 "고정 문장은 `--must-include`로"라고만 쓴다. 플레이어가 플래그 문법을 찾으려 `--help`와 `higgsfield-generation/SKILL.md` grep을 함. 고칠 곳: 두 명령 끝에 `[--must-include tmp/고정문장파일]`을 붙인다.
총평: real8 PASS 3에서 후퇴(3턴 검사 절차만 부분, 프롬프트 품질은 그대로). G1: mcp__ 없음, 생성 없음.
