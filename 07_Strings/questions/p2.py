"""
Ask a string from user. count the no:of uppercase and
lowercase characters in that string
"""

my_string = input("Enter a string: ")
lower_count = 0
upper_count = 0
# for ch in my_string:
#     if ch.isupper():
#         upper_count += 1
#     elif ch.islower:
#         lower_count += 1

# the cpp way of solving this without methods
for ch in my_string:
    ascii = ord(ch)
    if ascii >= 65 and ascii <= 90:
        upper_count += 1
    elif ascii >= 97 and ascii <= 122:
        lower_count += 1

print(upper_count)
print(lower_count)
