import prompt


def run_game(game):
    print('Welcome to the Brain Games!')
    name_user = prompt.string('May I have your name? ')
    print('Hello, ' + name_user + '!')
    print(game.DESCRIPTION)
    rounds_count = 3
    for i in range(rounds_count):
        question, correct_answer = game.get_question_and_answer()
        print(f'Question: {question}')
        answer_user = prompt.string('Your answer: ')
        if answer_user != correct_answer:
            print(f"'{answer_user}' is wrong answer ;(."
                  f" Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {name_user}!")
            break
        elif answer_user == correct_answer:
            print('Correct!')
    else:
        print(f'Congratulations, {name_user}!')
