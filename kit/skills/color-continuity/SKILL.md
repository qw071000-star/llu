---
name: color-continuity
description: 확정 컷끼리 색·밝기를 ffmpeg로 재고 기준 컷에 맞춘다(Claude Code). "색이 컷마다 달라", "3-2가 더 노래", "3-1이랑 색 맞춰", "밝기 맞춰", "톤 통일", "LUT". 그레이딩·생성은 안 한다.
---

# 컷 간 색 맞추기

Claude Code의 Bash에서 `color.py`(ffmpeg/ffprobe)로 한다. MCP는 쓰지 않는다. 창작 그레이딩(새 룩 만들기)은 범위 밖이다.

## 1. 언제 쓰나

- 확정 컷(영상·이미지)끼리 색온도·밝기·대비가 튀어 보일 때
- 러프컷(`assembly`)을 보기 전에 컷 톤을 맞출 때

## 2. 기준 컷

- 기준은 OK 컷 하나다. 사용자가 정한다(제안: OK 대장의 OK 이유가 "색감"인 컷).
- 정한 기준은 `decisions.md` §3 "기준 색 컷" 줄에 적는다(정본 수정은 `production-session` §1). 있으면 묻지 않는다.
- 파일은 `media/<컷 번호>.mp4`(이미지면 `.png`)로 본다. 없으면 어느 job을 어디에 둘지 묻는다.

## 3. 레시피

명령은 리포 루트에서 이 글자 그대로 한 줄씩 돌린다(cd·`&&` 없이. 허용 목록과 같은 글자). 스크립트가 실행 전에 ffmpeg 명령을 출력한다.

| 할 일 | 명령 |
|---|---|
| 재기 | `python3 .claude/skills/color-continuity/color.py measure media/3-1.mp4 media/3-2.mp4` |
| 맞추기 | `python3 .claude/skills/color-continuity/color.py match media/3-1.mp4 media/3-2.mp4 media/color/3-2_match.mp4` |
| 비교 이미지 | `python3 .claude/skills/color-continuity/color.py compare media/3-1.mp4 media/3-2.mp4 media/color/3-2_match.mp4 media/color/3-2_compare.png` |

- **재는 것:** 프레임 5장 남짓을 고르게 뽑은 평균. Y = 밝기, U·V = 색 기울기(U가 낮으면 노랑, V가 높으면 빨강 쪽), R·G·B, Y 표준편차 = 대비. 첫 파일(기준) 대비 차이를 같이 낸다.
- **맞추는 법:** `colorchannelmixer`(R·G·B 이득)로 색을, `eq`(대비·밝기)로 노출을 기준에 가깝게 한다. 값은 안전 범위로 자르고 자르면 알린다. 맞춘 뒤 `measure`를 다시 돌려 차이가 줄었는지 숫자로 보인다.
- **비교 이미지:** 가운데 프레임으로 기준 | 원본 | 맞춘 것.

## 4. 기록 · 승인

- 맞춘 파일과 비교 이미지, 쓴 필터 문자열, 전후 숫자를 보이고 쓸지 묻는다. **승인 전에는 제안만 한다.**
- 승인되면 필터 문자열을 그 컷 카드나 `decisions.md` §3 룩 메모(기준 색 컷 줄 아래)에 한 줄로 남긴다(`3-2: colorchannelmixer=… , eq=… (기준 3-1)`).
- LUT 파일은 만들지 않는다. 필터 문자열이 그 컷의 1차 맞춤 기록이다.

## 5. 다시 만들 때

차이가 크면(스크립트가 "차이가 크다"·"안전 범위로 잘랐다"를 내거나, 시간대·빛 방향이 달라 보이면) 후반 보정 대신 그 컷을 다시 만드는 것을 제안한다. 고칠 곳은 `video-prompt`·`image-prompt`의 LIGHT LOCK·PALETTE 줄이다.

## 6. 하지 않는 것

- 생성, Higgsfield 업로드, 창작 룩 만들기
- **원본은 덮어쓰지 않는다.** 출력은 `media/color/`에 새 파일로만. 스크립트는 입력과 같은 출력, 이미 있는 출력을 거절한다.
- ffmpeg가 없거나 오류가 나면 스크립트의 한국어 오류를 그대로 보인다.
