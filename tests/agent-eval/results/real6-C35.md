# real6 C35

**PASS 2 / 부분 0 / FAIL 0** (real5 PASS 2 유지)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `video-prompt/SKILL.md`만(`fixes.md` 안 염); 승인 컷 → 새 테이크 질문; 구간이 이미 동작 전체라 시작을 0:03으로 당겨 5초로(길이 10초는 정본과 어긋나 제외); 생성 없음 |
| 2 | PASS | `job-v-2-1` 카드 대비 diff: 두 줄만 변경 `0:04–0:08 … settle` → `0:03–0:08 … taking the full five seconds … finished in under three seconds = failed take`; 사건 수 그대로; 위험 목록; 생성 안 보냄 |

## 검사기
내 실행(`--kind video --refs 3 --seconds 8 --must-include grandpa+bag+light`): `OK — video 프롬프트 4207자, 걸린 항목 없음`

## 추가 발견
G1(mcp 호출·생성) 위반 없음, RUN 밖 읽기 없음. 전문을 답에 내지 않고 파일(`2-1_v2.txt`, 리포 루트)로 둠(지침 '바뀐 줄만 전 → 후' 허용). 임시 파일을 루트에 남김(경미).

## 키트 결함
없음.
