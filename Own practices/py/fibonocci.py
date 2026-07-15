#print fibonocci series using loop

n = int(input("Enter a number of terms you want: "))

a = 0
b= 1

for i in range(n):
    print(a, end=" ")

    c = a+b
    a = b
    b = c
