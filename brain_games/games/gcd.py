from math import gcd
from random import randint


def get_correct_answer_and_task():
    number_1, number_2 = randint(10, 20), randint(1, 50)
    correct_answer = gcd(number_1, number_2)
    task = f'Question: {number_1} {number_2}'
    return correct_answer, task
