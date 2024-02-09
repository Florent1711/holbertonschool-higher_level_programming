#!/usr/bin/python3

class Rectangle:
    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance with optional width and height.
        Args:
            width (int): Width of the rectangle (default is 0).
            height (int): Height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter method for retrieving the width.
        """
        return self._width

    @width.setter
    def width(self, value):
        """
        Setter method for setting the width.
        Args:
            value (int): New width value.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("Width must be >= 0")
        self._width = value

    @property
    def height(self):
        """
        Getter method for retrieving the height.
        """
        return self._height

    @height.setter
    def height(self, value):
        """
        Setter method for setting the height.
        Args:
            value (int): New height value.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("Height must be >= 0")
        self._height = value

    def area(self):
        """
        Calculates and returns the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.
        If width or height is equal to 0, perimeter is 0.
        """
        return 2 * (self.width + self.height)
