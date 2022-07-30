import random
from brain_games.answer_user import reply
from brain_games.games_api import compare_answer
from brain_games.welcom_user import greet_user


def calculate_answer(number_one, number_two, action):
    if action == '+':
        return str(number_one + number_two)
    elif action == '-':
        return str(number_one - number_two)
    elif action == '*':
        return str(number_one * number_two)


def main_calc():
    name_user = greet_user()
    print('What is the result of the expression?')
    number_of_correct_answers = 0
    while number_of_correct_answers < 3:
        random_number_one = random.randint(1, 100)
        random_number_two = random.randint(1, 100)
        actions = ('+', '-', '*')
        operation = actions[random.randint(0, 2)]
        question = str(random_number_one) + ' ' + operation + ' ' + str(random_number_two)
        answer_user = reply(question)
        correct_answer = calculate_answer(random_number_one, random_number_two, operation)
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
    main_calc()
