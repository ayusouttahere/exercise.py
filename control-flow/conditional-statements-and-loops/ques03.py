# 3. Write a Python program to guess a number between 1 and 9.
# Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.

num = 0

while(True): 
   if(num <=  9 and num >=1): 
      guess = 0 
      while(True):
         if(guess == num): 
            print("Your guess was correct !") 
            break ; 
         else:
            guess = int(input("Guess the number() : "))
            print(guess)
      break ; 
   else: 
      num = int(input("Enter a Number bw 1-9 :"))

   

   