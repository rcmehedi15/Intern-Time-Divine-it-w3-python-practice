import datetime
m = datetime.datetime.now()
print(m)

# year and name weekday

print("Year and name weekday")
import datetime
y = datetime.datetime.now()
print(y.year)
print(y.strftime("%A"))

# Creating Date Objects
import datetime
mm = datetime.datetime(2022,10,25)
print(mm)


print('---------')
# The strftime() Method
import datetime

dt = datetime.datetime(2022,10,25)
print(dt.strftime("%B"))