#!/usr/bin/python3
"""
This module contains a class 'Base'

Attributes ===>
        __nb_objects

Methods ===>
        __init__
"""


import json
import csv


class Base(object):
    """
    This class creates an instance of a Base Class.
    It has private attributes called __nb_objects, and
    the __init__ method for its initialization.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the 'JSON' string representation
        of a list of dictionaries
        """
        if list_dictionaries is not None:
            return json.dumps(list_dictionaries)
        else:
            return json.dumps([])

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of 'lists_objs' to a file"""
        files = []
        if list_objs is not None:
            for elem in list_objs:
                files.append(cls.to_dictionary(elem))
        my_file = cls.__name__ + ".json"
        with open(my_file, "w") as f:
            f.write(cls.to_json_string(files))

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of JSON string representation """
        if json_string is None or len(json_string) == 0:
            return json.loads([])
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes already set """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Returns the list of instances """
        my_file = cls.__name__ + ".json"
        my_list = []
        try:
            with open(my_file, "r") as f:
                instances = cls.from_json_string(f.read())
            for m, n in enumerate(instances):
                my_list.append(cls.create(**instances[m]))
        except Exception:
            pass
        return my_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Serializes a list object to 'csv' format """
        my_file = cls.__name__ + ".csv"
        with open(my_file, "w", newline="") as f:
            pen = csv.writer(f)
            for val in list_objs:
                if cls.__name__ == "Rectangle":
                    pen.writerow([val.id, val.width, val.height, val.x, val.y])
                if cls.__name__ == "Square":
                    pen.writerow([val.id, val.size, val.x, val.y])

    @classmethod
    def load_from_file_csv(cls):
        """ Deserializes a csv file """
        objs = []
        filename = cls.__name__ + ".csv"
        with open(filename, "r", newline="") as f:
            reader = csv.reader(f)
            for val in reader:
                if cls.__name__ == "Rectangle":
                    id = int(val[0])
                    wd = int(val[1])
                    hg = int(val[2])
                    x = int(val[3])
                    y = int(val[4])
                    dic = {"id": id, "width": wd, "height": hg, "x": x, "y": y}
                if cls.__name__ == "Square":
                    id = int(val[0])
                    size = int(val[1])
                    x = int(val[2])
                    y = int(val[3])
                    dic = {"id": id, "size": size, "x": x, "y": y}
                obj = cls.create(**dic)
                objs.append(obj)
            return objs
