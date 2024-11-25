#!/usr/bin/env python3
from brain_games.cli import welcome_user


def game_engine(game_function, task_function):
    name = welcome_user()
    task_function()
    for i in range(3):
        correct_answer, answer = game_function()
        if correct_answer == answer:
            print('Correct!')
        else:
            print(f"""'{answer}' is wrong answer ;(.\
 Correct answer was '{correct_answer}'.
Let's try again, {name}!""")
            return
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    game_engine()
