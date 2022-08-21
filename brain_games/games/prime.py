import random


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def calculate_answer(number):
    if number == 1:
        return 'no'
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return 'no'
    return 'yes'


def get_question_and_answer():
    random_number = random.randint(1, 100)
    correct_answer = calculate_answer(random_number)
    question = str(random_number)
    return question, correct_answer
