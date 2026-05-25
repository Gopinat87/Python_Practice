#CALCULATION USING FUNCTION RETURNS--------
import sys
def calci(a,b) :
    a = int(input("Enter a 1st number : "))
    b = int(input("Enter a 2nd number : "))
    cal = input("select a operaot (+,-,*,/) : ")
    if cal =="+" :
        return a+b 
    elif cal == "-" :
        return a-b
    elif cal == "*" :
        return a*b 
    else :
        return a/b
result = calci("a","b")
print(result)
print(sys.getsizeof(result), "Bytes")

import sys 
def calculator (c,d) :
    c = int(input("Enter c value"))
    d = int(input("enter d value"))
    e = input("Enter a operator (+,-,*,/) : ")

    if e == "+" :
        return c + d 
    elif e == "-" :
        return c - d
    elif e == "*" :
        return c * d
    else :
        return c / d
calcu = calculator("c","d")
print(calcu)
print(sys.getsizeof(calcu))