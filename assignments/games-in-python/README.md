
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a Hangman game that uses Python strings, loops, conditionals, and random selection to let a player reveal a hidden word before attempts run out.

## 📝 Tasks

### 🛠️ Set Up the Game

#### Description
Prepare the word, guessed letters, and attempt counter that the game needs to begin.

#### Requirements
Completed program should:

- Randomly select a word from the predefined list in `starter-code.py`.
- Store the selected word as the hidden word.
- Initialize an empty collection to track guessed letters.
- Set the maximum number of incorrect guesses.

### 🛠️ Process Player Guesses

#### Description
Repeatedly ask the player to enter one letter and update the game state based on the guess.

#### Requirements
Completed program should:

- Accept one letter from the user during each turn.
- Add valid guesses to the collection of guessed letters.
- Reveal every occurrence of a correctly guessed letter in the word.
- Display the hidden word in `_ _ _` format, with spaces between unrevealed letters.
- Decrease the remaining incorrect guesses after a wrong guess.
- Notify the player about repeated guesses and invalid input.

Example progress:

```text
Word: p y t _ _ _
Incorrect guesses remaining: 4
Enter a letter: h
```

### 🛠️ End the Game

#### Description
Stop the game when the player guesses the full word or uses all incorrect guesses.

#### Requirements
Completed program should:

- Display a win message when every letter in the hidden word has been guessed.
- Display a lose message and reveal the hidden word when no incorrect guesses remain.
- End the game loop immediately after either condition is reached.
