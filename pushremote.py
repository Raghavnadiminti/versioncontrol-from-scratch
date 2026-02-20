from uploads3 import upload_repo_safe 
from pathlib import Path
upload_repo_safe(
    user_id="123",
    repo_name="my-project",
    bundle_path=Path("./bundle")
)