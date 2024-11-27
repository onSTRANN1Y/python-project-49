### Hexlet tests and linter status:

[![Actions Status](https://github.com/onSTRANN1Y/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/onSTRANN1Y/python-project-49/actions)

[![Maintainability](https://api.codeclimate.com/v1/badges/92ecef7fa48501f2d7cd/maintainability)](https://codeclimate.com/github/onSTRANN1Y/python-project-49/maintainability)

<!--Установка-->
# Установка и запуск проекта

Этот проект использует Poetry для управления зависимостями и виртуальным окружением. Чтобы установить и запустить проект, выполните следующие шаги:

## Шаг 1:  Установите Poetry

Сначала убедитесь, что у вас установлена последняя версия Poetry. Если она еще не установлена, следуйте инструкциям на официальном сайте: https://python-poetry.org/docs/#installation.

1. Установка Poetry через pipx (рекомендуется)

```bash```
```pip install --user pipx```
```pipx ensurepath```
```pipx install poetry```

2.  Установка Poetry через curl (для Linux/macOS)

```curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -```

3.  Установка Poetry через Scoop (для Windows)

```scoop bucket add extras```
```scoop install poetry```

## Шаг 2: Клонируйте репозиторий

Клонируйте репозиторий проекта на свой компьютер:

```git clone https://github.com/onSTRANN1Y/python-project-49```
```cd python-project-49```


## Шаг 3: Установите зависимости

Используйте Poetry для установки всех необходимых зависимостей:

```poetry install```


## Шаг 4: Активируйте виртуальное окружение

Активируйте виртуальное окружение, созданное Poetry:

```poetry shell```


## Шаг 5: Запустите игру выбрав нужную команду


1.		Игра:«Проверка на чётность» 

Суть игры в следующем: пользователю показывается случайное число. И ему нужно ответить yes, если число чётное, или no — если нечётное

Команда для вызова игры:
```poetry run brain-even```

[Демонстрация игры](https://asciinema.org/a/mc34MGyaLHGwrZetgAM799gi0)

2.		Игра: «Калькулятор»

Суть игры в следующем: пользователю показывается случайное математическое выражение, например, 35 + 16, которое нужно вычислить и записать правильный ответ.

Команда для вызова игры:
```poetry run brain-calc```

[Демонстрация игры](https://asciinema.org/a/G1mAVrt71NGE9tmQHNEsgXdhD)

3.		Игра: «НОД»

Суть игры в следующем: пользователю показывается два случайных числа, например, 25 50. Пользователь должен вычислить и ввести наибольший общий делитель этих чисел.

Команда для вызова игры:
```poetry run brain-gcd```

[Демонстрация игры](https://asciinema.org/a/5Dm5bHRv2qLQXs6hrPFUM6WkS)

4.		Игра: «Арифметическая прогрессия»

Суть игры в следующем: показывается ряд чисел, который образует арифметическую прогрессию, заменив любое из чисел двумя точками. Игрок должен определить это число.

Команда для вызова игры:
```poetry run brain-progression.```

[Демонстрация игры](https://asciinema.org/a/KxWWY5FWVV50R4pKGq96UrT0f)

5.		Игра: «Простое ли число?»

Суть игры в следующем: нужно ответить 'yes' если число простое или 'no' если нет.

Команда для вызова игры:
```poetry run brain-prime```

[Демонстрация игры](https://asciinema.org/a/86ciaYcLN4dedMlcDQ6ZTsG0t)
