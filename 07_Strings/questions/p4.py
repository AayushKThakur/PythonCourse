"""
Count the number of spaces in a string entered by user.
"""

my_string = "abc123 3AC^&* ^*(%8NSK"
count = 0

# for ch in my_string:
#     if ch == " ":
#         count += 1

for ch in my_string:
    if ord(ch) == 32:
        count += 1

print(count)
