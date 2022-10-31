#Python's map() is a built-in function that allows you to process and transform all the items in an iterable without using an explicit for loop, a technique commonly known as mapping. map() is useful when you need to apply a transformation function to each item in an iterable and transform them into a new iterable.

#all catagroy selected 
#filter specific category selected

def square(x):
    return x*x
num = [1,2,3,4,5,]

result = list(map(square,num))
print(result)