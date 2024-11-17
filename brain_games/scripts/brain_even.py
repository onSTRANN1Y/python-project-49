#!/usr/bin/env python3
from brain_games.scripts.brain_games import main
from brain_games.cli import welcome_user
import prompt
import random




def parity_check():
    name = main()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    x = 0
    flag = ''
    for i in range(3):
        number = random.randint(1,100)
        if number % 2 == 0:
            flag = 'yes'
        else:
            flag = 'no'
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        if answer == flag:
            print('Correct!')
        else:
            print(f'{answer} is wrong answer ;(. Correct answer was {flag}.')
            print(f'''Let's try again, {name}!''')
            break
    if i == 2:
        print(f'Congratulations, {name}!')


def brain_games():
    parity_check()


if __name__ == '__main__':
    brain_games()


