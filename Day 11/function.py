# function 2 
# user defind function,libarary function ( alredy make)
#print(),Input()
#user defind function 

def add(x,y):
    sum = x + y
    print(sum)
add(10,20)


def addition(x,y,z):
    sum = x + y + z
    print(sum)
addition(0,20,20)

# returning function
def large(a,b):
    if a > b:
        return a
    else:
        return b
result = large(40,30)
print("Result = ",result)