import prompt

from brain_games.answer_user import reply
from brain_games.games_api import compare_answer


def run_game(game):
    print('Welcome to the Brain Games!')
    name_user = prompt.string('May I have your name? ')
    print('Hello, ' + name_user + '!')
    print(game.DESCRIPTION)
    number_of_correct_answers = 0
    while number_of_correct_answers < 3:
        question, correct_answer = game.get_question_and_answer()
        answer_user = reply(question)
        if compare_answer(answer_user, correct_answer):
            print('Correct!')
            number_of_correct_answers += 1
        else:
            print(f"""'{answer_user}' is wrong answer ;(. Correct answer was '{correct_answer}'.
    Let's try again, {name_user}!""")
            break
    if number_of_correct_answers == 3:
        print(f'Congratulations, {name_user}!')
