from math import gcd
from random import randint
from brain_games.engine import run_game
from brain_games.consts import GCD_INSTRUCTION


def get_correct_answer_and_task():
    number_1, number_2 = randint(10, 20), randint(1, 50)
    correct_answer = gcd(number_1, number_2)
    question = f'{number_1} {number_2}'
    return question, str(correct_answer)

def run_gcd_game():
    run_game(get_correct_answer_and_task, GCD_INSTRUCTION)
