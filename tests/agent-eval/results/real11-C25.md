# real11-C25 같은 쪽 클로즈업 새 시점 — 시간표 표지판 (2턴) — PASS 2 / 부분 0 / FAIL 0 (real9: PASS 2 / 부분 0 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `location.md` + `location-view.md`, 부모 `job-lc001v1`. 유지할 랜드마크(정류장 벽·양철 지붕 오른쪽 끝)·프레임 밖으로 밀 것·표지판 모양(V1을 참조로 고정, 글자 안 읽힘)·배경 초점을 제안값으로 4개. 카메라(V1 위치에서 같은 시선선, 1.6m, 35mm)·빛(화면 왼쪽 그대로)은 "기본값으로 씀"에 적고 대장에 기록 |
| 2 | PASS | `Do not inherit its camera angle, framing or composition.` 있음. `Move in from the same side and along the same line of sight; no reverse angle and no view from behind.` 있음, `newly observed direction … not a horizontal mirror`는 없음(같은 쪽이므로 정답). `The sign face is hand-lettered, text not legible`, 랜드마크 1개(정류장 벽·지붕 오른쪽 끝) 유지. 화면 기준 `the shelter is at screen left and the timetable sign is at screen right of centre`, LIGHT LOCK 글자 그대로. 틀 B로 썼으나 필요한 문장이 모두 있어 PASS(시나리오 허용) |

검사기: `--kind image C25_t2 --refs 1 --must-include light` → `OK — image 프롬프트 2598자, 걸린 항목 없음`
추가 발견: 랜드마크를 1개만 남겼으나 시나리오 허용(1~3개). 프롬프트에 "MASTER GEOMETRY (as seen from across the road …)"가 감나무를 LEFT로 기술하는데 `FRAMING`은 감나무를 프레임 밖으로 둠 — `Except:` 줄로 정리돼 있어 모순 아님.
키트 결함: 없음.
총평: real9와 같은 PASS 2.
