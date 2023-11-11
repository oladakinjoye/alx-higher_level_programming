#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """
    function that replace all occurrence
    of an element by another in a new list
    """
    new_list_1 = []
    for element in my_list:
        if element == search:
            new_list_1.append(replace)
        else:
            new_list_1.append(element)
    return new_list_1
