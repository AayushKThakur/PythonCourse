# Mutable/Immutable Data types

a = [54, 23, 10, 99, -90]

# these are prebuild functions
print(len(a))
print(sum(a))
print(max(a))
print(min(a))

# functions used in the list object, are list methods

a.append("Aayush")
a.append(-100)
a.insert(4, "Python")
a[0] = 100  # updating values
a.pop(1)  # Remove by index
a.remove(99)  # Remove by value
del a[0]  # Delte by index
# a.clear() #clear all elements of the list
print(a)
