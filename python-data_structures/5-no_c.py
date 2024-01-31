#!/usr/bin/python3
def no_c(my_string):
    result = ""
    for char in my_string:
        if char not in "Cc":
            result += char
    return result
