import random

TASK = 'What number is missing in the progression?'


def generate_progression(start, end, step):
    return list(range(start, end, step))


def get_game():
    start_number = random.randint(0, 30)
    end_number = random.randint(30, 50)
    step = random.randint(1, 10)
    progression = generate_progression(start_number, end_number, step)

    length_question = random.randint(0, len(progression) - 1)
    correct_answer = progression[length_question]
    progression[length_question] = '..'
    question = ' '.join(map(str, progression))

    return question, str(correct_answer)
