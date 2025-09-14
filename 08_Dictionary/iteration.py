my_dict = {
    "name": "Aayush",
    "age": 22,
    "gender": "male",
}

# Print all keys
# print(my_dict.keys())

# Loop through keys
# for k in my_dict.keys():
#     print(k)              # printing key
#     print(my_dict[k])     # printing corresponding value

# Loop through values
# (we usually don’t take keys from values since values can repeat)
# for v in my_dict.values():
#     print(v)


# New dictionary with marks
my_dict1 = {
    "history": 67,
    "comp": 99,
    "science": 78,
    "maths": 11,
}

# Calculate total marks
total_marks = 0
for v in my_dict1.values():
    total_marks = total_marks + v

print(total_marks)  # Output: 255
