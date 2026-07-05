# Task 3 – Password Generator

## CODSOFT Python Programming Internship

### Overview
A command-line tool that generates strong, random passwords. Users can specify the desired password length and choose which character types to include (uppercase letters, lowercase letters, digits, and symbols).

### Features
- **Custom Length** – User chooses exactly how long the password should be.
- **Custom Complexity** – Choose to include/exclude uppercase, lowercase, digits, and symbols.
- **Randomized Output** – Uses Python's `random` module to shuffle characters from the selected pool.
- **Input Validation** – Prevents invalid lengths and requires at least one character type to be selected.

### How to Run
```bash
python3 task3_password_generator.py
```

### Sample Usage
```
===== PASSWORD GENERATOR =====
Enter the desired password length: 12
Include uppercase letters? (y/n): y
Include lowercase letters? (y/n): y
Include numbers? (y/n): y
Include symbols? (y/n): y

Generated Password: Kd8#pQzL2@fn
```

### Tech Used
- Python 3 (`random` and `string` modules from the standard library)

### Possible Improvements
- Add a password strength meter
- Allow excluding ambiguous characters (e.g., `0`, `O`, `l`, `1`)
- Generate and save multiple passwords at once

---
*Part of the CODSOFT Python Programming Internship – [www.codsoft.in](https://www.codsoft.in)*
