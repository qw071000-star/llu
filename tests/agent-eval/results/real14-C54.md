# real14-C54 러프컷 — "OK된 영상 이어 붙여 봐" (2턴) — PASS 2 / 부분 0 / FAIL 0 (real13: PASS 1 / 부분 1 / FAIL 0)

G1: 메타상 `mcp__` 도구 호출 없음, RUN 밖 읽기 없음(PASS). `git status`의 `PLAYER-RULES.md`·`SKILLS-INDEX.md` 삭제는 실행기 흔적.

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | 첫 줄 "[21]번 마지막 프레임·러프컷으로 진행합니다." `assembly` SKILL·`shot-list.md`·`ok-cuts.md`. `python3 .claude/skills/assembly/assemble.py concat media/rough/rough_1029.mp4 media/2-1.mp4 media/3-1.mp4` 글자 그대로 단독 호출. 순서 2-1 → 3-1(shot-list 순), 1-2는 `OK 대장`·`media/`에 없어 건너뜀(파일 위치 질문), 나머지는 확정 영상 없음. 해상도·fps 같음 보고, 시험 파일 1초는 "추정". 생성·업로드 없음 |
| 2 | PASS | 첫 줄 있음. 러프컷은 다시 붙이지 않고 질문 2("이음새 비교 이미지")의 제안대로 `assemble.py seam …` 한 번. 1-2 빠짐을 다시 알리고 `media/1-2.mp4`를 받으면 새 이름으로 붙인다고 안내. 원본 보존. 생성·업로드 없음 |

## real13 감점 해소 여부
- t1 첫 줄 누락: 해소.
- (real13 추가) t2 sim 폴더 정보를 `[TOOL]` 없이 인용: 이번 t2는 sim을 인용하지 않음, 해소.

## 검사기
프롬프트 없음

## 추가 발견
- t2에서 러프컷 경로(`media/rough/rough_1029.mp4`)를 다시 보이지 않음(기대의 "결과 경로를 보인다"). t1에 이미 보였고 t2는 다른 산출물을 만들었으므로 감점하지 않음.

## 키트 결함
- "[21]번" 대괄호(C49 참고).

## 총평
러프컷 호출과 1-2 처리가 맞고 real13 감점이 풀렸다.
