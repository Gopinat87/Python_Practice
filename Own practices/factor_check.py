n = int(input("Enter a number: "))
# print(f"factor of {n} is ")
count = 0
for i in range(1,n+1) :
    if n % i == 0:
        count += 1
        print(i)
print(f"Total factor counts are {count}")

num = int(input("Enter number: "))
factors = []

for i in range(1, num + 1):
    if num % i == 0:
        factors.append(i)

print("Factors:", factors)



