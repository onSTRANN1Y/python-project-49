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


def task():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def brain_prime():
    random_number = randint(1, 100)
    correct_answer = prime_number(random_number)
    print(f'Question: {random_number}')
    answer = string('You answer: ')
    return correct_answer, answer


if __name__ == '__main__':
    brain_prime()
