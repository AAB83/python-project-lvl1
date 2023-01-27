import random


DESCRIPTION = 'What number is missing in the progression?'


def get_question_and_answer():
    start = random.randint(1, 20)
    step = random.randint(2, 10)
    length = 10
    end = start + step * length
    index_correct_answer = random.randint(1, length - 1)
    progression = \
        list(range(start, end, step))
    progression[index_correct_answer] = '..'
    question = str(start)
    for i in range(1, length):
        question = f'{question} {progression[i]}'
    correct_answer = \
        str(start + step * index_correct_answer)
    return question, correct_answer
