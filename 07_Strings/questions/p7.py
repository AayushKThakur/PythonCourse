# reverse the characters of each word in a sentence
# maintaining the word order

my_string = input("Enter words to reverse: ")

words = my_string.split()

result = " ".join(i[::-1] for i in words)
print(result)
