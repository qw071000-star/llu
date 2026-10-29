# real13-C04 인물 시트 의상 수정 (2턴) — PASS 2 / 부분 0 / FAIL 0 (real12: PASS 1 / 부분 1 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | "5번 인물 시트 고치기로 진행합니다." `image-prompt`+`character-edit.md`, CH-001 카드 기준 편집. 질문 4개: 적용 범위(새 상태 `char_grandpa_winter_v1`, 이유 2-1~3-1이 가을 의상 사용) / 새 의상 머리부터 발끝(길이·여밈·칼라·주머니) / 지울 것과 목선 / 의상 참조 이미지 없음. 기본값 한 줄 있음 |
| 2 | PASS | 틀 1 전문. 목선 3곳: REMOVE `At the neckline, only the white shirt collar…`, PRESERVE LEFT `Its clothes change fully: …`, ONLY CHANGE `including the neckline of the headless panel`. GONE 목록(올리브 작업 점퍼·가슴 덮개 주머니·단추 앞섶) = LEFT 줄의 `no …` 목록과 일치. 얼굴 재묘사 없이 IDENTITY 보존 문장만. 새 옷 4요소(길이 knee, 토글 4개, 후드, 패치 주머니 2) + `No profession-signaling props.` `LEFT and RIGHT are SCREEN directions…` 포함. 블록 밖 "전 → 후" 5줄, 위험 5줄. registry `초안(제안값)` 기록(diff), 사용자 말만 "사용자 답" |

검사기: `--kind image --refs 1` → `OK — image 프롬프트 2592자, 걸린 항목 없음`
추가 발견: 없음. 목선·GONE 일치 규칙(통합된 `character-edit.md` 규칙)을 지킴.
키트 결함: 없음.
총평: real11보다 개선, PASS 2.
