my_list = [4, -98, "Aayush Thakur", 22.22, 100]

# output should be reverse list
# 100 22.22 "Aayush Thakur"-98 4

for i in range(len(my_list) - 1, -1, -1):
    print(my_list[i], end=" ")
