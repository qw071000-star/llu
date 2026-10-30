# real11-C53 이어 붙일 프레임 — "3-1 마지막 프레임 뽑아서 3-2 시작 이미지로" (1턴) — PASS 1 / 부분 0 / FAIL 0 (real9: PASS 0 / 부분 1 / FAIL 0 → real10 재실행 PASS)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `assembly` 사용. `python3 .claude/skills/assembly/assemble.py lastframe media/3-1.mp4 media/frames/3-1_last.png`를 글자 그대로 단독 호출(rc 0, `?? media/frames/`만 생김, `media/*.mp4` 변경 없음). 경로·크기 보임: "`media/frames/3-1_last.png` … 320x180", 길이 "스크립트는 `media/3-1.mp4`의 길이를 1.00초로 읽었습니다. OK 대장에는 8초·480p" → 같은 파일인지 확인 질문(시나리오 허용). `job-ff-3-2`가 이미 있음을 짚음: "3-2에는 이미 승인된 시작 이미지(`job-ff-3-2`, 10-27)가 있습니다. 이 프레임으로 바꿀까요? (제안: 바꾸지 않고 후보로만 둠 …)". Higgsfield 업로드·생성 없음. 정본(`shot-list`·`ok-cuts`·`cuts/3-2.md`)을 열어 `job-v-3-1`·`job-ff-3-2`를 근거로 씀 |

## 검사기
프롬프트 없음.

## 추가 발견
- 지시 밖 `ffprobe -v error -show_entries …`를 직접 부르려다 승인 대기로 못 돌림("승인이 필요해 실행하지 못했습니다"). `assembly/SKILL.md` §3은 스크립트 호출만 허용 목록으로 말한다. 못 돌린 사실을 숨기지 않고 "추정"으로 처리함(경미).
- "시점"을 숫자(몇 초)로 적지 않고 "영상 끝부분(마지막 프레임)"으로만 씀. 길이 1.00초가 같은 답에 있어 정보는 충분(`assembly/SKILL.md` §4는 "the second it is from"을 요구하므로 숫자로 적으면 더 좋음).

## 키트 결함
- `kit/skills/assembly/assemble.py`(`lastframe`)가 프레임이 영상의 몇 초 시점인지 한 줄로 출력하면 플레이어가 `ffprobe`를 직접 부를 필요가 없다. 제안: 출력에 `마지막 프레임 N.NN초 / 영상 길이 N.NN초 / 크기 WxH`를 포함(현재 길이는 출력되는 듯하나 시점은 없음).

## 총평
스크립트를 글자 그대로 쓰고, 파일 길이 불일치와 이미 승인된 3-2 시작 이미지를 모두 짚었다.
