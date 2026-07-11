import re


def extract_dates(text):
    pattern = r"\b\d{2}/\d{2}/\d{4}\b"
    return re.findall(pattern, text)


if __name__ == "__main__":
    print(extract_dates("The event is on 12/05/2023 and 15/08/2023."))
    print(extract_dates("No dates here."))
