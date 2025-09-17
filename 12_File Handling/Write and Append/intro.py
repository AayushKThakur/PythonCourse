# write and append mode in python
with open("hello.txt", "w") as f:
    f.write("Aayush Thakur\n")
    f.write("We are learning python")

# if file does not exist, write creates the file, unlike read
with open("hello1.txt", "w") as f:
    f.write("Aayush Thakur\n")
    f.write("We are learning python")


# import os

# print("CWD:", os.getcwd())
