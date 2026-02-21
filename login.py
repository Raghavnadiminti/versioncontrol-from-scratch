from pymongo import MongoClient
import bcrypt
import getpass
import json
from pathlib import Path



client = MongoClient("")
db = client["githubclone"]
users = db["users"]



CONFIG_DIR = Path.cwd() / "config"
CONFIG_FILE = CONFIG_DIR / "config.json"



def save_session(username: str, userid: str):
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)

    data = {
        "username": username,
        "userid": userid
    }

    with CONFIG_FILE.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print("Login session saved")



def cli_login():
    print("\n=== VCS LOGIN ===")

    username = input("Username: ").strip()
    email = input("Email: ").strip()
    password = getpass.getpass("Password: ")
    print(password)
    if not username or not email or not password:
        print("All fields required")
        return


    user = users.find_one({
        "username": username,
        "email": email
    })

    if not user:
        print("User not found")
        return

    stored_hash = user.get("password")

    if not stored_hash:
        print("Password not set for user")
        return


    if not bcrypt.checkpw(
        password.encode("utf-8"),
        stored_hash.encode("utf-8")
    ):
        print("Wrong password")
        return

    userid = str(user["_id"])

    save_session(username, userid)

    print("Login successful!")

if __name__ == "__main__":
    cli_login()