# 1 + 2 + 3 + 4 ........ + n

n = int(input("Enter the N Value :"))
sum = 0
for x in range(1,n+1,1):
    sum = sum + x
print("Series Number is the = ",sum)

# 2 + 4 + 6 + 8 ........ + n
n2 = int(input("Enter the N Value :"))
sum = 0
for x in range(2,n2+1,2):
    sum = sum + x
print("Series Number is the = ",sum)

# 1 + 3 + 5 + 7 ........ + n
n3 = int(input("Enter the N Value :"))
sum = 0
for x in range(1,n3+1,2):
    sum = sum + x
print("Series Number is the = ",sum)


# 1*2 + 2*2 + 3*2 + 4*2 ........ + n
n4 = int(input("Enter the N Value :"))
sum = 1
for x in range(1,n4+1,2):
    sum = sum + x*x
print("Series Number is the = ",sum)

# 1*1/2 + 2*1/2 + 3*1/2 + 4*1/2 ........ + n
n5 = int(input("Enter the N Value :"))
sum = 1
for x in range(1,n5+1,2):
    sum = sum + x*0.5
print("Series Number is the = ",sum)
