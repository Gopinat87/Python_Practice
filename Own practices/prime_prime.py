n = int(input("Enter a number: "))

if n <= 1 :
    print("Its not prime Number")

else:
    for i in range(2,n) :
        if n % i == 0 :
            print("Its not prime Number")
            break
    else :
        print("its a prime number")