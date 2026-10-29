# real7 C21

**PASS 2 / 부분 0 / FAIL 0** (real6 PASS 2 유지)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | '한 생성에 한 층만'; 층 순서 ①구조면 ②설비·가구 ③표지판 판·글자 ④조명 ⑤이미지 질감(`location-edit.md` 틀 2 층 이름과 일치); 정본 §3·§7(1990년대)과 충돌 짚고 '별도 뷰 `LC-001-V2` vs 작품 전체' 질문; 프롬프트 없음 |
| 2 | PASS | `this step changes only its STRUCTURAL SURFACES`; 요소마다 목표 시대 대응물(함석 → 도장 강판 등); `REMOVE:`; PRESERVE에 다른 층·건물 볼륨·V1 LIGHT LOCK 글자 그대로; `ONLY CHANGE: STRUCTURAL SURFACES`; 1990s 잠금 없음(Era lock은 2020s 표면); 1단계 결과는 아직 2020년대가 아님 알림 |

## 검사기
내 실행 `--kind image --refs 1`: `WARN 인물이 있는 프롬프트에서 좌우를 썼는데 좌표 문장이 없다 … — FAIL 0 · WARN 1 · 1814자`. **검사기 오탐**: 프롬프트에 인물이 없고 `No people, no cars`의 `people`이 인물로 잡힘. 플레이어도 같은 WARN을 보고 '인물 없음'으로 근거를 적어 남김(합당).

## 추가 발견
G1(mcp 호출·생성) 위반 없음, RUN 밖 읽기 없음. 없음.

## 키트 결함
있음: `.claude/skills/higgsfield-generation/check_prompt.py:50,68-71`의 `people` 정규식이 `no people`/`no other people`(부정문)도 인물로 세어 인물 없는 장소 프롬프트(LEFT/RIGHT 사용)에 WARN을 낸다 → 부정문(`\bno (?:other )?(?:people|persons?)\b`)을 지운 뒤 인물 여부를 판정.

## 총평
층 분리·시대 교체 정확, 검사기 오탐 1건.
