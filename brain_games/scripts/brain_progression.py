#!/usr/bin/env python3
from brain_games.games.progression import get_correct_answer_and_task
from brain_games.games.instructions import QUESTION_PROGRESSION_GAME
from brain_games.game_launcher import launching_the_engine


def main():
    launching_the_engine(get_correct_answer_and_task, QUESTION_PROGRESSION_GAME)


if __name__ == '__main__':
    main()
