#!/usr/bin/env python3
from brain_games.games.brain_prime import brain_prime, task
from brain_games.engine import game_engine


def main():
    game_engine(brain_prime, task)


if __name__ == '__main__':
    brain_prime()
