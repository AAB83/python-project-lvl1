import random


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def calculate_answer(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def get_question_and_answer():
    random_number = random.randint(1, 100)
    question = random_number
    correct_answer = calculate_answer(random_number)
    return question, correct_answer
