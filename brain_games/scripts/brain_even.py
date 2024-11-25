#!/usr/bin/env python3
from brain_games.games.brain_even import brain_even, task
from brain_games.engine import game_engine

def main():
    game_engine(brain_even, task)


if __name__ == '__main__':
    main()
