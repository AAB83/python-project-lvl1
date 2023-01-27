import random


DESCRIPTION = 'What number is missing in the progression?'


def get_question_and_answer():
    random_number_one = random.randint(1, 20)
    step = random.randint(2, 10)
    length = 10
    end = random_number_one + step * length
    index_correct_answer = random.randint(0, length - 1)
    progression = \
        list(range(random_number_one, end, step))
    progression[index_correct_answer] = '..'
    question = str(random_number_one)
    for i in progression:
        question = f'{question} {i}'
    correct_answer = \
        str(random_number_one + step * index_correct_answer)
    return question, correct_answer
