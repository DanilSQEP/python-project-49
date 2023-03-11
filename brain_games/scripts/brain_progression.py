#!/usr/bin/env python3
from brain_games.general_logic import greet, welcome_user, number_of_rounds
from brain_games.games.brain_progression import receive_expression, \
                                                true_expression


def main():
    greet()
    name = welcome_user()
    print('What number is missing in the progression?')
    number_of_rounds(name, receive_expression, true_expression)


if __name__ == "__main__":
    main()
