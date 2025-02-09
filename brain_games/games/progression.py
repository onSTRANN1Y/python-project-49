from random import randint
from brain_games.engine import run_game
from brain_games.consts import PROGRESSION_INSTRUCTION


def generate_progression():
    start = randint(1, 50)
    step = randint(1, 5)
    return [str(start + i * step) for i in range(10)]


def get_correct_answer_and_task():
    progression = generate_progression()
    hidden_index = randint(0, 9)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = '..'
    question = ' '.join(progression)
    return question, correct_answer


def run_progression_game():
    run_game(get_correct_answer_and_task, PROGRESSION_INSTRUCTION)
