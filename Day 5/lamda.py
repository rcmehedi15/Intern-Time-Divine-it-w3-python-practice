#lamda

print((lambda a,b : a*a + 2 *a*b + b*b)(2,4))

# Return Lambda Function

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))