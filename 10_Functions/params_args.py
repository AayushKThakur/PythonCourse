# a parameter is a variable in a function's definition,
#  acting as a placeholder for a value, while an argument
# is the actual value that is passed to the function when
# it is called


# input statements can not be inside function because
# we are asking for arguments from outside the function scope


def add(a, b):  # here a and b are parameters
    print(a + b)


add(11, 23)  # here 11 and 23 are arguments
add(100, 200)
add("Python", "Programming")

# add("Python", 12) #TypeError: can only concatenate str (not "int") to str
# add() #TypeError: add() missing 2 required positional arguments: 'a' and 'b'
# add(55, 100, 300) #TypeError: add() takes 2 positional arguments but 3 were given

# input statements can not be inside function because
# we are asking for arguments from outside the function scope
x = int(input("Enter number 1 = "))
y = int(input("Enter number 2 = "))
add(x, y)
