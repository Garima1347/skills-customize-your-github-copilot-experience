# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a command-line Hangman game in Python to practice string manipulation, loops, and user input handling.

## 📝 Tasks

### 🛠️ Task 1 — Implement the Core Game

#### Description
Create a playable Hangman game that selects a secret word, accepts letter guesses, shows progress, and ends when the player wins or runs out of attempts.

#### Requirements
Completed program should:

- Randomly select a secret word from a predefined list.
- Accept single-letter guesses and reveal correctly guessed letters in the word.
- Display current progress using blanks and guessed letters, such as `_ a _ g _ a _`.
- Track and display the number of incorrect attempts remaining.
- End the game with a clear win or lose message and reveal the secret word on loss.
- Validate input so only single alphabetical characters are accepted and repeated guesses are ignored.

### 🛠️ Task 2 — Add Optional Enhancements

#### Description
Improve the game with one or more extra features to make it more engaging.

#### Requirements
Completed program should:

- Add at least one enhancement from the list below:
  - Load the word list from a file.
  - Add ASCII-art hangman stages.
  - Allow difficulty levels with different attempt counts.
  - Add a replay option and basic score tracking.
