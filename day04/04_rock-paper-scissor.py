import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print('----------- Rock Paper Scissor Game ----------')

print('What do you choose?')
user_input = input('Type 0 for Rock\n1 for Paper\n2 for Scissor\n----->>> ')
computer_choice = random.randint(0,2)

if not user_input.isdigit():
    print('Your choice is invlid. Please choose a digit: 0, 1 or 2.')
else:
    user_input = int(user_input)
    if user_input < 0 and user_input > 2:
        print('Please enter a number between 0 and 2')
    else:
        if user_input == 0:
            print(f'You chose: Rock {rock}')
        elif user_input == 1:
            print(f'You chose: Paper {paper}')
        else:     
            print(f'You chose: Scissors {scissors}')
    
if computer_choice == 0:
    print(f'Computer chose: Rock {rock}')
    if user_input == 2:
        print('You lose. Rock wins agaist Scissors.')
    elif user_input == 0:
        print('It\'s a draw.')
    else:
        print('You win!')

elif computer_choice == 1:
    print(f"Computer chose: Paper {paper}")
    if user_input == 1:
        print('It\'s a draw!')
    elif user_input == 0:
        print('You loose. Paper wins against rock.')
    else:
        print("You win!")

elif computer_choice == 2:
    print(f"Computer chose: Scissors {scissors}")
    if user_input == 2:
        print('It\'s a draw!')
    elif user_input == 1:
        print('You lose. Scissors win against paper.')
    else:
        print('You win!')
