my_dict = {
    "name": "Aayush",
    "age": 22,
    "gender": "male",
}

print(my_dict)

# Method 2: Using update()
my_dict.update({"marks": 99, "address": "Delhi", "name": "Xyz"})
print(my_dict)

# Method 1: Direct assignment
# If the key exists → value gets updated
# If the key doesn’t exist → new key-value pair gets added
my_dict["age"] = 100
print(my_dict)

my_dict["marks"] = 100
print(my_dict)
