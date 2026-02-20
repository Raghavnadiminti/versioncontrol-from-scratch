import sys
import subprocess

def run_script(script, args):
    subprocess.run(
        [sys.executable, script] + args,
        check=True
    )

def main():
    if len(sys.argv) < 2:
        print("Usage: myvcs <command> [args]")
        return

    cmd = sys.argv[1]
    args = sys.argv[2:]

    if cmd == "commit":
        run_script("commit.py", args)

    elif cmd == "createBranch":
        run_script("createBranch.py", args)

    elif cmd == "switchBranch":
        run_script("switchBranch.py", args)

    elif cmd == "bundle":
        run_script("bundle.py", args)

    elif cmd == "getBack":
        run_script("getBack.py", args)

    else:
        print("Unknown command")

if __name__ == "__main__":
    main()
