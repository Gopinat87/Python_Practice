#multiplication in for loop 
"""num = int(input("Enter any number : "))
for a in range (1,11):
    print(num,"*",a,"=",num*a) """


# multiplication in while loop
"""num = int(input("Enter any number : "))
a = 1
while a < 11 :
    print(num,"*",a,"=", num*a)
    a += 1
    """
#prime number check in for loop
a = int(input("enter any number : "))

is_prime = True

if a <= 1 :
    is_prime = False

else :
    for i in range(2,a):
        if a % i==0 :
            is_prime = False
            break

if  is_prime :
    print(a, " is a prime number")

else :
    print(a , "is not a prime")
