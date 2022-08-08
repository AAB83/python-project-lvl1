import math
import random
from brain_games.answer_user import reply
from brain_games.games_api import compare_answer
from brain_games.welcom_user import greet_user


def calculate_answer(number_one, number_two):
    return str(math.gcd(number_one, number_two))


def main_gcd():
    name_user = greet_user()
    print('Find the greatest common divisor of given numbers.')
    number_of_correct_answers = 0
    while number_of_correct_answers < 3:
        random_number_one = random.randint(1, 100)
        random_number_two = random.randint(1, 100)
        question = str(random_number_one) + ' ' + str(random_number_two)
        answer_user = reply(question)
        correct_answer = calculate_answer(random_number_one, random_number_two)
        if compare_answer(answer_user, correct_answer):
            print('Correct!')
            number_of_correct_answers += 1
        else:
            print(f"""'{answer_user}' is wrong answer ;(. Correct answer was '{correct_answer}'.
Let's try again, {name_user}!""")
            break

    if number_of_correct_answers == 3:
        print(f'Congratulations, {name_user}!')
