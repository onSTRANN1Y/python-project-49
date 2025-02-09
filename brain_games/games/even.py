from random import randint
from brain_games.engine import run_game
from brain_games.consts import EVEN_INSTRUCTION


def is_even(number):
    return number % 2 == 0


def get_correct_answer_and_task():
    number = randint(1, 100)
    correct_answer = 'yes' if is_even(number) else 'no'
    question = str(number)
    return question, correct_answer


def run_even_game():
    run_game(get_correct_answer_and_task, EVEN_INSTRUCTION)
