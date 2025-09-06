# Q10. Calculate sum of 5 subjects and Find percentage.

English = float(input(("Enter marks obtained in English: ")))
Hindi = float(input(("Enter marks obtained in Hindi: ")))
Science = float(input(("Enter marks obtained in Science: ")))
Social_Science = float(input(("Enter marks obtained in Social_Science: ")))
Maths = float(input(("Enter marks obtained in Maths: ")))

percentage = ((English + Hindi + Science + Social_Science + Maths) / 500) * 100

print (f"The obtained percentage is {percentage}")