my_list = []

# normal way of making a list.
for i in range(1, 21):
    my_list.append(i)
print(my_list)

# list comprehensions
my_list2 = [i for i in range(1, 21)]
print(my_list2)

# example for better understanding. this prints even 20 times
my_list3 = ["even" for i in range(1, 21)]
print(my_list3)

my_list4 = [i % 2 for i in range(1, 21)]
print(my_list4)

my_list5 = ["EVEN" if i % 2 == 0 else "ODD" for i in range(1, 21)]
print(my_list5)

my_list6 = [i for i in range(1, 31) if i % 2 == 0]
print(my_list6)
