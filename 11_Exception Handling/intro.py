# What is exception handling

try:
    lst = [4, 5, 5, 34, 2, 3, 6]
    print(lst[1])
    print(lst[5])
    print(lst[65])
    print(lst[2])
    print(lst[4])
    print(lst[34])
except:
    print("Some error occurred")

print("Done")
print("Bye")
