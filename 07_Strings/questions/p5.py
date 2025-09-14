# write a program to reverse the order of words
# example 1
# my_string = "Hello World"
# output
# World Hello

my_string = input("Enter words to reverse: ")

words = my_string.split()

# words.reverse()
words = words[::-1]  # words override

# final_string = " ".join(words)
final_string = " ".join(i for i in words)

print(final_string)
