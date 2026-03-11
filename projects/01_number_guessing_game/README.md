# 🎯 Project 01: Number Guessing Game

## Difficulty: 🟢 Beginner

## Description
Build a command-line number guessing game where the computer picks a random number
and the player tries to guess it. The game should provide hints like "Too high!" or
"Too low!" after each guess.

## Requirements

1. Generate a random number between 1 and 100
2. Ask the user for guesses until they get the correct number
3. After each guess, tell the user if their guess is too high, too low, or correct
4. Track the number of attempts and display it at the end
5. Handle invalid input gracefully (non-numeric input)
6. Ask the player if they want to play again after winning

## Concepts You'll Practice

- `while` loops
- `if/elif/else` conditionals
- `random` module
- `try/except` error handling
- `input()` function
- f-strings

## Example Output

```
🎯 Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100...

Enter your guess: 50
📉 Too low! Try again.

Enter your guess: 75
📈 Too high! Try again.

Enter your guess: 63
🎉 Congratulations! You guessed it in 3 attempts!

Play again? (yes/no): no
Thanks for playing! Goodbye! 👋
```

## How to Run

```bash
cd projects/01_number_guessing_game
python solution.py
```

## Bonus Challenges

- [ ] Add difficulty levels (Easy: 1-50, Medium: 1-100, Hard: 1-500)
- [ ] Add a scoreboard that tracks best scores across games
- [ ] Set a maximum number of attempts based on difficulty
