from random import randint


RULES_GAME = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_answer():
    expression = randint(1, 1001)
    for i in range(2, int(expression**0.5) + 1):
        if expression % i == 0:
            return expression, "no"
    return expression, "yes"
