import re


# Level 1: Easy

def validate_email(email):
    """Question 1: Validate an email address using regex."""
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    return bool(re.fullmatch(pattern, email))


def format_phone_number(number):
    """Question 2: Format a phone number into +1-xxx-xxx-xxxx."""
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


def extract_numbers(text):
    """Question 3: Extract all integers and floating-point numbers."""
    pattern = r"\d+(?:\.\d+)?"
    return re.findall(pattern, text)


def validate_password(password):
    """Question 4: Validate password strength using regex."""
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*]).{8,}$"
    return bool(re.fullmatch(pattern, password))


# Level 2: Medium

def extract_dates(text):
    """Question 5: Extract dates in DD/MM/YYYY format."""
    pattern = r"\b\d{2}/\d{2}/\d{4}\b"
    return re.findall(pattern, text)


def validate_username(username):
    """Question 6: Validate a username (alphanumeric, 5 to 15 characters)."""
    pattern = r"^[A-Za-z0-9]{5,15}$"
    return "Valid" if re.fullmatch(pattern, username) else "Invalid"


def extract_hashtags(text):
    """Question 7: Extract all hashtags from a string."""
    pattern = r"#\w+"
    return re.findall(pattern, text)


def extract_words_of_length(text, length=4):
    """Question 8: Extract words of a specific length from a string."""
    pattern = rf"\b[A-Za-z]{{{length}}}\b"
    return re.findall(pattern, text)


if __name__ == "__main__":
    print("Question 1: Validate Email")
    print(validate_email("user@example.com"))
    print(validate_email("invalid_email@.com"))

    print("\nQuestion 2: Format Phone Number")
    print(format_phone_number("1234567890"))
    print(format_phone_number("87-654-3210"))

    print("\nQuestion 3: Extract Numbers")
    print(extract_numbers("The price is $19.99 and the quantity is 25."))
    print(extract_numbers("The population of the city is 1,234,567."))

    print("\nQuestion 4: Validate Password")
    print(validate_password("StrongPassword!1"))
    print(validate_password("weakpassword123"))

    print("\nQuestion 5: Extract Dates")
    print(extract_dates("The event is on 12/05/2023 and 15/08/2023."))
    print(extract_dates("No dates here."))

    print("\nQuestion 6: Validate Username")
    print(validate_username("user123"))
    print(validate_username("u!@#"))

    print("\nQuestion 7: Extract Hashtags")
    print(extract_hashtags("Loving the #weather and the #sunshine!"))
    print(extract_hashtags("No hashtags here."))

    print("\nQuestion 8: Extract Words of Length 4")
    print(extract_words_of_length("This test has four word lengths."))
    print(extract_words_of_length("Hello world!"))
