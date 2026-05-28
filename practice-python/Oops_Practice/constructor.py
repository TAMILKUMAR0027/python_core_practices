class Myclass:
    def __init__(self,age):
        self.age=age
    def __init__(self,name):
        self.name=name
    
    def dis(self):
        print(f"Hello ,{self.name}")
        
obj=Myclass('Tamil')
obj.dis()