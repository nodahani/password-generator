import random
import string

print("Welcome to the password generator!")


def get_password_length():
    while True:
        user_input = input(
            "Enter password length (e.g., 8 to 64), or press Enter for default (12), or type 'b' to go back: "
        )

        if user_input == "":
            return 12

        if user_input.lower() == "b":
            return None

        try:
            length = int(user_input)
        except ValueError:
            print("** Please enter a valid number. **")
            continue

        if 8 <= length <= 64:
            return length

        print("** Invalid length! **")


def get_password_types():
    while True:
        user_input = input(
            f"Select character types to include (separate by comma)(default: 1,2,3):\n1. Lowercase (abc)\n2. Uppercase (ABC)\n3. Numbers (123)\n4. Symbols (!@#)\nExample: 1,3,4\n: "
        )

        if user_input == "":
            return [1, 2, 3]

        if user_input.lower() == "b":
            return None

        parts = user_input.split(",")  # '1,2,3'= ['1', '2', '3']
        try:
            numbers = [int(p) for p in parts]  # [1, 2, 3]
        except ValueError:
            print("** Please enter a valid number. **")
            continue

        result = []
        valid_options = [1, 2, 3, 4]
        for num in numbers:
            if num in valid_options:
                result.append(num)
            else:
                print(f"** Invalid option [{num}] **")

        if result:
            return result
        else:
            print("** No character types selected! **")


def password_generator():
    length = get_password_length()
    if length is None:
        return None

    types = get_password_types()
    if types is None:
        return None

    allowed = ""
    if 1 in types:
        allowed += string.ascii_lowercase
    if 2 in types:
        allowed += string.ascii_uppercase
    if 3 in types:
        allowed += string.digits
    if 4 in types:
        allowed += string.punctuation

    password = ""
    for _ in range(length):
        password += random.choice(allowed)
    return password


password = password_generator()
if password is None:
    print("** Cancelled. **")
else:
    print(f"Your password: {password}")
