# scope 

def myfunc():
    x = 300
    print(x)
myfunc()

# Global Scope
x = 400
def myfuncr():
    print(x)
myfuncr()
print(x)

print("------------")
# Naming Variables
m = 200
def myfuncrr():
    m = 300
    print(m)
myfuncrr()
print(m)

print("----------")
# global keyword

def myfunctt():
    global T
    T = 400
myfunctt()
print(T)