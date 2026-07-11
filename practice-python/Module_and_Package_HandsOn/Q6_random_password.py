import random
import string


def generate_password(length):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(random.choice(characters) for _ in range(length))


if __name__ == "__main__":
    print("Generated password:", generate_password(8))
