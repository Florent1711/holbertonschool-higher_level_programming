#!/usr/bin/python3
"""
Write a function that returns True if the object is an instance of a class
that inherited
"""


def inherits_from(obj, a_class):
    """ Return True if the object is a instance of a class that ingerited from
        the specified class"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
