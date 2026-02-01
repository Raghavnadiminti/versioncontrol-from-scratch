import sys
from createcommit import Commit
from pathlib import Path
if "-m" not in sys.argv:
    print("Usage: python main.py -m \"commit message\"")
    sys.exit(1)

msg_index=sys.argv.index("-m") + 1
if msg_index>=len(sys.argv):
    print("Commit message missing")
    sys.exit(1)

cwd = Path.cwd()
branch_file = cwd / "crntBranch"

if not branch_file.exists():
    print("No current branch found")
    sys.exit(1)

branch = branch_file.read_text(encoding="utf-8").strip()

if not branch:
    print("Current branch file is empty")
    sys.exit(1)

message = sys.argv[msg_index]

commit = Commit("obj",branch)
commit_hash = commit.commit(message)

branch_path = cwd / "ref" / "branches" / branch
head_file = branch_path / "head"
commitref_file = branch_path / "commitRef"


entry = f"{commit_hash}\t{message}"
print(entry)

head_file.write_text(entry, encoding="utf-8")

print(f"[{branch} {commit_hash}] {message}")



