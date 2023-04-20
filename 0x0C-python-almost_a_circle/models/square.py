#!/usr/bin/python3
"""
This module contains a Square class
inherits from the Rectangle class.
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This Square class inherits from the
    Rectangle class. It uses all the attributes of
    the parent class except that width and height are of
    the same values.

    -------
    Attributes ===>
    id
    width
    height
    x
    y
    """

    def __init__(self, size, x=0, y=0, id=None):
        """ Instantiates the Square object """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """ Prints a stirng representation of the object """
        a = self.__class__.__name__
        b = self.id
        c = self.x
        d = self.y
        e = self.width
        return f"[{a}] ({b}) {c}/{d} - {e}"

    @property
    def size(self):
        """ Returns the width and height of the square object """
        return self.width

    @size.setter
    def size(self, value):
        """ sets a new value for size attribute """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ updates the attributes of the Square object """
        if args:
            for arg in range(len(args)):
                try:
                    self.id = args[0]
                    self.width = args[1]
                    self.height = args[1]
                    self.x = args[2]
                    self.y = args[3]
                except IndexError:
                    pass
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.width = kwargs["size"]
                self.height = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """ Returns the dictionary representation of the Square object """
        e_dict = {}
        e_dict["id"] = self.id
        e_dict["size"] = self.size
        e_dict["x"] = self.x
        e_dict["y"] = self.y
        return e_dict
