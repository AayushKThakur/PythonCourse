''' 
title, capitalized, upper, lower, swapcase isupper, 
islower, isalpha, isalnum, isspace 

.isalpha() → only letters
.isdigit() → only digits
.isalnum() → letters + digits
'''

a = "aayush kunal thakur"

# String transformations
print(a.title())      # Each word → First letter capital
print(a.capitalize()) # Only first char capital, rest lower
print(a.upper())      # All uppercase
print(a.lower())      # All lowercase
print(a.swapcase())   # Swap case (upper ↔ lower)

# String checks (return True/False)
print(a.isupper())    # True if all chars uppercase
print(a.islower())    # True if all chars lowercase
print(a.isalpha())    # True if only alphabets
print(a.isalnum())    # True if only alphabets + numbers
print(a.isdigit())    # True if only digits
print(a.isspace())    # True if only whitespace

# Check if string is an integer
a = "aayush123"

if a.isdigit():
    a = int(a)
    print(a, type(a))   # Will print integer if only digits
else:
    print("Cannot be converted to integer")  # Mixed → not int
