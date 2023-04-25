#!/usr/bin/python3
"""
This module contains a function that
returns the list of avalable attributes and
methods of an object
"""


def lookup(obj):
    """
    This function returns the list of available
    attributes and methods of a object. It takes as
    parameter
    'obj'=> which the attributes and methods is required
    """
    return dir(obj)
