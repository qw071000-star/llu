# real-C44 — "3-2 퍼스트 프레임 카메라 좀 더 가까이"

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | reads: production-session, image-prompt, first-frame.md (+정본). `location-view.md` 안 엶. "프롬프트 쓰기 전에 확인할 것이 3개" — 승인 컷 대체 여부, 얼마나 가까이(샷 크기 한 단계, 75mm 유지), 남길 것. 이음새(3-1→3-2 한 걸음) 언급. 틀 2 선언. 카드 렌즈 35° vs 승인 75mm 불일치도 짚음 |
| 2 ("그대로", 프롬프트 턴) | FAIL | G5·G6·G9 통과(빈칸 없음, 블록 밖 모드·참조·모델·해상도·폴더, 화면 기준). G7: 검사기를 "실행 승인이 안 나서" 못 돌림(정직하게 밝힘). 채점자가 돌린 결과 아래 |

검사기(`--kind image --refs 4 --must-include bag+light+girl+grandpa`):
```
WARN  이전 샷을 가리키는 말 ['the previous take']. 새 생성에는 그 내용을 직접 쓴다
WARN  새 시점인데 'Do not inherit its camera angle, framing or composition.'이 없다. 원본 구도가 따라온다
— FAIL 0 · WARN 2 · 2443자
```
둘 다 근거 있음(CAMERA 줄에 `closer than the previous take`, 틀 2의 Do-not-inherit 문장 누락).

추가 발견: 카메라 줄만 "전 → 후"로 보이고 전문도 보임(지침 3은 전문은 붙여 넣을 때만) — 경미.

키트 결함
- `image-prompt/first-frame.md:62`는 틀 2에 `Do not inherit its camera angle…`를 요구하는데, 정본 OK 카드(`ok-cuts.md:373` 등)에는 그 문장이 없다. 지침 3("바뀌는 줄만")대로 OK 카드를 복사하다 문장이 빠졌다. → 지침 3 또는 first-frame.md에 "틀 2 고유 문장(Do not inherit)은 OK 카드에 없어도 넣는다" 한 줄 추가.
- 검사기 Bash 실행이 권한 때문에 막힘. → 키트 `.claude/settings.json`에 `Bash(python3 .claude/skills/higgsfield-generation/check_prompt.py:*)` 허용 추가.

총평: PASS 1 / 부분 0 / FAIL 1 — 질문은 좋았으나 프롬프트에서 틀 2 문장 누락·"previous take"·검사 미실행.
