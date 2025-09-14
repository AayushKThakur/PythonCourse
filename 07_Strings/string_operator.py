a = "Aayush"
b = "Thakur"

print(a + b)  # Concatenation → AayushThakur
# print(a * b) #error
print(a * 3)  # Repetition → AayushAayushAayush
# print(a / b) #error
# print(a - b) #error

# Rule: String comparisons are done character by character using 
# ASCII/Unicode values. 
# Uppercase letters (A–Z, 65–90) come before 
# lowercase (a–z, 97–122).

print(a == b) # False → checks equality
print(a > b)  # False → compares lexicographically (dictionary order using ASCII)
print(a < b) # True

#ASCII codes
first_ch = "a"    # ASCII 97
second_ch = "A"   # ASCII 65

print(first_ch < second_ch)  # False (97 < 65 → False)

#printing ASCII 
ch="a"
print(ord(ch))

num=97
print(chr(num))