# real13-C34 소품 지적 — "왕진 가방이 너무 새 거 같아" (2턴) — PASS 2 / 부분 0 / FAIL 0 (real11: PASS 2 / 부분 0 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | 첫 줄 "9번 소품 만들기·고치기로 진행합니다." `image-prompt` SKILL + `prop.md`만 열었다. "'새 거 같다'는 재생성 지시가 아니므로 원인과 고치는 방향을 말하고 묻습니다". 에셋 자체(PR-001)로 판단하고 범위를 질문 2로 확인, 원인은 "추정"(결과를 볼 수 없음). 고정 설명문이 바뀌면 `prop_doctor_bag_v2`로 확정하고 v1은 폐기 목록으로 옮기는 절차 제시. 원본 job이 대장에 없어 요소 ID를 수정 원본으로 쓴다고 한 줄 고지(`prop.md:24`). 사용 흔적 문장(색 바램·모서리·걸쇠 변색)을 제안값으로. 생성 없음 |
| 2 | PASS | LOCKED EDIT(`Edit <<<prop_doctor_bag_v1>>> WITHOUT reframing …`), `CHANGE / PRESERVE EXACTLY / ONLY CHANGE`, 크기 40cm·형태·갈색 계열을 PRESERVE, 배경은 `the existing background`, `no dirt, no tears`. 블록 밖에 모드·참조·모델·해상도·폴더, 고정 설명문 "전 → 후"와 v1 → v2, 위험 4개, 미확인 상태 "추정". 대장 `PR-001` 아래에 `초안(제안값)` 줄 기록(diff). 생성 안 함 |

검사기: `--kind image C34t2_1.txt --refs 1` → `OK — image 프롬프트 1365자, 걸린 항목 없음`

추가 발견: 없음. `tmp/`를 지움, G1 위반 없음.
키트 결함: 없음.
총평: real11과 같다. 결과 지적을 재생성 지시로 받지 않았고 v2 절차까지 맞다.
