my_string = "hello world"

# Count, Startswith, Endwith
# Index, Find, Replace, Strip

# c = my_string.count("h")
# print(c)
# c = my_string.count("z")
# print(c)
# c = my_string.count("ll")
# print(c)

# c = my_string.startswith("h")
# print(c)
# c = my_string.startswith("hello")
# print(c)

# c = my_string.endswith("world")
# print(c)
# c = my_string.endswith("ld")
# print(c)

# c = my_string.index("world")
# print(c)
# c = my_string.index("h")
# print(c)

# c = my_string.find("z")  # Return -1 on failure.
# print(c)

# c = my_string.replace("l", "z")
# print(c)

my_string = "    hello world        "
c = my_string.strip()
print(my_string)
print(c)

my_string = "@@@@@@hello world@@@@@@"
c = my_string.strip("@")
print(my_string)
print(c)
