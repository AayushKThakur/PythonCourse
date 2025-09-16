# print number of occureence of each character in a string


def charCount(string):
    # my_dict = {}
    my_dict = dict()
    for ch in string:
        if ch not in my_dict:
            my_dict[ch] = 1
        else:
            my_dict[ch] += 1
    # print(my_dict)
    for k, v in my_dict.items():
        print(f"{k} occurs {v} times")


charCount("aaabbb  cccddcls  def")
