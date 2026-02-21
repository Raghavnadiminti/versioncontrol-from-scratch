from uploads3 import upload_repo_safe 
from pathlib import Path
from auth import get_userid,getreponame  
import sys 
user_id=get_userid() 
repo_name=getreponame() 
if not user_id or not repo_name:
    sys.exit(1) 

upload_repo_safe(
    user_id=user_id,
    repo_name=repo_name,
    bundle_path=Path("./bundle")
) 

