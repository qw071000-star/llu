제안값 6개를 그대로 쓰기로 하고 에셋 대장 CH-003에 `제안값`으로 기록했습니다. 시트를 아직 생성하지 않았으므로 IDENTITY·WARDROBE는 초안이고, 연기 프로필·목소리는 보류로 적었습니다.
보내기 전에 실패 위험과 프롬프트를 먼저 보여 드립니다.

**실패 위험과 막는 문장**
1. 왼쪽 패널에 머리가 생기거나, 잘린 목이 상처처럼 보입니다 → `intentionally HEADLESS … not an injury`
2. 모자·장갑·시계·핸들·버스 같은 기사 소품이 저절로 생깁니다 → `No profession-signaling props: no cap, no gloves, no wristwatch, no steering wheel, no bus.`
3. 점퍼에 명찰·회사 이름·로고가 생깁니다(§7 글자 금지) → `No name tag, no badge, no embroidered company name, no logos …`
4. 반사띠·형광 조끼·기능성 소재 같은 요즘 작업복이 나옵니다 → `Plain early-1990s cotton workwear: no reflective strips, no high-visibility vest, no technical fabric.`
5. "굳게 다문 입"이 화난 얼굴로 과장됩니다(§5 절제) → `a calm, expressionless face, not angry, not frowning`
6. 세 패널에 서로 비슷한 다른 남자 셋이 나옵니다 → `one person only. Do not create three similar men.`
7. GPT Image 2.5에서 질감이 3D 렌더처럼 나옵니다 → `REALISM` 문단(피부결, 비대칭, 보정 필터 금지)
8. 배경·조명이 기존 시트와 달라집니다 → `BACKGROUND AND LIGHTING` 줄을 CH-001 카드에서 글자 그대로 옮김

- 모드: 신규 (인물 시트 틀 1)
- 참조: 없음
- 모델: GPT Image 2.5
- 해상도: 1k(확인용) · 16:9 · 1장
- 길이: 해당 없음(이미지)
- 저장: 「빈 정류장」/00 에셋/인물 `fld-chars`
- 검사: `check_prompt.py`를 통과했습니다(걸린 항목 없음)

```text
Create a photorealistic single wide horizontal three-panel character reference sheet of the same man. The image is divided into three clean vertical sections with no borders, captions or text.

CHARACTER IDENTITY:
A Korean man in his early fifties with sun-tanned skin, a square jaw, narrow single-lidded dark eyes, thick dark brows, short black hair greying at the temples, a stocky medium build and slightly rounded shoulders. A firmly closed mouth and a calm, expressionless face, not angry, not frowning. The same exact identity must be maintained wherever the face is visible.

PANEL LAYOUT:
- LEFT PANEL: a front-facing full-body wardrobe view shown strictly from the neck down. The panel is intentionally HEADLESS and ends cleanly at the base of the neck. This is an editorial clothing crop, not an injury: no head, no face, no wound, no gore, no dark opening. The plain background continues cleanly above the neckline. Both hands visible and empty, feet fully visible.
- CENTER PANEL: a full-body rear view of the same man from head to toe, same neutral pose.
- RIGHT PANEL: a large front-facing close-up portrait from the upper chest upward, calm neutral expression, the gaze with a definite focal distance just behind the lens.

BODY AND PROPORTIONS: medium height, a stocky, solid build, shoulders slightly rounded forward from years of driving, a small belly.
OUTFIT — IDENTICAL IN ALL THREE PANELS: A dark navy work jumper zipped to mid-chest, with two flapped chest pockets, over a pale blue collared shirt, grey cotton trousers, worn black leather shoes. Plain early-1990s cotton workwear: no reflective strips, no high-visibility vest, no technical fabric. One physically identical outfit seen from different views. No name tag, no badge, no embroidered company name, no logos, no prints, no unintended accessories. No profession-signaling props: no cap, no gloves, no wristwatch, no steering wheel, no bus.
HAIR — CENTER AND RIGHT PANELS: short straight black hair parted on the left, slightly grey at the temples, tapered short at the back and nape, natural matte finish.
REALISM: visible fine skin texture with natural pores, subtle asymmetries and uneven skin tone, no digital smoothing, no beauty filter, matte natural complexion. Eyes have genuine moisture and a small specular catchlight, one eyelid very slightly lower than the other, real iris texture.
BACKGROUND AND LIGHTING: one continuous plain warm-grey seamless backdrop across all panels, soft frontal key light from slightly above. All panels share the same lighting direction, exposure, palette and finish.
CONSISTENCY RULES: one person only. Do not create three similar men. Preserve the exact left-to-right order: headless front outfit view / full-body rear view / front close-up portrait.
no text, no watermark, no logos, no frame borders, no other people, no duplicate figures, no extra panels, no props, no beauty filter, no plastic skin, no extra fingers
```

이 프롬프트로 1k 한 장을 `fld-chars`에 보낼까요? 고칠 곳이 있으면 그 줄만 말씀해 주세요.

=== 메타 ===
연 파일(순서대로):
1. project/asset-registry.md — `### CH-003` 절만 검색(같은 명령에서 out/ 목록과 check_prompt.py 앞 40줄 중 인자 정의 줄만 grep)
2. .claude/skills/higgsfield-generation/check_prompt.py — 실행만 함(`--kind image 초안파일 --refs 0` → OK, 걸린 항목 없음). 초안은 스크래치패드 /tmp/claude-0/-home-user/dca0a83f-e443-5698-9f4c-755968d364fc/scratchpad/ch003_sheet.txt에 저장
3. project/asset-registry.md 66–77행(고치기 전 확인)
(1턴에 읽은 지침·스킬·정본·OK 대장 CH-001 카드 내용을 그대로 사용했고, 다시 열지 않음)

부른 [TOOL]: 없음 (생성 지시 전이라 보내지 않음)

고친 정본 파일:
- project/asset-registry.md — CH-003 블록의 IDENTITY·WARDROBE 줄에 제안값을 기록하고, ACTING PROFILE·VOICE 줄은 보류로 표시함. 그 아래에 근거 메모 한 줄(2026-10-28 · 제안값, 시트 생성 전 초안, 직업 소품·명찰 없음)을 추가함
