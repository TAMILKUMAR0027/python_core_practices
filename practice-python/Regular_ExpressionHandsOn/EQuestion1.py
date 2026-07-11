import re


def validate_email(email):
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    return bool(re.fullmatch(pattern, email))


if __name__ == "__main__":
    print(validate_email("user@example.com"))
    print(validate_email("invalid_email@.com"))
