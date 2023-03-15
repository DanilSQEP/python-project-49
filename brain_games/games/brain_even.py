from random import randint


RULES_GAME = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_answer():
    expression = randint(1, 101)
    if expression % 2 == 0:
        return expression, "yes"
    else:
        return expression, "no"
