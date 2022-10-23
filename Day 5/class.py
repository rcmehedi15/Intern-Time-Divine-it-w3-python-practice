# class MyClass:
#   x = 5

# print(MyClass)


# self class

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
p1 = Person("Mehedi",22)
print(p1.name)
print(p1.age)

#The __str__() Function

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1)
