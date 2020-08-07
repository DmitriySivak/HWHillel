start_game = input('Do you want to start? Write Y or N: ')
import score
from restart import restart


def total():
    res = 0
    while start_game == 'Y':
        res = res + score.score()
        print(f'You have', res, 'points')
        if restart() == 'yes':
            continue
        break
    return res
print('hello')

if __name__ == '__main__':
    print(f'Your total score', total())