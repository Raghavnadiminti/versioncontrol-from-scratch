import sys

class CreateFile:
    def __init__(self,pattern):
        self.pattern=pattern 
    def create(self,filename):
        import re
        pattern =self.pattern
        if not re.match(pattern, filename):
            raise KeyError("need correct filename")

        open(filename, "w").close()
        print("File created:", filename)


class Readfile:
    def __init__(self,pattern):
        self.pattern=pattern 

    def read(self,filename):
        import re
        pattern =self.pattern
        if not re.match(pattern, filename):
            raise KeyError("need correct filename")
        with open(filename, "r") as f:
            for line in f:
                print(line, end="") 

class Writefile:

    def __init__(self,pattern):
        self.pattern=pattern  

    def write(self,filename,data):
        import re
        pattern =self.pattern
        if not re.match(pattern, filename):
            raise KeyError("need correct filename")
        
        with open("out.txt", "w") as f:
            f.write(data)


class DeletFile:
    def __init__(self,pattern):
        self.pattern=pattern 

    def delete(self,filename):
        import re
        pattern =self.pattern
        if not re.match(pattern, filename):
            raise KeyError("need correct filename")
        from pathlib import Path

        file = Path(filename)

        if file.exists():
            file.unlink()
            print("Deleted:", file)
        else:
            print("File not found:", file)








class CreateFolder:
    def __init__(self, folder_name):
        from pathlib import Path
        self.folder = Path(folder_name)

   
    def create(self):
        
        self.folder.mkdir(exist_ok=True)
        return f"Folder created: {self.folder.resolve()}"

   
    def create_with_parents(self):
        
        self.folder.mkdir(parents=True, exist_ok=True)
        return f"Folder (with parents) created: {self.folder.resolve()}"







