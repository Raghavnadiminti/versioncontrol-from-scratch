from branch import Branch
from pathlib import Path
import sys

BASE = Path.cwd()


branch_file = BASE / "crntBranch"
if not branch_file.exists():
    print("No current branch found")
    exit(1)

current_branch = branch_file.read_text(encoding="utf-8").strip()


current_head = BASE / "ref" / "branches" / current_branch / "head"
if not current_head.exists():
    print("Current branch head not found")
    exit(1)

head_content = current_head.read_text(encoding="utf-8").strip()

if len(sys.argv) < 2:
    print("branch name not provided")
    sys.exit(1)


new_branch = sys.argv[1]  

branch_base = BASE / "ref" / "branches" / new_branch
branch_base.mkdir(parents=True, exist_ok=False)

commitRef = branch_base / "commitRef"
head = branch_base / "head"
head_content=head_content+'\n'

commitRef.write_text(head_content, encoding="utf-8")

head.write_text(head_content, encoding="utf-8")

print(f"Branch '{new_branch}' created at {head_content}")




