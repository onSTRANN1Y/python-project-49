### Hexlet tests and linter status:

[![Actions Status](https://github.com/onSTRANN1Y/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/onSTRANN1Y/python-project-49/actions)

[![Maintainability](https://api.codeclimate.com/v1/badges/92ecef7fa48501f2d7cd/maintainability)](https://codeclimate.com/github/onSTRANN1Y/python-project-49/maintainability)

<!--Installation-->
# Project Installation and Launch

This project uses Poetry for dependency management and virtual environment. To install and run the project, follow these steps:

## Step 1: Install Poetry

First, make sure you have the latest version of Poetry installed. If it's not installed yet, follow the instructions on the official website: https://python-poetry.org/docs/#installation.

1. Installing Poetry via pipx (recommended)

```bash```
```pip install --user pipx```
```pipx ensurepath```
```pipx install poetry```

2. Installing Poetry via curl (for Linux/macOS)

```curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -```

3. Installing Poetry via Scoop (for Windows)

```scoop bucket add extras```
```scoop install poetry```

## Step 2: Clone the Repository

Clone the project repository to your computer:

```git clone git@github.com:onSTRANN1Y/python-project-49.git```

Navigate to the cloned repository:

```cd python-project-49```

## Step 3: Install Dependencies

Use Poetry to install all necessary dependencies:

```poetry install```

## Step 4: Activate Virtual Environment

Activate the virtual environment created by Poetry:

```poetry shell```

## Step 5: Launch the Selected Game Using the Appropriate Command

1. Game: "Even Check"

The essence of the game: the user is shown a random number. They need to answer 'yes' if the number is even, or 'no' if it's odd.

Command to launch the game:
```poetry run brain-even```

[![asciicast](https://asciinema.org/a/mc34MGyaLHGwrZetgAM799gi0.svg)](https://asciinema.org/a/mc34MGyaLHGwrZetgAM799gi0)

2. Game: "Calculator"

The essence of the game: the user is shown a random mathematical expression, for example, 35 + 16, which needs to be calculated and the correct answer entered.

Command to launch the game:
```poetry run brain-calc```

[![asciicast](https://asciinema.org/a/G1mAVrt71NGE9tmQHNEsgXdhD.svg)](https://asciinema.org/a/G1mAVrt71NGE9tmQHNEsgXdhD)

3. Game: "GCD"

The essence of the game: the user is shown two random numbers, for example, 25 50. The user must calculate and enter the greatest common divisor of these numbers.

Command to launch the game:
```poetry run brain-gcd```

[![asciicast](https://asciinema.org/a/5Dm5bHRv2qLQXs6hrPFUM6WkS.svg)](https://asciinema.org/a/5Dm5bHRv2qLQXs6hrPFUM6WkS)

4. Game: "Arithmetic Progression"

The essence of the game: a series of numbers forming an arithmetic progression is shown, with one number replaced by two dots. The player must determine this number.

Command to launch the game:
```poetry run brain-progression```

[![asciicast](https://asciinema.org/a/KxWWY5FWVV50R4pKGq96UrT0f.svg)](https://asciinema.org/a/KxWWY5FWVV50R4pKGq96UrT0f)

5. Game: "Is it Prime?"

The essence of the game: you need to answer 'yes' if the number is prime or 'no' if it's not.

Command to launch the game:
```poetry run brain-prime```

[![asciicast](https://asciinema.org/a/86ciaYcLN4dedMlcDQ6ZTsG0t.svg)](https://asciinema.org/a/86ciaYcLN4dedMlcDQ6ZTsG0t)

## Technology Stack

1. Python 3.12
2. Dependency management tool: Poetry
3. Code analysis tool: Flake8
4. Automatic import sorting and formatting: isort
5. Functionality library: prompt

