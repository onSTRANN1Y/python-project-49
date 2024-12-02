from random import randint, choice
from prompt import integer


def get_correct_answer_and_task():
    correct_answer, number1, operathion, number2 = calculating()
    task = f'Question: {number1} {operathion} {number2}'
    return correct_answer, task



def calculating():
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
    return correct_answer, number1, operathion, number2
