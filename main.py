import sys
import commit
import createBranch
import bundle
import getBack
import switchBranch


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  myvcs commit -m \"message\"")
        print("  myvcs createBranch <branch_name>")
        print("  myvcs switchBranch <branch_name>")
        print("  myvcs bundle <bundle_name>")
        print("  myvcs getBack <commit_hash>")
        return

    command = sys.argv[1]
    args = sys.argv[2:]

    if command == "commit":
       
        commit.run(args)

    elif command == "createBranch":
       
        if len(args) != 1:
            print("Usage: myvcs createBranch <branch_name>")
            return
        createBranch.run(args)

    elif command == "switchBranch":
      
        if len(args) != 1:
            print("Usage: myvcs switchBranch <branch_name>")
            return
        switchBranch.run(args)

    elif command == "bundle":
     
        if len(args) != 1:
            print("Usage: myvcs bundle <bundle_name>")
            return
        bundle.run(args)

    elif command == "getBack":
      
        if len(args) != 1:
            print("Usage: myvcs getBack <commit_hash>")
            return
        getBack.run(args)

    else:
        print(f"Unknown command: {command}")


if __name__ == "__main__":
    main()
