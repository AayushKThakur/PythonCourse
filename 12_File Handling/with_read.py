# WITH keyword

with open(
    "C:\\Users\\hp\\Desktop\\PythonCourse\\12_File Handling\\hello.txt", "r"
) as f:
    print(f.read())

# the file is closed to we will get error
print(f.read)
