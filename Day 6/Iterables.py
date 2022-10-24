# Iterables
mytupple = ("apple","banana","orange")
myit = iter(mytupple)

print(next(myit))
print(next(myit))
print(next(myit))

print("--------------")
mstr = "banana"
myitt = iter(mstr)

print(next(myitt))
print(next(myitt))
print(next(myitt))
print(next(myitt))
print(next(myitt))


print("------------")
#Create an Iterator
class Mynumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x

myClasss = Mynumbers()
myiter = iter(myClasss)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))