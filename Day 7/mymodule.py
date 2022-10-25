def greeting(name):
  print("Hello, " + name)
  
import mymodule
mymodule.greeting("Mehedi")

# variable in module

person1 = {
  "name": "Rifat",
  "age": 36,
  "country": "Norway"
}
import mymodule

a = mymodule.person1["age"]
print(a)

print("----------")
# Re-naming a Module

import mymodule as mx
a = mx.person1['age']
print(a)

# Built-in Modules

import platform
B = platform.system()
print(B)

# using the dir() function

import platform

u = dir(platform)
print(u)