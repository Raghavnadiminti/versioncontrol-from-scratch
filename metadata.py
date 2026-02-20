from pathlib import Path
import json
from typing import Dict, List


def _safe_read_text(path: Path) -> str:
    """Safely read file text."""
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8").strip()


def _parse_commit_ref(commit_ref_path: Path) -> List[Dict]:
    """
    Parse commitRef file safely.
    Format:
        <hash>\t<message>
    """
    commits = []

    if not commit_ref_path.exists():
        return commits

    for line in _safe_read_text(commit_ref_path).splitlines():
        if not line.strip():
            continue

        parts = line.split("\t", 1)

        if len(parts) != 2:
            continue 

        commit_hash, message = parts

        commits.append({
            "hash": commit_hash.strip(),
            "message": message.strip()
        })

  
    commits.reverse()

    return commits


def _read_head(head_path: Path) -> str | None:
    """Extract head commit hash safely."""
    text = _safe_read_text(head_path)

    if not text:
        return None

    return text.split("\t")[0].strip()


def build_repo_metadata(repo_root: Path) -> dict:
    """
    Build repository metadata JSON.

    Parameters
    ----------
    repo_root : Path
        Root folder of local VCS repository.

    Returns
    -------
    dict
        Metadata dictionary.
    """

    repo_root = Path(repo_root).resolve()

    ref_dir = repo_root / "ref" / "branches"

    if not ref_dir.exists():
        raise RuntimeError("Branches directory not found")

    metadata = {
        "defaultBranch": None,
        "branches": {}
    }

    # detect default branch
    current_branch_file = repo_root / "crntBranch"
    if current_branch_file.exists():
        metadata["defaultBranch"] = _safe_read_text(
            current_branch_file
        )

    # iterate branches safely
    for branch_dir in sorted(
        p for p in ref_dir.iterdir() if p.is_dir()
    ):
        branch_name = branch_dir.name

        head_path = branch_dir / "head"
        commit_ref_path = branch_dir / "commitRef"

        head_hash = _read_head(head_path)
        commits = _parse_commit_ref(commit_ref_path)

        metadata["branches"][branch_name] = {
            "head": head_hash,
            "commitCount": len(commits),
            "commits": commits
        }

    # fallback default branch
    if not metadata["defaultBranch"]:
        metadata["defaultBranch"] = (
            next(iter(metadata["branches"]), None)
        )

    return metadata


def write_metadata_file(repo_root: Path) -> Path:
    

    repo_root = Path(repo_root).resolve()

    metadata = build_repo_metadata(repo_root)

    metadata_path = repo_root / "metadata.json"

    metadata_path.write_text(
        json.dumps(metadata, indent=2),
        encoding="utf-8"
    )

    return metadata_path