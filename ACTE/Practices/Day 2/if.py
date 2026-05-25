a = int(input())
if a > 1 :
    for i in range(2,a):
        if a % i == 0 :
            print("is not a prime")
            break
        else:
           print("is a prime")
           break
else:
    print("is not a prime ")
