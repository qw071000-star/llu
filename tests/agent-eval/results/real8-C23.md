# real8 C23

**PASS 2 / 부분 0 / FAIL 0** (real7 PASS 2 유지)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `character-edit.md`; 기준 `job-ch002`+참조2 `job-ref-coat`; 5개 항목(새 상태·없앨 옛 항목·재단·목둘레·범위) 제안값; 우비만 교체(교복·흰 양말·빨간 부츠 유지); 생성 없음 |
| 2 | PASS | `<<<image_1>>>` 권한 두 줄+`Do not transfer the face, body, pose, background or lighting from <<<image_2>>>.`; 목둘레 3곳(`At the neckline`, `Its clothes change fully`, `including the neckline of the headless panel`); GONE 목록(yellow raincoat/hood/flap pockets) = LEFT 줄 `no …` 목록; `No profession-signaling props.` 있음(real7 지적 해소); 얼굴 재묘사 없음; 위험 5개; 바뀐 값 전 → 후; 첫머리에서 T1 오기 정정 |

## 검사기
내 실행 `--kind image --refs 2`: `OK — image 프롬프트 2781자, 걸린 항목 없음`.

## 추가 발견
G1(mcp 호출·생성) 위반 없음, RUN 밖 읽기 없음. T1에 '`job-ch-ref-coat`가 아니라 `job-ref-coat`'라는 불필요한 오기(T2에서 정정). `job-ref-coat`의 내용(sim: 무릎 위 길이·토글 4개·후드)을 읽지 않고 '볼 수 없어 추정'(엉덩이 길이·후드 내림·패치 주머니)으로 씀 — 참조가 이기도록 쓴 문장이 있어 결과 영향은 작음(시험 환경 사정). `tmp/` 삭제 확인.

## 키트 결함
없음.

## 총평
의상 수정 틀 1 충실.
