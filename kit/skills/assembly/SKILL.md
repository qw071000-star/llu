---
name: assembly
description: 확정 영상을 Claude Code에서 ffmpeg로 다룬다. "마지막 프레임 뽑아", "다음 컷 시작 이미지로", "3초 프레임", "이어 붙여 봐", "러프컷", "컷 경계 비교", 트림·해상도 맞추기. 생성은 하지 않는다.
---

# 러프컷 조립 · 이어 붙이기 프레임

Claude Code의 Bash에서 `assemble.py`(ffmpeg/ffprobe)로 한다. MCP는 쓰지 않는다. 그레이딩·사운드는 범위 밖이다.

## 1. 언제 쓰나

- 앞 컷 마지막 프레임을 다음 컷 시작 이미지 후보로 뽑을 때
- 확정 컷을 순서대로 붙여 흐름을 볼 때(러프컷)
- 컷 경계(앞 컷 끝 | 다음 컷 시작)를 나란히 비교할 때

## 2. 받는 것 · 만드는 것

- **받는 것:** OK 대장(`ok-cuts.md`)의 확정 영상 job과 그 로컬 파일. Higgsfield에서 내려받은 mp4가 리포 `media/`에 `3-1.mp4`처럼 있다고 본다. 없으면 어느 job을 어디에 둘지 묻는다(제안: `media/<컷 번호>.mp4`).
- **만드는 것:** 프레임 `media/frames/<컷>_last.png`·`<컷>_<초>s.png`·`seam_<앞>_<뒤>.png`, 러프컷 `media/rough/rough_<날짜>.mp4`.

## 3. 레시피

명령은 리포 루트에서 이 글자 그대로 한 줄씩 돌린다(cd·`&&` 없이. 허용 목록과 같은 글자). 스크립트가 실행 전에 ffmpeg 명령을 출력한다.

| 할 일 | 명령 |
|---|---|
| 마지막 프레임 | `python3 .claude/skills/assembly/assemble.py lastframe media/3-1.mp4 media/frames/3-1_last.png` |
| 지정 시각 프레임 | `python3 .claude/skills/assembly/assemble.py frame media/3-1.mp4 2.5 media/frames/3-1_2.5s.png` |
| 이어 붙이기(러프컷) | `python3 .claude/skills/assembly/assemble.py concat media/rough/rough_1029.mp4 media/3-1.mp4 media/3-2.mp4` |
| 경계 비교 | `python3 .claude/skills/assembly/assemble.py seam media/3-1.mp4 media/3-2.mp4 media/frames/seam_3-1_3-2.png` |

- **해상도·fps 통일:** `concat`이 한다. 다르면 첫 영상에 맞춰 다시 인코딩하고(비율이 다르면 레터박스) 무엇을 바꿨는지 출력한다. 같으면 다시 인코딩하지 않는다.
- **트림:** 스크립트에 없다. `ffmpeg -ss 0.5 -to 4.0 -i media/3-1.mp4 -c:v libx264 -crf 18 -c:a aac media/rough/3-1_trim.mp4`(시작·끝 초). 러프컷 확인용이며 원본은 그대로 둔다.

## 4. 주의

- **원본은 덮어쓰지 않는다.** 출력은 `media/frames/`·`media/rough/`에만. 스크립트는 입력과 같은 출력, 이미 있는 출력을 거절한다(새 이름을 쓴다).
- **시작 이미지로 쓸 프레임은 사용자 확인을 받은 뒤** Higgsfield에 올려 그 컷의 시작 이미지로 쓴다. 뽑은 프레임의 경로와 몇 초인지 보이고 묻는다.
- **생성은 하지 않는다.** 이음새가 어긋나 보이면 경계 비교 이미지와 함께 어느 컷을 고칠지 제안만 한다.
- **러프컷 순서는 `shot-list.md` 순서다.** 확정 영상 칸이 빈 컷은 빼고 뺀 컷을 알린다.
- ffmpeg가 없거나 오류가 나면 스크립트의 한국어 오류를 그대로 보인다.
