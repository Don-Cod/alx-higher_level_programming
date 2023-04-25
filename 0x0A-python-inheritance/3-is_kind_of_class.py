#!/usr/bin/python3
"""
This module contains a function that returns
True if the object is an instance of, or if the
object is an instance of a class that inherited
from, the specified class ; otherwise False
"""


def is_kind_of_class(obj, a_class):
    """
    This function checks if the object is an instance of,
    or if the object is an instance of a class that
    inherited from, the specified class. It takes as parameters
    'obj=> This element to be checked for
    'a_class'=> The element to be compared against.
    Returns True if it matches, else False.
    """
    return isinstance(obj, a_class)
