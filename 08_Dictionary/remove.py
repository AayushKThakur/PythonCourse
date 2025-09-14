my_dict = {
    "name": "Aayush",
    "age": 22,
    "gender": "male",
}

print(my_dict)

# del my_dict   # would delete the entire dictionary

# Remove specific key-value pairs
my_dict.pop("name")  # removes key "name"
my_dict.pop  # this just shows the function reference (not used here)
my_dict.popitem()  # removes last inserted item (in Python 3.7+, dicts are ordered)

print(my_dict)
