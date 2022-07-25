import prompt


def greet_user():
    print('Welcom to the Brain Games')
    name_user = prompt.string('May I have your name? ')
    print('Hello, ' + name_user + '!')
    return name_user


if __name__ == '__main__':
    greet_user()
