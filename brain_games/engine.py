import prompt
from brain_games.consts import ROUNDS_COUNT, WELCOME_MESSAGE


def run_game(game_function, game_rules):
    print(WELCOME_MESSAGE)
    name = prompt.string('May I have your name?')
    print(f'Hello, {name}!')
    print(game_rules)
    for _ in range(ROUNDS_COUNT):
        question, correct_answer = game_function()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer:')
        if user_answer != str(correct_answer):
            print(f"'{user_answer}' is wrong answer ;(."
                  f"Correct answer is '{correct_answer}'.\n"
                  f"Let's try again, {name}!")
            return
        print('Correct!')
    print(f'Congratulations, {name}!')
