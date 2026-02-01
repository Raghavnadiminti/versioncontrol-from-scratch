from pathlib import Path
import shutil
import sys

def create_bundle(bundle_path):
    repo = Path.cwd()
    bundle = Path(bundle_path)

    if not (repo / "obj").exists() or not (repo / "ref").exists():
        print("Not a valid repo (obj/ or ref/ missing)")
        sys.exit(1)

    if bundle.exists():
        print("Bundle path already exists")
        sys.exit(1)

    bundle.mkdir(parents=True)

    shutil.copytree(repo / "obj", bundle / "obj")
    shutil.copytree(repo / "ref", bundle / "ref")

curr=Path.cwd()
create_bundle(curr/'bundle')