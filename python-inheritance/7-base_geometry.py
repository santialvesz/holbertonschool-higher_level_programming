#!/usr/bin/python3
"""class BaseGeometry"""


class BaseGeometry:
    """class name: BaseGeometry"""
    def area(self):
        """Geometry base area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """That validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
