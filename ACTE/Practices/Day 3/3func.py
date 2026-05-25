#--------------ADDER---------------------------------------
def add(a,b) :
    return a+b 
result = add(10,20) 
print("sum of a+b is " , result)
#-----------SUB------------------
def minus(a,b) :
    return a-b
result = minus(30,20)
print("Sub of a,b is" , result )

#-------------MULTI---------
def mutli(a,b) :
    return a*b
result = mutli(20,10)
print("Multi of a,b is" , result)

#-------------DIVIDE----------K
def divide(a,b) :
    return a/b 
result = divide(40,4)
print("Divide of a,b is " , result)

import sys
arr = [1,23,3]
print(type(arr))
print(sys.getsizeof(arr))