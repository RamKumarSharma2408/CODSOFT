"""
CODSOFT Python Programming Internship
Task 3 - Password Generator

Generates a strong, random password based on the length and
character types (uppercase, lowercase, digits, symbols) chosen
by the user.
"""

import random
import string


def get_length():
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length <= 0:
                print("Length must be a positive number.")
                continue
            return length
        except ValueError:
            print("Please enter a valid number.")


def get_yes_no(prompt):
    while True:
        answer = input(prompt + " (y/n): ").strip().lower()
        if answer in ("y", "n"):
            return answer == "y"
        print("Please enter 'y' or 'n'.")


def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    char_pool = ""
    if use_upper:
        char_pool += string.ascii_uppercase
    if use_lower:
        char_pool += string.ascii_lowercase
    if use_digits:
        char_pool += string.digits
    if use_symbols:
        char_pool += string.punctuation

    if not char_pool:
        return None

    password = "".join(random.choice(char_pool) for _ in range(length))
    return password


def main():
    print("===== PASSWORD GENERATOR =====")

    length = get_length()
    use_upper = get_yes_no("Include uppercase letters?")
    use_lower = get_yes_no("Include lowercase letters?")
    use_digits = get_yes_no("Include numbers?")
    use_symbols = get_yes_no("Include symbols?")

    password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)

    if password is None:
        print("\nYou must select at least one character type. Try again.")
    else:
        print(f"\nGenerated Password: {password}")


if __name__ == "__main__":
    main()
