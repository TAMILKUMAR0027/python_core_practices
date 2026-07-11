import re


def extract_numbers(text):
    pattern = r"\d+(?:\.\d+)?"
    return re.findall(pattern, text)


if __name__ == "__main__":
    print(extract_numbers("The price is $19.99 and the quantity is 25."))
    print(extract_numbers("The population of the city is 1,234,567."))
