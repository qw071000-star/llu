# real7 C23

**PASS 2 / 부분 0 / FAIL 0** (real6 PASS 2 유지)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `character-edit.md`; 기준 `job-ch002`, 참조 2개(시트·`job-ref-coat`); 4개 항목(새 상태·재단·없앨 옛 항목/목둘레·적용 범위) 제안값; 우비만 교체(교복·양말·장화 유지); 생성 없음 |
| 2 | PASS | 권한 줄 세 개 + `Do not transfer the face, body, pose, background or lighting from reference image 2.`; 목둘레 3곳(`At the neckline`, `Its clothes change fully`, `including the neckline of the headless panel`); GONE 목록(yellow raincoat / hood / flap pockets) = LEFT 줄 `no …` 목록; 얼굴 재묘사 없음; 위험 목록; 바뀐 값 전 → 후 |

## 검사기
내 실행 `--kind image --refs 2`: `OK — image 프롬프트 2739자, 걸린 항목 없음`.

## 추가 발견
G1(mcp 호출·생성) 위반 없음, RUN 밖 읽기 없음. 턴1에서 `sim/higgsfield.md`의 `job-ref-coat` 설명을 답에 인용하면서 `[TOOL]` 줄이 없고 '시험 환경 표에서 찾아 읽었습니다'라고 사용자에게 말함(플레이어 규칙 4 어긋남). 사용자가 job을 직접 말했는데도 '대화에 없는 job'이라 적음(문구 오류). `character-edit.md` 규칙의 `No profession-signaling props.`가 프롬프트에 없음(재단 네 가지 중 칼라·주머니는 있으나 이 문장 누락, 경미).

## 키트 결함
없음.

## 총평
의상 수정 틀 1 충실, 시험 환경 언급 누설만 흠.
