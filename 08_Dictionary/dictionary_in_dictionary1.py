students_data = {
    "aayush": {
        "roll_number": 431,
        "gender": "Male",
        "marks": [78, 89, 67, 99, 69],
    },
    "kunal": {
        "roll_number": 122,
        "gender": "Female",
        "marks": [78, 89, 67, 99, 69],
    },
    "thakur": {
        "roll_number": 786,
        "gender": "Female",
        "marks": [78, 89, 67, 99, 69],
    },
}

# Calculate total marks using sum()
for name, details in students_data.items():
    total = sum(details["marks"])
    print(f"{name} has scored {total} marks")

    # print(name)
    # print(details["marks"])
