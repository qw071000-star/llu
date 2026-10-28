import sys
base = "/home/user/llu/tests/agent-eval/runs-r2/C01/project/"
def sub(fn, pairs):
    p = base + fn
    s = open(p, encoding="utf-8").read()
    for a, b in pairs:
        if s.count(a) != 1:
            sys.exit(f"{fn}: not unique/missing: {a!r} ({s.count(a)})")
        s = s.replace(a, b)
    open(p, "w", encoding="utf-8").write(s)

ch2 = """### CH-002 손녀

| 확정 시트 job | 처리 모델 | 요소 ID | 파생 | 한계 |
|---|---|---|---|---|
| | | | | |

```text
IDENTITY: [ ]
WARDROBE: [ ]
ACTING PROFILE (참고용. 장면마다 그 장면의 행동으로 다시 쓴다): [ ]
VOICE: "[ ]"
알려진 실패 → 막는 문장: [ ]
```
초안(제안값): [ ]

## 장소
"""
sub("asset-registry.md", [
("## 장소\n", ch2),
("### PR-001 [이름]", "### PR-001 (아직 없음 — 막차 버스 등장 여부는 decisions.md 미결 3)"),
("### ST-001 [이름]", "### ST-001 해당 없음 (실사)"),
])

ok_example_row = "| (예시 — 첫 기록 때 이 줄을 지운다) 3-1 | 영상 | `[ ]` | [모델 · 해상도 · 길이 · 비율 · 소리] | | [예: 고개 돌리는 속도, 표정, 색감] | |\n"
p = base + "ok-cuts.md"
s = open(p, encoding="utf-8").read()
assert s.count(ok_example_row) == 1
s = s.replace(ok_example_row, "")
i = s.index("### 3-1 영상")
s = s[:i].rstrip() + "\n\n(아직 없음 — 첫 승인부터 쓴다)\n"
open(p, "w", encoding="utf-8").write(s)
