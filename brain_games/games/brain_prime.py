from random import randint


def receive_expression():
    expression = randint(1, 1001)
    return expression


def true_expression(expression):
    for i in range(2, int(expression**0.5) + 1):
        if expression % i == 0:
            return "no"
    return 'yes'
