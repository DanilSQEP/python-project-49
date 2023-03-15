from random import randint, choice


RULES_GAME = 'What is the result of the expression?'


def get_question_and_answer():
    first_num = randint(1, 101)
    second_num = randint(1, 101)
    operation_on_num = choice(["+", "-", "*"])
    expression = f'{first_num} {operation_on_num} {second_num}'
    if operation_on_num == '+':
        return expression, f'{first_num + second_num}'
    elif operation_on_num == '-':
        return expression, f'{first_num - second_num}'
    else:
        return expression, f'{first_num * second_num}'
