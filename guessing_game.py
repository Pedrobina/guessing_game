import random

guess = 0
guess_counter = 0
number_select = random.randint(1, 100)

while guess != number_select:
    guess_counter += 1
    print(f"\nGuess {guess_counter}:")
    guess = int(input("Guess a number between 1 and 100\n"))

    if guess < number_select:
        print(f"{guess} is to low, try again.")
    elif guess > number_select:
        print(f"{guess} is to high, try again.")
    else:
        print(f"Congratulations {guess} is the correct number")
        print(f"Total guesses: {guess_counter}")
        break
