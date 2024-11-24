#!/usr/bin/env python3
from brain_games.scripts.brain_games import main
from prompt import integer
from random import randint
from math import gcd


def gcd_game():
    name = main()
    print(f'Hello, {name}!')
    print('Find the greatest common divisor of given numbers.')
    count = 0
    flag = ''
    for i in range(3):
        number_1 = randint(10, 20)
        number_2 = randint(1, 50)
        numbers_gcd = gcd(number_1, number_2)
        print(f'Question: {number_1} {number_2}')
        answer = integer('You answer: ')
        if answer == numbers_gcd:
            print('Correct')
            count += 1
        else:
            lose_game(answer, numbers_gcd, name)
            break
    if count == 3:
        print(f'Congratulations, {name}!')


def lose_game(answer, numbers_gcd, name):
    print(f'{answer} is wrong answer ;(. Correct answer was {numbers_gcd}.')
    print(f'''Let's try again, {name}!''')


if __name__ == '__main__':
    gcd_game()



