from pathlib import Path

BASE = Path.cwd()


dirs = [
    BASE / "obj",
    BASE / "ref" / "branches",
]

for d in dirs:
    d.mkdir(parents=True, exist_ok=True)

crnt_branch = BASE / "crntBranch"
if not crnt_branch.exists():
    crnt_branch.write_text("main", encoding="utf-8")


main_branch = BASE / "ref" / "branches" / "main"
main_branch.mkdir(exist_ok=True)


(main_branch / "head").touch(exist_ok=True)
(main_branch / "commitRef").touch(exist_ok=True)

print("Initialized empty repository with main branch")
