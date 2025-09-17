# with open(
#     "C:\\Users\\hp\\Desktop\\PythonCourse\\12_File Handling\\hello.txt", "r"
# ) as f:
with open("hello.txt", "r") as f:
    # print(f)

    for line in f:
        print(line)

    # x = f.read()
    # for ch in x:
    #     print(ch)
