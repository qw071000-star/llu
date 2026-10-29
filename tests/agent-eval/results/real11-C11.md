# real11-C11 배경 영상 1-1 (+C26 4~6턴) (6턴) — PASS 5 / 부분 1 / FAIL 0 (real9: PASS 6 / 부분 0 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | "1-1 배경 영상(14번)으로 이해하고 진행합니다." `video-prompt` SKILL + `background.md`. 구름 움직임·가지 움직임·Keep을 제안값+이유로 3개. 카메라 고정·소리·길이는 "기본값으로 씀". 시작 이미지 `job-ff-1-1` 앎 |
| 2 | 부분 | 사용자 값 3개가 정본·시작 이미지와 다르다고 짚음(10초↔컷당 8초, 소리 없음↔효과음, 감나무 잎↔잎 없음) + "조금" 양 제안. 내용은 PASS. **감점:** 질문만 하는 턴인데 `cut-card.md`를 열어 `project/cuts/1-1.md`를 새로 만듦(`git status`: `?? project/cuts/1-1.md`). `kit/context/tasks.md` §3 "On question-only turns do not open `cut-card.md` and do not create card files"에 어긋남. 다만 `kit/instructions.md` 끝줄 "Before ending the turn: check that the answers you received are written on the cut card"가 반대로 시키므로 키트 모순(아래) |
| 3 | PASS | 4문단 Camera / Motion / Keep / Silent. 이미지 재묘사 없음, 움직임은 %(전진 3%, 구름 2%, 가지 <1%), 끝 상태·페이드 없음. 정본과 다른 점(10초, 무음, 잎 없음)을 앞 턴에 짚음 → 시나리오 3턴 기대 충족. 카드 기록 |
| 4 | PASS | "구름 속도만 절반" `Motion` 줄 2% → 1% "전 → 후", 다른 문단 그대로(§0 표 속도 행). 검사 다시 돌림 |
| 5 | PASS | 풀 = 시작 이미지의 논 그루터기(추정)로 확인, 카메라+구름+가지+풀 = 4개가 3개 한도를 넘는다며 "가지를 빼고 풀로" 제안(background.md 허용). 생성·프롬프트 갱신 없음 |
| 6 | PASS | 해 질 녘 장면에 별 없음과 충돌 짚음, "작은 반짝임은 모델이 못 잡음", 시작 이미지에 없으면 시도 않고 후반 합성 제안(§0 별 행). 생성 없음. 앞서 못 받은 5턴 질문을 다시 상기(새 질문 아님) |

검사기:
- 3턴 `--kind video C11_t3 --refs 0 --seconds 10` → `OK — video 프롬프트 895자, 걸린 항목 없음`
- 같은 프롬프트를 `--refs 1`로 돌리면 `WARN 붙일 참조 1개인데 … 태그가 없다`. 배경 영상은 시작 이미지를 태그 없이 쓰므로 `--refs 0`이 맞음(플레이어가 설명함). 검사기 오탐 아님: 판정 영향 없음
- 4턴은 "전 → 후" 변경이라 코드블록 없음(플레이어가 저장본으로 검사, 출력 `FAIL 0, WARN 0`)
추가 발견: 4·5·6턴은 반환 파일을 안 읽고 앞 턴 맥락만 씀(적절).
키트 결함:
1. `kit/instructions.md` 마지막 줄("Before ending the turn: check that the answers … are written on the cut card") ↔ `kit/context/tasks.md:§3` 마지막 줄("On question-only turns … do not create card files")이 모순. 고침: instructions 끝줄에 "(not on question-only turns that only ask; write the card on the turn that writes the prompt)" 추가하거나 tasks 줄에 "answers already received → write them to the existing card; do not create a new one".
2. `kit/skills/video-prompt/background.md`에 "컷 카드가 없는 컷은 사용자 답을 어디에 기록하나"가 없음(카드 신설 vs 대화 유지) — 위 1과 함께 정리.
총평: 6턴 중 5턴 PASS. 2턴은 키트 모순 탓에 부분.
