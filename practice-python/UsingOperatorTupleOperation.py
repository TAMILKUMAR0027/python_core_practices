addr = "monty@python.org"
print(type(addr))
uname, domain = addr.split("@")
t = (uname, domain)
print(t[0], t[1])