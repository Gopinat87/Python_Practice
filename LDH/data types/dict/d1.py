a = {"name": "gopinath", "age":25,"Native":"Salem"}
print(id(a))   #GET ID
print("name" in a) # CHECK KEY
print(a)
a["name"] = "yuvi"
a["city"] = "Chennai"
print(a)
a.pop("city")
print(a)
del a["Native"]
print(a)
print(a.keys())
print(a.values())
print(len(a))
b = {"Company":"KIA", "Model": 2025,"Color":"Blue"}
a.update(b)
print(a)
print(a.clear(), b.clear())

