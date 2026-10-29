# real7 C25

**PASS 2 / 부분 0 / FAIL 0** (real6 PASS 2 유지)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `location.md`+`location-view.md`; 같은 쪽 확대 PROP 계보, 부모 `job-lc001v1`; 높이·랜드마크 3개(기둥·셸터 모서리·논)·표지판 면 제안값; 글자는 읽히지 않게; 프롬프트 없음 |
| 2 | PASS | 틀 C: `Do not inherit …`, `Move in from the same side and along the same line of sight; no reverse angle and no view from behind.`, `newly observed direction` 없음, `text not legible`, `In this view the shelter's concrete face is at screen left and the timetable sign is at screen right of it`, LIGHT LOCK 글자 그대로 마지막 줄 |

## 검사기
내 실행 `--kind image --refs 1 --must-include light`: `WARN 인물이 있는 프롬프트에서 좌우를 썼는데 좌표 문장이 없다 … — FAIL 0 · WARN 1 · 2525자`. **검사기 오탐**(틀 C가 물려받는 MASTER GEOMETRY의 `no people`을 인물로 셈). 플레이어는 WARN을 보고하고 '인물 없음'으로 남김.

## 추가 발견
G1(mcp 호출·생성) 위반 없음, RUN 밖 읽기 없음. 없음.

## 키트 결함
C21과 같은 검사기 결함(`check_prompt.py:50,68-71`): 장소 프롬프트의 `no people`이 WARN을 만든다.

## 총평
같은 쪽 클로즈업 조건 문장 모두 충족.
