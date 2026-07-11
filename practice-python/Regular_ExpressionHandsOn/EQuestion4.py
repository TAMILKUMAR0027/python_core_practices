import re


def validate_password(password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*]).{8,}$"
    return bool(re.fullmatch(pattern, password))


if __name__ == "__main__":
    print(validate_password("StrongPassword!1"))
    print(validate_password("weakpassword123"))
