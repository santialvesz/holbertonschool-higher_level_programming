#!/usr/bin/python3
"""class Rectangle"""


from models.base import Base


class Rectangle(Base):
    """class name: Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """return area of rectangle"""

        return self.__width * self.__height

    def display(self):
        """print the rectangle"""

        for i in range(self.__y):
            print()
        for j in range(self.__height):
            for w in range(self.__x):
                print(" ", end="")
            for k in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """string representation of a rectangle"""

        return f'[Rectangle] ({self.id}) {self.__x}/{self.__y} \
- {self.__width}/{self.__height}'

    def update(self, *args, **kwargs):
        """Attributes of an instance"""

        if args:
            for i in range(len(args)):
                if i == 0:
                    setattr(self, "id", args[i])
                if i == 1:
                    setattr(self, "width", args[i])
                if i == 2:
                    setattr(self, "height", args[i])
                if i == 3:
                    setattr(self, "x", args[i])
                if i == 4:
                    setattr(self, "y", args[i])
        else:
            for key, value in kwargs.items():
                if key == "id":
                    setattr(self, "id", value)
                if key == "width":
                    setattr(self, "width", value)
                if key == "height":
                    setattr(self, "height", value)
                if key == "x":
                    setattr(self, "x", value)
                if key == "y":
                    setattr(self, "y", value)

    def to_dictionary(self):
        """dictionary"""
        my_dict = {"id": self.id,
                   "width": self.__width,
                   "height": self.__height,
                   "x": self.__x,
                   "y": self.__y}
        return my_dict
