# simple factorial

n = int(input("Enter Value : "))
f = 1

for i in range(1,n+1):
    f = f * i
print(f)

# function factorial

def fact(n):
    initial = 1
    for i in range(1,n+1):
        initial = initial * i
    return initial
result = fact(5)
print(result)

# very easy way
import math
n = 5
r = math.factorial(n)
print(r)