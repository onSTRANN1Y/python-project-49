from random import randint
from prompt import string


def get_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def get_correct_answer_and_task():
    random_number = randint(1, 100)
    correct_answer = 'yes' if get_prime(random_number) == True else 'no'
    task = f'Question: {random_number}'
    return correct_answer, task

