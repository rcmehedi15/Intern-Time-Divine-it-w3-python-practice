# curly bracket
num = {1,2,3,4,5}
num2 = set([4,5,6,7])

print(num)
num2.add(8)
num2.remove(6)
print(num2)
print(5 in num2)
print(5 not in num2)

#union

num11 = {1,2,3,4,5}
num22 = set([4,5,6,7])

print(num11 | num22)
print(num11 & num22)
print(num11 - num22)