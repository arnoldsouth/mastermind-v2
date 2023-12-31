# Mastermind Game

In this version of the Mastermind Game, the computer generates a secret code, and the player tries to guess it. After each guess, players receive feedback on how many numbers they got right and how many are in the correct position.

## Overview

- Player 1 inputs a secret code.
- Player 2 tries to guess the secret code.
- Player 2 receives feedback on how many numbers they got right and how many are in the correct location.
- The game ends either when Player 2 guesses the correct code or after 10 incorrect guesses.

## Features

- The secret code is generated by the computer upon game initialization.
- Provides feedback on the number of correct numbers and correct locations.
- Maximum of 10 attempts to guess the secret code.
- View game history.

## Installation and Setup

1. Clone this repository.
2. Install the required packages.
   ```bash
   pip install django requests
   ```
3. Run migrations to set up the database.
   ```
   python manage.py migrate
   ```
4. Start the development server.
   ```
   python manage.py runserver
   ```

## Usage

1. Navigate to the root URL (`http://127.0.0.1:8000/` by default) to access the game's homepage.
2. Click on "Start Game" to begin a new game.
3. Enter your guess and view its feedback.
4. Game history is displayed once the game is over.

## File Structure

- `views.py`: Contains the main logic for the game, including initializing a new game, processing guesses, and viewing game history.
- `utils.py`: Utility functions, including generating the secret code.
- `urls.py`: URL configuration for the game.
- HTML Templates:
  - `home.html`: The game's homepage providing an overview and an option to start a new game.
  - `game.html`: Game interface allowing users to input their guesses.
  - `game_over.html`: Displays results after a game is over, either after 10 unsuccessful attempts or after guessing correctly.
  - `history.html`: Shows a history of the 10 most recent played games.

## API Used

For generating random combinations, the app uses an API provided by `random.org`.
