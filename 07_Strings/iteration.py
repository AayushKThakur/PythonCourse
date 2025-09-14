my_string = "Aayush Kunal Thakur"

#by index, by value, we can iterate 

for index in range(0,len(my_string)):
    print(my_string[index], end="")

print('\n')

for ch in my_string:
    print(ch, end="")

print('\n')

for i in range(len(my_string)-1, -1, -1):
    print(my_string[i], end="")