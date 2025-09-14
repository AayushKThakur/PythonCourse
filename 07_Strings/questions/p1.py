"""
ask a string from user. count how many alphabets are there in that
string.
"""

my_string = "abc123"

count = 0
# for ch in my_string:
#     if ch.isalpha():
#         count += 1

# the cpp way of solving this without methods
for ch in my_string:
    ascii = ord(ch)
    if (ascii >= 65 and ascii <= 90) or (ascii >= 97 and ascii <= 122):
        count += 1

print(count)
