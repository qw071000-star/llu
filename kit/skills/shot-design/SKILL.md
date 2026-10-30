---
name: shot-design
description: Designs one script scene into cuts (the stage before the cut card). Use for "이 장면 컷 나눠줘", "콘티 짜줘", "커버리지", "어디서 찍어야 해", "샷 리스트", the 180-degree line, master/reverse/insert shots, and cut-length allocation.
---

# Scene coverage · cut design

This is the stage before the cut card (`production-session`). Design one scene in the order blocking → 180-degree line → coverage → cut length → shot-list lines, and show it **as a proposal only**.

## 1. Inputs

- The scene's script (dialogue and action lines). If none, say that the cut list's content lines will be used as beats, and show the proposed design (blocking, 180-degree line, coverage table) in the same reply as the questions.
- Location assets: confirmed views (`LC-001-V1`…) and each view's LIGHT LOCK (asset ledger).
- Characters: asset IDs of the characters who appear, and their positions at scene start.

## 2. What to produce

1. **Blocking memo:** at scene start and at each major beat, write character and object positions as screen side + an on-screen object in the master view (instructions rule 6). Write movement as "from where → to where".
2. **180-degree line:** which two characters (or character and object) it is drawn between, and which side of that line the camera is on (by an on-screen object).
3. **Coverage table:** whichever of master, two-shot, reverse, insert, reaction the scene needs. For each shot: camera position and height, field of view (°) and shot size, and the location view used. If no suitable view exists, write `새 뷰 필요` (making it is `image-prompt` → `location-view.md`).
4. **Cut length allocation** (not asked: start from the `decisions.md` cut length, e.g. 8 s): events per cut as in `video-prompt` §2 "Event count", at most 15 seconds per cut, 2–4 seconds per dialogue line. Split the cut if exceeded.
5. **Lines to move into `shot-list.md`:** always show every cut line of the scene (kept cuts copy their existing fields), in that table's column order, status `대기`. A cut that already has a confirmed start image keeps that image's field of view (write it as `NN° (OK 카드)`) and its job in the `확정 job` column; the moved lines keep every column of `shot-list.md`.

## 3. Rules

- **Use a cut that crosses the 180-degree line only when intended,** and mark it in the table as `선 넘음(의도: …)`.
- **When the user says "리버스", the proposal is the true opposite view of the master**; an over-the-shoulder or 90° side shot is only an alternative. A reverse needs its own view and LIGHT LOCK (sides flip: `image-prompt` → `location.md` "Writing directions"); point to `location-view.md` template A and do not write the LIGHT LOCK sentence here.
- **Make neighboring cuts connect.** The previous cut's end state (character positions, gaze, prop state) is the next cut's start state. Write it in the table's `끝 → 다음 시작` column.
- **AI constraints:** one location per generation, one camera movement (or static), and a location/view that does not exist yet is made as an image first.
- **Do not edit the canon before the user confirms.** Until the user says "확정" or "그대로", do not touch `shot-list.md`; only show proposals. Who edits after confirmation follows `production-session` §1.
- **For a cut that already has a start image/video** (confirmed field in the cut list), write that job in the coverage table and ask whether to keep or replace it. Do not suggest remaking an existing view.
- Do not write cut cards. Issuing cut cards from confirmed lines is `production-session`'s job.

## 4. Template

```text
장면 [N] — [장소 ID] · [시간대]

블로킹 메모 (마스터 뷰 [LC-…-V…] 기준, 화면 쪽 + 물건)
- 시작: [인물 A]는 화면 [쪽], [물건] 앞 [거리]. [인물 B]는 화면 [쪽], [물건] 옆.
- 비트 [n] ([대사·지문 한 줄]): [인물]이 [어디] → [어디]. [소품] [상태].
180도 선: [인물 A] ↔ [인물 B]. 카메라는 [물건] 쪽.

커버리지
| 샷 | 종류 | 카메라 위치·높이 | 화각°·크기 | 장소 뷰 | 확정 job | 선 | 사건(1~3) | 길이 | 끝 → 다음 시작 |
|---|---|---|---|---|---|---|---|---|---|
| [N]-1 | 마스터 | [물건] 맞은편, [m] | [°] · 풀 | [V…] | | 안 | | [초] | |
| [N]-2 | 리버스 | [물건] 뒤, [m] | [°] · 바스트 | 새 뷰 필요 | | 안 | | [초] | |
| [N]-3 | 인서트 | [물건] 위, [m] | [°] · 클로즈업 | [V…] | | 안 | | [초] | |

shot-list.md로 옮길 줄 (확정 후)
| [N]-1 | [초] | [내용 한 줄] | 대기 | [V…] | [인물·소품] | | | |
```
