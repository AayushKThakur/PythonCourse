# for eg, mom-mom. noon-noon.

my_string = input("Enter a string: ")

if my_string == my_string[::-1]:
    print("It is a palindrom")
else:
    print("It is not a palindrome")