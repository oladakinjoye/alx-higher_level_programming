#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x elememts of a list.
    Args:
        my_list (list): list to print elements.
        x (int): number of elements of my_list to print.

    Returns:
        number of elements printed.
 """ 
    ret = 0
    for j in range(x):
        try:
            print("{}".format(my_list[j]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)
