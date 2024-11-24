#!/usr/bin/env python3
from brain_games.scripts.brain_games import main
from prompt import string
from random import randint


def parity_check():
    name = main()
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    flag = ''
    for i in range(3):
        number = randint(1, 100)
        if number % 2 == 0:
            flag = 'yes'
        else:
            flag = 'no'
        print(f'Question: {number}')
        answer = string('Your answer: ')
        if answer == flag:
            print('Correct!')
            count += 1
        else:
            print(f'{answer} is wrong answer ;(. Correct answer was {flag}.')
            print(f'''Let's try again, {name}!''')
            break
    if count == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    parity_check()
