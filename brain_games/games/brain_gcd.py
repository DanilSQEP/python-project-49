from random import randint


def receive_expression():
    expression = f'{randint(1, 101)} {randint(1, 101)}'
    return expression


def true_expression(expression):
    split_expression = expression.split()
    a = int(split_expression[0])
    b = int(split_expression[-1])
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return f'{a + b}'
