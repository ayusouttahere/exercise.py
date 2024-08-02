# 4. Write a Python program to construct the following pattern, using a nested for loop.

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

for i in range (1,6,1):
   for j in range (1,i,1):
      print("*",end="")
   print("\n",end="")

for i in range (6,1,-1):
   for j in range (1,i,1):
      print("*",end="")
   print("\n",end="")