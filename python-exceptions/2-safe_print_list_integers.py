#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    # initialize a counter for the number of integers printed
    count = 0
    # loop through the first x elements of the list
    for i in range(x):
        try:
            # try to print the element as an integer
            print("{:d}".format(my_list[i]), end="")
            # increment the counter
            count += 1
        except (ValueError, TypeError):
            # if the element is not an integer, skip it
            pass
        except IndexError:
            # if the index is out of range, raise an exception
            raise
    # print a new line at the end
    print()
    # return the number of integers printed
    return count
