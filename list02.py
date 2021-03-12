list = [1,2,3,4,5,6,7,8]

list.append(9)

print(list.count(1))
print(dir(list))

temp = list[4:] + [100] + list[:4]
print(temp)
print(list)
print(list[0])
print(list[1])
