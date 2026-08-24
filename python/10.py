# data = {10, 50, 3.25, "python", 10}
# user = {}
# tech = set()

# print(type(data))
# print(type(user))
# print(type(tech))

# data.add(100)
# data.update([200,"java", 3.25])
# data.pop()
# data.remove(50)
# data.clear()
# print(data)

# a = {1,5,7,10}
# b = {10,15,6,8}

# print(a | b)
# print(a.union(b))
# print(a & b)


data = {"tech":"python", "version":3.15}

# print(type(data))

# data["tech"] = "java"
# data["year"] = 1991
# print(data.get("tech", "Tech not found"))
# data.update({"tech1":"python", "year":1996})
# data.clear()
# data.pop("version")
# print(data)

# for key in data.keys():
#     print(key)
    
# for value in data.values():
#     print(value)
    
for key, value in data.items():
    print(f"{key} = {value}")