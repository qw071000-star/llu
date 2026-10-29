# real14-C25 같은 쪽 클로즈업 새 시점 — 시간표 표지판 (2턴) — PASS 1 / 부분 1 / FAIL 0 (real13: PASS 1 / 부분 1 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | 첫 줄 "7번 장소 새 시점으로 진행합니다." `image-prompt` SKILL·`location.md`·`location-view.md`만 열음. "같은 쪽에서 표지판만 확대하는 작업이라 계보는 PROP, 틀은 C", "반대쪽 시점이 아니라서 LIGHT LOCK은 그대로". 질문 4개 한 묶음(계보·이름 / 화면 절반 기준과 위치 / 남길 것·밀어낼 것 / 판면 방향·모양). 모델·해상도·폴더·렌즈·글자 불가는 "기본값으로 씀". 프롬프트·생성·정본 변경 없음 |
| 2 | 부분 | 틀 C. `Do not inherit its camera angle, framing or composition.`, `Move in from the same side and along the same line of sight; no reverse angle and no view from behind.` 있음, `newly observed direction … not a horizontal mirror`는 안 씀. `text not legible` 두 번, 랜드마크 2개(콘크리트 벽·양철 지붕 모서리). LIGHT LOCK 글자 그대로. 블록 밖 모드·참조·모델·해상도·폴더·위험 6줄. registry `LC-001-V2` 초안(제안값) 기록(diff). 감점: ① `Use <<<image_1>>> as the sole geometry and design authority; do not inherit from discarded variants.`(`location-view.md:22` 공통 규칙)이 없다. ② 같은 공통 규칙이 화면 좌우를 `In this view … is at screen LEFT/RIGHT` 줄에 쓰라고 하는데 그 줄이 없다(감나무가 프레임 밖이라 화면 쪽이 LIGHT LOCK 안에만 암시). 둘 다 틀 C 코드블록에 해당 줄이 없어서 플레이어가 틀대로 쓴 결과다 |

검사기: `python3 kit/skills/higgsfield-generation/check_prompt.py --kind image C25t2_1.txt --refs 1 --must-include light` → `OK — image 프롬프트 2062자, 걸린 항목 없음` (검사기는 위 두 줄을 못 잡는다)

real13 감점 해소: ① 질문 턴 첫 줄 누락 — 해소. ② `sole geometry` 문장 누락 — 미해소(real13은 추가 발견으로만 적고 PASS를 줬으나, 이번엔 `In this view` 줄까지 빠져 부분으로 친다).

추가 발견: 프롬프트에 `Palette of roughly 80%…`를 넣고 FINISH·ERA까지 넣어 틀 C의 "Parent's finish and era lock"보다 많이 넣음(해는 없음).

키트 결함: `kit/skills/image-prompt/location-view.md:22` — 두 공통 문장(`sole geometry`, `In this view …`)이 산문 불릿에만 있고 틀 C(약 76~100행) 코드블록에는 없다 → 틀 A·B·C 코드블록 첫 문단 뒤에 `Use <<<image_1>>> as the sole geometry…` 줄을, 틀 C 끝에 `In this view [landmark] is at screen [side]…` 줄을 직접 넣는다.

총평: 질문 턴 형식은 고쳐졌으나 틀 C에 줄이 빠진 탓에 2턴이 부분으로 남았다.
