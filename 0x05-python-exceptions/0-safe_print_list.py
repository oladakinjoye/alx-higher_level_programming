#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    sum_totl = 0
    for j in range(x):
        try:
            print(f"{my_list[j]}", end="")
            sum_totl += 1
        except IndexError:
            break
    print()
    return(sum_totl)
