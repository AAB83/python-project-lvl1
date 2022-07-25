import prompt


def compare_answer(question, correct_answer, name_user):
    print(f'Question: {str(question)}')
    answer = prompt.string('Your answer: ')
    if answer == correct_answer:
        return True
    else:
        print(f"""'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.
Let's try again, {name_user}!""")
        return False


if __name__ == '__main__':
    compare_answer()
