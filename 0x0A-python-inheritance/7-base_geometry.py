#!/usr/bin/python3
"""
This nmodule contains a class
BaseGeometry (based on 5-base_geometry.py).
"""


class BaseGeometry(object):
    """
    This class defines a Base Geometry Class
    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates a value """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
