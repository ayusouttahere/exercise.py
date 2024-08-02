# 5. Write a Python program that accepts a word from the user and reverses it.

num = int(input("Enter a Number : ")) 
reverse = 0 
n = 1

temp = num ; 

while(temp > 0): 
   ld = temp%10 
   reverse = reverse * 10 + ld  
   temp = temp//10 
   n *= 10 
   
print("Reverse number is : ", reverse) 