import uuid
from functools import reduce

# id = uuid.uuid4()
# id = str(uuid.uuid4())
# print(id)
# print(type(id))

num = [50,10,5,13,60]
# print(num)
# num.sort()
# res = sorted(num)
# res = ["Ali", "Monica", "Raj", "Hello"]
# res.sort()

# print(res)

# res = map(lambda x: x * 5, num)
# def multi(x):
#     return x * x
# res = map(multi, num)

# res = filter(lambda x: x > 20, num)
# print(list(res))

# res = reduce(lambda a,b: a + b, num)
res = reduce(lambda a,b: a if a > b else b, num)

print(res)