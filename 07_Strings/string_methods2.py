# SPLIT
a = "hello world this is python"
words = a.split()
print(words)  # ['hello', 'world', 'this', 'is', 'python']

b = "hello-world-this-is-python"
words2 = b.split()
print(words2)
# the whole list prints at one position in memory,
# that is zero index. ['hello-world-this-is-python']

words3 = b.split("-")
print(words3)  # ['hello', 'world', 'this', 'is', 'python']

print(len(words))  # length of words
######################################################
# JOIN

my_list = ["Aayush", "Kunal", "Thakur"]

my_string = " ".join(my_list)
print(my_string)  # Aayush Kunal Thakur
print(type(my_string))

my_string = "-".join(my_list)
print(my_string)  # Aayush-Kunal-Thakur

my_string = " | ".join(my_list)
print(my_string)  # Aayush | Kunal | Thakur

my_list = ["abc", "xyz", "hello", "aayush", 22]
my_string = " ".join(str(i) for i in my_list)
# in order to join integer, using 'list comprehension'
print(my_string)
print(type(my_string))

# slicing
my_string = " ".join(str(i)[::-1] for i in my_list)
print(my_string)
