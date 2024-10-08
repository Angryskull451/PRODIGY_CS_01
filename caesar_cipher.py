def caesar_cipher(text, shift, direction):
    result = ""
    if direction == "decrypt":
        shift = -shift

    for char in text:
        # Check if it's an uppercase letter
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Check if it's a lowercase letter
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char

    return result

# Get user inputs
message = input("Enter your message: ")
shift_value = int(input("Enter shift value: "))
mode = input("Do you want to encrypt or decrypt? ").strip().lower()

# Run the Caesar Cipher
encrypted_message = caesar_cipher(message, shift_value, mode)
print(f"The result is: {encrypted_message}")
