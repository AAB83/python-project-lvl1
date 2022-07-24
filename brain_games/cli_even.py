import prompt
import random


def games_even():
    print('Welcom to the Brain Games')
    name_user = prompt.string('May I have your name? ')
    print('Hello, ' + name_user + '!')
    print('Answer "yes" if the number is even, otherwise answer "no".')

    number_of_correct_answers = 0
    while number_of_correct_answers < 3:
        random_number = random.randint(1, 100)
        print(f'Question: {random_number}')
        answ = prompt.string('Your answer: ')
        if random_number % 2 == 0:
            correct_answ = 'yes'
        else:
            correct_answ = 'no'
        if answ == correct_answ:
            print('Correct!')
            number_of_correct_answers += 1
        else:
            print(f"""'{answ}' is wrong answer ;(. Correct answer was '{correct_answ}'.
Let's try again, {name_user}""")
            return

    print(f'Congratulations, {name_user}!')


if __name__ == '__main__':
    games_even()
