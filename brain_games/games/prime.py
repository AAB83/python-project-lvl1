import random

from brain_games.lib.is_prime import is_prime

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_answer():
    random_number = random.randint(1, 100)
    question = str(random_number)
    correct_answer = 'yes' if is_prime(random_number) else 'no'
    return question, correct_answer
