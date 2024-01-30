#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    num_args = (len(argv) - 1)
if num_args == 0:
    print(f"{num_args} arguments.")
else:
    if num_args == 1:
        print(f"{num_args} argument:")
    else:
        print(f"{num_args} arguments:")
    for index, value in enumerate(argv[1:]):
        print(f"{index + 1}: {value}")
        