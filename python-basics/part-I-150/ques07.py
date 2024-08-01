# 7. Write a Python program that accepts a filename from the user and prints the extension of the file.
# Sample filename : abc.java
# Output : java

f_name = input("Enter a file name with extensions : ") 

f_extnsns = f_name.split(".") 

print("Extension of the file will be : " + f_extnsns[-1])




