#!/usr/bin/python3
"""json"""
import json


def from_json_string(my_str):
    # convert the json string to a python object
    return json.loads(my_str)
