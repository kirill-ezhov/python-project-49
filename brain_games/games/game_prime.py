import random

OUTPUT_TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_game():
    question = random.randint(1, 100)
    count = 0
    for i in range(2, question // 2 + 1):
        if question % i == 0:
            count = count + 1
    if count <= 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, str(correct_answer)
