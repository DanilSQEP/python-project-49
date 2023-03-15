#!/usr/bin/env python3
from brain_games.general_logic import run_game
from brain_games.games.brain_calc import RULES_GAME, get_question_and_answer


def main():
    run_game(RULES_GAME, get_question_and_answer)


if __name__ == "__main__":
    main()
