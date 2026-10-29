# real7-C44 — "카메라 좀 더 가까이"

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `image-prompt/SKILL.md`·`first-frame.md`, 3-2 카드·핸드오프(자기 컷)·OK 카드. "이미 틀 2(새 시점)라서 틀 1·2 선택은 묻지 않습니다", 얼마나(1: 같은 자리·같은 75mm, 미디엄 → 미디엄 클로즈 투샷 허벅지 위까지, 이유: 가방·두 손·손녀 손이 프레임에 남음), 승인본 새 테이크 질문(2), 더 바짝이면 가방 연속성(3-4) 영향 예고, 3-1과 같은 동작 카드 [1]. 생성 없음 |
| 2 (그대로, 프롬프트 턴) | PASS | 코드블록 1(DERIVED VIEW 전문 — 6회차 누락 해소), 블록 밖 모드·참조 4(순서)·모델·해상도·저장 폴더, `전 → 후` 한 줄(샷 크기)·렌즈 같음, 승인본에 없던 `Do not inherit …`·`Nobody looks at the camera.` 추가 공개, 위험 3. 첫 검사 WARN(손 화면 쪽 없음)을 `screen-right hand, nearer the sign`으로 고침. `cuts/3-2.md` v2에 `(제안값)` 기록(git diff 확인). 생성 없음 |

검사기(내 실행, `--kind image --refs 4`, must-include grandpa+girl+bag+light): `OK — image 프롬프트 2485자, 걸린 항목 없음`.
추가 발견: 임시 파일 `ff-3-2-v2.txt`·`ff-3-2-v2-must.txt`가 RUN 루트에 남음(답에서 "보내신 뒤 지우겠습니다"). 
키트 결함: 검사용 임시 파일 위치 규칙이 없음(`image-prompt/SKILL.md:108`, `video-prompt/SKILL.md:92`는 "파일로 저장해"만). 고칠 것: 두 줄에 "임시 파일은 `tmp/`에 저장하고 검사 뒤 지운다(`project/`·리포 루트에 남기지 않는다)" 추가.
6회차 대비: PASS 1 / 부분 1 → PASS 2.
총평: PASS 2 / 부분 0 / FAIL 0.
