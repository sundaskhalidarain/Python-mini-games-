# 6. Password Guess Game

# Concept:
# Store a secret password.
# User gets 3 attempts.
# Print "Access Granted" or "Access Denied."

password=2789
attempts=0

while True < 3:
 guess=int(input("Guess the password: "))

 if guess==password:
  attempts=attempts+1
  print("Access Granted")
  break
 
 else:
  attempts=attempts+1
  print("wrong password")

 if attempts==3:
  print("Access Denied")
   