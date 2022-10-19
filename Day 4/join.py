#union

set1 = {"mehedi","Rana","Tana"}
set2 = {"Mamun","Johir","Hasan"}
set3 = set1.union(set2)

print(set3)

#update

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

#intersection update

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

#symetric method
a = {"apple", "banana", "cherry"}
b = {"google", "microsoft", "apple"}

z = a.symmetric_difference(y)

print(z)