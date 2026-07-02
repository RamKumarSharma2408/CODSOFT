# Task 2 – Calculator

## CODSOFT Python Programming Internship

### Overview
A simple command-line calculator that performs basic arithmetic operations. The user inputs two numbers and chooses an operation, and the program displays the result. The calculator runs in a loop, allowing multiple calculations in one session.

### Features
- **Addition, Subtraction, Multiplication, Division**
- **Input Validation** – Re-prompts the user if a non-numeric value is entered.
- **Division by Zero Handling** – Displays a friendly error instead of crashing.
- **Repeat Calculations** – Keep calculating until you choose to exit.

### How to Run
```bash
python3 task2_calculator.py
```

### Sample Usage
```
===== SIMPLE CALCULATOR =====

Select operation:
1. Add (+)
2. Subtract (-)
3. Multiply (*)
4. Divide (/)
5. Exit
Enter choice (1-5): 1
Enter first number: 12
Enter second number: 8

Result: 12.0 + 8.0 = 20.0
```

### Tech Used
- Python 3 (standard library only — no external packages required)

### Possible Improvements
- Add support for more operations (exponents, square roots, modulus)
- Support chained expressions (e.g., `2 + 3 * 4`)
- Build a GUI version using Tkinter

---
*Part of the CODSOFT Python Programming Internship – [www.codsoft.in](https://www.codsoft.in)*
