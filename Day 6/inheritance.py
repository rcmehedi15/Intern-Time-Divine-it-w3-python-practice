# parrent class, super class , base class
# child class, sub class , Derived class


class phone:
    def call(self):
        print("You Can Call")
    def message(self):
        print("you Can message")

class samsung(phone):
    def call(self):
        print("You Can Call")
    def message(self):
        print("you Can message")
    def photo(self):
        print("you can take photo")

m = samsung()
m.call()
m.message()
m.photo()

print(issubclass(samsung, phone))


#inherit

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)
x.welcome()
