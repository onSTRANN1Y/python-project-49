import prompt


def get_game_rules(get_function, question):
    name = prompt.string('Welcome to the Brain Games\nMay I have your name? ')
    print(f'Hello, {name}')
    MAX_ROUNDS = 3
    print(question)

    for _ in range(MAX_ROUNDS):
        correct_answer, task = get_function()
        print(task)
        answer = prompt.string('You answer: ')
        if str(correct_answer) == str(answer):
            print('Correct!')
        else:
            print(f"""'{answer}' is wrong answer ;(.\
 Correct answer was '{correct_answer}'.
Let's try again, {name}!""")
            return
    print(f'Congratulations, {name}!')
