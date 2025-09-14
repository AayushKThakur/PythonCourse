#Tuple. Are Immutable. We can't add remove or update. 
my_tuple = (56,87, 74, 41,52)

x = my_tuple.count(87)
y = my_tuple.index(87)
print(x,y, type(my_tuple))

for i in my_tuple:
    print(i, end=" ")
