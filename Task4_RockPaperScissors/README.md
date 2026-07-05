# Task 4 – Rock-Paper-Scissors Game

## CODSOFT Python Programming Internship

### Overview
A command-line implementation of the classic Rock-Paper-Scissors game. The user plays against the computer, which makes a random choice each round. Scores are tracked across multiple rounds, and the user decides when to stop playing.

### Features
- **User Input** – Choose rock, paper, or scissors.
- **Computer Selection** – Random choice generated for the computer each round.
- **Game Logic** – Determines the winner based on standard rules (rock beats scissors, scissors beat paper, paper beats rock).
- **Score Tracking** – Keeps a running tally of wins, losses, and ties.
- **Play Again Option** – Keep playing multiple rounds or exit at any time.

### How to Run
```bash
python3 task4_rock_paper_scissors.py
```

### Sample Usage
```
===== ROCK, PAPER, SCISSORS =====
Choose rock, paper, or scissors: rock

You chose: rock
Computer chose: scissors
You win this round!

Score -> You: 1 | Computer: 0 | Ties: 0
Play again? (y/n): n

Final Score:
You: 1 | Computer: 0 | Ties: 0
Thanks for playing!
```

### Tech Used
- Python 3 (`random` module from the standard library)

### Possible Improvements
- Add a best-of-N round mode
- Build a GUI version using Tkinter
- Add extra options like "lizard" and "Spock"

---
*Part of the CODSOFT Python Programming Internship – [www.codsoft.in](https://www.codsoft.in)*
