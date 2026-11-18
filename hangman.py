# CodeAlpha Internship - Task 1
# Project: Hangman Game

import random

# List of 5 predefined words
words = ["python", "coding", "computer", "program", "developer"]

# Randomly select a word
secret_word = random.choice(words)

# Create blank spaces for each letter
guessed_word = ["_"] * len(secret_word)

# Maximum incorrect guesses
max_attempts = 6
wrong_guesses = 0

# Store already guessed letters
guessed_letters = []

print("=" * 35)
print("       WELCOME TO HANGMAN!")
print("=" * 35)
print("Guess the hidden word one letter at a time.")
print("You have 6 incorrect guesses allowed.\n")

# Main game loop
while wrong_guesses < max_attempts and "_" in guessed_word:

    print("Word:", " ".join(guessed_word))
    print("Wrong guesses:", wrong_guesses, "/", max_attempts)
    print("Guessed letters:", guessed_letters)

    # Take user input
    guess = input("\nEnter a letter: ").lower().strip()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet letter!\n")
        continue

    # Check if letter already guessed
    if guess in guessed_letters:
        print("You already guessed this letter!\n")
        continue

    guessed_letters.append(guess)

    # Check if letter exists
    if guess in secret_word:
        print("Correct guess!")

        # Reveal matching letters
        for index in range(len(secret_word)):
            if secret_word[index] == guess:
                guessed_word[index] = guess

    else:
        print("Wrong guess!")
        wrong_guesses += 1

    print()

# Final result
if "_" not in guessed_word:
    print("=" * 35)
    print("🎉 CONGRATULATIONS! YOU WON!")
    print("The word was:", secret_word)
else:
    print("=" * 35)
    print("GAME OVER! YOU LOST.")
    print("The correct word was:", secret_word)

print("=" * 35)