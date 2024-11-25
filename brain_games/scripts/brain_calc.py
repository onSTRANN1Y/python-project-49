#!/usr/bin/env python3
from brain_games.games.calc import calc, task
from brain_games.engine import game_engine


def main():
    game_engine(calc, task)


if __name__ == '__main__':
    main()
