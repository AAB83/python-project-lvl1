import random
from brain_games.answer_user import reply
from brain_games.games_api import compare_answer
from brain_games.welcom_user import greet_user


def calculate_answer(index_correct_answer, random_number_one, step_progression):
    return str(random_number_one + step_progression * index_correct_answer)


def main_progression():
    name_user = greet_user()
    print('What number is missing in the progression?')
    number_of_correct_answers = 0
    while number_of_correct_answers < 3:
        random_number_one = random.randint(1, 20)
        step_progression = random.randint(2, 10)
        index_correct_answer = random.randint(1, 9)
        i = 1
        progression = str(random_number_one)
        while i < 10:
            if i != index_correct_answer:
                progression = progression + ' ' + \
                    str(random_number_one + step_progression * i)
            else:
                progression = progression + ' ' + '..'
            i += 1
        answer_user = reply(progression)
        correct_answer = calculate_answer(index_correct_answer,
                                          random_number_one, step_progression)
        print(correct_answer)
        if compare_answer(answer_user, correct_answer):
            print('Correct!')
            number_of_correct_answers += 1
        else:
            print(f"""'{answer_user}' is wrong answer ;(. Correct answer was '{correct_answer}'.
Let's try again, {name_user}!""")
            break

    if number_of_correct_answers == 3:
        print(f'Congratulations, {name_user}!')
