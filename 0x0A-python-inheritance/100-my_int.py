#!/usr/bin/python3
"""
This module contains a class
MyInt that inherits from the native
class of int.
"""


class MyInt(int):
    """
    This class inherits from the native class
    of 'int'. It has every other method of the
    native 'int' class except that it inverts the
    '__eq__' and '__ne__' methods or operators.
    """


    def __eq__(self, other):
        """ It checks for inverted equality with a compared number """
        self.other = other
        return self.numerator != self.other

    def __ne__(self, other):
        """ It checks for inverted non-equality with a compared number """
        self.other = other
        return self.numerator == self.other
