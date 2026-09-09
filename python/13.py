data = [10,20,30,40,41,83,80,5,3]

# print(data)

# for i in data:
#     print(i, end=" ") 

# even = 0
# odd = 0

# for i in data:
#     if i % 2 == 0:
#         even = even + 1
#     else:
#         odd = odd + 1

# print("Even: ", even)
# print("Odd: ", odd)


data = [
    [1,2,3],
    [10,20,30],
    [111,222,333]
]

print(data[1][1])

for row in data:
    for col in row:
        print(col, end=" ")
    print()