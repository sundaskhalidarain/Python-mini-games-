# Guess the Number (Beginner Project)

import random
secret = random.randint(1, 10)  # a method used to import random  number

attempts=0

while True: 
       guess=int(input("Guess the number 1-10: "))
       attempts= attempts+1

       if guess==secret:
        print("You Win!")
        print(f"You Win in Total Attempt: {attempts}")
        break
       
       elif guess > secret:
        print("Too HIGH!")
        
       else: 
        print("Too Low!")