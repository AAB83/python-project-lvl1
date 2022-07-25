import random
from brain_games.games_api import compare_answer
from brain_games.welcom_user import greet_user


def main_even():
    name_user = greet_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    number_of_correct_answers = 0
    while number_of_correct_answers < 3:
        random_number = random.randint(1, 100)
        if random_number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        if compare_answer(random_number, correct_answer, name_user):
            print('Correct!')
            number_of_correct_answers += 1
        else:
            break
    if number_of_correct_answers == 3:
        print(f'Congratulations, {name_user}!')


if __name__ == '__main__':
    main_even()
