file = open("student.txt","r+")

#print(file.writeable())

text = file.read()
print(text)
file.close()