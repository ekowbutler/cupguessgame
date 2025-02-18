# Empty cups
from random import shuffle


def game_set():
    cups = ["", "0", ""]
    return cups


# Shuffling empty cups
def shuffle_game_set(game_cups):
    shuffle(game_cups)
    return game_cups  # Not necessary, but keeping it explicit


# User guess function
def user_guess():
    user_input = input("Guess position of ball [0,1,2]: ")
    return int(user_input)  # Convert input to integer


# Main game function
def tikito_game_app(shuffled_game_set, users_guess):
    if users_guess == shuffled_game_set.index("0"):
        print("Player wins!")
    else:
        print("Try again!")


# Run game
game_cups = game_set()  # Create game set
shuffled_game_set = shuffle_game_set(game_cups)  # Shuffle cups
users_guess = user_guess()  # Get user guess
tikito_game_app(shuffled_game_set, users_guess)  # Check if user won

# Print for debugging
print("Shuffled cups:", shuffled_game_set)
print("User guessed:", users_guess)
