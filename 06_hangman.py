# 10. Hangman (Mini Version)

# Concept:

# Choose a simple 4–5 letter word.
# User guesses one letter at a time.
# Show the remaining blanks.

# Example:

# Word: _ _ _ _
# Guess: a

# Word: _ a _ _

word="animal"
guessed=[]
attempts=10
while attempts > 0:
 guess=input("Guess the letter of a word: ").lower()

 if guess in word and guess not in guessed:
  guessed.append(guess)
  print("correct")
 else:
  attempts=attempts-1
  print("wrong guessed")
  print(f"Attempts lesft {attempts}")

 for letter in word:

     if letter in guessed:
      print(letter, end=" ")

     else:
      print("_", end=" ")

 print()

 if len(guessed) == len(set(word)):
    print("🎉 You guessed the word!") 
    break

    if attempts==0:
     print("❌ Game Over!")

 print("The word was:", word)