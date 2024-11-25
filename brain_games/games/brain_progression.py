#!/usr/bin/env python3
from random import randint
from prompt import integer


def random_progression():
    progression = []
    start_number = randint(1, 50)
    step = randint(1, 5)
    for i in range(start_number, start_number + 10 * step, step):
        progression.append(i)
    return progression


def task():
    print('What number is missing in the progression?')


def brain_progression():
    progression = random_progression()
    random_index = randint(0, 9)
    correct_answer = progression[random_index]
    progression[random_index] = '..'
    print('Question:', ' '.join(map(str, progression)))
    answer = integer('Your answer: ')
    return correct_answer, answer

if __name__ == '__main__':
    brain_progression()
