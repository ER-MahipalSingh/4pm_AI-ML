# data = (10, 23.50, "Python", 42, 10)

# data[1] = 50.50
# print(len(data))
# print(data.count(10))
# print(data.index(42))
# print(len(data))
# print(type(data))

# a = 10
# b = 100,
# c = (100)
# d = (100,)

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))


data = ["java", 10, "node", 30.2, 50]

# print(type(data))

# data[1] = 100
# data.append("python")
# data.insert(2, "numpy")
# data.extend(["panda", 10, "python", 10.25])
# data.remove(10)
# data.clear()
# val = data.pop(1)
# print(data)
# print(val)

# num = []

# for i in range(1,6):
#     val = int(input("Enter a num: "))
#     num.append(val)
    
# num = [i for i in range(1,6)]
num = [int(input("Enter num: ")) for i in range(1,6)]
print(num)