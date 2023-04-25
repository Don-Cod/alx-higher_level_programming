#!/usr/bin/python3
"""
This module contains a function that checks if an
object is of the same class as specified.
"""


def is_same_class(obj, a_class):
    """
    This function checks if the object is of
    the specified class. It takes as parameters,
    'obj'=> the python object to be checked
    'a_class'=> the specified to be checked for.
    Returns True if it matches, else False.
    """
    return type(obj) == a_class
