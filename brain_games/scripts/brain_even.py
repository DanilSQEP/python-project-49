#!/usr/bin/env python3
from random import randint
import prompt

def greet():
    print('Welcome to the Brain Games!')


def welcome_user():
    name = prompt.string('May I have your name? ')
    return name


def even_number(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count_true_answer = 0
    while count_true_answer < 3:
        random_number = randint(1, 101)
        print(f'Question: {random_number}')
        answer = prompt.string('Your answer: ') 
        if random_number % 2 == 0 and answer == 'yes':
            count_true_answer += 1
            print('Correct!')
        elif random_number % 2 != 0 and answer == 'no':
            count_true_answer += 1
            print('Correct!')
        elif random_number % 2 == 0 and answer != 'yes':
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.")
            break
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.")
            break
    else:
        print(f'Congratulations, {name}!')
    if count_true_answer != 3:
        print(f"Let's try again, {name}!")


def main():
    greet()
    name = welcome_user()
    even_number(name)


if __name__ == "__main__":
    main()
