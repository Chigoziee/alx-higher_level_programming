#!/usr/bin/python3
def max_integer(my_list = []):
    max_ = my_list[0]
    for x in range(0, len(my_list)):
        if my_list[x] > max_:
            max_ = my_list[x]
    return max_
