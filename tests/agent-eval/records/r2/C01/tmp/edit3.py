import sys
R = "/home/user/llu/tests/agent-eval/runs-r2/C01/"
def sub(fn, pairs):
    p = R + fn
    s = open(p, encoding="utf-8").read()
    for a, b in pairs:
        if s.count(a) != 1:
            sys.exit(f"{fn}: {a!r} count {s.count(a)}")
        s = s.replace(a, b)
    open(p, "w", encoding="utf-8").write(s)
T = "「빈 정류장」"
sub("project/asset-registry.md", [
("# 에셋·폴더 대장 — 「[작품명]」", f"# 에셋·폴더 대장 — {T}"),
("| 프로젝트 | 「[작품명]」 | `[ ]` |", f"| 프로젝트 | {T} | `prj-new-0001` |"),
("| 공통 에셋 | 00 에셋 / 인물 · 장소 · 소품 (실사라 그림체 폴더 없음) | `[ ]` · `[ ]` · `[ ]` |",
 "| 공통 에셋 | 00 에셋 / 인물 · 장소 · 소품 (실사라 그림체 폴더 없음) | `fld-00 에셋` / `fld-인물` · `fld-장소` · `fld-소품` |"),
("| 시험·보관 | 99 시험·보관 | `[ ]` |", "| 시험·보관 | 99 시험·보관 | `fld-99 시험·보관` |"),
])
sub("project/decisions.md", [
("# 확정 사항 — 「[작품명]」", f"# 확정 사항 — {T}"),
("| 1 | 작품명(가제) | — (필수) | 없음 — 사용자에게 물음. Higgsfield 프로젝트 이름에 쓴다 |",
 f"| ~~1~~ | ~~작품명(가제)~~ | — | 해결: {T} — 2026-10-28 사용자 답. Higgsfield 프로젝트 `prj-new-0001` |"),
])
sub("project/ok-cuts.md", [("# OK 대장 — 「[작품명]」", f"# OK 대장 — {T}")])
sub("project/shot-list.md", [("# 컷 목록 — 「[작품명]」", f"# 컷 목록 — {T}")])
sub(".claude/instructions.md", [
("- 작품: 「[작품명]」 · Higgsfield 프로젝트: [이름] (`[project_id]`)",
 f"- 작품: {T} · Higgsfield 프로젝트: 빈 정류장 (`prj-new-0001`, 워크스페이스 `ws-sim-0001`)"),
("- 정본 위치: [Claude Doc 링크 / 프로젝트 지식 / 리포 `project/`]", "- 정본 위치: 리포 `project/`"),
])
