제안값 6개를 모두 그대로 반영했습니다. 정본에는 `제안값`으로 기록했습니다.
- 에셋 대장 PR-002: 크기·물성·상태 머신·고정 설명문 초안
- 컷 목록: 3-4 "가방을 열고 할머니 사진 액자를 꺼낸다", 3-5 "손에 액자". 이음새 3-4 → 3-5 행과 연속성 표의 PR-002 열 추가
- decisions §6: PR-002 상태 한 줄

아래는 위험 목록과 프롬프트입니다. 아직 보내지 않았습니다. 검사 스크립트는 통과했습니다(1,535자, 걸린 항목 없음).

**실패 위험 → 막는 문장**
1. 사진 속 여성이 실제 사람처럼 튀어나오거나 액자 밖으로 나옴 → `The woman exists only as a flat printed photograph behind the glass: no depth, no part of her extends beyond the frame.`
2. "no people"과 부딪쳐 사진이 비어 나옴 → `no real people; the only person is the woman inside the printed photograph.`
3. GPT Image의 3D 렌더 질감 → 첫 문장 `shot as a real photograph on film with natural fine grain — not a 3D render, not CGI.`
4. 현대식 액자(플라스틱·아크릴·금박 장식·흰 매트) → `Era lock: … early-1990s rural South Korea` + Avoid 목록
5. 사진·액자 위의 날짜 스탬프나 글씨(글자 금지) → `date stamps or any writing on the photograph or the frame`
6. 유리 반사가 얼굴을 덮음 → `one soft diagonal reflection that does not hide her face.`

- 모드: 신규 · 참조 없음
- 모델: GPT Image 2.5 · 1k(확인용) · 16:9 · 1장 · 약 4 크레딧
- 저장: 「빈 정류장」/00 에셋/소품 `fld-props`
- 요소 이름(확정 후): `prop_photo_frame_v1`

```text
Photorealistic product-reference photograph, shot as a real photograph on film with natural fine grain — not a 3D render, not CGI. A small dark brown wooden standing photo frame, about 15 x 20 cm (one and a half times an old man's palm), with a glass front and a folding wooden easel stand at the back, holding a faded colour 10 x 15 cm portrait photograph of a Korean woman in her sixties, head and shoulders, facing the camera, short permed hair, a faint smile; paint worn off at the frame corners, fine scratches on the glass, the photograph's edges yellowed with age.
The frame stands upright on its easel stand, seen from the front at a slight three-quarter angle so the edge of the wooden frame is visible. The woman exists only as a flat printed photograph behind the glass: no depth, no part of her extends beyond the frame. The wood and glass are light and rigid; nothing bends. The glass shows one soft diagonal reflection that does not hide her face.
Isolated on a plain seamless light grey studio background, nothing else in frame — no scene, no room, no other objects, no hands, no real people; the only person is the woman inside the printed photograph. Soft even studio lighting from the front-top, minimal shadow. Sharp focus throughout.
Era lock: an ordinary household object from early-1990s rural South Korea; nothing more recent.
Avoid: plastic, acrylic, metal or ornate gilded frames, white photo mats, digital-print gloss, date stamps or any writing on the photograph or the frame, brand logos, text, watermarks.
```

참고: 이 스튜디오 이미지는 모양과 재질의 기준입니다. 영상에 쓸 요소는 소품 규칙대로 3-4 장면 프레임에서 잘라 만들어야 크기가 맞습니다.

질문 두 가지:
1. 이대로 1k 한 장 보낼까요?
2. 영상에서 할머니 얼굴이 또렷이 보여야 하나요? 제안 — 또렷이 보이지 않게 둠. 액자는 비스듬히 들고 유리 반사가 얼굴을 일부 가림 (이유: 할머니는 새 인물이라 컷마다 얼굴이 달라질 위험이 큽니다. 이 답은 소품 이미지에는 영향이 없고 3-4·3-5 프롬프트에만 들어갑니다)

=== 메타 ===
연 파일(순서대로):
1. RUN/.claude/skills/higgsfield-generation/check_prompt.py (사용법 머리 부분, SKILL §1의 5번이 가리킴)
2. RUN/project/asset-registry.md (PR-002 절 수정)
3. RUN/project/shot-list.md (3-4·3-5 줄, 이음새, 연속성 표 수정)
4. RUN/project/decisions.md (§6 수정)
(지침·스킬·정본은 turn1에서 읽은 내용을 사용)

임시 파일: RUN/tmp/pr002_prompt.txt, RUN/tmp/pr002_fixed.txt
검사: python3 check_prompt.py --kind image tmp/pr002_prompt.txt --refs 0 --must-include tmp/pr002_fixed.txt → OK(1535자, 걸린 항목 없음)

부른 [TOOL]: 없음 (생성 지시 전이므로 보내지 않음. 이미지 1k 비용은 sim 표의 값 약 4 크레딧)

고친 정본 파일:
- RUN/project/asset-registry.md — PR-002 표(요소 ID·출처·크기·물성·상태 머신, 제안값), 초안 줄, 고정 설명문 초안
- RUN/project/shot-list.md — 3-4·3-5 내용과 인물·소품 칸(PR-002 추가), 이음새 3-4 → 3-5 행 추가, 연속성 표에 PR-002 열과 3-5 행 추가
- RUN/project/decisions.md — §6에 PR-002 상태 한 줄(제안값)
