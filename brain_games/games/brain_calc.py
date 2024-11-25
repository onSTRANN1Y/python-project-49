#!/usr/bin/env python3
from random import randint, choice
from prompt import integer


def task():
    print('What is the result of the expression?')


def calc():
    number1 = randint(1, 50)
    number2 = randint(1, 25)
    operathion = choice('+-*')
    match operathion:
        case '+':
            correct_answer = number1 + number2
        case '-':
            correct_answer = number1 - number2
        case '*':
            correct_answer = number1 * number2
    print(f'Question: {number1} {operathion} {number2}')
    answer = integer('You answer: ')
    return correct_answer, answer


if __name__ == '__main__':
    calc()
