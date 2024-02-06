#!/usr/bin/python3
"""class Square that define a square"""


class Square:
    """class Square that define a square"""
    __size = None

    def __init__(self, size=0):
        """instantiation with optional size"""
        if type(size) is int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("Size must be an integer")

    def area(self):
        """Public instance method area"""
        return self.__size * self.__size
