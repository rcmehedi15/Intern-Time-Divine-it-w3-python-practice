thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#item by item check 
tupple_item = ['me','ne','to']

print(tupple_item[1])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:2])


#check item
checkitem = ("apple", "banana", "cherry")
if "apple" in checkitem:
  print("Yes, 'apple' is in the fruits tuple")


#count

tuplevai = (1, 3, 3, 3, 7, 5, 4, 3, 8, 5)

tuple_monu = tuplevai.count(3)

print(tuple_monu)