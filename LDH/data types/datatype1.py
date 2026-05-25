#----------How to see the size of variable --------
a = 121212
b =1234567890
import sys  #--- (import sys ) is a module or libraries 
print(sys.getsizeof(a))
print(sys.getsizeof(b))

#-------how to see data type-----
a = 10
b = "Gopi"
c = 20
print(type(a), type(b),type(c))

#------ how to see the address location -----
a = 10
b = 10
c = 25
d = 12
print(id(a),id(b),id(c),id(d))

#--------------DATA TYPES--------------------------------------------------------------------------------

#-------String------- are immutable
try:
    a = "Hello!"   
    print(a[0])
except TypeError :
    print("hi")

b = "helloworld"
print(id(b)) # --- see the location id---
c = "J" + b[1:]
print(c)
print(id(c)) # now see the location id so strings are immutable to change anything 
             #to create new location not will replace or chnage already stored string data
 
#-------list data type-------------------------

 #------array and lsit-----
a = [1,"gopi",87,"salem", 2] #---- array is mutable can add list in array 
a[1]= "Hi"
print(a)
print(type(a))
