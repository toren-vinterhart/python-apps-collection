import random

MIN_NUM = 1
MAX_NUM = 10

max_guess_count = 3

def generate_random_num():
    return random.randint(MIN_NUM, MAX_NUM)

def get_user_input():
    while True:
        try:
            user_input = int(input(f'Please enter a number between {MIN_NUM} and {MAX_NUM}: '))
            if MIN_NUM <= user_input <= MAX_NUM:
                return user_input 
            print('Not in range!!!')
        except ValueError:
            print('Not Valid!!!')

def check_guessed_number(user_input, random_num):
    return user_input == random_num

def main(max_guess_count=max_guess_count):
    # global max_guess_count
    random_num = generate_random_num()

    while max_guess_count > 0:
        user_input = get_user_input()

        if check_guessed_number(user_input, random_num):
            print('Your guess is correct!')
            print('YOU WON!')
            return
        
        max_guess_count -= 1
        if max_guess_count == 0:
            print('Your guess is incorrect')
        else:
            print(f'Your guess is incorrect. You can guess {max_guess_count} more times')

    print("YOU LOSE!")
    
if __name__ == '__main__':
    main()
