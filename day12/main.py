from random import randint
from art import logo
import os

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"Correct guess! The answer is indeed {answer}.")
        return turns 

def set_difficulty():
    while True:
        level = input("Choose a difficulty.\n1. Easy\n2. Hard\nType 1 or 2: ")
        if level in ['1', '2']:
            return EASY_LEVEL_TURNS if level == '1' else HARD_LEVEL_TURNS
        else:
            print("Invalid input. Please try again.")

def play():
    while True:
        print(logo)
        print("Welcome to the Number Guessing Game!")
        print("Guess a number between 1 and 100.")
        answer = randint(1, 100)

        turns = set_difficulty()
        guess = None
        while turns > 0:
            print(f"You have {turns} attempts remaining to guess the number.")
            guess = int(input("Make a guess: "))
            turns = check_answer(guess, answer, turns)

            if guess == answer:
                print("You've won!")
                break # Exit the loop if the guess is correct

            if turns == 0:
                print("You've run out of guesses, you lose.")
                break

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != "y":
            break
        os.system('cls') 

play()
