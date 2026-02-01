class Tree:
    def __init__(self, objects_dir):
        self.objects_dir = objects_dir

    def read_path(self, node):
        from pathlib import Path
        from createblob import CreateBlob
        import hashlib
        blob =CreateBlob(self.objects_dir)
        if node.is_file():
            blob_hash=blob.blob(node)
            return blob_hash
        entries =[]
        
        for child in sorted(node.iterdir(), key=lambda x: x.name):
            child_hash = self.read_path(child)
            if child.is_file():
                mode="100644"
            else:
                mode="40000"
            entries.append(f"{mode} {child.name} {child_hash}")

        tree_content="\n".join(entries).encode()
        header=f"tree {len(tree_content)}\0".encode()
        full=header + tree_content
        tree_hash = hashlib.sha1(full).hexdigest()
        obj_path = Path(self.objects_dir) / tree_hash
        if not obj_path.exists():
            obj_path.write_bytes(full)

        return tree_hash


class Commit:
    def __init__(self,obj,branch):
        self.branch = branch
        self.objects_dir=obj

    def create_commit(self, tree_hash, message, author="raghavraghav"):
        import time
        import hashlib
        from pathlib import Path

        timestamp=int(time.time())
        content =(
            f"tree {tree_hash}\n"
            f"author {author} {timestamp}\n"
            f"committer {author} {timestamp}\n\n"
            f"{message}\n"
        ).encode()

        header=f"commit {len(content)}\0".encode()
        full=header + content
        commit_hash=hashlib.sha1(full).hexdigest()

        obj_path = Path(self.objects_dir) / commit_hash
        if not obj_path.exists():
            obj_path.write_bytes(full)

        return commit_hash 
    
    def commit(self,message):
        from pathlib import Path

        tree=Tree('obj') 
        current = Path.cwd() 
        pat = Path(current)/Path('folder1')
        tree_hash=tree.read_path(pat) 
        print(tree_hash)
        treeHash_path = current / "obj" /tree_hash

        # if treeHash_path.exists():
        #     raise Exception('cant commit no changs')
          

        commit_hash=self.create_commit(tree_hash,message) 

        comref_path = Path(current) / Path("ref") / Path('branches') /Path(self.branch) / Path("commitRef")
        comref_path.parent.mkdir(parents=True, exist_ok=True) 


        with comref_path.open("a", encoding="utf-8") as f:
            f.write(f"{commit_hash}\t{message}\n")

        head_path = Path(current) / Path("ref") / Path('branches') /Path(self.branch) / Path("head")
        head_path.parent.mkdir(parents=True, exist_ok=True) 

        with head_path.open("w", encoding="utf-8") as f:
            f.write(f"{commit_hash}\t{message}\n")


        return commit_hash


        
class FetchTree:

    def __init__(self,basePath=None):
        self.basepath=basePath

    def read_tree(self,hash,curr_path):
        from pathlib import Path 
        current = Path.cwd() 
        pat = Path(current) 
        file=pat/Path('obj')/Path(hash)
        raw=file.read_bytes() 
        i,content=raw.split(b'\0',1)


        for line in content.decode().splitlines():
            
            mode,name,hash_=line.split()
            target = Path(curr_path) / Path(name)
            if mode == "40000": 
                target.mkdir(exist_ok=True)
                self.read_tree(hash_, target)
            else: 
                self.write_blob(hash_, target)


    def write_blob(self, blob_hash, target_path):
        from pathlib import Path 
        current = Path.cwd() 
        pat = Path(current) 
        file=pat/Path('obj')/Path(blob_hash)
        raw = Path(file).read_bytes()
        _, content = raw.split(b"\0", 1) 
        target_path = Path(target_path)

        target_path.parent.mkdir(parents=True, exist_ok=True)

        target_path.write_bytes(content)







        



        

        


    
    





    