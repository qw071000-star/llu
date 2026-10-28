제안값을 모두 적용했습니다. 정본에는 `제안값`으로 기록했습니다.
- **에셋 대장 PR-002:** 크기, 물성, 상태 머신, 모양·사진·사용 흔적, 금지 항목
- **shot-list:** 3-4 "가방을 열고 할머니 사진 액자를 꺼낸다", 3-5 "열린 가방 위에서 액자를 든 할아버지 손 클로즈업"(소품 칸에 PR-002 추가), 3-4 → 3-5 이음새 줄, 연속성 표 3-4·3-5

아직 생성하지 않았습니다. 아래 위험 목록과 프롬프트를 먼저 봐 주세요.

**실패 위험과 막는 문장**
1. 틀의 "no people" 때문에 사진 속 인물이 빠질 수 있음 → `no real people; the only person is the one inside the photograph.`
2. GPT Image 2.5의 질감이 3D 렌더 쪽으로 돌 수 있음 → 질감 문장을 맨 앞에 둠: `a real camera photograph with natural wood grain, glass and paper texture, not a 3D render or illustration`
3. 사진관 이름, 날짜 도장, 서명 같은 글자가 생길 수 있음 → `Avoid: … text, studio name stamps, dates, signatures, watermarks.`
4. 현대 액자나 인화로 보일 수 있음 → `Avoid: plastic, acrylic, chrome or gold-metal frames, … a colour or glossy modern print`
5. 사진 속 얼굴이 요즘 얼굴처럼 보일 수 있음(보정 피부, 요즘 머리) → `her hair neatly tied back in the style of the time` 와 `Avoid: modern hairstyle or makeup, retouched beauty-filter skin`
6. 유리 반사가 얼굴을 가릴 수 있음 → `one faint soft reflection along its upper edge; the portrait stays fully readable.`
7. 16:9 화면에서 세로 액자가 작게 나올 수 있음 → `centred, filling about two thirds of the image height.`
8. 스튜디오 사진에는 크기 단서가 없음 → 이 시안은 모양과 사진 내용의 기준으로만 씁니다. 영상용 요소는 3-4 장면 프레임에서 잘라 만듭니다(에셋 대장에 기록함).

- 모드: 신규, 참조 없음
- 모델: GPT Image 2.5
- 해상도: 1k(확인용), 16:9, 1장
- 저장: 「빈 정류장」/00 에셋/소품 `fld-props`
- 자동 검사: `check_prompt.py --kind image --refs 0` → 걸린 항목 없음

```text
Photorealistic product-reference photograph — a real camera photograph with natural wood grain, glass and paper texture, not a 3D render or illustration — of an old photo frame from early-1990s rural Korea: a dark brown stained wooden frame with a plain moulding about 2 cm wide, a glass front and a grey cardboard back with a folding easel stand, portrait orientation, about 18 × 23 cm, isolated on a plain seamless light grey studio background, nothing else in frame — no scene, no room, no other objects, no hands, and no real people; the only person is the one inside the photograph.
THE PHOTOGRAPH IN THE FRAME: a 5 × 7 inch black-and-white studio portrait from the 1960s of a Korean woman in her forties, half-length, facing the camera with a calm, closed-mouth expression, her hair neatly tied back in the style of the time, wearing a dark hanbok jeogori, against a plain studio backdrop. Soft focus and fine grain of an old print.
Use marks: paint worn off at the corners of the frame, the bottom edge rubbed smooth and slightly glossy from handling, fine hairline scratches on the glass, the photograph's white border yellowed at the edges.
The frame is rigid and flat with square corners; nothing is bent or warped. It stands upright on its stand, seen from the front and turned about 15 degrees to the left so its thickness shows, centred, filling about two thirds of the image height. The glass shows one faint soft reflection along its upper edge; the portrait stays fully readable.
Soft even studio lighting from the front-top, minimal shadow. Sharp focus throughout.
Avoid: plastic, acrylic, chrome or gold-metal frames, carved ornate frames, a colour or glossy modern print, modern hairstyle or makeup, retouched beauty-filter skin, brand logos, text, studio name stamps, dates, signatures, watermarks.
```

질문: 이대로 1k 한 장을 `fld-props`에 보낼까요? 고칠 줄이 있으면 그 줄만 말씀해 주세요.

=== 메타 ===
연 파일(순서대로):
1. RUN/project/shot-list.md (고칠 줄 확인)
2. RUN/project/asset-registry.md (PR-002 절 확인)
3. RUN/.claude/skills/higgsfield-generation/check_prompt.py (SKILL.md §1-5 지시대로 실행만 하고 내용은 읽지 않음)
(지침·정본·스킬 SKILL.md·prop.md는 turn1에서 이미 읽어 다시 열지 않음. 프롬프트 검사용 임시 파일은 scratchpad에 직접 써서 넘김)

부른 [TOOL]:
- 없음 (생성 지시가 아직 없어 generate_image를 보내지 않음. 이 프로젝트에서 써 본 모델·해상도라 get_cost도 생략)

고친 정본 파일:
- RUN/project/asset-registry.md: PR-002 절(크기, 물성, 상태 머신, 모양·사진·사용 흔적, 금지 항목. 제안값으로 표시)
- RUN/project/shot-list.md: 3-4·3-5 내용 줄과 소품 칸, 이음새 점검 3-4 → 3-5 줄 추가, 연속성 표 3-4 줄 수정 + 3-5 줄 추가
