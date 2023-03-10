#!/usr/bin/env python3
from brain_games.general_logic import greet, welcome_user, number_of_rounds
from brain_games.games.brain_even import receive_expression, true_expression


def main():
    greet()
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    number_of_rounds(name, receive_expression, true_expression)


if __name__ == "__main__":
    main()
