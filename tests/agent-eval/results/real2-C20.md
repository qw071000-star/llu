# real2-C20

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | image-prompt SKILL·location.md·location-edit.md. 부모 `job-lc001v1`, STATE. "시간대와 광원 켜기는 떼어 낼 수 있어서 한 생성에 하나만" 나누기 제안, 새 LIGHT LOCK 고지, 형광등 위치(화면 기준) 질문, 번짐 문장 예고. 프롬프트 안 보임. 사소: 나누는 순서를 시간대 먼저로 제안해 사용자가 앞세운 형광등과 반대(시나리오는 형광등 먼저) |
| 2 | PASS | 형광등만 먼저. LOCKED EDIT 여는 문장(lens·zero reframing), `CHANGE / PRESERVE EXACTLY / ONLY CHANGE`, `one state change only: the tube switched off becomes the tube switched on`, `lit but does NOT glow: no halo, no bloom, no light spilling onto the road…`. 장소 재묘사 없음. 해는 그대로이고 "해 진 직후 아님"을 고지. 검사 내가: `--kind image --refs 1` → `OK — image 프롬프트 1633자, 걸린 항목 없음`. 플레이어 실행 보고 |

**PASS 2 / 부분 0 / FAIL 0** (지난 회차 PASS 2 유지; 검사 실행 확인)

## 키트 결함
- `.claude/context/must-ask.md` "장소 — 같은 사진 수정" 먼저 짚는다 항목 — 나눌 때 어느 변경을 먼저 할지 규칙이 없다. 고침: "나눌 때는 사용자 말에서 주된(앞세운) 변경을 먼저로 제안한다" 한 줄 추가(경미).

총평: 변경 분리와 번짐 방지 충족.
