import random
import os


## Greetings, traveler!
def greet_player():
    os.system('cls' if os.name == 'nt' else 'clear')
    name = input("What's your name? ")
    print(f"Hello, {name}! Let's play a guessing game.")
    return name


## Random number generator
def generate_secret_number():
    return random.randint(1, 20)


## Asks for a value between 1 and 20. If it receives a number outside this range,
## or not an integer, it returns the error and asks again.
def get_player_guess():
    while True:
        try:
            guess = int(input("Guess the secret number (between 1 and 20): "))
            if 1 <= guess <= 20:
                return guess
            else:
                print("Please enter a number between 1 and 20.")
        except ValueError:
            print("Please enter a valid number.")


## The game - Creates the random number, then sets the attempts to 0.
def play_game(stats):
    secret_number = generate_secret_number()
    attempts = 0

    ## Sets loop so that as long as attempts is less than 6, it continues.
    ## This works because the loop starts at 0, and the range consists of 6 values.
    while attempts < 6:
        attempts += 1
        guess = get_player_guess()

        ## Checks for secret number guess. This is where it checks if secret guess is
        ## less than, greater than, or equal to the random guess.
        if guess == secret_number:
            print(f"Congratulations! You've guessed the secret number {secret_number} in {attempts} attempts!")
            stats['times_won'] += 1
            return True
        elif guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")

    ## For if you run out of guesses.
    print(f"Sorry, you've run out of attempts! The secret number was {secret_number}.")
    stats['times_lost'] += 1
    return False


## Main function where things happen. Loops!
def main(player_name):
    stats = {'times_played': 0, 'times_won': 0, 'times_lost': 0}
    
    while True:
        if not play_game(stats):
            print("Game over!")
        stats['times_played'] += 1

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes" and play_again != "y":
            print("Thank you for playing!")
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Let's play again, {player_name}")

    print("\n--- Statistics ---")
    print(f"Times played: {stats['times_played']}")
    print(f"Times won: {stats['times_won']}")
    print(f"Times lost: {stats['times_lost']}")

## Assertion tests
def test():
    secret_number = generate_secret_number()
    assert 1 <= secret_number <= 20
    secret_number = generate_secret_number()
    assert 1 <= secret_number <= 20

test()

## Habit
if __name__ == "__main__":
    player_name = greet_player()
    main(player_name)
