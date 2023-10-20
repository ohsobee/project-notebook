#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

# List of words for the Hangman game
words = ["python", "jupyter", "notebook", "programming", "challenge"]

# Select a random word from the list
word = random.choice(words)

# Create a list to store the guessed letters
guessed_letters = []

# Set the maximum number of allowed attempts
max_attempts = 6

# Initialize the number of incorrect guesses
incorrect_guesses = 0

# Display underscores to represent the letters in the word
display_word = ["_"] * len(word)

# Function to display the current state of the word
def display_current_word():
    return " ".join(display_word)

# Function to update the display word with correctly guessed letters
def update_display_word(word, display_word, letter):
    for i in range(len(word)):
        if word[i] == letter:
            display_word[i] = letter

# Main game loop
while True:
    print(display_current_word())
    
    # Check if the player has guessed all the letters
    if "_" not in display_word:
        print("Congratulations! You guessed the word:", word)
        break

    # Ask the player for a letter guess
    guess = input("Guess a letter: ").lower()

    # Check if the guess is a single letter
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    # Check if the letter has already been guessed
    if guess in guessed_letters:
        print("You've already guessed that letter.")
        continue

    # Add the guessed letter to the list of guessed letters
    guessed_letters.append(guess)

    # Check if the guessed letter is in the word
    if guess in word:
        update_display_word(word, display_word, guess)
    else:
        print("Incorrect guess.")
        incorrect_guesses += 1

    # Check if the player has used all allowed attempts
    if incorrect_guesses == max_attempts:
        print("Game over! You've used all your attempts. The word was:", word)
        break


# In[ ]:




