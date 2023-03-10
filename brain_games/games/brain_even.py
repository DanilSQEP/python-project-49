from random import randint


def receive_expression():
    expression = randint(1, 101)
    return expression


def true_expression(expression):
    if expression % 2 == 0:
        return "yes"
    else:
        return 'no'
