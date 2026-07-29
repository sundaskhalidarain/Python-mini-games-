# Dice Rolling Game
# Concepts used:

# random
# while
# input()

import random

while True:
         input("Press Eneter to roll the dice! ")

         num=random.randint(1,6)

         print(f"You rolled {num}")

         again=input("Do You want to play again? ").lower()

         if again == "no":
            print("Thanks for playing!")
            break