# real13-C22 새 인물 시트, 정보 일부 — 60대 상인 (2턴) — PASS 1 / 부분 1 / FAIL 0 (real12: PASS 1 / 부분 1 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | 부분 | 틀 1 전문: CH-004, 첫 문단 `including the intentionally HEADLESS left panel`, `Do not add, infer, reconstruct or complete a head or face`, `mature adult bone structure with deep nasolabial folds`, `no babyface`, 나이 든 인물 문장(`lined forehead and crow's feet… reddened knuckles and short unpainted nails`), 일관성 잠금, 리얼리즘·눈 블록, 시대 금지 줄, 2k·16:9·`fld-chars`, 위험 5줄, registry CH-004 초안(제안값) 기록(말한 값만 사용자 말). 감점: 답이 "지금은 프롬프트 검사를 끝내고 임시 파일을 지운 상태입니다. 이제 결과를 정리해 드립니다."로 시작(내부 진행 문장이 샘)하고 "[4]번 인물 시트 만들기로 진행합니다."가 없음. 직업 소품 금지를 `no fish, no knife, no bucket, no basket`으로 이름까지 적음(금지어가 소환할 수 있음, 템플릿은 `unless explicitly requested`만) |
| 2 | PASS | "그대로"를 제안값 수락으로 보고 생성하지 않음: "CH-004 시트를 위 프롬프트 그대로 2k로 생성해 보낼까요?". 대사 없음으로 확정 기록 |

검사기: `--kind image --refs 0` → `OK — image 프롬프트 5165자, 걸린 항목 없음`
추가 발견: 위 직업 소품 이름 나열. t1 끝에 "대사를 하나요"와 "보낼까요"를 한 질문 묶음에 섞음.
키트 결함: 첫 줄 누락 — C01과 같은 원인(`kit/instructions.md:41`); 이번엔 검사 직후 턴이라 첫 줄 앞에 작업 로그가 샘 → `instructions.md`에 "첫 줄 앞에 아무것도 쓰지 않는다(검사·정리 이야기 포함)" 한 줄. `character.md` 템플릿의 `No profession-signaling props unless explicitly requested.`는 그대로 쓰고 소품 이름을 나열하지 말라는 한 줄을 `character.md` Rules에 추가.
총평: 시트 내용 정확, 첫 줄 누락으로 t1 부분.
