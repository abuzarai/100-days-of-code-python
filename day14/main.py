from art import logo, vs
from game_data import data
import random
import os

def get_random_account():
    return random.choice(data)

def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]

    return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
    return guess.lower() == 'a' and a_followers > b_followers or guess.lower() == 'b' and a_followers < b_followers

def game():
    print(logo)
    score = 0
    game_should_continue = True
    account_b = random.choice(data)

    while game_should_continue:
        account_a = account_b
        account_b = get_random_account()

        if account_a == account_b:
            account_b = random.choice(data)

        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}.")

        guess = input("Who has more followers. Type 'A' or 'B': ").lower()
        a_follower_count = account_a['follower_count']
        b_follower_count = account_b['follower_count']
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        os.system('cls' if os.name == 'nt' else 'clear') # Clear the screen
        print(logo)
        if is_correct:
            score += 1
            print(f"You are correct! Current score: {score}")
        else:
            print(f"Wrong answer!")
            game_should_continue = False

    print(f"Game over! Your final score is: {score}")
    play_again = input("Do you want to play again? Type 'y' or 'n': ")
    if play_again == 'y':
        os.system('cls' if os.name == 'nt' else 'clear')
        game()
    else:
        print("Thanks for playing! Have a nice day!")

game()
