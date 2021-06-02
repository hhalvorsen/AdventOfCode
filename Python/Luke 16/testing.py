test = ['class', "seat", "row"]
r = {"field": "class"}
print(test.index(r["field"]))
print(type(test))
print(len(test))
test.pop(2)
test.pop(1)
print(type(test))
print(len(test))
test.pop(0)
print(len(test))
