#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if not isinstance(key, str):
        return "Invalid key type. Key must be a string."
    a_dictionary[key] = value
    return a_dictionary
