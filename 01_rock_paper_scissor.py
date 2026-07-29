import random

choices=["rock","paper","scissor"]

# Take input from the user
user=input("Enter the choice:").lower()

# Check if the input is valid
if  user not in choices:
     print("Invalid choice! Please enter rock, paper, or scissor.")

# Compare choices and decide the winner

else: 
 # Generate the computer's choice
 cpu=random.choice(choices)
 print("cpu choice",cpu)

 if user==cpu:
    print("its a draw!")

 elif user=="rock" and cpu=="scissor":
    print(" you win!")

 elif user=="paper" and cpu=="rock":
      print(" you win!")

 elif user=="scissor" and cpu=="paper":
      print(" you win!")

 else:
     print("Computer wins!")
   
