#!/usr/bin/python3
class Square:
    """A class that represent a square"""


    def __init__(self, size = 0):
        """Initialize the square with an optionnal size"""

        # check if size is an integer
        if not isinstance(size, int):
            #raise a TypeError exception with the message size
            raise TypeError("Size must be an integer")
        
        # Assign the size to the private instance attribute
        self.__size = size
