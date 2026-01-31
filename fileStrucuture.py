class File:
    def __init__(self,name):
        self.isFile=True
        self.isFolder=False
        self.name=name   
        self.hash=None 

    def assignHash(self,hash):
        self.hash=hash

    

class Folder:
    def __init__(self,name):
        self.isFile=False 
        self.isFolder=True  
        self.children=set()
        self.parent=None 
        self.name=name   
        self.hash=None 

    def assignHash(self,hash):
        self.hash=hash
    
    def assignParent(self,Folder):
        self.parent=Folder 
    
    def addChildren(self,File):
        self.children.add(File)


