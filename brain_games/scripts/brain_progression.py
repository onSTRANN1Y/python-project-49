#!/usr/bin/env python3
from brain_games.games.progression import brain_progression, task
from brain_games.engine import game_engine


def main():
    game_engine(brain_progression, task)


if __name__ == '__main__':
    main()
