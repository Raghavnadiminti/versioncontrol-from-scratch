from pathlib import Path
import sys
from createcommit import FetchTree


current = Path.cwd()


if len(sys.argv) < 2:
    print("branch name not provided")
    sys.exit(1)

branch_name =sys.argv[1]

print(current)
branches_base = current / Path("ref") / Path("branches") 
print(branches_base)
branch_path = branches_base / branch_name


if not branch_path.exists() or not branch_path.is_dir():
    print("Cannot switch branch")
    sys.exit(1)


current_branch_file = current / "crntbranch"
current_branch_file.write_text(branch_name, encoding="utf-8")

print(f"Switched to branch '{branch_name}'") 


head_file = branch_path / "head"

if not head_file.exists():
    print("head file not found")
    exit(1)

commit_hash, commit_msg = head_file.read_text(
    encoding="utf-8"
).strip().split("\t", 1)

BASE=Path.cwd()
OBJ_DIR = BASE / "obj"
commit_obj = OBJ_DIR / commit_hash

if not commit_obj.exists():
    print("Commit object not found in obj/")
    sys.exit(1)

raw = commit_obj.read_bytes()
_, content = raw.split(b"\0", 1)


print(content.decode())

first_line = content.decode().splitlines()[0]
print(first_line.split(' ')[1])

ft=FetchTree() 
cur=Path.cwd()/Path('folder1')
ft.read_tree(first_line.split(' ')[1],cur)







