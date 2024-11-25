#!/usr/bin/env python3
from prompt import string
from random import randint


def task():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def brain_even():
    number = randint(1, 100)
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    print(f'Question: {number}')
    answer = string('Your answer: ')
    return correct_answer, answer


if __name__ == '__main__':
    brain_even()
