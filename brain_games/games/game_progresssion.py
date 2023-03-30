import random
import math

OUTPUT_TASK = 'What number is missing in the progression?'


def get_game():
    progression = list(range(random.randint(0, 30), random.randint(30, 50), random.randint(1, 10)))
    length_question = (random.randint(0, len(progression)))
    correct_answer = progression[length_question]
    progression[length_question] = '..'
    question = ' '.join(list(map(str, progression)))
    return question, str(correct_answer)
