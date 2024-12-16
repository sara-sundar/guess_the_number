#Number Guessing Game Objectives:
from art import logo
import random
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

print(logo)
print("Welcome to the Number Guessing Game!")
level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
guessed_number = random.randint(1,100)
print(guessed_number)
def guess_number(level):
  if level == "easy": attempts = 10
  elif level == "hard": attempts = 5
  print(f"You have {attempts} attempts remaining to guess the number.")
  Flag = True
  while Flag and attempts>0 :
    guess = int(input("Make a guess: "))
    if guess == guessed_number:
      print(f"You got it! The answer was {guessed_number}")
      Flag = False
    else :
      if guess > guessed_number :
        print("Too high.")
      elif guess < guessed_number :
        print("Too low.")
      attempts -= 1
      print(f"You have {attempts} attempts remaining to guess the number.")
  if attempts == 0 :
    print("You've run out of guesses, you lose.")
guess_number(level)

#GIT COMMITTED PROJECT