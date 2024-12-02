#!/usr/bin/env python3
from brain_games.game_launcher import launching_the_engine
from brain_games.games.instructions import QUESTION_PRIME_GAME
from brain_games.games.prime import get_correct_answer_and_task


def main():
    launching_the_engine(get_correct_answer_and_task, QUESTION_PRIME_GAME)


if __name__ == '__main__':
    main()
