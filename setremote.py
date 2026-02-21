import json
from pathlib import Path
from pymongo import MongoClient
from bson import ObjectId


CONFIG_FILE = Path.cwd() / "config" / "config.json"


def set_reponame_verified(reponame: str, mongo_uri: str):


    if not CONFIG_FILE.exists():
        raise Exception("Not logged in. Please run login first.")

    try:
        with CONFIG_FILE.open("r", encoding="utf-8") as f:
            config = json.load(f)
    except json.JSONDecodeError:
        raise Exception("Config corrupted. Please login again.")

    userid = config.get("userid")

    if not userid:
        raise Exception("userid missing. Please login again.")

    reponame = reponame.strip()
    if not reponame:
        raise ValueError("Repository name cannot be empty.")


    client = MongoClient(mongo_uri)
    db = client.get_default_database()

    repos = db["repositories"]  # ← collection name

    try:
        owner_id = ObjectId(userid)
    except Exception:
        raise Exception("Invalid userid format in config.")

    repo = repos.find_one({
        "name": reponame,
        "owner": owner_id
    })

    if not repo:
        raise Exception(
            f"Repository '{reponame}' not found for this user."
        )


    config["reponame"] = reponame

    with CONFIG_FILE.open("w", encoding="utf-8") as f:
        json.dump(config, f, indent=2)

    print(f"Repository set to '{reponame}'")


if __name__=="__main__":

    reponame=input("enter repo name: ") 

    set_reponame_verified(reponame,"")
        
