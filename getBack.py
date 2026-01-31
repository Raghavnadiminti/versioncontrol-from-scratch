from createcommit import FetchTree 
import sys
from pathlib import Path


if "-m" not in sys.argv:
    print('Usage: python main.py -m "commit message"')
    sys.exit(1)

msg_index = sys.argv.index("-m") + 1
if msg_index >= len(sys.argv):
    print("Commit message missing")
    sys.exit(1)

target_message = sys.argv[msg_index]


BASE = Path.cwd()

branch_file = BASE / "crntBranch"
if not branch_file.exists():
    print("No current branch found")
    sys.exit(1)

branch = branch_file.read_text(encoding="utf-8").strip()


REF_FILE = BASE /  "ref" / "branches" / branch / "commitRef"
OBJ_DIR = BASE / "obj"

if not REF_FILE.exists():
    print("commitRef file not found")
    sys.exit(1)


commit_hash = None

with REF_FILE.open() as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        h, msg = line.split("\t", 1)
        if msg == target_message:
            commit_hash = h
            break

if not commit_hash:
    print("Commit message not found")
    sys.exit(1)


commit_obj = OBJ_DIR / commit_hash

head_FILE = BASE /  "ref" / "branches" / branch / "head"

with head_FILE.open("w", encoding="utf-8") as f:
    f.write(f"{commit_hash}\t{target_message}")



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

