# real13-C23 의상 수정 + 의상 참조 이미지 (2턴) — PASS 2 / 부분 0 / FAIL 0 (real11: PASS 2 / 부분 0 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | "5번 인물 시트 고치기로 진행합니다." `character-edit.md` 엶(`character.md`도 엶), CH-002 `job-ch002` 기준, 참고 사진 `job-ref-coat`의 내용(무릎 위 길이·토글 4·후드)을 읽음. 질문 3개(여밈 / 후드 / 주머니, 모두 제안·이유, 참고 사진에 안 보이는 주머니는 "추정"). 새 요소 `char_girl_coat_v1`, 기존 상태 보존. 기본값 줄에 속옷·신발 유지 |
| 2 | PASS | 틀 1(참조 있음): 권한 문장 3개 `Reference image 1 controls identity…` / `Reference image 2 controls only the design, cut, length, material and details of the duffle coat.` / `Do not transfer the face, body, pose, background or lighting from reference image 2.` 목선 3곳: REMOVE `At the neckline, only the navy school uniform collar is visible…`, PRESERVE LEFT `Its clothes change fully: …`, ONLY CHANGE `including the neckline of the headless panel`. GONE(노란 우비·노란 후드·플랩 주머니) = LEFT `no …` 목록 일치. 교복·흰 양말·빨간 장화 유지. 얼굴 재묘사 없음. 코트 4요소(길이·여밈·후드·주머니)+`No profession-signaling props`. `LEFT and RIGHT are SCREEN directions…` 포함. 블록 밖 전 → 후, 위험 5줄. registry 초안(제안값) 기록(diff) |

검사기: `--kind image --refs 2` → `OK — image 프롬프트 2833자, 걸린 항목 없음`
추가 발견: t1이 sim 결과표의 `job-ref-coat` 설명을 인용하면서 `[TOOL]` 줄을 적지 않음(플레이어 규칙 4, 키트 아님).
키트 결함: 없음. 통합된 `character-edit.md`의 목선·GONE 일치 규칙이 정확히 지켜짐.
총평: PASS 2.
