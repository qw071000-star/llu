# real2-C44 — "3-2 퍼스트 프레임 카메라 좀 더 가까이"

열기는 세션 기록(`~/.claude/projects/...C44`)으로 확인했다. 메타 reads는 Read 도구만 잡으므로 Bash cat도 함께 봤다.

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | 연 것: image-prompt/SKILL, production-session/SKILL, first-frame.md(+정본, OK 카드 3-2·3-1 시작 이미지). `location-view.md` 안 엶. "모드는 틀 2(DERIVED VIEW)". 3개 질문(승인 컷 새 테이크 대체 / 75→100mm·25~30% / 남길 것)이 제안값·이유 포함, 3-1→3-2 이음새 언급. 생성 없음 |
| 2 ("그대로", 프롬프트 턴) | PASS | G5 빈칸 없음, G9 `room at screen right`·`screen left` 화면 기준, 블록 밖에 모드·참조 4·모델·해상도·폴더 있음. G7 검사기 실행 기록 있음(check_prompt.py 4번). 틀 2 문장 `Do not inherit its camera angle…`을 CAMERA 앞에 넣음, `previous take` 표현 없앰. 경미: 코드블록에는 전/후 CAMERA 두 줄만 있고 전문은 RUN 밖 임시 파일(`scratchpad/ff32_v2.txt`)에만 있음 / 끝에 위험 1 추가 여부를 다시 물음 |

검사기(`--kind image --refs 4 --must-include`, 채점자 재실행): `OK — image 프롬프트 2497자, 걸린 항목 없음`

지난 회차 대비
- FAIL(검사 미실행) → 고침: 실제로 돌림(settings 허용 + 이번엔 허용).
- FAIL(`the previous take`, Do-not-inherit 누락) → 고침: `first-frame.md:26`에 "틀 2 고유 문장은 OK 카드에 없어도 넣는다"가 생겼고 플레이어가 따름.

추가 발견: 임시 파일을 RUN/tmp가 아니라 세션 scratchpad에 씀(실제 Claude Code라 어쩔 수 없음, 감점 안 함).

키트 결함
- `.claude/instructions.md:18` 규칙 3("바뀌는 줄만 전 → 후, 전문은 붙여 넣을 때만")과 `:51` 출력("새 프롬프트: 코드블록 하나에 전문")이 부딪친다. 플레이어는 규칙 3을 따라 전문을 안 보였다. → 51줄에 "확정 프롬프트를 고친 경우는 전 → 후 줄과, 사용자가 보내기 전엔 전문 코드블록도" 중 하나로 명시.

총평: PASS 2 / 부분 0 / FAIL 0 (지난 회차 PASS 1 / FAIL 1).
