#!/usr/bin/env python3
from brain_games.scripts.brain_games import main
from random import randint
from prompt import string


def prime_number(number):
    if number <= 1:
        return 'no'
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return 'no'
    return 'yes'


def brain_prime():
    name = main()
    print(f'Hello, {name}!')
    count = 0
    flag = ''
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for i in range(3):
        random_number = randint(1, 100)
        flag = prime_number(random_number)
        print(f'Question: {random_number}')
        answer = string('You answer: ')
        if flag == answer:
            print('Correct!')
            count += 1
        else:
            lose_game(answer, flag, name)
            break
    if count == 3:
        print(f'Congratulations, {name}!')


def lose_game(answer, flag, name):
    print(f'{answer} is wrong answer ;(. Correct answer was {flag}.')
    print(f'''Let's try again, {name}!''')


if __name__ == '__main__':
    brain_prime()
