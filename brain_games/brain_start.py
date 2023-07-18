import prompt


def run_game(game):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.TASK)

    ROUNDS_TO_WIN = 3
    true_answer = 0

    while true_answer < ROUNDS_TO_WIN:
        question, correct_answer = game.get_game()
        print(f'Question: {question}')
        player_answer = prompt.string('Your answer: ')

        if player_answer == correct_answer:
            print('Correct!')
            true_answer += 1
        else:
            print(
                f"'{player_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'")
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')


