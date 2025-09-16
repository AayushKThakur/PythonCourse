# write a function that accepts an integer and prints
# whether its odd or even


def check(num):
    if num % 2 == 0:
        print("Number is Even")
    else:
        print("Number is odd")


check(int(input("Enter a number: ")))
