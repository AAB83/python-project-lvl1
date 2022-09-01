import random


DESCRIPTION = 'What number is missing in the progression?'


def get_question_and_answer():
    random_number_one = random.randint(1, 20)
    step_progression = random.randint(2, 10)
    progression_length = 10
    progression_end = random_number_one + step_progression * progression_length
    index_correct_answer = random.randint(1, progression_length - 1)
    progression = list(range(random_number_one, progression_end, step_progression))
    progression[index_correct_answer] = '..'
    question = ''
    for i in progression:
        question = f'{question} {i}'
    correct_answer = \
        str(random_number_one + step_progression * index_correct_answer)
    return question, correct_answer
