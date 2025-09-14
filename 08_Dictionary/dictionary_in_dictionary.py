# students_data is a dictionary where each student name is a key.
# The value is another dictionary with student details.

students_data = {
    "aayush": {
        "roll_number": 431,
        "gender": "Male",
        "physics": 78,
        "chemistry": 89,
        "maths": 67,
    },
    "kunal": {
        "roll_number": 122,
        "gender": "Female",
        "physics": 90,
        "chemistry": 75,
        "maths": 82,
    },
    "thakur": {
        "roll_number": 786,
        "gender": "Female",
        "physics": 82,
        "chemistry": 91,
        "maths": 56,
    },
}

# Example access
# print(students_data)
# print(type(students_data))
# print(students_data["aayush"]["roll_number"])
# print(students_data["aayush"]["gender"])

# Calculate total marks for each student
for name, details in students_data.items():
    print(name)
    total = details["physics"] + details["maths"] + details["chemistry"]
    print(f"{name} -> {total}")

    gender = details["gender"]
    print(f"{name} -> total={total}, gender={gender}")
