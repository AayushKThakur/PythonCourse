def evenNumber():
    for i in range(1, 11):
        if i % 2 == 0:
            print(i, end=" ")


evenNumber()

print()

# Scoping
# Local scope: varibles defined inside a funcation,
# local to and accessible to only that function
# Global scope: declared outside a function scope,
# valid everywhere, even inside any function


def add():
    num1 = int(input("Enter a num1 = "))
    num2 = int(input("Enter a num2 = "))
    print(f"Sum = {num1 + num2 }")


def sub():
    num1 = int(input("Enter a num1 = "))
    num2 = int(input("Enter a num2 = "))
    print(f"Sub = {num1 - num2 }")


add()
sub()
