# 4. Even or Odd Game
# Concept:
# Concepts used:
# % (modulus)
# random
# if

import random
num=random.randint(1,100)

 
while True:
       guess=input(f"{num} , Guess the number is odd or even: ").lower()
      
       if guess== "even" and num%2==0:
        print(f"correct the number is even")
        break
       
       elif guess =="odd" and num%2==1:
        print(f"correct the number is odd")

       else:
        print("You guess the wrong ")