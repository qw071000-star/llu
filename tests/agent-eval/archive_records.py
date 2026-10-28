#!/usr/bin/env python3
"""맹검 시험 기록 보관: 실행 폴더와 서브에이전트 대화 기록을 records/로 옮긴다.

실행: python3 tests/agent-eval/archive_records.py <서브에이전트 기록 폴더>
- 실행 폴더(runs, runs-r2, runs-sonnet)에서 .git과 .claude(키트 사본)는 뺀다. 키트 판은 records/README.md의 커밋으로 확인한다.
- 정본 변경은 실행 폴더의 git(시작 커밋 base)과 비교해 changes.diff로 남긴다.
- 서브에이전트 대화(jsonl)는 agents.tsv로 이름을 붙이고, 사용자 이메일을 가린 뒤 gzip으로 저장한다.
"""
import csv, gzip, os, re, shutil, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REC = os.path.join(HERE, "records")
SRC = sys.argv[1]
EMAIL = re.compile(rb"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")

for rnd, folder in [("r1", "runs"), ("r2", "runs-r2"), ("sonnet", "runs-sonnet")]:
    root = os.path.join(HERE, folder)
    if not os.path.isdir(root):
        continue
    for chain in sorted(os.listdir(root)):
        run = os.path.join(root, chain)
        dst = os.path.join(REC, rnd, chain)
        shutil.rmtree(dst, ignore_errors=True)
        shutil.copytree(run, dst, ignore=shutil.ignore_patterns(".git", ".claude"))
        diff = subprocess.run(["git", "-C", run, "diff", "base", "--", "project"], capture_output=True, text=True).stdout
        new = subprocess.run(["git", "-C", run, "status", "--short", "--", "project"], capture_output=True, text=True).stdout
        with open(os.path.join(dst, "changes.diff"), "w") as f:
            f.write("# 정본 변경 (시작 상태 대비)\n# 새 파일·바뀐 파일 목록\n" + new + "\n" + diff)

with open(os.path.join(HERE, "agents.tsv")) as f:
    rows = list(csv.DictReader(f, delimiter="\t"))
tdir = os.path.join(REC, "transcripts")
os.makedirs(tdir, exist_ok=True)
for r in rows:
    src = os.path.join(SRC, f"agent-{r['agent_id']}.jsonl")
    if not os.path.exists(src):
        continue
    name = f"{r['round']}_{r['role']}_{r['chain'].replace(',', '-')}_{r['model']}.jsonl.gz"
    data = EMAIL.sub(b"[email]", open(src, "rb").read())
    with gzip.open(os.path.join(tdir, name), "wb") as g:
        g.write(data)
print("archived")
