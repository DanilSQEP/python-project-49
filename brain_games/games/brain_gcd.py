from random import randint


RULES_GAME = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    first_num = randint(1, 101)
    second_num = randint(1, 101)
    expression = f'{first_num} {second_num}'
    while first_num != 0 and second_num != 0:
        if first_num > second_num:
            first_num = first_num % second_num
        else:
            second_num = second_num % first_num
    result = f'{second_num + first_num}'
    return expression, result
