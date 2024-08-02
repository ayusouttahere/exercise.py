# 6. Write a Python program to count the number of even and odd numbers in a series of numbers
# Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
# Expected Output :
# Number of even numbers : 5
# Number of odd numbers : 4

oddCount = 0
evenCount = 0 

num = input("Enter a series of numbers separated by commas : ")

num_list = num.split(",") 

for val in num_list : 
   val = int(val) 

   if val % 2 == 0 : 
      evenCount+=1 
   else : 
      oddCount+=1 

print("Odd count is :" , oddCount, " and even count is : ", evenCount)
