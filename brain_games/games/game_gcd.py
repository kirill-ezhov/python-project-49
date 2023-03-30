import random
import math

OUTPUT_TASK = 'Find the greatest common divisor of given numbers.'
min_number = 1
max_number = 100


def get_game():
    first_number: int = random.randint(min_number, max_number)
    second_number: int = random.randint(min_number, max_number)
    question: str = f'{first_number} {second_number}'
    correct_answer: int | str = math.gcd(first_number, second_number)
    return question, str(correct_answer)
