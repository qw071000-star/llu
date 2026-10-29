# 컷 카드 — 총괄 → 컷 세션

Write using only this template. Do not open other cut cards as format examples. [1] events: `video-prompt` §2. [4] lens °: 35mm=63 · 50mm=47 · 75mm=32 · 85mm=29. Write 3,000 characters or fewer; if over, move the old attempts in [11] to the log. Do not include other cuts, the full scenario, or trial-and-error. Who writes each field is in `SKILL.md` §1. When the number of events or actions changes, fix the [1] completion condition in the same turn.

```text
받는 세션: [컷 번호 3-1]
카드 버전: v[N] · [날짜]

[1] 목표: [이 컷이 하는 일 한 줄] / 완료 조건: [ ]
[2] 저장 위치: 에셋 대장 폴더 표의 `[컷 번호]` 행 (ID를 여기 베끼지 않는다)
[3] 형식: 길이 [ ] · 비율 [ ] · 크롭 [ ] · 가림 구역 [ ] · 모델 [ ] · 소리 [ ]
[4] 카메라: 위치(화면 쪽 + 물건) [ ] · 높이 [ ] · 방향 [ ] · 고정/움직임 [종류·속도·양]
    렌즈: [시작 이미지의 mm] = 대각 화각 [ ]° (`video-prompt` §2 환산표) · 관찰 결과 [ ] · 심도·초점 [ ]
[5] 인물 (인물마다)
    시작(0:00): [위치(화면 쪽 + 물건) · 자세 · 하던 동작 · 손]
    끝(마지막 프레임): [위치 · 자세]
    동선: [경로 · 지나가지 않는 구역 · 걸음 속도]
    시선: [0:00–0:0a 대상 → 0:0a– 대상] · 반응하지 않을 사람: [ ]
    소품: [위치 · 상태 A → 상태 B · 어느 손(화면 쪽 + 물건)]
[6] 타이밍: [0:00–0:0a 주요 액션] / [대사 원문 · 횟수 · 구간] / 마지막 프레임: [ ]
    이음새: 앞 컷에서 이어받는 것 [ ] / 다음 컷 첫 프레임과 맞출 것 [ ]
[7] 참조: [ID · 역할 · 권한] (줄마다 하나)
    가져온 OK: [번호 종류 — 요소(블록)] (없으면 "없음". [1]에 "3-1과 같게"처럼 다른 컷이 있으면 그 OK)
[8] 고정 설명문: [에셋 대장 항목 이름만. 예: CH-001 WARDROBE · PR-001 · LC-001-V1 LIGHT LOCK]
[9] 이 컷에 적용되는 확정 사항: [decisions.md의 해당 줄만]
[10] 난 실패 → 막는 문장: [이 컷과, 가져온 OK에서 실제로 났던 실패만. 예상 위험은 생성 전 위험 목록에]
[11] 이전 시도: [job — 승인/거절/보류 — 이유 한 줄]
[12] 확정 프롬프트: [OK 대장 카드 이름(3-1 영상)과 job. 전문은 그 카드에만 둔다]
```

Example of filled fields (made-up values; look at the format only):

```text
[3] 형식: 길이 6초 · 비율 16:9 · 크롭 없음 · 가림 구역 없음 · 모델 (기본값) · 소리 효과음만 (제안값)
[4] 카메라: 위치 화면 왼쪽 문 옆 · 높이 눈높이 · 방향 화면 오른쪽 창 · 고정
[5] 인물 남자 — 시작(0:00): 화면 오른쪽 창가에 서서 우산을 쥠, the screen-left hand, nearer the door / 끝: 문턱 (제안값)
[6] 타이밍: 0:00–0:03 우산을 편다 / 대사 없음 / 마지막 프레임: 문턱에 선 옆모습
[11] 이전 시도: job 1a2b3c4d — 거절 — 우산이 두 개로 보임
```
