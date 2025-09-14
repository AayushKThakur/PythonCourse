# key : value
# Keys must be unique and must be hashable
# (strings, numbers, tuples are allowed).

# Values can be anything: numbers, strings,
# lists, other dictionaries, etc.

x = {
    "Name": "Aayush",
    "age": 22,
    "Gender": "Male",
    "Marks": [45, 65, 76, 87, 89],
    1: 2,  # this is also allowed
    2: 3,
}

print(x)
print(type(x))
