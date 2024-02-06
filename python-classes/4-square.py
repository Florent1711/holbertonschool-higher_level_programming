#!/usr/bin/python3
class Square:
    """A class that represents a square"""

    def __init__(self, size=0):
        """Initialize the square with an optional size"""
        self.size = size  # This will call the setter method

    @property
    def size(self):
        """The size of the square"""
        return self.__size  # This is a private attribute

    @size.setter
    def size(self, value):
        """Set the size of the square"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value  # This will update the private attribute

    def area(self):
        """Return the current square area"""
        return self.__size ** 2
