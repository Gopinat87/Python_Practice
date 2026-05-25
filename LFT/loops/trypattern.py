"""
a = int(input("enter 1st number : "))
for i in range (1,a+1) :
    print("*" * i)

print("1st Completed")

b = int(input("Enter 2nd number : "))
for i in range(1,b+1) :
    print("*" * i + " " * (b-i) + "#")    

print("2nd Completed")

c = int(input("Enter 3rd number : "))
for i in range(c,0,-1) :
    print("*" * i + " " * (c-i) + "#")
print("3rd Completed") """

d = int(input("Enter 4th Number : "))
for i in range(1,d+1):
    print(" " * (d-i) + "*" * (2*i -1)) 