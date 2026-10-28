반영했습니다. 아직 생성하지 않았습니다.
- 겉옷: 남색 울 더플코트, 무릎 길이 (말씀하신 값)
- 안옷·바지·구두는 그대로, 목도리·모자·장갑은 없음 (제안값)
- 더플코트에 맞춰 고친 것: 단추 3개 → 토글 3개(모두 채움), 노치드 칼라 → 후드(내려 둠), 플랩 주머니 → 허리 양옆 플랩 패치 주머니. 다르면 말씀해 주세요.
- 에셋 대장 CH-001 아래에 "작업 중" 한 줄로 기록했습니다. 고정 문장은 승인 뒤에 바꿉니다.

**실패 위험과 막는 문장**
1. 옛 올리브 재킷이 코트 안에 겹치거나 섞임 → `The faded olive work jacket and its two chest pockets are GONE in every panel.`
2. 후드를 머리에 씌워 헤어까지 바뀜 → `Its hood is down, lying flat on his upper back, never on his head.`
3. 머리 없는 왼쪽 패널에 머리가 생기거나 상처처럼 보임 → `keep it intentionally HEADLESS, an editorial clothing crop, not an injury`
4. 얼굴이 새로 그려짐 → `preserve the exact same face; do not regenerate, reinterpret, beautify, age or reshape the face.`
5. 패널마다 코트 길이·토글이 다름 → `The hem falls at the knee in all three panels.` + `One physically identical outfit`
6. 소매가 손을 덮거나 손에 물건이 생김 → `The sleeves end at the wrist; both hands stay visible and empty.`
7. 겨울옷이라 목도리·모자·장갑이 저절로 생김 → `no scarf, no hat, no gloves`
8. GPT Image 2.5 질감이 3D 렌더 쪽으로 감 → `thick, matte, slightly worn wool with visible fibres, photographic, not CGI`

- 모드: 편집 (인물 시트 틀 2, 의상만 바꿈)
- 참조: image 1 = `job-ch001` (얼굴·헤어·세 패널 구조·배경·조명을 모두 지킬 기준)
- 모델: GPT Image 2.5
- 해상도: 1k 확인용 · 16:9 · 1장
- 길이: — (이미지)
- 저장: 「빈 정류장」/00 에셋/인물 `fld-chars`
- 검사 스크립트: 통과 (걸린 항목 없음)

```text
Edit reference image 1: change only the character's outfit, while keeping the character's identity exactly and preserving the sheet's existing three-panel structure exactly, including the intentionally HEADLESS left panel.

CHANGE — OUTFIT:
In all three panels: A knee-length navy wool duffle coat over a cream knit vest and a white collared shirt, dark grey wool trousers, scuffed brown leather shoes. The coat is thick, matte, slightly worn wool with visible fibres, photographic, not CGI. It closes with three toggles on rope loops, all fastened. Its hood is down, lying flat on his upper back, never on his head. Two flapped patch pockets sit at the hips. The hem falls at the knee in all three panels. Only the white shirt collar shows at the neck above the top toggle. The sleeves end at the wrist; both hands stay visible and empty. One physically identical outfit seen from different views. No logos, no prints, no unintended accessories: no scarf, no hat, no gloves.

REMOVE COMPLETELY:
The faded olive work jacket and its two chest pockets are GONE in every panel. Do not layer, merge or hybridize old and new clothing.

PRESERVE EXACTLY:
- LEFT PANEL: keep it intentionally HEADLESS, an editorial clothing crop, not an injury: no head, no face, no wound. Do not add, infer, reconstruct or complete a head or face.
- IDENTITY: preserve the exact same face; do not regenerate, reinterpret, beautify, age or reshape the face.
- HAIR: preserve the existing hair exactly; the hood never covers it.
- STRUCTURE: preserve all three poses, body proportions, crop boundaries, panel widths, panel order, empty hands.
- ENVIRONMENT: preserve the backdrop, lighting direction, exposure, shadows, palette, contrast and grain.

ONLY CHANGE: the outfit — the olive work jacket replaced by the knee-length navy wool duffle coat. The face and identity 100% identical to reference image 1.
```

남은 질문은 1번 하나입니다. A와 B 모두 프롬프트는 같습니다. 1번을 정하고 "보내"라고 하시면 1k로 1장 보냅니다.
1. 적용 범위: 지금 재킷은 승인 영상 1-2(지수 님 작업)·2-1·3-1과 OK 시작 이미지 2-2·3-2에 들어가 있습니다. 어느 쪽을 따를지 골라 주세요.
   - A. 교체: CH-001 의상을 더플코트로 바꿉니다(고정 문장 v2, 옛 시트는 폐기 목록으로). 위 5건을 다시 만들어야 장면이 이어집니다.
   - B. 파생: 지금 시트와 승인 컷은 그대로 두고 더플코트 상태를 따로 만듭니다(`char_grandpa_winter_v1`). 이 경우 쓸 컷을 알려 주세요.

=== 메타 ===
연 파일(순서대로):
1. project/asset-registry.md (40–53줄, CH-001 절을 고치려고 엶)
- 실행만 함: .claude/skills/higgsfield-generation/check_prompt.py (`--kind image --refs 1`, 결과 OK. 프롬프트는 스크래치패드 파일로 검사)

부른 [TOOL]: 없음

고친 정본 파일:
- project/asset-registry.md: CH-001 고정 문장 블록 아래에 "작업 중 · 겨울 코트 의상 수정" 한 줄 추가 (사용자 답 / 제안값 / 적용 범위 미정 표시). 고정 문장·확정 job은 그대로 둠
