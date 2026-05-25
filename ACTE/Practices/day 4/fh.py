h = open("file.txt" , "w")
h.write("Hi I'm Gopi\n Completed BE(computer Science) \n Passed out in 2024 \n looking for a job")
h.close()

h =open("file.txt" , "r")
s = h.read()
print(s)
h.close()

with open("file.txt" , "a") as h :
    h.write("\n Thank You")

h = open("file.txt" , "r")
g = h.read()
print(g)
h.close() 

with open("file.txt","a") as h:
    h.write("\nA\nB")

with open("file.txt","r") as h:
    d=h.read()
    print(d)

    