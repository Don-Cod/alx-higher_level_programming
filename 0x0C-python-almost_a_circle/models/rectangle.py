#!/usr/bin/python3
"""
This module contains a 'Rectangle' class
which inherits from the 'Base' class.
"""


from models.base import Base


class Rectangle(Base):
    """
    This class is a 'Rectangle' class which creates
    an instance of a Rectangle.
    Private Instances ===>
        __width ====width
        __height ==== height
        __x ==== x
        __y ==== y

    Methods ===>
        __init__
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Instantiates an object of 'Rectangle' class """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ gets the private instance attribute 'width' """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets the private instance attribute 'width' """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ gets the private instance attribute 'height' """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets the private instance attribute 'height' """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """ gets the private instance attribuite 'x' """
        return self.__x

    @x.setter
    def x(self, value):
        """ sets the private instance attribute 'x' """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """ gets the private instance attribute 'y' """
        return self.__y

    @y.setter
    def y(self, value):
        """ sets the private instance attribute 'y' """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """ returns the area of the rectnagle instance """
        return self.__width * self.__height

    def display(self):
        """ prints the instance of the 'Rectangle' to the stdout using '#' """
        y_spc = "\n" * self.__y
        x_spc = " " * self.__x
        w = self.__width
        h = self.__height
        print(y_spc + "\n".join(x_spc + "#" * w for i in range(h)))

    def __str__(self):
        """
        Updates the '__str__ method of the
        class by overriding its default behaviour
        """
        a = self.__class__.__name__
        b = self.id
        c = self.__x
        d = self.__y
        e = self.__width
        f = self.__height
        return f"[{a}] ({b}) {c}/{d} - {e}/{f}"

    def update(self, *args, **kwargs):
        """ Assigns an argument to each of the Instance attributes """
        if args:
            for arg in range(len(args)):
                try:
                    self.id = args[0]
                    self.width = args[1]
                    self.height = args[2]
                    self.x = args[3]
                    self.y = args[4]
                except IndexError:
                    pass
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """ Returns a dictionary representation of the Rectangle Object """
        e_dict = {}
        e_dict["id"] = self.id
        e_dict["width"] = self.width
        e_dict["height"] = self.height
        e_dict["x"] = self.x
        e_dict["y"] = self.y
        return e_dict
