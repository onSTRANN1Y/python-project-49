#!/usr/bin/env python3
from prompt import integer
from random import randint
from math import gcd


def task():
    print('Find the greatest common divisor of given numbers.')


def game_gcd():
    number_1 = randint(10, 20)
    number_2 = randint(1, 50)
    correct_answer = gcd(number_1, number_2)
    print(f'Question: {number_1} {number_2}')
    answer = integer('You answer: ')
    return correct_answer, answer


if __name__ == '__main__':
    game_gcd()
