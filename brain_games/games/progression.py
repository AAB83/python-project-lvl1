import random


DESCRIPTION = 'What number is missing in the progression?'


def get_question_and_answer():
    start = random.randint(1, 20)
    step = random.randint(2, 10)
    length = 10
    end = start + step * length
    index_correct_answer = random.randint(0, length - 1)
    progression = \
        list(range(start, end, step))
    progression = [str(i) for i in progression]
    progression[index_correct_answer] = '..'
    question = ' '.join(progression)
    correct_answer = \
        str(start + step * index_correct_answer)
    return question, correct_answer


get_question_and_answer()
