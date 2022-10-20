#if else

a = 22
b = 30
if b > a:
    print("b is greater than a")

# if else and elif

x = 33
y = 33

if y >  x:
    print("y is greater than x")
elif x == y:
    print("x and y equal")

# Short Hand If ... Else

p = 2
q = 22

print("P") if p > q else print(("Q"))

#both condition check

m = 200
n = 33
r = 500
if m > n and r > m:
  print("Both conditions are True")

#or conditions

M = 200
N = 33
R = 500
if M > N or M > R:
  print("At least one of the conditions is True")

  #nested if 

J = 41

if J > 10:
  print("Above ten,")
  if J > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")