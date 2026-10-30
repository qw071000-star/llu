# real16-C44 "카메라 좀 더 가까이" (2턴) — PASS 9 / 부분 1 / FAIL 0

> 채점: tests/agent-eval/runs-real16/C44/out/turn*.md·meta.json, git diff. 기준: grader-rules.md, scenarios.md(G1–G9 + C44), kit/.

## 턴별 판정표

| 턴 | 기대 항목 | 판정 | 근거 |
|---|---|---|---|
| 1 | 첫 줄 | PASS | "11번 퍼스트·끝 프레임으로 진행합니다." |
| 1 | 틀 2(DERIVED VIEW) 판단·승인본 job-ff-3-2 확인 | PASS | "3-2는 이미 시작 이미지 job-ff-3-2가 승인돼 있고 … 틀 2(새 시점)로 카메라 문장만 바꾼 새 프롬프트" — location-view.md 안 엶 |
| 1 | 얼마나 가까이: 값 제안(샷 크기·mm) | PASS | "75mm → 100mm, 미디엄 투샷 → 미디엄 클로즈 투샷 … 이 이상 당기면 손녀의 손이나 가방이 잘립니다" |
| 1 | 승인 컷 변경 → 새 테이크 여부(must-ask) | PASS | "1. 승인본 처리: 제안 — 새 테이크로 만들고 … job-ff-3-2는 그대로 둡니다" |
| 1 | 3-1→3-2 이음새 | PASS | "3-1과 같은 순간이라 … 편집에서 3-1과 섞어 쓰기 쉽습니다" · 실패 위험 3 "3-1과 인물 배치가 어긋날 수 있습니다" |
| 2 | 프롬프트: 카메라 줄만 바꾸고 틀 2 고유 문장 포함 | PASS | "Do not inherit its camera angle, framing or composition." + CAMERA 줄만 교체, 나머지 승인본과 글자 일치(OK 카드 대조) |
| 2 | 검사기(G7) | PASS | `check_prompt.py --kind image tmp/3-2_ff_v2.txt --refs 4 --must-include …` 실행 후 보임. 내 재검사: "OK — image 프롬프트 2442자, 걸린 항목 없음" |
| 2 | 블록 밖 모드·참조·모델·해상도·길이·저장 + 전 → 후 + 위험 목록(G6) | PASS | "- 모드: 틀 2(새 시점) … - 저장: fld-3-2", "바뀐 값 (전 → 후)", "실패 위험 1–4" |
| 2 | 카드 [4] 기록(제안값)·생성 안 함 | PASS | diff: `샷 크기: … (제안값) · 새 테이크로 만듦, 승인본 job-ff-3-2 유지 (제안값)` · "아직 생성하지 않았습니다 … "이미지로 만들어" 또는 "보내"" |
| 2 | 답은 한국어(G2) | 부분 | 채팅에 영어 한 줄 노출: "Now the card update and cleanup." |

## 검사기 결과

C44 T2 코드블록 1개(이미지, 참조 4: 장소·할아버지·손녀·가방), must-include = grandpa/girl/bag/light 4문장:
`OK — image 프롬프트 2442자, 걸린 항목 없음` (종료 0)

## 추가 발견

- 카드 [4]에 `렌즈: 100mm (제안값; 승인본은 75mm, 대각 화각 35°)` — 환산표상 75mm=32°, 100mm=24°. 카드 원문 35°가 테스트베드 오류인데 이 체인은 그대로 이어 적음(C47은 32°로 정정).
- `Nobody looks at the camera.`는 카드 [10]·거절된 job-ff-3-2-old 근거라 추가 변경이 아님(전 → 후에 명시함).

## 키트 결함

- `kit/skills/production-session/cut-card.md:3`의 렌즈 환산 한 줄과 `kit/skills/video-prompt/SKILL.md` §2 환산표가 이중 관리(규칙 한 곳 원칙) — 한쪽을 "§2 표 참조"로 줄이면 35° 같은 오기가 줄어든다.

## 총평

틀 2 선택·카메라 줄만 교체·검사 통과까지 정확했고, 영어 진행 멘트 한 줄만 감점.
