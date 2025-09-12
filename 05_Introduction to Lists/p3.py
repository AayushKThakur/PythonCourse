# print odd and even elements of list in ther own seprate list

my_list = [3, 4, 5, 6, 7, 8, 9]

odd = []
even = []

# for i in range(0, len(my_list)):
#     if my_list[i] % 2 == 0:
#         even.append(my_list[i])
#     else:
#         odd.append(my_list[i])

# iterate by value
for num in my_list:  # i ke badle num, no reason
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print(f"Even list= {even}")
print(f"Odd list= {odd}")
