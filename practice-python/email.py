import re

p1 = r".*\s\b[a-z0-9._%-]+@[a-z0-9.-_]+\.[a-z]{2}"
res = re.findall(p1, "my email is tamil00%27@gmail.co")
if res:
    print(res)
else:
    print("not")
    