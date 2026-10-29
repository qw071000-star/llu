# real6 C23

**PASS 2 / 부분 0 / FAIL 0** (real5 PASS 2 유지)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `character-edit.md`만; 기준 `job-ch002`+`job-ref-coat` 2개; 여밈·후드·주머니·신발 5개 제안값; 범위(인물 설정 자체)와 색 충돌 짚음; 프롬프트 없음 |
| 2 | PASS | 권한 줄 + `Do not transfer the face, body, pose, hanger, background or lighting from reference image 2.`; 목둘레 3곳(`At the neckline`, `Its clothes change fully`, `including the neckline of the headless panel`); GONE 목록 = LEFT `no …` 목록(yellow raincoat/hood/flap pockets); 교복·양말·장화 유지; 얼굴 재묘사 없음 |

## 검사기
내 실행(`--kind image --refs 2`): `OK — image 프롬프트 3148자, 걸린 항목 없음`

## 추가 발견
G1(mcp 호출·생성) 위반 없음, RUN 밖 읽기 없음. 권한 줄이 시나리오 문구 대비 'hanger' 추가(참조 사진에 맞춘 것, 무해).

## 키트 결함
없음.
