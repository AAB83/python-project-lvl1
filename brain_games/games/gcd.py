import math
import random


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    random_number_one = random.randint(1, 100)
    random_number_two = random.randint(1, 100)
    question = f"{random_number_one} {random_number_two}"
    correct_answer = math.gcd(random_number_one, random_number_two)
    return question, str(correct_answer)
