import random
import operator


DESCRIPTION = 'What is the result of the expression?'


def get_question_and_answer():
    random_number_one = random.randint(1, 100)
    random_number_two = random.randint(1, 100)
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
    }
    operation = random.choice(list(operations.keys()))
    question = f"{str(random_number_one)} {operation} {str(random_number_two)}"
    correct_answer = str(operations[operation](random_number_one, random_number_two))
    return question, correct_answer
