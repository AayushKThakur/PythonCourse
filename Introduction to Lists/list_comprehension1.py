"""
ask start and end number from user
print all divisible by 2 and 3
"""

start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

my_list = [i for i in range(start, end + 1) if i % 2 == 0 and i % 3 == 0]
print(my_list)
