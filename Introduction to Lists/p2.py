# print even numbers in list
my_list = [3, 4, 6, 7, 8, 335, 667]

# Iteration by index
for i in range(0, len(my_list)):
    if my_list[i] % 2 == 0:
        print(my_list[i], end=" ")


# Iteration by value
for i in my_list:
    if i % 2 == 0:
        print(i, end=" ")
