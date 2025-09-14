my_dict = {
    "name": "Aayush",
    "age": 22,
    "gender": "male",
}

# Get user input
k = input("Enter a key: ")

# Safely fetch value using get()
result = my_dict.get(k)

if result is not None:
    print(result)

# Access dictionary values directly
print(my_dict["name"])
print(my_dict["age"])

# Using .get() method
r = my_dict.get("name")
print(r)

# If key doesn’t exist, get() returns None instead of error
r = my_dict.get("namee")
print(r)  # None
print(type(r))  # <class 'NoneType'>
