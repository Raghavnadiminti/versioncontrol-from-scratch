from pathlib import Path
import boto3
from botocore.exceptions import ClientError
from bundle import create_bundle
from dotenv import load_dotenv
load_dotenv()


# BUCKET_NAME = ""

IGNORE_DIRS = {
    ".git",
    "__pycache__",
    "node_modules",
    ".DS_Store"
}

IGNORE_FILES = {
    ".env"
}

MAX_FILE_SIZE_MB = 100

s3 = boto3.client("s3")

from pathlib import Path
from metadata import write_metadata_file

repo = Path.cwd()

metadata_path = write_metadata_file(repo)

print("Metadata created at:", metadata_path)

def validate_name(value: str, name: str):
    """Prevent unsafe S3 prefixes"""
    if not value or "/" in value or ".." in value:
        raise ValueError(f"Invalid {name}")


def bucket_accessible():
    try:
        s3.head_bucket(Bucket=BUCKET_NAME)
    except ClientError as e:
        raise RuntimeError(f"S3 bucket not accessible: {e}")


def repo_exists(prefix: str) -> bool:
    res = s3.list_objects_v2(
        Bucket=BUCKET_NAME,
        Prefix=prefix,
        MaxKeys=1
    )
    return "Contents" in res


def safe_file_allowed(path: Path) -> bool:
    if path.name in IGNORE_FILES:
        return False

    size_mb = path.stat().st_size / (1024 * 1024)
    if size_mb > MAX_FILE_SIZE_MB:
        print(f"Skipping large file: {path.name}")
        return False

    return True

def object_exists_same_size(local_path: Path, key: str) -> bool:
    """
    Check if S3 object exists and has same size as local file.
    Used to skip unchanged uploads.
    """
    try:
        obj = s3.head_object(
            Bucket=BUCKET_NAME,
            Key=key
        )
        return obj["ContentLength"] == local_path.stat().st_size

    except ClientError as e:
     
        error_code = e.response.get("Error", {}).get("Code")

        if error_code in ("404", "NoSuchKey", "NotFound"):
            return False

        
        raise RuntimeError(f"S3 check failed: {e}")
    

def upload_folder(local_folder: Path, s3_prefix: str) -> int:

    if not local_folder.exists() or not local_folder.is_dir():
        raise FileNotFoundError("Bundle folder not found")

    uploaded = 0
    skipped = 0

    for path in local_folder.rglob("*"):

       
        if path.is_dir():
            continue

     
        if not safe_file_allowed(path):
            continue

        
        relative_path = path.relative_to(local_folder)
        s3_key = f"{s3_prefix}/{relative_path.as_posix()}"

        try:
            
            if object_exists_same_size(path, s3_key):
                print(f"Skipping unchanged → {s3_key}")
                skipped += 1
                continue

            print(f"Uploading → {s3_key}")

            s3.upload_file(
                Filename=str(path),
                Bucket=BUCKET_NAME,
                Key=s3_key
            )

            uploaded += 1

        except ClientError as e:
            raise RuntimeError(f"Upload failed for {path}: {e}")

    print(f"Uploaded: {uploaded}, Skipped: {skipped}")
    return uploaded


def upload_repo_safe(
    user_id: str,
    repo_name: str,
    bundle_path: str | Path,
    overwrite: bool = False
):
    """
    Safely upload repo bundle to S3
    """

    bundle_path = Path(bundle_path)

   
    validate_name(user_id, "user_id")
    validate_name(repo_name, "repo_name")

   
    bucket_accessible()

 
    print("Creating bundle...")
    create_bundle(bundle_path)

    if not bundle_path.exists():
        raise RuntimeError("Bundle creation failed")

    
    s3_prefix = f"users/{user_id}/repos/{repo_name}"

    
    if repo_exists(s3_prefix):
        print("Repo exists → updating files (overwrite mode)")
    else:
        print("New repo → creating")

   
    print("Uploading bundle...")
    total = upload_folder(bundle_path, s3_prefix)

    print(f"Upload completed ({total} files uploaded)")