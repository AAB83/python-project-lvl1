import random


DESCRIPTION = 'What is the result of the expression?'


def calculate_answer(number_one, number_two, action):
    if action == '+':
        return str(number_one + number_two)
    elif action == '-':
        return str(number_one - number_two)
    elif action == '*':
        return str(number_one * number_two)


def get_question_and_answer():
    random_number_one = random.randint(1, 100)
    random_number_two = random.randint(1, 100)
    actions = ('+', '-', '*')
    operation = actions[random.randint(0, 2)]
    question = str(random_number_one) + ' ' + operation + ' ' \
        + str(random_number_two)
    correct_answer = calculate_answer(random_number_one,
                                      random_number_two, operation)
    return question, correct_answer
