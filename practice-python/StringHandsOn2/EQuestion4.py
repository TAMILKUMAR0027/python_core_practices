s = "Emma25 is Data scientist50 and AI Expert"

for i in s.split():
    if any(ch.isalpha() for ch in i) and any(ch.isdigit() for ch in i):
        print(i, end=" ")
