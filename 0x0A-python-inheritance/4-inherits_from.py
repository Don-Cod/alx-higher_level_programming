#!/usr/bin/python3
"""
This module contains a function that returns
True if the object is an instance of a class
that inherited (directly or indirectly) from
the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """
    This function that checks if the object
    is an instance of a class that inherited from a specified class.
    It takes as parameter 'obj'=> the element to be checked for.
    'a_class'=> the element to be checked against.
    Returns True if it matches, else False.
    """
    return type(obj) is not a_class and issubclass(type(obj), a_class)
