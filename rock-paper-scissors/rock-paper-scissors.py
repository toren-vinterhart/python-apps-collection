import random

USER_CHOICES = ('rock', 'paper', 'scissors')

def get_user_input():
    choice = input("Pick your choice ['rock', 'paper', 'scissors']: ")
    while choice not in USER_CHOICES: 
        choice = input("Pick your choice ['rock', 'paper', 'scissors']: ")
    return choice

def get_pc_input():
    pc_choice = random.choice(USER_CHOICES)
    print(f'pc choice was: {pc_choice}')
    return pc_choice

def determine_winner(user_input, pc_input):
    if user_input == pc_input:
        print("DRAW!")
    elif (user_input == 'rock' and pc_input == 'scissors') or \
         (user_input == 'scissors' and pc_input == 'paper') or \
         (user_input == 'paper' and pc_input == 'rock'):
        print("user won!")
    else:
        print("pc won!")

def main():
    user_input = get_user_input()
    pc_input = get_pc_input()
    determine_winner(user_input, pc_input)

repeat = 'y'

while repeat == 'y':
    main()
    repeat = input("Do you want to continue? (y/n): ")

print("End of the program")
