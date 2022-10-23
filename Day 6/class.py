#trying class 

class MyClass:
    x = 5
p1 = MyClass()
print(p1.x)

# init class

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
p1 = Person("Mehedi","36")

print(p1.name)
print(p1.age)

#str() function

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1)

# insert function that prints a greeting

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello my name is "+self.name)

p1 = Person("Mehedi Hasan", "22")
p1.myfunc()

# The self Parameter

class Person:
    def __init__(mysillyobject,name,age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfuncr(abc):
        print("Hello my name is "+abc.name)
p1 = Person("Hasan","22")
p1.myfuncr()

# age modify

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 13)

p1.age = 22

print(p1.age)

# The pass Statement
class Person:
  pass
