# real-C11 (C11 1~3턴, C26 4~6턴)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | 부분 | background.md 열고 시작 이미지 job-ff-1-1·정본 기본값("기본값으로 씀")·움직일 것·유지할 것 질문은 맞음. 그러나 4번 "효과음: 제안 — 약한 들바람"은 정본(decisions §1 소리) 값인데 질문에 넣음(must-ask "묻지 않는다: 소리") |
| 2 | PASS | 정본 충돌 둘을 짚음: "감나무는 잎이 없는 마른 나무", "decisions §1은 컷당 8초…1-2가 0:08에 시작". 소리 없음은 사용자 말로 수용 |
| 3 | 부분 | Camera/Motion/Keep/Silent 4문단, %, 끝 상태 없음. 검사: 플레이어는 "check_prompt.py 실행이 승인되지 않아 돌리지 못"함(G7 미충족, 하네스 권한 거부). 내가 돌림: `OK — video 프롬프트 967자, 걸린 항목 없음` (--kind video --seconds 10). 컷 카드 v0 작성, (제안값) 표기 OK |
| 4 | 부분 | 구름 Motion만 3%→1.5%로 수정(맞음). 하지만 답에 "전 → 후"를 보이지 않고 "위 전→후 한 줄만 바뀌었고"라고만 씀(위에 그런 표시 없음) — 지침 3 위반 |
| 5 | PASS | 풀 추가 시 움직임 4개(>3)임을 알리고 하나 빼기를 제안(must-ask·background.md 3개 한도). 그루터기 확인, Motion 전→후 제시. 시나리오 기대(한 줄 추가+사건 늘었음 고지)보다 엄격하지만 키트 규칙상 맞음 → 기대 오류에 가까움(T3에서 카메라+구름+감나무=3이라 추가하면 4) |
| 6 | PASS | 시작 이미지에 별 없음 충돌 짚음, 모델 한계, 후반 오버레이 제안, 생성 안 함. 사소: "움직임이 5개"는 4개의 오계산 |

**PASS 3 / 부분 3 / FAIL 0**

G1 OK(mcp 미호출, [TOOL]은 sim). G4: video-prompt SKILL.md + background.md만, fixes.md 안 엶 OK.

## 키트 결함
- `.claude/skills/video-prompt/background.md:13` — 소리를 정본 값이라 묻지 말라 했지만 "대사 컷만 켬, 나머지 효과음"을 정본 소리로 보는지 불명확. 고침: "소리는 decisions 소리 줄(비대사 컷=효과음만)을 `Sound:`로 쓰고 질문에 넣지 않는다. 사용자가 '무음'이라 하면 그때만 바꾼다" 한 줄 추가.
- `.claude/skills/video-prompt/SKILL.md:48` 속도 줄 — "전 → 후 한 줄로 보인다"가 없음. 고침: 줄 끝에 "바뀐 Motion 줄을 전 → 후로 보인다" 추가.
- 하네스: acceptEdits 모드에서 `python3 check_prompt.py` 승인 거부 → G7 검증 불가(전 체인 공통). real_run.py에 `--allowedTools "Bash(python3 *check_prompt.py*)"` 추가 필요.

총평: 정본 충돌 판단은 좋으나 소리를 물었고 속도 수정에서 전→후를 빼먹음.
