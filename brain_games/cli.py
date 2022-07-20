import prompt


def welcom_user():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')


if __name__ == '__main__':
    welcom_user()
