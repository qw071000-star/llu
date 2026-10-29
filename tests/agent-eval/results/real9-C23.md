# real9-C23 의상 수정 + 의상 참조 이미지 (2턴) — PASS 2 / 부분 0 / FAIL 0 (real8: PASS 2 / 부분 0 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `image-prompt/SKILL.md`+`character-edit.md` Read; 기준 CH-002 `job-ch002` + 참조 `job-ref-coat`. "프롬프트만"이라 생성 없음. 5개 제안값(새 상태·후드/여밈·주머니·새 목둘레·적용 범위)을 한 묶음으로 묻고 "교복·흰 무릎양말·빨간 장화는 그대로" 명시. 코트·교복 둘 다 남색이라 경계 위험도 짚음 |
| 2 | PASS | 틀 2가 아닌 character-edit 틀 1(의상): `Edit reference image 1 … HEADLESS`. 권한 줄 `Reference image 1 controls … Reference image 2 controls only the design … Do not transfer the face, body, pose, background or lighting from reference image 2.` 목둘레 3곳: `At the neckline, only the navy school uniform collar …`, `Its clothes change fully: …`, `ONLY CHANGE: … including the neckline of the headless panel`. REMOVE의 GONE(yellow raincoat/hood/pocket flaps) = LEFT 줄 `no yellow raincoat, no yellow hood, no yellow pocket flaps`. 얼굴 재묘사 없음(`preserve the exact same face`만). "바뀐 값"을 전 → 후로, 위험 5개 |

## 검사기
내 실행 `--kind image --refs 2`: `OK — image 프롬프트 3022자, 걸린 항목 없음`

## 추가 발견
- G1 위반 없음. `tmp/` 삭제 확인. 대장 CH-002 아래 `초안(제안값)` 기록(규칙 4).
- 1턴에서 `sim/higgsfield.md`를 읽어 `job-ref-coat` 내용(무릎 위·토글 4·후드)을 답에 인용했으나 답 본문에 `[TOOL]` 줄은 보이지 않음(메타 부분이 파일에 없어 판정 불가, 시험 규칙 사항이라 키트 평가 밖).
- 코트 주머니는 사진에 정보가 없음을 밝히고 "추정"으로 표시함(규칙 10 충족).

## 키트 결함
없음.

## 총평
의상 수정 틀 충실, 참조 권한·목둘레 3곳·GONE 목록 일치.
