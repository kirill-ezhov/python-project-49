import random
import prompt



def question():
    name = prompt.string('May I have your name? ')
    print(f'Hello,  {name}!')
    n = 0
    while n < 3:
        n += 1
        questions = random.randint(0, 100)
        print(f'Answer "yes" if the number is even, otherwise answer "no".\nQuestion:{questions}')
        answer = input('Your answer:')
        if (questions % 2 == 0 and answer == 'yes') or (questions % 2 != 0 and answer == 'no'):
            print('Correct!')
        else:
            if answer == 'no':
                print(f"'no' is wrong answer ;(. Correct answer was 'yes'.Let's try again, {name}!")
            elif answer == 'yes':
                print(f"'yes' is wrong answer ;(. Correct answer was 'no'.Let's try again, {name}!")
            break
        print(f'Congratulations, {name}')