a = [59, 68, 100, 5, "aayush", True, 66.656, "thakur"]

# b = a
# # this shares the memory location of the beginning of the list
# print(a)
# print(id(a))
# print(b)
# print(id(b))
# # so when we do this, change in a, b also gets changed
# a[2] = 0
# print(a)
# print(b)

b = a.copy  # this copies a into another location with b
print(a)
print(id(a))
print(b)
print(id(b))

a[2] = 0
print(a)
print(b)
