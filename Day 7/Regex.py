import re
text = "The rain in Spain"
x = re.search("The.*Spain$",text)

if x:
    print("Yes! We Have a match!")
else:
    print("No Match")

# The findall() Function
import re

txt = "The rain in Spain"
e = re.findall("ai", txt)
print(e)

# The search() Function
import re
textt = "=The Rain in Spain"
x = re.search("\s",textt)

print("The first white-space character is located in position: ",x.start())

# The split() Function
import re 
texttt = "The rain is beautiful"
xx = re.split("\s", texttt)
print(xx)

# The sub() Function

import re
txtt = "The rain in spain"
s = re.sub("\s","9",txtt)
print(s)

# Match Object

import re

texxt = "The rain in spain"
aa = re.search("ai",texxt)

print(aa)