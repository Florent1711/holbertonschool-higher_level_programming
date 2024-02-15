#!/usr/bin/python3

"""
This module contains a class that create a square by
inheriting the class Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This class creates a square by inheriting
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        Rectangle.__init__(self, size, size)
        self.__size = size

    def __str__(self):
        return "[{}] {}/{}".format(
                self.__class__.__name__, self.__size, self.__size)
