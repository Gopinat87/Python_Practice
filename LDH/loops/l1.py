st = ["1st y" , "2nd y", "3rd y"]
sem = {"1st s", "2nd s"}
for year in st:
    for semes in sem:
        print(f"{year},{semes} padi")


store = [1,2,3,4]
for i in store:
    if i == 3 :
        continue
    print(f"Person {i} ready")


store = 1
while store <= 3 :
    print(f"person {store} ready ")
    store = store + 1

n = 0
for number in (1,2,3) :
    n += number
print(n)

