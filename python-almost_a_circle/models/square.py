#!/usr/bin/python3
"""class Square"""

from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """class name: Square"""

    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        self.x = size
        self.y = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str"""

        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        return self.__width

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    def update(self, *args, **kwargs):
        """adding the public method"""
        if args:
            for i in range(len(args)):
                if i == 0:
                    setattr(self, "id", args[i])
                if i == 1:
                    setattr(self, "size", args[i])
                if i == 2:
                    setattr(self, "x", args[i])
                if i == 3:
                    setattr(self, "y", args[i])
        else:
            for key, value in kwargs.items():
                if key == "id":
                    setattr(self, "id", value)
                if key == "size":
                    setattr(self, "size", value)
                if key == "x":
                    setattr(self, "x", value)
                if key == "y":
                    setattr(self, "y", value)

    def to_dictionary(self):
        """dictionary"""
        my_dict = {"id": self.id,
                   "size": self.size,
                   "x": self.x,
                   "y": self.y}
        return my_dict
