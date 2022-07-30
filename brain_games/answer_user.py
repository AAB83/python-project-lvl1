import prompt


def reply(question):
    print(f'Question: {str(question)}')
    answer = prompt.string('Your answer: ')
    return answer


if __name__ == '__main__':
    reply()
