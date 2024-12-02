from random import randint
from prompt import integer


def random_progression():
    progression = []
    start_number = randint(1, 50)
    step = randint(1, 5)
    for i in range(start_number, start_number + 10 * step, step):
        progression.append(i)
    return progression


def get_correct_answer_and_task():
    progression = random_progression()
    random_index = randint(0, 9)
    HIDEN_NUMBER = '..'
    correct_answer, progression[random_index] = progression[random_index], HIDEN_NUMBER
    task = f'''Question: {' '.join(map(str, progression))}'''
    return correct_answer, task
