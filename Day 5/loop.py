
# while loop 
# break

i = 1
while i < 10:
    print("1st program Result Is the ",i)
    if i == 6:
        break
    i +=1

print("           ")
#continue

i = 0
while i < 10 :
    i += 1
    if i == 3:
        continue
    print("2nd program Result Is the ",i)

#The else Statement

i = 1

while i < 10:
    print(i)
    i = i + 1
else:
    print("i is no longer less than 10")

# for loop

suppose = ["mehedi","rana","Rifat"]

for x in suppose:
    print(x)
    if x == "rana":
        break

datastore = ["mehedi","Johir","mamun","Hasan"]

for x in datastore:
    if x == "johir":
        continue
print(x)

# Range

for y in range (6):
    print(y)

print("Break")
#parameter

for h in range (2,9):
    print(h)

print("aktu niche nam beda")

#value increament 

for u in range (2,40,4): #4 increment
    print(u) 

# nested loop

nested_loop =  ["mehedi","rifat","tasty"]
nested_loop1 = ["apple","Banna","Ranna"]

for f in nested_loop:
    for z in nested_loop1:
        print(f,z)
