# Program to find common elements in three lists using sets

list1 = [3, 4, 5, 6, 7, 8, "aayush", "Python"]
list2 = [7, 6, 8, 1, "aayush"]
list3 = [1, 2, 3, 4, 5, 6, "aayush"]

print(set(list1) & set(list2) & set(list3))
