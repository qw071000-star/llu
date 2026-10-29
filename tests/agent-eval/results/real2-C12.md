# real2-C12

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | production-session SKILL → ok-reuse.md → video-prompt SKILL·live-action.md. 3-1 영상 카드 하나, ACTION_TIMING·PHYSICS·속도 문장 나열, "카드 [4]의 렌즈 35°와 시작 이미지 75mm(약 32°)가 다릅니다. 시작 이미지를 따르고", 입 잠금·카메라 응시 줄 이월. 질문 5개 한 묶음 |
| 2 | 부분 | 내용은 PASS: 코드블록 하나+블록 밖 모드·참조4·모델·해상도·길이·폴더, 본문에 "3-1"/previous 없음, 컷 카드 `가져온 OK: 3-1 영상 — 모션(ACTION_TIMING, PHYSICS, 속도 문장)`, 렌즈 35°→32° 고침. 그러나 G7 미충족: "검사 스크립트는 실행하지 못했습니다. Bash 실행이 승인되지 않았습니다" → 보이기 전 검사 없음. 내가 돌림: `--kind video --refs 4 --seconds 8 --must-include grandpa+girl+bag+light+motion_3-1` → `OK — video 프롬프트 5369자, 걸린 항목 없음`. 사용자에게 임시 파일 절대경로(scratchpad)를 노출함 |

**PASS 1 / 부분 1 / FAIL 0** (지난 회차 PASS 2: 지난 회차는 하네스 거부를 감안해 PASS로 쳤고, 이번엔 G7을 기준으로 삼아 부분)

acting/SKILL.md는 2턴(프롬프트 쓰는 턴)에 열었고 CHARACTER_ACTING을 새로 써서 정당. 이웃 컷 카드·핸드오프 안 엶.

## 키트 결함
- `.claude/skills/video-prompt/SKILL.md:92` — 명령 형태 제약이 없어 플레이어가 `--allowedTools` 패턴과 다른 형태(경로·cd·합성 명령 추정)로 돌려 거부당함. 고침: "명령은 위 한 줄 그대로 단독 Bash 호출로, cd·`&&`·파이프·절대경로 없이" 한 구절 추가(image-prompt/SKILL.md:108도 같이).
- 하네스: real_run.py 허용 패턴을 `Bash(python3 *check_prompt.py*)`로 넓히고, 메타에 Bash 명령 문자열도 기록(Read가 아닌 cat 읽기·검사 실행 여부를 확인할 수 없음).

총평: 3-1 모션 이월·렌즈 충돌 고지 모범. 검사 미실행만 감점.
