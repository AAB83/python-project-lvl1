import prompt


def reply(question):
    print(f'Question: {str(question)}')
    answer = prompt.string('Your answer: ')
    return answer
