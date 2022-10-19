#python dictionary 

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#call item

call = {
    "brand": "Mehedi",
    "model": "asus",
    "year": "1933"
}
print(call["brand"])
print(len(call))

#data_type

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

print(thisdict)

print(type(thisdict))

#access dictionary
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)


#get method

umm =	{
  "brand": "Ford",
  "model": "uu",
  "year": 1964
}
x = umm.get("model")
print(x)

#chceking value

checking={
    "Brand": "Johir",
    "model": "hp",
    "year" : "2022"
}
if "model" in checking:
    print("yes,model value ace")

#value changing

values =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
values["year"] = 2018

print(values)


#Adding Items

addedvalue = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
addedvalue["color"] = "red"
print(addedvalue)

#update

updateee = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
updateee.update({"color": "red"})
print(updateee)

#Removing Items

removerr = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
removerr.pop("model")
print(removerr)

#pop item 

popitemee = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
popitemee.popitem()
print(popitemee)

#del 