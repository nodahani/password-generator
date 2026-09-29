print("Welcome to the password generator!")
password_length = input(
    "Enter password length (e.g., 8 to 64), or press Enter for default (12), or type 'b' to go back: "
)
password_type = input(
    f"Select character types to include (separate by comma):\n1. Lowercase (abc)\n2. Uppercase (ABC)\n3. Numbers (123)\n4. Symbols (!@#)\nExample: 1,3,4\n"
)
