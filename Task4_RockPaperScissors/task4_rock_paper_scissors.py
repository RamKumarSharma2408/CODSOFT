"""
CODSOFT Python Programming Internship
Task 4 - Rock, Paper, Scissors Game

The user plays against the computer. The computer's choice is
random. Scores are tracked across rounds, and the user can choose
to keep playing or stop at any time.
"""

import random

CHOICES = ["rock", "paper", "scissors"]


def get_user_choice():
    while True:
        choice = input("Choose rock, paper, or scissors: ").strip().lower()
        if choice in CHOICES:
            return choice
        print("Invalid choice. Please type rock, paper, or scissors.")


def get_computer_choice():
    return random.choice(CHOICES)


def determine_winner(user, computer):
    if user == computer:
        return "tie"

    beats = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock",
    }

    if beats[user] == computer:
        return "user"
    return "computer"


def play_again():
    while True:
        answer = input("Play again? (y/n): ").strip().lower()
        if answer in ("y", "n"):
            return answer == "y"
        print("Please enter 'y' or 'n'.")


def main():
    print("===== ROCK, PAPER, SCISSORS =====")

    user_score = 0
    computer_score = 0
    ties = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)

        if result == "tie":
            print("It's a tie!")
            ties += 1
        elif result == "user":
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"\nScore -> You: {user_score} | Computer: {computer_score} | Ties: {ties}")

        if not play_again():
            print("\nFinal Score:")
            print(f"You: {user_score} | Computer: {computer_score} | Ties: {ties}")
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
