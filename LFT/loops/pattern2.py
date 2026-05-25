n = int(input("Enter an number :"))
for a in range (1,6) :
    print("*" * a )
    
a = int(input("enter any number : "))
for i in range(a,0,-1):
    print('*' * i + ' ' * (a - i) + '#')

r= int(input("Enter any number : "))
for a in range (r,0,-1) :
    print("*" * a +" "*(r-a)+"#")

a = 6
for i in range(1,a+1) :
    print("*" * i + " "*(a-i) +"#")

print("NEXT")
for i in range(a,0,-1) :
    print("*" * i + " "*(a-i))


    
for i in range(1,a+1) :
    print(" "*(a-i) + "*" *(2*i-1))

