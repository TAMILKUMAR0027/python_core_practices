numbers = dict(x=5, y=0)

d1 = dict({"x": 4, "y": 10})
d2 = dict([("x", 5), ("y", 7)])

d3 = {"name": "Tamil", "Age": 20}
print(d3.pop("name"))
print(d3.popitem())
print(d3)

d={1:'one',2:'two'}
d4={2:'three'}
d.update(d4)
print(d)

square={x:x*x for x in range(11)if x%2==1}
print(square)