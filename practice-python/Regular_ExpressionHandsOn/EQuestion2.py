import re


def format_phone_number(number):
    digits = re.sub(r"\D", "", str(number))

    if len(digits) == 9:
        digits = "9" + digits
    elif len(digits) > 10:
        digits = digits[-10:]
    elif len(digits) < 9:
        return "Invalid phone number"

    if len(digits) == 10:
        return f"+1-{digits[0:3]}-{digits[3:6]}-{digits[6:]}"

    return "Invalid phone number"


if __name__ == "__main__":
    print(format_phone_number("1234567890"))
    print(format_phone_number("87-654-3210"))
