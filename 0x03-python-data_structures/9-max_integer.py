#!/usr/bin/python3
def max_integer(my_list=[]):
    my_list.sort()
    if my_list == None:
        return None
    return my_list[-1]
