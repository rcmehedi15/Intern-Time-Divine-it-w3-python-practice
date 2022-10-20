#Function 

def mehedi():
    print("Hello function")
mehedi()

#argument function

def mfunction(fname):
    print(fname+ " mehedi")
mfunction("Email")
mfunction("Johir")
mfunction("Mamun")


print("       ")
# number of function


def myfun(fname, lname):
  print(fname + " " + lname)

myfun("tamim", "hasan")

# Arbitrary Arguments, *args

def mufun(*kids):
    print("The youngest child is "+ kids[2])

# Keyword Arguments

def mmfun(child3,child2,child1):
    print("the youngest child is "+ child3)
    mmfun(child1 = "mehedi", child2 = "Rifat",child3 = "Johir")

#arbitray keyword **kwargs

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

#default prameter value

def myfunn(country = " Bangladesh"):
    print("I am from"+ country)

myfunn(" India")
myfunn(" Sweden")
myfunn(" Brazil")
myfunn()

double 

def myfunc(x):
    return 5 * x
print(myfunc(3))
print(myfunc(6))
print(myfunc(8))

#recursion

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
