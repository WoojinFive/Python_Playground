#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
from random import randint

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Typa 'easy' or 'hard': ").lower()

should_continue = True
target = randint(1, 100)
attemps = 10 if difficulty == 'easy' else 5

def compare(num):
    if num > target:
        print("Too high.")
        return True
    elif num < target:
        print("Too low.")
        return True
    else:
        print(f"You got it! The answer was {target}.")
        return False


while attemps > 0 and should_continue:
    print(f"You have {attemps} attemps remaining to guess the number.")
    guess = int(input("Make a guess: "))
    should_continue = compare(guess)
    attemps -= 1
    if attemps == 0 and should_continue:
        print("You've run out of guesses, you lose")
    else:
        print("Guess again.")
