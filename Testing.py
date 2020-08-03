#File used to test code

class Example:
    def __init__(self):
        self.ok = "ok"
    
    def modifyOk(self):
        self.ok += " 2"
    
    def modifyToo(self):
        self.modifyOk()
ex = Example()
ex.modifyToo()
print(ex.ok)