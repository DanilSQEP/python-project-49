from random import randint, choice


def receive_expression():
    length_progression = randint(5, 10)
    member_progression = randint(1, 1000)
    step_progression = randint(1, 100)
    list_progression = list()
    for i in range(length_progression):
        list_progression.append(str(member_progression))
        member_progression += step_progression
    index_member_replacment = list_progression.index(choice(list_progression))
    list_progression[index_member_replacment] = '..'
    return ' '.join(list_progression)


def true_expression(expression):
    split_expression = expression.split()
    unknow_number = split_expression.index('..')
    if unknow_number == 0:
        return str(int(split_expression[1]) - \
               (int(split_expression[-1]) - int(split_expression[-2])))
    elif unknow_number == len(split_expression) - 1:
        return str(int(split_expression[-2]) + \
               (int(split_expression[1]) - int(split_expression[0])))
    else:
        return str(int(split_expression[unknow_number - 1]) + \
               ((int(split_expression[unknow_number + 1]) - \
               int(split_expression[unknow_number - 1])) // 2))
