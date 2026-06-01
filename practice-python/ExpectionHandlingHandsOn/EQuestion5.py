person={"name":"Alice","age":30}

try:
    print(person["name"])
except KeyError:
    print("Error: Key not found!")