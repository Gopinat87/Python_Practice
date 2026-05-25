a,b,c = 10,20,15

# BRUTE FORCE

if a>b and a>c :
    print(a)
elif b>c :
    print(b)
else :
    print(c)

# OPTIMIZED

print(max(a,b,c))
