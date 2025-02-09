import random
from brain_games.engine import run_game
from brain_games.consts import CALC_INSTRUCTION

def get_correct_answer_and_task():
    first_num = random.randint(1, 50)
    second_num = random.randint(1, 25)
    
    operation, result = random.choice([
        ('+', first_num + second_num),
        ('-', first_num - second_num),
        ('*', first_num * second_num)
    ])
    
    question = f'{first_num} {operation} {second_num}'
    return question, str(result)

def run_calc_game():
    run_game(get_correct_answer_and_task, CALC_INSTRUCTION)
