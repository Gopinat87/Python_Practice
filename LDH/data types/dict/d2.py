#------------EASY----------
details = {"name":"Gopinath","age":24,"city":"Salem"}

print(details["age"])

details["email"] = "gopinath2002@gmail.com"

details["city"] = "Chennai"

details.pop("age")

print(details)

#---------------MEDIUM
#q8
print(len(details))
#Q9
vales = {"a" : 1 , "b" : 2}
values = {"c" : 3 , "d" : 4}

vales.update(values)
print(vales)
#Q10
print(vales.keys())
print(vales.values())


