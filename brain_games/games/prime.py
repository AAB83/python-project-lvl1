import random

from brain_games.is_prime import is_prime

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_answer():
    random_number = random.randint(1, 100)
    question = str(random_number)
    return question, 'yes' if is_prime(random_number) else 'no'
