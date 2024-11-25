#!/usr/bin/env python3
from brain_games.games.brain_gcd import game_gcd, task
from brain_games.engine import game_engine


def main():
    game_engine(game_gcd, task)


if __name__ == '__main__':
    main()
