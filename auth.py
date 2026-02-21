import json
from pathlib import Path


CONFIG_FILE = Path.cwd() / "config" / "config.json"


class LoginRequiredError(Exception):
    pass


def get_userid():
    """
    Returns logged-in user's userid.
    Raises:
        LoginRequiredError -> if user not logged in
    """


    if not CONFIG_FILE.exists():
        raise LoginRequiredError(
            " Not logged in. Please run: vcs login"
        )

    try:
        with open(CONFIG_FILE, "r") as f:
            data = json.load(f)

    except json.JSONDecodeError:
        raise LoginRequiredError(
            "Invalid login session. Please login again."
        )

    userid = data.get("userid")

    if not userid:
        raise LoginRequiredError(
            " Login data missing. Please run: vcs login"
        )

    return userid 


def getreponame():
    """
    Returns logged-in user's userid.
    Raises:
        LoginRequiredError -> if user not logged in
    """


    if not CONFIG_FILE.exists():
        raise LoginRequiredError(
            " Not logged in. Please run: vcs login"
        )

    try:
        with open(CONFIG_FILE, "r") as f:
            data = json.load(f)

    except json.JSONDecodeError:
        raise LoginRequiredError(
            "Invalid login session. Please login again."
        )

    reponame = data.get("reponame")

    if not reponame:
        raise LoginRequiredError(
            " Login data missing. Please run: vcs login"
        )

    return reponame 

