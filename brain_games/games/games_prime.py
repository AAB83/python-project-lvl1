import random
from brain_games.answer_user import reply
from brain_games.games_api import compare_answer
from brain_games.welcom_user import greet_user


def calculate_answer(number):
    if number == 1:
        return 'no'
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return 'no'
    return 'yes'


def main_prime():
    name_user = greet_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    number_of_correct_answers = 0
    while number_of_correct_answers < 3:
        random_number = random.randint(1, 100)
        answer_user = reply(random_number)
        correct_answer = calculate_answer(random_number)
        if compare_answer(answer_user, correct_answer):
            print('Correct!')
            number_of_correct_answers += 1
        else:
            print(f"""'{answer_user}' is wrong answer ;(. Correct answer was '{correct_answer}'.
Let's try again, {name_user}!""")
            break

    if number_of_correct_answers == 3:
        print(f'Congratulations, {name_user}!')


if __name__ == '__main__':
    main_prime()
