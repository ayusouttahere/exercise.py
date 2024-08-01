# 10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
# Sample value of n is 5
# Expected Result : 615

str= input("Enter a number : ")


num = int(str) 
num2 = int(str+ str) ; 
num3 = int(str+str+str) ; 


sum = int(num+num2+num3) 

print("Output is : ", sum) 