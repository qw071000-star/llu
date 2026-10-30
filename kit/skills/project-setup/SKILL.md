---
name: project-setup
description: Use when starting a new AI image/video work. Applies to requests like "새 작품 시작", "프로젝트 세팅", "처음부터 준비", or when the canon is empty.
---

# Starting a new work

Goal: reach a state where the user can start working after answering one question round. Do not split the questions across several rounds.

## 1. Ask all at once

Show the table below as is, and write the exact Korean sentence "바꿀 것만 답해 주세요. 나머지는 기본값으로 합니다."
Ask once whether a script or storyboard exists; no answer means none, do not ask again. If the user gave a scenario or storyboard, read it first and fill in the fields that can be known from it before showing the table.

The table is shown to the user in Korean; keep it entirely in Korean.

| # | 질문 | 기본값 |
|---|---|---|
| 1 | 최종 화면 크기·비율, 가려지는 구역(자막·출연자·로고) | 16:9, 가림 없음 |
| 2 | 전체 길이, 장면·컷 수, 컷당 길이, 컷 번호 방식 | 컷당 8초, 번호는 장면-컷(3-1) |
| 3 | 실사인가 그림체인가 (그림체면 기준이 될 이미지) | — (필수) |
| 4 | 이미지·영상 모델 | 이미지 GPT Image 2.5 / 영상: 실사는 Seedance 2.5, 배경은 Kling 4.0 |
| 5 | 확인용·확정 해상도, 소리 | 확인 1k·480p, 확정 2k·1080p, 소리 끔(대사 컷만 켬) |
| 6 | 시대·장소, 고증 수준 | 현재, 자료 조사 안 함 |
| 7 | 카메라 기본 | 고정·아이레벨, 움직임은 컷별로 지정 |
| 8 | 허용·금지 요소(사람, 동물, 글자, 불 등) | 글자 금지 |
| 9 | 승인 절차 | 프롬프트 먼저 보기, 한 장씩, 같은 실패 한도는 지침 8번대로, "픽스" = 승인 |
| 10 | 후반 작업 가능 여부 | 편집·색 보정 가능 |
| 11 | Higgsfield 프로젝트·폴더: 새로 만들지, 기존 것을 쓸지 / Claude가 만들지, 직접 만들지 | 새 프로젝트, Claude가 만듦 (이 기본값에 동의하면 그것이 만들어도 된다는 승인이다) |
| 12 | 답변 언어, 보고 길이 | 한국어, 짧게 |
| 13 | 작품명(가제) | — (필수) |
| 14 | 연기: 쓰는 연기 / 쓰지 않는 연기 | 절제, 감정은 손과 시선으로 / 울음·과장된 표정 없음 |

## 2. After the answers, build the canon drafts

- `decisions.md`: write one line per answer in each section. Add the date and "사용자 답" or "기본값". Put unknowns in the open-items table.
- `shot-list.md`: if there is a scenario or storyboard, split it into cuts and write one line each (status `대기`). If not, leave an empty table.
- `asset-registry.md`: assign IDs only to the characters, locations, and props that will appear (CH-001, LC-001, PR-001). Fill the content when the asset is confirmed.
- `ok-cuts.md`: leave as an empty list. Fill it from the first approval.
- Do not fill `(필수)` fields with defaults. Even if the user says "나머지는 기본값", ask again for only those fields.
- If there is no scenario, the cut list holds only scene numbers in an empty table. Do not invent a plot.
- After writing the canon, remove template traces:
  - [ ] the example rows and example cards in `ok-cuts.md`
  - [ ] the `[예: …]` items in `decisions.md` and the bracketed canon-priority line (fill them in, or with defaults)
  - [ ] the work title in headings (and the `CLAUDE.md` heading too in Claude Code)
- If the user answered that there is no scenario, do not ask again.

## 3. Higgsfield project and folders

1. If using an existing project, find it with `list_projects` and verify the ID.
2. If creating a new one, agreeing to the §1 item 11 default is itself the approval. Do not ask again. Create the project with `create_project` (folders as in `higgsfield-generation` §2); write the returned IDs in the registry.
3. Show the folder structure plan and create immediately: now only `00 에셋` (subfolders for characters, locations, props, plus art style for art-style works) and `99 시험·보관`; cut folders come when the cut card is issued. How to create, name and record them: `higgsfield-generation` §2.

## 4. Place the canon

**If a Docs tool is available (recommended):** build the canon as a single Claude Doc.
- Tab layout: 확정 사항 / 에셋·폴더 / 컷 목록 / 컷 카드 (one section per cut, title `3-1`) / OK 컷 / 핸드오프 로그
- Every later conversation reads and edits this Doc directly. The user never has to move files.

**If no Docs tool:**
- Claude app: give the four canon files as one code block per file. The user uploads them to project knowledge.
  - The OK ledger grows longer as it accumulates, since every conversation reads it. When OK cards reach 10, or `ok-cuts.md` exceeds 30,000 characters, Claude proposes first to move it to Docs or split it into per-scene files.
  - Do not upload cut cards to knowledge. Ask the user to paste only that cut's card in the first message of the cut conversation.
- Claude Code: save under `project/`.

**Last, fill the "이 프로젝트" field.** In the Claude app, ask once for it to be written at the very top of the instructions field. In Claude Code, Claude fills that field in `.claude/instructions.md`. If the edit is rejected (`.claude/` is a protected path), show the lines to change exactly as they are and have the user paste them.
- Work title
- Higgsfield project ID
- Canon location (Doc link, etc.)

With only this, the next conversation can start working right away.

## 5. Announce the next order (one line each)

1. Confirm the art-style or look reference image (art-style works only).
2. Make the character + wardrobe sheets.
3. Make the location masters.
4. Make the prop assets.
5. Issue cut cards and open cut sessions.
