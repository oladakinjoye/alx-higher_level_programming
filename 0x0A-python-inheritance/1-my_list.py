#!/usr/bin/python3
"""MyList inherit from the list class"""


class MyList(list):
    """A class that inherit from list"""
    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))
