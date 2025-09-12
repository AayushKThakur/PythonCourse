a = [59, 68, 100, 5, "Aayush", True, 55.656, "Thakur"]
print(105 in a)
print(105 not in a)

# ask a number from user.
# print yes if number exists in list else print no

num = int(input("Enter a number: "))

# if a.count(num) > 0:
#     print("Yes")
# else:
#     print("no")

if num in a:
    print("yes")
else:
    print("no")
