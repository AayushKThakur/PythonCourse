# Given two lists a,b. check if two lists have at least one
# element common in them

lst1 = [3, 6, 7, 5, 55, 3, 1, 2, 2, "Python", "Aayush"]
lst2 = [7, 8, 5, 6, 1, "Aayush"]

print(set(lst1) & set(lst2))

# set1 = set(lst1)
# set2 = set(lst2)

# print(set1.intersection(set2))
# print(set1 & set2)
# print(set1 | set2)
