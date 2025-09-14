students_data = {
    "aayush": {
        "roll_number": 431,
        "gender": "Male",
        "marks": {"physics": 78, "maths": 89, "chemistry": 67},
    },
    "kunal": {
        "roll_number": 122,
        "gender": "Female",
        "marks": {"physics": 78, "maths": 89, "chemistry": 67},
    },
    "thakur": {
        "roll_number": 786,
        "gender": "Female",
        "marks": {"physics": 78, "maths": 89, "chemistry": 67},
    },
}

# Calculate total marks from dictionary of subjects
for name, details in students_data.items():
    total = (
        details["marks"]["physics"]
        + details["marks"]["chemistry"]
        + details["marks"]["maths"]
    )
    print(f"{name} has scored {total} marks")


# print(name)
# print(details["marks"])
# print(details["marks"]["physics"])
# print(details["marks"]["chemistry"])
# print(details["marks"]["maths"])
