# real3-C20

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | image-prompt SKILL·location.md·location-edit.md. 부모 loc_busstop_road_v1(job-lc001v1), STATE. "2번에 나눠 생성. ① 형광등 켜기 → ② 해 진 직후" — 사용자가 앞세운 형광등 먼저(2회차 사소 지적이 고쳐짐). LIGHT LOCK 승계 고지, 형광등 위치·빛 성질·번짐 문장 질문. 프롬프트는 아직 안 보임 |
| 2 | PASS | LOCKED EDIT 여는 문장(lens·zero reframing), CHANGE/PRESERVE EXACTLY/ONLY CHANGE, `one state change only: off becomes on`, `lit but does NOT glow: no halo, no bloom, no light spilling onto the road…`. 장소 재묘사 없음. 해가 아직 있어 "해 진 직후" 상태는 아님을 고지 |

검사(내가): `--kind image --refs 1` → `OK — image 프롬프트 1759자, 걸린 항목 없음`.

**PASS 2 / 부분 0 / FAIL 0** (2회차 PASS 2 유지)

키트 결함: 없음. 총평: 변경 분리·번짐 방지 충족.
