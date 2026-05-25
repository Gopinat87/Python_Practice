n = int(input())
add = 0
#BRUTE FORCE 

for i in range(1,n+1):
    add += i
print(add)

#optimized

print(n * (n+1) // 2)


