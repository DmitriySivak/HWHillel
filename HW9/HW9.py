import random
from array import array

def game_loop(dice_roll):
    for i in range(10):
        input_str = input('To guess enter the number: ')
        if input_str == '':
            return False
        try:
            guess_number = int(input_str)
        except ValueError:
            print('Ooops, error! Not a number. Please, try again!')
            continue
        if guess_number == dice_roll:
            print('Congrats! You WIN!')
            return True
        elif guess_number > dice_roll:
            print('Try again! Enter a lower number!')
        elif guess_number < dice_roll:
            print('Try again! Enter a greater number!')
    return False

def get_continue(res1, res2):
    return 'yes' if res1 == res2 else input('Do you want to continue playing? (yes/no)')

res1 = 0
res2 = 0
guessed_numbers = array('i')
continue_condition = 'yes'
while continue_condition == 'yes':
    dice_roll = random.randint(10, 60)
    guessed_numbers.append(dice_roll)

    if game_loop(dice_roll):
        res1 += dice_roll
    else:
        res2 += dice_roll

    print('First player result = ' + str(res1))
    print('Second player result = ' + str(res2))
    continue_condition = get_continue(res1, res2)