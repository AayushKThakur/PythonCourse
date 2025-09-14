#in order to append a data in tuple, override a tuple into
# list and then append the element and then again override it 
# to be a tuple.

my_tuple = (56,87, 74, 41,52)

my_list=list(my_tuple)
my_list.append(100)

print(my_list, type(my_list))

my_tuple=tuple(my_list)
print(my_tuple,type(my_tuple))