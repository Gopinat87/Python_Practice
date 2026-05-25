#-----------------BREAK-----------
print("Enter a numbers: " , "Enter z to exit")
l = []
while True:
    inp = input("Enter: ")
    l.append(inp)
    if inp == "z":
        break

print(l)
#---------CONTINUE--------
s = ",A,B,C,D,E,F"
s1 =""
for i in s:
    if i==",":
        continue
    s1 += i
print(s1)


#------------PATTERN PRINT----------

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()

for a in range (1,6) :
    print("*" * a )
    

    