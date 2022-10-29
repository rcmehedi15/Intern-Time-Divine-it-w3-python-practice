"""
*
** 
*** 
****
*****
******
********
"""
n = int(input("Enter The Value of : "))
for i in range(n+1):
    print("*"*i)

"""
*
*** 
*****
*******
*********
***********
*************
"""
n = int(input("Enter The Value of : "))
for i in range(n+1):
    print((2*i-1)*"*")

"""
    *
    **
   ***
  ****
 *****
******
"""
n = int(input("Enter The Value of : "))
for i in range(1,n+1):
	print((n-i)*" ",end="")
	print(i*"*")