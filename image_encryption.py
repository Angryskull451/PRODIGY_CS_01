from PIL import Image

# Function to encrypt an image
def encrypt_image(input_image_path, output_image_path, key):
    image = Image.open(input_image_path)
    encrypted_image = image.copy()  # Create a copy of the image for manipulation

    # Loop through each pixel in the image
    for x in range(image.width):
        for y in range(image.height):
            r, g, b = image.getpixel((x, y))

            # Apply a simple encryption by shifting pixel values using the key
            encrypted_r = (r + key) % 256
            encrypted_g = (g + key) % 256
            encrypted_b = (b + key) % 256

            # Set the new encrypted pixel values
            encrypted_image.putpixel((x, y), (encrypted_r, encrypted_g, encrypted_b))

    encrypted_image.save(output_image_path)
    print(f"Encrypted image saved as {output_image_path}")

# Function to decrypt an image
def decrypt_image(input_image_path, output_image_path, key):
    image = Image.open(input_image_path)
    decrypted_image = image.copy()  # Create a copy of the image for manipulation

    # Loop through each pixel in the image
    for x in range(image.width):
        for y in range(image.height):
            r, g, b = image.getpixel((x, y))

            # Reverse the encryption by shifting pixel values back using the key
            decrypted_r = (r - key) % 256
            decrypted_g = (g - key) % 256
            decrypted_b = (b - key) % 256

            # Set the new decrypted pixel values
            decrypted_image.putpixel((x, y), (decrypted_r, decrypted_g, decrypted_b))

    decrypted_image.save(output_image_path)
    print(f"Decrypted image saved as {output_image_path}")

# Example usage
encrypt_image('input_image.png', 'encrypted_image.png', 50)  # Replace with your image path and key
decrypt_image('encrypted_image.png', 'decrypted_image.png', 50)  # Use the same key to decrypt
