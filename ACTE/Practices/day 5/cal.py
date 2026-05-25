class calculator():
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        return a/b
Calci = calculator()
print(Calci.add(10,4))
print(Calci.sub(10,3))
print(Calci.mul(5,3))
print(Calci.div(10,5))

Add = Calci.add(10,21)
print(Add)

