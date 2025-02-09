from random import randint
from brain_games.engine import run_game
from brain_games.consts import PRIME_INSTRUCTION


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def get_correct_answer_and_task():
    number = randint(1, 100)
    correct_answer = 'yes' if is_prime(number) else 'no'
    question = str(number)
    return question, correct_answer


def run_prime_game():
    run_game(get_correct_answer_and_task, PRIME_INSTRUCTION)
