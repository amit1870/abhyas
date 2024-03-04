import string
import random

def generate_password(psd_length=8):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special = list("!@#$%^&*")

    # Generate a list of alphanumeric characters
    alphanumeric_chars = random.sample(
        lowercase_letters + uppercase_letters, 5
    )

    # Generate a list of remaining characters
    remaining_chars = random.choices(digits, k=(psd_length-5))

    # add a special character
    special_char = random.choices(special, k=1)

    # Combine the two lists and shuffle
    password_chars = alphanumeric_chars + remaining_chars + special_char
    random.shuffle(password_chars)

    # Create the password string
    password = "".join(password_chars)

    return password

def simple_password(psd_length=8):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits

    # Generate a list of alphanumeric characters
    alphanumeric_chars = random.sample(
        lowercase_letters + uppercase_letters, 6
    )

    # Generate a list of remaining characters
    remaining_chars = random.choices(digits, k=(psd_length-6))

    # Combine the two lists and shuffle
    password_chars = alphanumeric_chars + remaining_chars
    random.shuffle(password_chars)

    # Create the password string
    password = "".join(password_chars)

    return password