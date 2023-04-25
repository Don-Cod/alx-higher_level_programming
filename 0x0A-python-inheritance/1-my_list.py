#!/usr/bin/python3
"""
This file contains a class definition for
a MyList object.
"""


class MyList(list):
    """
    This class inherits from the
    list class.
    """

    def print_sorted(self):
        """ prints the list in ascending order """
        print(sorted(self))
