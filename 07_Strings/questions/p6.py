# capitalise first letter of each word while converting
# all other letters to lowercase
my_string = input("Enter words to reverse: ")

words = my_string.split()

result = " ".join(i.capitalize() for i in words)
print(result)
