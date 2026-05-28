class Example:
    def method(self,a,b=None):
        if b is None:
            print("Single argument : ",a)
        elif isinstance(a,int) and isinstance(b,int):
            print("Two integers : ",a,b)
        elif isinstance(a,str) and isinstance(b,str):
            print("Two string : ",a,b)
        else:
            print("Mixed types :",a,b)
        
obj=Example()
obj.method(1)
obj.method(1,2)
obj.method("Tamil","Rishwanth")
obj.method("Tamil",4)