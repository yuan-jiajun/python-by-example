"""
================================================================================
Project 01: Number Guessing Game
Difficulty: 🟢 Beginner
================================================================================

A command-line number guessing game where the computer picks a random number
and the player tries to guess it with hints provided after each attempt.

Concepts Used:
- while loops
- if/elif/else conditionals
- random module
- try/except error handling
- input() function
- f-strings

================================================================================
"""

import random


# -----------------------------------------------------------------------------
# Game Configuration
# -----------------------------------------------------------------------------

DIFFICULTIES = {
    "easy": {"min": 1, "max": 50, "attempts": 10},
    "medium": {"min": 1, "max": 100, "attempts": 7},
    "hard": {"min": 1, "max": 500, "attempts": 10},
}


# -----------------------------------------------------------------------------
# Helper Functions
# -----------------------------------------------------------------------------

def display_welcome():
    """Display the welcome banner."""
    print("""
╔══════════════════════════════════════════╗
║       🎯 NUMBER GUESSING GAME 🎯        ║
╚══════════════════════════════════════════╝
    """)


def choose_difficulty() -> dict:
    """Let the player choose a difficulty level."""
    print("Choose your difficulty:")
    print("  [1] 🟢 Easy   (1-50,  10 attempts)")
    print("  [2] 🟡 Medium (1-100,  7 attempts)")
    print("  [3] 🔴 Hard   (1-500, 10 attempts)")

    while True:
        choice = input("\nYour choice (1/2/3): ").strip()
        if choice == "1":
            return DIFFICULTIES["easy"]
        elif choice == "2":
            return DIFFICULTIES["medium"]
        elif choice == "3":
            return DIFFICULTIES["hard"]
        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")


def get_guess(min_val: int, max_val: int) -> int:
    """Get a valid integer guess from the player."""
    while True:
        try:
            guess = int(input(f"\nEnter your guess ({min_val}-{max_val}): "))
            if min_val <= guess <= max_val:
                return guess
            else:
                print(f"⚠️  Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("⚠️  That's not a valid number. Try again!")


def play_round():
    """Play a single round of the guessing game."""
    # Setup
    config = choose_difficulty()
    min_val = config["min"]
    max_val = config["max"]
    max_attempts = config["attempts"]
    secret = random.randint(min_val, max_val)
    attempts = 0

    print(f"\n🤔 I'm thinking of a number between {min_val} and {max_val}...")
    print(f"   You have {max_attempts} attempts. Good luck!\n")

    # Game loop
    while attempts < max_attempts:
        guess = get_guess(min_val, max_val)
        attempts += 1
        remaining = max_attempts - attempts

        if guess < secret:
            print(f"📉 Too low! ({remaining} attempts remaining)")
        elif guess > secret:
            print(f"📈 Too high! ({remaining} attempts remaining)")
        else:
            print(f"\n🎉 Congratulations! You guessed it in {attempts} attempt(s)!")
            if attempts <= 3:
                print("🏆 Amazing! You're a natural!")
            elif attempts <= 5:
                print("👏 Well done!")
            else:
                print("😅 That was close!")
            return True

    # Out of attempts
    print(f"\n💀 Game over! The number was {secret}.")
    return False


def play_again() -> bool:
    """Ask the player if they want to play again."""
    while True:
        answer = input("\n🔄 Play again? (yes/no): ").strip().lower()
        if answer in ("yes", "y"):
            print()
            return True
        elif answer in ("no", "n"):
            return False
        else:
            print("Please enter 'yes' or 'no'.")


# -----------------------------------------------------------------------------
# Main Game Loop
# -----------------------------------------------------------------------------

def main():
    """Main entry point for the game."""
    display_welcome()

    wins = 0
    total = 0

    while True:
        total += 1
        if play_round():
            wins += 1

        print(f"\n📊 Score: {wins} wins out of {total} games")

        if not play_again():
            break

    print(f"\n{'='*40}")
    print(f"  Final Score: {wins}/{total} games won")
    print(f"  Thanks for playing! Goodbye! 👋")
    print(f"{'='*40}\n")


if __name__ == "__main__":
    main()
