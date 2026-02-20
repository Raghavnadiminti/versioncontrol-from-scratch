
class CreateBlob:

    def __init__(self,path):
        from pathlib import Path
        current=Path(__file__).resolve().parent
        self.basePath=current/Path(path)
        
    def read_file_bytes(self,path):
        from pathlib import Path 
        return Path(path).read_bytes()

    def create_blob(self,file):
        import hashlib
        from pathlib import Path
        data = self.read_file_bytes(file)
        header = f"blob {len(data)}\0".encode()
        full = header + data
        sha = hashlib.sha1(full).hexdigest()
        return sha,full

    def write_blob(self,data,hash):
        from pathlib import Path
        obj_path=self.basePath
        path = obj_path/Path(hash)
        path.parent.mkdir(parents=True, exist_ok=True)
       
        if not path.exists():
            path.write_bytes(data)

    def blob(self,file,hash=None):
        sha,blobdata=self.create_blob(file)
        self.write_blob(blobdata,sha) 
        return sha 









