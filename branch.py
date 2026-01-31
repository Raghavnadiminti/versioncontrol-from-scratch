from pathlib import Path

class Branch:
    def __init__(self, name):
        self.name=name
        base = Path("ref/branches")
        base.mkdir(parents=True, exist_ok=True)
        self.path = base / name
        self.path.mkdir(exist_ok=True)
        self.head = self.path /"head" 
        self.commitRef=self.path /"commitRef"

        if not self.head.exists():
            self.head.write_text("", encoding="utf-8")
        if not self.commitRef.exists():
            self.commitRef.write_text("", encoding="utf-8") 

    def getLatestCommit(self):   
        return self.head.read_text(encoding="utf-8").strip()
    
    











