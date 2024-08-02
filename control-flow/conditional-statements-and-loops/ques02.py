# 2. Write a Python program to convert temperatures to and from Celsius and Fahrenheit.
# [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
# Expected Output :
# 60°C is 140 in Fahrenheit
# 45°F is 7 in Celsius 

format = input("Enter 'c' for Celcius and 'f' for Fahrenheit : ") 
temp = int(input("Enter temperature : "))

if(format == 'c'):
   conv = (temp * (9/5)) + 32   
elif(format == 'f'):
   conv = (temp*5)/9 - 32 

print("converted temperature is : ", conv) 

