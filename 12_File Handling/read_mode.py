f = open("C:\\Users\\hp\\Desktop\\PythonCourse\\12_File Handling\\hello.txt", "r")
x = f.read()
print(x)
print(f.read(5))
print(f.read(5))

print(f.readline())
print(f.readline())

print(f.readlines())
f.close()
