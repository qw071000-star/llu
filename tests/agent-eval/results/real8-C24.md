# real8 C24

**PASS 2 / 부분 0 / FAIL 0** (real7 PASS 2 유지)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `video-prompt` SKILL+`live-action.md`만(`acting`·`ok-reuse.md`·3-1 카드 안 열림); '카드 [4]의 렌즈는 35°인데 시작 이미지는 75mm(약 32°)' 알림, 렌즈는 묻지 않음; 카드 [1] '3-1과 같은 동작·타이밍'과 지시 충돌 짚음; 9개 항목(사건 3개·대사·타이밍·끝 상태·시선·손녀/할아버지 연기 목표·손·양 끝) 제안값 |
| 2 | PASS | `acting/SKILL.md`+`cut-card.md` 열림(프롬프트·카드 쓰는 턴); `CHARACTER_ACTING` 인물마다 상대를 향한 목표·몸(무게·호흡)·눈·양 끝 `failed take`; 비트 3개; 손녀 목소리 문장 에셋 대장과 글자 그대로; `does not say a single word: no attempt to speak, no parted lips, no mouthing`; 절제 레지스터 내; 5,865자 WARN에 숫자·이유; 카드 3-2 v2에 `(제안값)` 기록 |

## 검사기
내 실행 `--kind video --refs 4 --seconds 8 --must-include grandpa+girl+bag+light`: `WARN 길이 5865자. 5,500자 이하가 안전했다 … — FAIL 0 · WARN 1 · 5865자` (플레이어가 5,865자와 이유 명시 → 허용).

## 추가 발견
G1(mcp 호출·생성) 위반 없음, RUN 밖 읽기 없음. T2의 [ACTIVE_REFERENCES] 정정('장소 요소는 안 붙임')을 스스로 알림. 카드 [8]을 고정 문장 원문에서 ID 목록으로 바꿈(대장 참조라 무해). 빈 `tmp/` 폴더만 남음.

## 키트 결함
없음.

## 총평
연기 새로 잡기·OK 미반입 충족.
