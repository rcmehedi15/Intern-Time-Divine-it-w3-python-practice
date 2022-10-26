price = 49
txt = "The price is {} dollars"
print(txt.format(price))

print(12 * 64) 


quantity = 4
itemno = 343
pricee = 32
myorder = 'I Want {} pieces of item number {} for {:.6f} dollars.'

print(myorder.format(quantity,itemno,pricee))

# formating Index Numbers

age = 38
name = "Mehedi"

txxt ="His name is {1}. {1} is {0} years old."
print(txxt.format(age,name))

# Named Indexes

myyorder = "I Have a{carname}, it is a {model} ."
print(myyorder.format(carname = " Ford",model ="Mustang"))