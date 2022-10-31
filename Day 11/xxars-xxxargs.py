#xxargs
def student(*details):
    print(details)

student(101,"Mehedi")
student(101,"Mehedi",3.77)

# xxxargs
def student(**details):
    print(details)

student(id=101,name="Mehedi")