# check palindrome


def check_palindrome(string):
    if string == string[::-1]:
        print("It is a palindrome")
    else:
        print("It is not a palindrome")


check_palindrome("mom")
check_palindrome("aayush")
