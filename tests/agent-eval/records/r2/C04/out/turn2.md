반영했습니다. 겨울 코트는 **추가 상태(파생)**로 만들고, 기존 시트와 승인 컷은 그대로 둡니다. 코트 안 옷, 바지, 구두는 유지하고 목도리·모자·장갑은 넣지 않습니다. 이 셋은 "그대로"라고 하셔서 제안값으로 기록했습니다.

더플코트로 정해지면서 제가 앞서 제안한 코트 세부(노치드 칼라, 덮개 주머니)는 맞지 않게 됐습니다. 그래서 세부를 아래처럼 바꿨습니다. 확인해 주세요.
- 바뀐 제안: **혼 토글 4개를 로프 고리로 채움, 후드는 내려 등에 붙임, 허리에 패치 주머니 2개, 지퍼·로고 없음**

**실패 위험과 막는 문장**
1. 옛 올리브 재킷이 코트 안이나 위에 겹쳐 남음 → `The faded olive work jacket … GONE in every panel. Do not layer, merge or hybridize…`
2. 얼굴이 다시 그려져 다른 사람이 됨 → `preserve the exact same face; do not regenerate…`
3. 왼쪽 패널에 머리나 목 상처가 생김 → `intentionally HEADLESS … not an injury`
4. 후드가 올라가거나 모자·목도리가 생겨 헤어가 가려짐 → `the hood is down…` · `No scarf, no hat, no gloves`
5. 코트 길이가 허벅지나 발목으로 흔들림 → `knee length, the hem ending at the knee`
6. 요즘 스포츠웨어처럼 지퍼나 로고가 생김(현대 물건 금지) → `no zip, no logos, no prints`
7. 손에 물건이 생기거나 손이 주머니에 들어감 → `empty hands`
8. 배경·조명·질감이 바뀜 → `ENVIRONMENT: preserve the backdrop, lighting…`

- 모드: 편집(틀 2, 시트 구조·얼굴 보존)
- 참조: reference image 1 = `job-ch001` (얼굴·체형·시트 구조·배경 기준, 1장)
- 모델: GPT Image 2.5 · 1k(확인용) · 16:9 · 1장 · 약 4 크레딧(추정)
- 저장: 「빈 정류장」/00 에셋/인물 (`fld-chars`)
- 확정되면 요소 이름: `char_grandpa_wintercoat_v1`
- 검사 스크립트: 통과(FAIL 0 · WARN 0)

```text
Edit reference image 1: change only the character's outer coat, while keeping the character's identity exactly and preserving the sheet's existing three-panel structure exactly, including the intentionally HEADLESS left panel.

CHANGE — OUTFIT:
In all three panels, the outer jacket becomes a navy wool duffle coat, knee length, the hem ending at the knee. It is fastened with four horn toggles on dark rope loops, the hood is down and lies flat on the upper back, and it has two plain patch pockets at the hips. Matte, slightly worn wool with soft creases at the elbows; no zip, no logos, no prints. At the neck, the same white collared shirt collar sits over the same cream knit vest. Below the hem, the same dark grey wool trousers and scuffed brown leather shoes.

REMOVE COMPLETELY:
The faded olive work jacket and its two flapped chest pockets are GONE in every panel. Do not layer, merge or hybridize old and new clothing. No scarf, no hat, no gloves, no added layers.

PRESERVE EXACTLY:
- LEFT PANEL: keep it intentionally HEADLESS, an editorial clothing crop, not an injury: no head, no face, no wound. Do not add, infer, reconstruct or complete a head or face.
- IDENTITY: preserve the exact same face; do not regenerate, reinterpret, beautify, age or reshape the face. Keep the same short grey crew cut.
- STRUCTURE: preserve all three poses, body proportions, crop boundaries, panel widths, panel order, empty hands.
- ENVIRONMENT: preserve the backdrop, lighting direction, exposure, shadows, palette, contrast and grain.

ONLY CHANGE: the outer jacket becomes the navy wool knee-length duffle coat described above. The face and identity 100% identical to reference image 1.
```

에셋 대장 CH-001 아래에 이 초안 한 줄을 기록했습니다(제안값 표시 포함).

질문: 토글·후드·주머니 세부를 이대로 두고 1k 확인용으로 보낼까요? 바꿀 것만 말씀해 주세요.

=== 메타 ===
연 파일(순서대로):
1. .claude/skills/higgsfield-generation/check_prompt.py
2. project/asset-registry.md (CH-001 절, 기록 확인용)

(이전 턴에서 연 파일·OK 대장 CH-001 카드 내용을 이어서 사용)

부른 [TOOL]: 없음 (생성 지시 전이라 보내지 않음)

임시 파일: tmp/ch001_wintercoat.txt (검사 스크립트 입력, `--kind image --refs 1` → OK, 걸린 항목 없음)

고친 정본 파일:
- project/asset-registry.md: CH-001 아래에 `초안(제안값) — CH-001 겨울 코트` 한 줄을 추가
