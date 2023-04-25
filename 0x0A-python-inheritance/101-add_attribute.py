#!/usr/bin/python3
"""
This module contains a function that adds
a new attribute to an object if it's possible
"""


def add_attribute(cls, attr, value):
    """
    This function adds a new attribute to
    an object if it's possible. It takes as parameter
    'cls'=> the class that will take a new attribute,
    'attr'=> the new attribute name to be added,
    'value'=> the value of the new attribute to be added.
    """

    """
    print(dir(cls))
    print(cls.__dict__)
    print("===============")
    print(help(cls.__setattr__))
    """

    if ("__dict__" in dir(cls)):
        setattr(cls, attr, value)
    else:
        raise TypeError(f"can't add new attribute")
