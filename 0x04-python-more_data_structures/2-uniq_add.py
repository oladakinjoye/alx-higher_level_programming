#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
    function that adds all unique
    integers in a list, only once for each integer
    """
    new_list = []
    sum1 = 0
    for num in my_list:
        if num not in new_list:
            sum1 += num
            new_list.append(num)
    return sum1
