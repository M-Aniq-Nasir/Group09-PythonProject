import random

print("Welcome to the Number Guessing game!")
print("Guess the number between 1-50 which is in my mind.")

def play_game():
    secret_number = random.randint(1, 50)
    guess = 0
    attempts = 0

    while guess != secret_number:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < 1 or guess > 50:
            print("Guess between 1-50! Try again.")
            continue

        if guess < secret_number:
            print("Too low! Try again.")

        elif guess > secret_number:
            print("Too high! Try again.")

        else:
            print(f"Correct! The number was {secret_number}.")
            print(f"You guessed it in {attempts} attempts.\n")
        
play_again = 'y'

while play_again == 'y':
    play_game()
    play_again = input("Do you want to play again? (y/n): ")

print("Thanks for playing.")