try: 
    print(x)
except:
    print("An exception occurred")

# Many Exceptions
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

# Finally

try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

#the try block will raise an error when trying to write to a read only file

try:
    f = open("demofile.txt")
    try:
        f.write("Lorem Ipsum")
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()
except:
        print("Something went wrong when opening the file")