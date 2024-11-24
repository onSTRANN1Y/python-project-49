#!/usr/bin/env python3
from brain_games.scripts.brain_games import main
from random import randint, choice
from prompt import integer


def random_progression():
    progression = []
    start_number = randint(1, 50)
    step = randint(1,5)
    flag = 0
    for i in range(start_number, start_number + 10 * step, step):
        progression.append(i)
    return progression 


def lose_game(answer, hide_number, name):
    print(f'{answer} is wrong answer ;(. Correct answer was {hide_number}.')
    print(f'''Let's try again, {name}!''')



def brain_progression():
    count = 0
    name = main()
    print(f'Hello, {name}!')
    print('What number is missing in the progression?')
    for i in range(3):
        progression = random_progression()
        random_index = randint(0, 9)
        hide_number = progression[random_index]
        progression[random_index] = '..'
        print(' '.join(map(str, progression)))
        answer = integer('Your answer: ')
        if answer == hide_number:
            print('Correct!')
            count += 1
        else:
            lose_game(answer, hide_number, name)
            break
    if count == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    brain_progression()

