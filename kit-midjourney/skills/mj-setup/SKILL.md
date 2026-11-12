---
name: mj-setup
description: Use when starting a new Midjourney work. Applies to requests like "새 작품 시작", "프로젝트 세팅", "처음부터 준비", or when the canon is empty. Asks one question round and prepares the canon.
---

# New work setup

Goal: the user can start after answering **one** question round.

## 1. Ask all at once

Show the table as is, and write the exact Korean sentence "바꿀 것만 답해 주세요. 나머지는 기본값으로 합니다." Ask once whether a script or storyboard exists. If one was given, read it first and fill what it answers. The table is shown to the user in Korean.

| # | 질문 | 기본값 |
|---|---|---|
| 1 | 최종 화면 비율, 가려지는 구역(자막·로고) | 16:9, 가림 없음 |
| 2 | 전체 길이나 장면·컷 수, 컷 번호 방식 | 번호는 장면-컷(3-1) |
| 3 | 실사인가 그림체인가 (그림체면 기준 이미지 링크) | — (필수) |
| 4 | Midjourney 버전, Omni Reference·Draft 모드 같은 쓸 수 있는 기능 | — (필수. 모르면 설정 화면을 확인해 알려 달라고 한다) |
| 5 | 스타일 참조(`--sref`)로 쓸 이미지가 있나 | 없음 |
| 6 | 시대·장소, 고증 수준 | 현재, 자료 조사 안 함 |
| 7 | 카메라 기본 | 눈높이, 정면 |
| 8 | 허용·금지 요소(사람, 동물, 글자 등) | 글자 금지 |
| 9 | 승인 절차, 운영 방식(단독 / 공용 계정이면 사용자 이름들, 총괄, 사용량 한도) | 단독, 결과를 붙이면 항목별로 판정하고 사용자가 OK |
| 10 | 이미지 저장·파일 이름 | 사용자가 만든 `00 에셋/인물·장소·소품·그림체`, `99 시험·보관` 폴더에 요소 이름으로 저장 |
| 11 | 짧은 영상(이미지→영상)을 쓰나 | 안 씀(쓰면 `mj-video`) |
| 12 | 답변 언어, 보고 길이, 작품명(가제) | 한국어, 짧게, — (작품명 필수) |

Do not ask what the user already answered. If the user answers only some items, take the proposals for the rest and say so in one line.

## 2. Fill the canon

- `decisions.md`: put the answers in the matching sections; mark each line's source (사용자 답 / 기본값).
- `asset-registry.md`: assign IDs only to the characters, locations and props that will appear (CH-001, LC-001, PR-001). Fill the content when the asset is confirmed.
- `shot-list.md`: if a script exists, leave the cut lines to `mj-shots`; otherwise leave the table with one empty row.
- `ok-cuts.md`: empty template.

## 3. Place the canon

**Claude Docs available (recommended):** build one Doc with tabs 확정 사항 / 에셋 / 컷 목록 / 컷 카드 (one section per cut, title `3-1`) / OK 컷 / 핸드오프 로그. Every later conversation reads and edits it directly. **No Docs tool:** give the four canon files, one code block per file; the user uploads them to project knowledge (then writes go as "정본 갱신" blocks). Cut cards are not uploaded: the user pastes only that cut's card in the cut conversation.

Last, ask once for "이 프로젝트" at the top of the instructions field to be filled: work title, Midjourney version, Canon location.

## 4. Announce the next order (one line each)

1. Style reference or look (illustration works).
2. Character portraits, then views.
3. Location masters.
4. Props.
5. Cut cards, stills, and clips if used.
