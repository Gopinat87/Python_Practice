#types of arguments---------

#1. Default 
def name() :
    print("my name is Gopinath ")
name()


#-----------POSITIONAL ARGUMENTS-----
def num(a,b) :
    result = a+b
    return result
numbers = num(10,20)
print(numbers)

def names(c,d):
    return c+d
re = names(10,30)
print(re) 

#--------default ARUGUMENTS --------
def alpha(a,b=20) :
    return a+b
apha = alpha(5)
print (apha)

#--------*args Arguments----------
def numm(*args) :
    result =(args)
    return result
value = numm(100,20)
print(value)

#--------------LEMDA ARGUMENTS--------
abc = lambda a,b : a+b
op = abc(12,14)
print(op)

