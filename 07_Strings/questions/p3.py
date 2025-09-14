"""
Ask a string from user. convert all the alphabets to uppercase.
"""

my_string = "abc123ABCD"

# result = my_string.upper()
# print(result)

result = ""

for ch in my_string:
    ascii = ord(ch)
    if ascii >= 97 and ascii <= 122:
        new_ascii = ascii - 32
        char = chr(new_ascii)
        result += char
    else:
        result += ch
print(result)
