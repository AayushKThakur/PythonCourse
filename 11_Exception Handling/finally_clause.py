try:
    my_list = [2, 5, 6, 7, 88, 0]
    print(my_list[0])
    print(my_list[0] / my_list[-1])
    # my_list = my_list * "abc"
except IndexError:
    print("Invalid Index")
except ZeroDivisionError:
    print("You cannot divide by zero")
except:
    print("Some error occurred")
# else:
#     print("Everything worked fine")
# finally clause Always prints
# use, for eg, disconnet th edatabase at the end irrespective
# of whether the code ran or not
finally:
    print("This is a finally clause")
