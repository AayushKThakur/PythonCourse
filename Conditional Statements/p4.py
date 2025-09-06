"""
Ask 5 marks from user.
calculate percentage and print it

91-100 -> A grade
81-90 -> B grade
71-80 -> C grade
61-70 -> D grade
1-60 -> FAIL
Invalid
"""
maths= int(input("Enter the marks for maths: "))
science= int(input("Enter the marks for science : ")) 
hindi= int(input("Enter the marks for hindi: "))
english= int(input("Enter the marks for english: "))
marathi= int(input("Enter the marks for marathi: "))

total = maths+science+hindi+english+marathi

percentage = (total/500)*100
print(f"Percentage scored = {percentage}")

if percentage>=91 and percentage<=100:
    print("A grade")
elif percentage>=81 and percentage<=90:
    print("B grade")
elif percentage>=71 and percentage<=80:
    print("C grade")
elif percentage>=61 and percentage<=70:
    print("D grade")
elif percentage>=1 and percentage<=60:
    print("FAIL")
else:
    print("Invalid percentage")

