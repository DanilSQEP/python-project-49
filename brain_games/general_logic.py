import prompt


def greet():
    print('Welcome to the Brain Games!')


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def number_of_rounds(name, receive_expression, true_expression):
    count_true_answer = 0
    while count_true_answer < 3:
        expression = receive_expression()
        print(f'Question: {expression}')
        answer_user = prompt.string('Your answer: ')
        right_answer = true_expression(expression)
        if answer_user == right_answer:
            count_true_answer += 1
            print('Correct!')
        else:
            print(f"'{answer_user}' is wrong answer ;(. Correct answer was '{right_answer}'.")
            break
    else:
        print(f'Congratulations, {name}!')
    if count_true_answer != 3:
        print(f"Let's try again, {name}!")
