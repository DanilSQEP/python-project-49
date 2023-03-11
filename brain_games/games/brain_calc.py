from random import randint, choice


def receive_expression():
    expression = f'{randint(1, 101)} '\
                 f'{choice(["+", "-", "*"])} {randint(1, 101)}'
    return expression


def true_expression(expression):
    split_expression = expression.split()
    if split_expression[1] == '+':
        return f'{int(split_expression[0]) + int(split_expression[-1])}'
    elif split_expression[1] == '-':
        return f'{int(split_expression[0]) - int(split_expression[-1])}'
    else:
        return f'{int(split_expression[0]) * int(split_expression[-1])}'
