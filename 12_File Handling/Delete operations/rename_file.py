import os

if os.path.exists("hello.txt"):
    os.rename("hello.txt", "new_hello.txt")
    print("File renamed.")
else:
    print("file does not exist.")
