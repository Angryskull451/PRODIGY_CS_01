import re

def check_password_strength(password):
    """
    This function checks the strength of a given password based on:
    1. Length: Minimum of 8 characters
    2. Uppercase Letters: At least one
    3. Lowercase Letters: At least one
    4. Numbers: At least one
    5. Special Characters: At least one (!@#$%^&*()-+)
    """
    # Criteria checks
    length_error = len(password) < 8
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    digit_error = re.search(r"\d", password) is None
    special_char_error = re.search(r"[!@#$%^&*()-+]", password) is None

    # Error count and feedback
    error_count = sum([length_error, uppercase_error, lowercase_error, digit_error, special_char_error])
    if error_count == 0:
        print("Strong Password! ✔️")
    else:
        print("Weak Password! ❌")
        print("Password must meet the following criteria:")
        if length_error:
            print("- At least 8 characters")
        if uppercase_error:
            print("- At least one uppercase letter")
        if lowercase_error:
            print("- At least one lowercase letter")
        if digit_error:
            print("- At least one number")
        if special_char_error:
            print("- At least one special character (!@#$%^&*()-+)")

# Input from user
user_password = input("Enter a password to check its strength: ")
check_password_strength(user_password)
