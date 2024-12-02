from prompt import string
from random import randint


def is_even(number):
    return number % 2 == 0


def get_correct_answer_and_task():
    number = randint(1, 100)
    correct_answer = 'yes' if is_even(number) == True else 'no'
    task = f'Question: {number}'
    return correct_answer, task

