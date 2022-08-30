import random


DESCRIPTION = 'What number is missing in the progression?'


def calculate_answer(index_correct_answer, random_number_one, step_progression):
    return str(random_number_one + step_progression * index_correct_answer)


def get_question_and_answer():
    random_number_one = random.randint(1, 20)
    step_progression = random.randint(2, 10)
    index_correct_answer = random.randint(1, 9)
    i = 1
    progression = str(random_number_one)
    while i < 10:
        if i != index_correct_answer:
            progression = f"{progression} " \
                          f"{str(random_number_one + step_progression * i)}"
        else:
            progression = f"{progression} .."
        i += 1

    question = progression
    correct_answer = calculate_answer(index_correct_answer,
                                      random_number_one, step_progression)
    return question, correct_answer
