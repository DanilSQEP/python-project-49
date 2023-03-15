import prompt


def run_game(RULES_GAME, get_question_and_answer):
    NUM_OF_ROUNDS = 3
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(RULES_GAME)
    count_true_answer = 0
    while count_true_answer < NUM_OF_ROUNDS:
        question, right_answer = get_question_and_answer()
        print(f'Question: {question}')
        answer_user = prompt.string('Your answer: ')
        if answer_user == right_answer:
            count_true_answer += 1
            print('Correct!')
        else:
            print(f"'{answer_user}' is wrong answer ;(. "
                  f"Correct answer was '{right_answer}'.")
            break
    else:
        print(f'Congratulations, {name}!')
    if count_true_answer != 3:
        print(f"Let's try again, {name}!")
