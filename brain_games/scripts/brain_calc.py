#!/usr/bin/env python3
from brain_games.scripts.brain_games import main
from brain_games.cli import welcome_user
import prompt
import random


def calculator():
    name = main()
    print(f'Hello, {name}!')
    print('What is the result of the expression?')
    flag = 0
    for i in range(3):
        number1 = random.randint(1,50)
        number2 = random.randint(1,25)
        operathion = random.choice('+-*')
        print(f'Question:{number1} {operathion} {number2}')
        answer = prompt.integer('You answer: ')
        if operathion == '+':
            flag = number1 + number2
            if answer == flag:
                print('Correct!')
            else:
                lose_game(answer,flag,name)
                break
        if operathion == '-':
            flag = number1 - number2
            if answer == flag:
                print('Correct!')
            else:
                lose_game(answer,flag,name)
                break
        if operathion == '*':
            flag = number1 * number2
            if answer == flag:
                print('Correct!')
            else:
                lose_game(answer,flag,name)
                break
    if i == 2:
        print(f'Congratulations, {name}!')


def lose_game(answer,flag,name):
    print(f'{answer} is wrong answer ;(. Correct answer was {flag}.')
    print(f'''Let's try again, {name}!''')



if __name__ == '__main__':
    calculator()
