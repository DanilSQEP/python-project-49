from random import randint, choice


RULES_GAME = 'What number is missing in the progression?'


def get_question_and_answer():
    length_progression = randint(5, 10)
    member_progression = randint(1, 1000)
    step_progression = randint(1, 100)
    list_progression = list()
    for i in range(length_progression):
        list_progression.append(str(member_progression))
        member_progression += step_progression
    random_element = choice(list_progression)
    index_member_replacment = list_progression.index(random_element)
    list_progression[index_member_replacment] = '..'
    return ' '.join(list_progression), random_element
