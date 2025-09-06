# Enter a number: 8
# 1 1 1 1 1 
# 2 2 2 2 2 
# 3 3 3 3 3 
# 4 4 4 4 4 
# 5 5 5 5 5 
# 6 6 6 6 6 
# 7 7 7 7 7 
# 8 8 8 8 8

number = int(input("Enter a number: "))

for i in range(1,number+1):
    for j in range(1,6):
        print(i, end=" ")
    print()