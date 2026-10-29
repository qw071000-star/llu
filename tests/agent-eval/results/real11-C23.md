# real11-C23 의상 수정 + 의상 참조 이미지 (2턴) — PASS 2 / 부분 0 / FAIL 0 (real9: PASS 2 / 부분 0 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `character-edit.md`, 기준 `job-ch002`(CH-002 카드). 앞 여밈·후드·주머니·적용 범위(새 상태 `char_girl_duffle_v1`)를 제안값으로 4개. 우비만 바뀌고 교복·양말·장화는 그대로라고 확인. 남색 코트와 남색 교복이 섞이는 위험도 사전 고지. 프롬프트는 안 보임(답이 질문 턴) |
| 2 | PASS | 틀 2가 아닌 참조 있는 틀 1: 참조 2개(시트, 코트). 권한 줄 3개(`Reference image 1 controls …`, `Reference image 2 controls only the design, cut, length, material …`, `Do not transfer the face, body, pose, background or lighting from reference image 2.`). 목둘레 3곳(REMOVE `At the neckline`, PRESERVE LEFT `Its clothes change fully`, ONLY CHANGE `including the neckline of the headless panel`). REMOVE의 GONE 목록(yellow raincoat · hood · flap pockets) = LEFT 줄 `no …` 목록과 같은 3개. 교복·흰 양말·빨간 장화 유지. 얼굴 재묘사 없음. 생성 안 함 |

검사기: `--kind image C23_t2 --refs 2` → `OK — image 프롬프트 2940자, 걸린 항목 없음`
추가 발견: 1턴에 `sim/higgsfield.md`를 읽고 `job-ref-coat`의 내용("남색 울 더플코트, 무릎 위 길이, 토글 4개, 후드")을 답에 썼으나 `[TOOL]` 줄이 없음(플레이어 규칙 4, 경미). 시트 해상도 2k는 `character.md` 규칙으로 "기본값으로 씀"에 적음(`character-edit.md`에는 근거 없음 — C04 키트 결함 참고).
키트 결함: C04와 같음(`character-edit.md` 해상도 줄 없음).
총평: real9와 같은 PASS 2.
